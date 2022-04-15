# Downloaded Images EXIF Reader
A simple script that downloads images from webpages and extracts their EXIF metadata

### Background and Motivation
This project builds on the contributions of [@abhigoya](https://auth.geeksforgeeks.org/user/abhigoya) and [@ruhelaa48](https://auth.geeksforgeeks.org/user/ruhelaa48) on [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-download-all-images-from-a-web-page-in-python/), which served as the starting point. 

I worked on this purely on a support capacity to try and help solve a unique problem that required the fusion of functionalities to fetch multiple images from webpages, extract their respective metadata using ExifTool, and output some sort of report - in this case we're just saving the information in text files. 

### Requirements

1. Python v3.7.x and newer. Download [here](https://www.python.org/downloads/).
2. [ExifTool by Phil Harvey](https://exiftool.org/index.html) to read image metadata. Download v12.41 for [Windows](https://exiftool.org/exiftool-12.41.zip) or [Mac](https://exiftool.org/ExifTool-12.41.dmg).

### Usage
1. Clone the project and set up your local environment.
2. From the command line, change directory to the folder with the script. Ensure ExifTool is added to PATH in your system. More instructions are available [here](https://exiftool.org/install.html).
3. Run `python main.py`
4. Enter the full URL to download images from, e.g., `https://picsum.photos`
5. Wait for the script to fetch the images, which will be saved in an auto-generated folder based on the URL and the date and time of the operation.

### Example

````
python main.py
Enter URL: https://picsum.photos/

Attempting to download and save 9 image(s) to 'picsum.photos_20220415_175214'

1 of 9 image(s) downloaded [md5: 721cded57cc607d25fe1bbba784295af]
2 of 9 image(s) downloaded [md5: c12178a78b690b0576e272b857c330e0]
3 of 9 image(s) downloaded [md5: ac271de883faa03617b212beeda73db3]
4 of 9 image(s) downloaded [md5: 4703c28a2ab0130dbbb4347476361bb8]
5 of 9 image(s) downloaded [md5: 9610239df6470e4ddea8dcaffc663ecf]
6 of 9 image(s) downloaded [md5: abc220c50d08a26cd604a8ddb2dd41ab]

6 image(s) downloaded. Failed to download 3 image(s)

````
### Result
![](../../Downloads/2022-04-15 17_55_05-picsum.photos_20220415_175311.png)