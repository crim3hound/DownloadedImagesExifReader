# Downloaded Images EXIF Reader
A simple script that downloads images from webpages and extracts their EXIF metadata

### Background and Motivation
This project builds on the contributions of [@abhigoya](https://auth.geeksforgeeks.org/user/abhigoya) and [@ruhelaa48](https://auth.geeksforgeeks.org/user/ruhelaa48) on [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-download-all-images-from-a-web-page-in-python/), which served as the starting point. 

I worked on this purely on a support capacity to try and help solve a unique problem that required the fusion of functionalities to fetch multiple images from webpages, extract their respective metadata using ExifTool, and output some sort of report - in this case we're just saving the information in text files. 

### Requirements

1. Python v3
2. [ExifTool](http://www.sno.phy.queensu.ca/~phil/exiftool/) by Phil Harvey to read image metadata.