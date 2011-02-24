# Name: Sean Seah
# Centre No / Index No: 3024 /
# Description: Supporting classes for resources, music cd and film dvd

# Superclass Resource
class Resource():

    ''' Resource class constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo# typing two _ in front of the variable makes it 'private' in python
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType
 
    ''' Resource number accessor '''
    def getResourceNo(self):
        return self.__ResourceNo
 
    ''' Title accessor '''
    def getTitle(self):
        return self.__Title
 
    ''' Date acquired accessor '''
    def getDateAcquired(self):
        return self.__DateAcquired

    ''' Resource type accessor '''
    def getResourceType(self):
        return self.__ResourceType

    ''' Title modifier '''
    def setTitle(self, newTitle):
        self.__Title = newTitle

    ''' Date acquired modifier '''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    ''' Resource Type modifier '''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    ''' Helper function to display all data '''
    def display(self):
        return("{0:5s}{1:30s}{2:6s}{3:1s}".format \
               (self.__ResourceNo, self.__Title, self.__DateAcquired, self.__ResourceType))    
 
# Subclass MusicCD
class MusicCD(Resource): # declare the parent class in the bracket

    ''' MusicCD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks

    ''' Artist accessor ''' 
    def getArtist(self):
        return self.__Artist

    ''' NoOfTacks accessor '''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    ''' Artist modifier '''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    ''' NoOfTracks modifier '''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks

    ''' Helper function to display all data '''
    def display(self):
        return("{0:42s}{1:50s}{2:2s}{3:50s}{4:3s}".format(super().display(), self.__Artist, self.__NoOfTracks.zfill(2), "NULL", "000"))
    

# Subclass FilmDVD
class FilmDVD(Resource):
 
    ''' FilmDVD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime

    ''' Artist accessor ''' 
    def getDirector(self):
        return self.__Director

    ''' NoOfTacks accessor '''
    def getRunningTime(self):
        return self.__RunningTime

    ''' Artist modifier '''
    def setDirector(self, newDirector):
        self.__Director = newDirector

    ''' NoOfTracks modifier '''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime

    ''' Helper function to display all data '''
    def display(self):
        return("{0:42s}{1:50s}{2:2s}{3:50s}{4:3s}".format(super().display(), "NULL", "00", self.__Director, self.__RunningTime.zfill(3)))

##r1 = Resource("00001", "Best of Super Junior", "090911", "C")
##r2 = Resource("00002", "Shaolin Temple", "121210", "D")
##
##print(r1.getResourceNo())
##print(r1.display())
##r1.setTitle("SUPER JUNIOR SUCKS")
##print(r1.display())
##r3 = Resource("00003", "","","")
##print(r3.display())
##r3.setTitle("LUCIFERZ")
##r3.setDateAcquired("080810")
##r3.setResourceType("C")
##print(r3.display())
##cd1 = MusicCD("00004", "Michael Jackson Last Album", "050508", "C", "Michael Jackson", 10)
##
##print(cd1.getResourceNo()) # inheritance
##print(cd1.display()) # overriding the parent display method
##
### print(cd1.__Title) is illegal cause of information hiding (private data protected, cannot be directly accessed)
##
##dvd1 = FilmDVD("00005", "Green Hornet", "030311", "D", "Jay Chou", 120) 
##
##res_list = []
##res_list.append(cd1)
##res_list.append(dvd1)
##
##for item in res_list: # polymorhpism
##    print(item.display())
