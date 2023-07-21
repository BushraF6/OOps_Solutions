# Create class of DataExtracter that extracts data from datafile.
class DataExtractor:   
    def __init__(self,data_file):
        self.file=open(data_file,'r')
        self.data_reader=self.file.readlines()
    def get_info(self):
        return  self.data_reader
# Create class of DataAnalyzer to analyze the data and calculate minimum difference.
class DataAnalyzer(DataExtractor):    # inheriting features/methods of class DataExtractor
    def min_diff(self):
        self.data_reader= self.get_info()
        diff_l=[]
        # To get list of difference of maximum and minimum temperatures from weather file.
        if len(self.data_reader)==33:       
            for data in self.data_reader[2:len(self.data_reader)-1]:
                diff=int(data[6:8])-int(data[12:14])
                diff_l.append(diff)
            return diff_l.index(min(diff_l))+1
        # To get list of difference of FA and A scores from football file.
        else:                               
            for data in self.data_reader[1:]:
                if data[3]!='-':
                    diff=abs(int(data[43:45])-int(data[50:52]))
                    diff_l.append(diff)
            return self.data_reader[diff_l.index(min(diff_l))+1][7:20]
# Create a class of Calculate for initialising class and executing.
class Calculate:
    def __init__(self,file):
        self.analyse=DataAnalyzer(file)     #Initializing Calculate object
    def execute(self):
        print(self.analyse.min_diff())      #Executing the result i.e minimum difference

weather=Calculate('weather.dat')
weather.execute()
football=Calculate('football.dat')
football.execute()


        

        