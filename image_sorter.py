from PIL import Image
import os 
import glob
import datetime
import shutil


class SortFiles():
    def __init__(self):
        self.months = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUNE', 7:'JULY', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
        self.current_dir = os.getcwd()
    
    def main(self):
        files = glob.glob("*")
        for file in files:
            isFIle = os.path.isfile(self.current_dir + '/' + file)
            if isFIle:
                extension = file.split(sep=".")
                if extension[1].lower() == 'jpeg' or extension[1].lower() == 'jpg' or extension[1].lower() =='png':
                    image = Image.open(file)
                    exifdata = image.getexif()
                    image.close()
                    dateTime = exifdata.get(306)
                    if dateTime:
                        dateTimeArray = dateTime.split()
                        date, time = dateTimeArray[0], dateTimeArray[1]
                        dateArray = date.split(':')
                        timeArray = time.split(':')
                        year, month, date = dateArray[0], dateArray[1], dateArray[2]
                        hour, min, sec = timeArray[0], timeArray[1], timeArray[2]
                        new_name = year + '-' + month + '-' + date + '@'+ '1' + '.' + extension[1].lower()
                        new_dir = self.current_dir + "/Photos/" + year + "/" + self.months.get(int(month)) + "/" + date
                        self.sorter(file, new_dir, new_name, year, month, date, extension)
                        
                    else:
                        fileName = file.split(sep="-")
                        if len(fileName)<2:
                            fileName = file.split(sep="_")
                        dateArray = fileName[1]
                        year, month, date = dateArray[:4], dateArray[4:6], dateArray[6:8]
                        new_name = year + '-' + month + '-' + date + '@' + '1' + '.' + extension[1].lower()
                        new_dir = self.current_dir + "/Photos/" + year + "/" + self.months.get(int(month)) + "/" + date
                        self.sorter(file, new_dir, new_name, year, month, date, extension)
                        
    def sorter(self, file, new_dir, new_name, year, month, date, extension):
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
            
        checkFile = os.path.isfile(new_dir + '/' + new_name)
        
        i=2
        while (checkFile):
            new_name = year + '-' + month + '-' + date + '@' + str(i) + '.' + extension[1].lower()
            checkFile = os.path.isfile(new_dir + '/' + new_name)
            i+=1
            
        os.rename(file, new_name)
        shutil.move(new_name, new_dir)
        return 
                        
a = SortFiles()
a.main()
                        
                        
                        