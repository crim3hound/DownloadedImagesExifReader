# TODO: Unable to fetch SVG images at the moment; SVG code is quietly ignored
# TODO: Possible bug - Unable to fetch images if paths are relative


from bs4 import *
from urllib.parse import urlparse
from datetime import datetime
import time
import requests
import os
import magic
import hashlib
import pyexifinfo as p
import json


# Create folder to store images
def folder_create(url, images):
    try:
        # get domain name from entered url
        domain_name = urlparse(url).netloc

        # get current date and time
        now = str(datetime.now())

        # format date to suit folder name parameters
        date_time = now.replace('-', '').replace(' ', '_').replace(':', '').split('.')

        # generate save location folder name
        folder_name = f"{domain_name}_{date_time[0]}"

        # create the save location folder
        os.mkdir(folder_name)

    # if folder exists with that name, ask another name
    except:
        print("Folder with that name already exists! Enter a different name.")
        folder_create()

    # image download start
    download_images(images, folder_name)

    # read exif for all downloaded images
    time.sleep(1)
    retrieve_exif(folder_name)


# Download all image from given URL
def download_images(images, folder_name):
    # initial count is zero
    count = 0

    # print total images found in URL
    print(f"\nAttempting to download and save {len(images)} image(s) to '{folder_name}'\n")

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

            # 1. data-srcset
            # 2. data-src
            # 3. data-fallback-src
            # 4. src

            # Here we will use exception handling

            # first, search for "data-srcset" in img tag
            try:
                # search for "data-srcset" in img tag
                image_link = image["data-srcset"]

            # then we will search for "data-src" in img tag and so on.
            except:
                try:
                    # search for "data-src" in img tag
                    image_link = image["data-src"]
                except:
                    try:
                        # search for "data-fallback-src" in img tag
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # search for "src" in img tag
                            image_link = image["src"]

                        # if no source URL found
                        except:
                            pass

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                # Handle images with relative source paths
                if 'http' not in image_link.lower():
                    image_link = url.rstrip('/') + image_link

                    # Parse image link to allow removal of query strings
                    scheme = urlparse(image_link).scheme
                    host = urlparse(image_link).netloc
                    path = urlparse(image_link).path

                    formatted_link = f"{scheme}://{host}{path}"

                    r = requests.get(formatted_link).content

                # Default for images with full paths
                else:
                    # Parse image link to allow removal of query strings
                    scheme = urlparse(image_link).scheme
                    host = urlparse(image_link).netloc
                    path = urlparse(image_link).path

                    formatted_link = f"{scheme}://{host}{path}"

                    r = requests.get(formatted_link).content

                # Get image name and extension from the link
                basename = os.path.basename(formatted_link)

                # extract image name and extension from basename
                img_name, img_ext = os.path.splitext(basename)

                try:

                    # possibility of decode
                    r = str(r, 'utf-8')

                except UnicodeDecodeError:

                    # Calculate md5 hash of downloaded image
                    img_hash = hashlib.md5(r).hexdigest()

                    # After checking above condition, download image with original filename
                    # Append hash to filename for unique names to prevent overwriting
                    image_path = f"{folder_name}/image{count + 1}__md5-{img_hash}{img_ext}"

                    with open(f"{image_path}", "wb+") as f:
                        f.write(r)

                    # Rudimentary image download progress
                    count += 1
                    print(f"{count} of {len(images)} image(s) downloaded [md5: {img_hash}]")
            except:
                pass

        # There might be a possibility not all images will download
        # if all images were downloaded
        if count == len(images):
            print(f"\nAll images downloaded!\n")

        # if not all images were downloaded
        else:
            not_downloaded = len(images) - count
            print(f"\n{count} image(s) downloaded. Failed to download {not_downloaded} image(s)\n")


# Retrieve EXIF for all images downloaded
def retrieve_exif(folder_name):

    # First, rename images without extensions
    with os.scandir(f"{folder_name}/") as files:
        for f in files:
            if f.is_file():
                # extract image name and extension from basename
                f_name, f_ext = os.path.splitext(f.name)

                if f_ext == "":
                    mime = magic.from_file(f"{folder_name}/{f.name}", mime=True)
                    f_ext = mime.split("/")[1]

                    os.rename(f"{folder_name}/{f.name}", f"{folder_name}/{f.name}.{f_ext}")

    # Then, get exif data from images
    with os.scandir(f"{folder_name}/") as images:
        for image in images:
            if image.is_file():

                data = p.get_json(f"{folder_name}/{image.name}")
                formatted_json = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
                # print(formatted_json)

                with open(f"{folder_name}/{image.name}.txt", "w") as f:
                    f.write(formatted_json)


# Main Function
def main(url):
    # content of URL
    r = requests.get(url)

    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')

    # Find all images in URL
    images = soup.findAll('img')

    # Call folder create function
    folder_create(url, images)


# Capture entered link
url = input("Enter URL: ")

# Call the main function
main(url)
