# Image-sorter
A python script which helps in sorting your bulk images according to the date of the Image which was captured

## Folder Structure
- Images
	- Year
		- Month
			- Date
				- File Name


### Description

- Every image has some data which includes date of the photo taken, location, device through which photo was taken etc. This data is called Exif data **(Exchangeable image file format)**. Our task is to extract the date from the exif data and sort according to it

- Images which has been shared through whatsapp will not have any exif data as whatsapp remove those data inorder to reduce the file size. Inorder to tackle that I have extracted the date from the file name. whatsapp follows the certain naming pattern Example **IMG-20191122-WA0023.jpg** here 2019 represent year 11 represents month and 22 represents date and WA represents whatsapp.

- If a image doesnot follow any pattern name like **IMG-20191122-WA0023.jpg** or **snapchat-2019122-0023.jpg** then the date is extracted from the inbuilt os module i.e creation date of the image.

- I can simply follow the 3rd step instead of 1st and 2nd step but **Creation dates do not necessarily reflect when a file was actually created or image was taken. Rather, creation date stamps indicate when a file came to exist on a particular storage medium, such as a hard drive. Creation dates can thus indicate when a user or computer process created a file. However, they can also reflect the date and time that a file was copied onto a particular storage medium**. I need the actual date of image when the image was taken thus the priority order goes like this.

### How to Run
#### Requirements
- Python 3.x
- Pillow libray package

> I am assuming you already know the basic installation of python and python packages

1. Install pillow library package using the following command in your terminal
`pip install pillow`

2. Paste the **image_sorter.py** inside the folder where you want to sort the images

3. Run `python image_sorter.py` in terminal


------------


#### Feel free to star the repo if you liked it 


