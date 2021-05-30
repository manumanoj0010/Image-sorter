from PIL import Image
import os 
import glob
import datetime
import shutil

class SortImages():
    """ Organize images into folders according to the date time """
    
    def __init__(self):
        """ constructor methond """
        
        self.months = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUNE', 7:'JULY', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
        self.current_dir = os.getcwd()
        self.image_extensions = ['jpeg','jpg','png']
    
    def sort_by_date(self):
        """ function will take extract the dates from the images """
        
        files = glob.glob("*")
        for file in files:
            isFIle = os.path.isfile(self.current_dir + '/' + file)
            # checking whether its a file or directory
            if isFIle:
                extension = file.split(sep=".")
                # if a file doesnot have any extension like LICENSE file
                if len(extension)<2:
                    continue
                file_extension = extension[1].lower()
                if file_extension in self.image_extensions:
                    image = Image.open(file)
                    exifdata = image.getexif()
                    image.close()
                    # 306 represent the date time code in exif data
                    dateTime = exifdata.get(306)
                    # if image has exif data i.e date and time
                    if dateTime:
                        dateTimeArray = dateTime.split()
                        date, time = dateTimeArray[0], dateTimeArray[1]
                        dateArray = date.split(':')
                        timeArray = time.split(':')
                        year, month, date = dateArray[0], dateArray[1], dateArray[2]
                        hour, min, sec = timeArray[0], timeArray[1], timeArray[2]
                        # format for image name (new name)
                        new_name = year + '-' + month + '-' + date + '@'+ '1' + '.' + file_extension
                        # new directory path
                        new_dir = self.current_dir + "/Photos/" + year + "/" + self.months.get(int(month)) + "/" + date
                        self.file_organiser(file, new_dir, new_name, year, month, date, extension)
                    
                    # if image doesnot have any exif data
                    else:
                        # files whose naming pattern is IMG-20191122-WA0023.jpg
                        fileName = file.split(sep="-")
                        #files whose naming pattern is IMG_20191122_0023.jpg
                        if len(fileName)<2:
                            fileName = file.split(sep="_")
                        # files which doesnot have any naming pattern
                        if len(fileName)<2:                           
                            ti_m = os.path.getctime(file)
                            date_stamp = datetime.date.fromtimestamp(ti_m)
                            dateArray = str(date_stamp).split(sep="-")
                            year, month, date =dateArray[0], dateArray[1], dateArray[2]
                        else:
                            dateArray = fileName[1]
                            year, month, date = dateArray[:4], dateArray[4:6], dateArray[6:8]
                            
                        new_name = year + '-' + month + '-' + date + '@' + '1' + '.' + file_extension
                        new_dir = self.current_dir + "/Photos/" + year + "/" + self.months.get(int(month)) + "/" + date
                        self.file_organiser(file, new_dir, new_name, year, month, date, extension)
                        
    def file_organiser(self, file, new_dir, new_name, year, month, date, extension):
        """ organize the image files into folders by date """
        # creating a new directory if it doesnot exists
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            
        checkFile = os.path.isfile(new_dir + '/' + new_name)
        
        # creating a new file name if a similar file already exists in folder. the file will chanage to 2020-02-01@1 2020-02-01@2 and so on
        i=2
        while (checkFile):
            new_name = year + '-' + month + '-' + date + '@' + str(i) + '.' + extension[1].lower()
            checkFile = os.path.isfile(new_dir + '/' + new_name)
            i+=1
        
        #renaming the file and moving the file to a specified folder
        os.rename(file, new_name)
        shutil.move(new_name, new_dir)
        return 
                        

if __name__ == "__main__":
    a = SortImages()
    a.sort_by_date()
    