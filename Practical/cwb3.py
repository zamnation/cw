# Filename: cwb3.py
# Author: Sean
# Centre No / Index No: 3024 /

import time
import datetime
from datetime import date

def LOANRESOURCE():
    try:
        # Open URESOURCE.DAT for reading
        uresource_file = open("URESOURCE.DAT", "r")
        
        # Read and skip first line
        uresource_file.readline()
        
        # Read record
        detail_lines = uresource_file.readlines()
        
        # Initialize resource number list
        resourcenumber_list = []
        
        # Loop through each record
        for record in detail_lines:
            # Slice to get resource number
            resource_number = record[0:5]
            # Append resource number to resource number list
            resourcenumber_list.append(resource_number)
            
        # Open LOAN.DAT for append
        loan_file = open("LOAN.DAT", "a")
        
        # Get and validate resource number
        valid_resourcenumber = False
        while not valid_resourcenumber:
            # Obtain input from user
            resource_number = input("Enter resource number: ")
            # Presence check
            if len(resource_number) == 0:
                print("Invalid! Resource number cannot be null. Try again.")
            # isdigit check
            elif not resource_number.isdigit():
                print("Invalid! Resource number should be digits only. Try again.")
            # Length check
            elif len(resource_number) > 5:
                print("Invalid! Resource number cannot be more than 5 digits in length. Try again.")
            # Checking with resource number list
            elif resource_number not in resourcenumber_list:
                print("Invalid! Resource does not exist. Try again.")
            else:
                valid_resourcenumber = True
                
        # Get and validate StudentID
        valid_student_ID = False
        while not valid_student_ID:
            # Obtain input from user
            student_ID = input("Enter Student ID: ")
            # Presence check
            if len(student_ID) == 0:
                print("Invalid! Student ID cannot be null. Try again.")
            # Length check
            elif len(student_ID) > 5:
                print("Invalid! Student ID cannot be more than 5 characters in length. Try again.")
            # First character = "S" check
            elif not student_ID[0] == "S":
                print("Invalid! First character of Student ID must be 'S' or 's'. Try again.")
            # Last 4 characters isdigit check
            elif not student_ID[1:4].isdigit():
                print("Invalid! Last four characters of StudentID must be digits. Try again.")
            else:
                valid_student_ID = True
                
        # Get and validate StudentName
        valid_student_name = False
        while not valid_student_name:
            # Obtain input from user
            student_name = input("Enter Student Name: ")
            # Presence check
            if len(student_name) == 0:
                print("Invalid! Student name cannot be null. Try again.")
            # Length check (30)
            elif len(student_name) > 30:
                print("Invalid! Student name cannot be more than 30 characters in length. Try again.")
            else:
                valid_student_name = True
                
        # Generate DateDueBack
        current_date = date.today()
        date_due_back = current_date + datetime.timedelta(weeks=1)
        # Format DateDueBack into appropriate form
        date_due_back = date_due_back.strftime("%d%m%y")

        # Generate evaluation
        evaluation = " "        
        
        # Write valid records to file
        loan_file.write("{0:5s}{1:5s}{2:30s}{3:6s}{4:50s}".format(resource_number, student_ID, student_name, date_due_back, evaluation)+ "\n")

        # Close files
        uresource_file.close()
        

    except IOError:
        print("Error! Cannot read from input file or write to output file.")


# main
if __name__ == "__main__":
    LOANRESOURCE()
