# Filename: cwb2.py
# Name: Sean
# Centre No / Index No: 3024
# Description: Read from RESOURCE.DAT, get extra info based on resource type
#              perform validation and write to URESOURCE.DAT

from classes import *

def UPDATERESOURCE():
    try:
        # open resource file for reading
        resource_file = open("RESOURCE.DAT", "r")
        
        # open updated resource file for writing
        uresource_file = open("URESOURCE.DAT", "w")
            
        # read heading line from resource file (creation date, number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n")
        
        # store creation date and number of records
        creation_date = heading_line[0:10]
        num_records = heading_line[10:]

        # write creation date and number of recods to updated resource file
        uresource_file.write(creation_date + num_records + "\n")

        # read remaining record details
        detail_lines = resource_file.readlines()

        # initialize resource list
        resource_list = []
        
        # loop for number of records
        for record_line in detail_lines:
            # remove spaces in record_line
            record_line = record_line.rstrip("\n")

            # store resource number, title, date acquired, resource type
            resource_no = record_line[0:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]
            # print resource info
            print("Resource number: " + resource_no)
            print("Title: " + title)
            print("Date Acquired: " + date_acquired)
            print("Resource type: " + resource_type)
            
            # if resource type is music CD
            if resource_type == "C":
                # get and validate artist
                valid_artist = False
                while not valid_artist:
                    artist = input("Enter artist: ")
                    if len(artist) == 0: # presence check
                        print("Invalid! Empty input. Try again.")
                    elif len(artist) > 50: # length check
                        print("Invalid! Exceeds 50 characters. Try again.")
                    else:
                        valid_artist = True
                        
                # get and validate number of tracks
                valid_NoOfTracks = False
                while not valid_NoOfTracks:
                    NoOfTracks = input("Enter number of tracks: ")
                    if len(NoOfTracks) == 0: # presence check
                        print("Invalid! Empty input. Try again.")
                    elif not NoOfTracks.isdigit(): # range check
                        print("Invalid! Must be a number. Try again.")
                    elif not (0 < int(NoOfTracks) <= 20): # range check
                        print("Invalid! Must be between 1 and 20. Try again.")
                    else:
                        valid_NoOfTracks = True
                resource_list.append(MusicCD(resource_no, title, date_acquired, resource_type, artist, NoOfTracks))

            
            # else resource type is film DVD
            elif resource_type == "D":
                # get and validate director
                valid_director = False
                while not valid_director:
                    director = input("Enter director: ")
                    if len(director) == 0: # presence check
                        print("Invalid! Empty input. Try again.")
                    elif len(director) > 50: # length check
                        print("Invalid! Exceeds 50 characters. Try again.")
                    else:
                        valid_director = True
                        
                # get and validate running time
                valid_RunningTime = False
                while not valid_RunningTime:
                    RunningTime = input("Enter running time: ")
                    if len(RunningTime) == 0: # presence check
                        print("Invalid! Empty input. Try again.")
                    elif not RunningTime.isdigit(): # range check
                        print("Invalid! Must be a number. Try again.")
                    elif not (0 < int(RunningTime) <= 600): # range check
                        print("Invalid! Must be between 1 and 600. Try again.")
                    else:
                        valid_RunningTime = True
                resource_list.append(FilmDVD(resource_no, title, date_acquired, resource_type, director, RunningTime))

            
        # write resource info and extra details to updated resource file
##        for resource in resource_list:
##            if resource.getResourceType() == "C":
##                uresource_file.write(resource.getResourceNo() + resource.getTitle() + resource.getDateAcquired() + \
##                                     resource.getResourceType() + resource.getArtist() + resource.getNoOfTracks() + \
##                                     "NULL (count 50)" + "000" + "\n")
##            else:
##                uresource_file.write(resource.getResourceNo() + resource.getTitle() + resource.getDateAcquired() + \
##                                     resource.getResourceType() + "NULL (count to 50)   " + "00" + \
##                                     resource.getDirector() + resource.getRunningTime() + "\n")

        for resource in resource_list:
            uresource_file.write(resource.display() + "\n")

            
        # close files
        resource_file.close()
        uresource_file.close()
        
    except IOError:
        # display file input/output errors
        print("Error! Cannot read from input file or write to output file.")

# main
if __name__ == "__main__":
    UPDATERESOURCE()
