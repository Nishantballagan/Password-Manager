#DigiCore Password manager 
#File name = passman.py
#Author Name = Nishant 
#Development date = 03/11/2022 

#Start program
# Import os and sys modules provide numerous tools to deal with filenames, paths, directories.
import os
import sys
#Create function to append data
def write(): 
        Data_base = open("password.txt",'a') #open text file and append data
        User_name = "Username: " + input("Enter Username: ") + "\n" #input  username by staff
        Password = "Password: " + input("Enter password: ") + "\n"#input password by staff
        Web_address = input("Enter web address: ")#input web address by staff
        print()
        Data_base.write("***********"+(Web_address)+"*************\n")# Write input data to text file
        Data_base.write(User_name)#Write input data to text file
        Data_base.write(Password)#Write input data to text file
        Data_base.write("*****************************************\n")#Write input data to text file
        Data_base.write("\n")
        Data_base.close()#Close text file
        print("Password Entered")

#Create function to Read and Retrieve  data
def read():
        filesize = os.path.getsize("password.txt")#Check data in text file
        if filesize == 0:# if no data in text file then print no data
            print("No data in text file. Add new credentials\n")
        else:
            Data_base = open("password.txt",'r')#open text file password.txt and read data if data is there
            pass_words = Data_base.read()
            print(pass_words)#Output all data in text file
            print("File is closed\n")
            Data_base.close()# close text file
 
#Create function help   
def help():
        print("Help guide\n")
        print("Add new password: this option will let you add a new username and password to the text file\n")
        print("Show password: this option will let you to view password save on the text file\n")
        print("Exit: this option will exit from program\n")
#Create text file
if os.path.exists("password.txt"):# check if text file is already exist
    print("File is already created\n")
else:
    Data_base=open("password.txt",'w')# create text file if no password file is created
    print("Text file name password is created")
    Data_base.close()#close text file

# create selection menu
while True:
    print("Select from the menu\n")
    print("(A) Adding new password")
    print("(B) Show existing passwords")
    print("(C) Exit")
    print("(D) Help")
    select_option=input("\nSelect one from above option: ")# ask from staff to choose option
    if select_option=="A":# choose option A
        write()        #recall write function
    elif select_option=="B":# choose option B
        read()         #recall read function
    elif select_option=="C":# choose option C
        print("Exit from program..")
        sys.exit()        # exit from program
    elif select_option=="D":# choose option D
        help()            ##recall help function
    else:
        print("You did not enter a valid capital alphabet\n")
    
    #end program
         
#    Task 2.6 – Document the script

# 1.	The name of reviewer = Nishant
# 2.	Completion date = 6/11/2022
# 3.	Final version number =Passman01
# 4.	An overview of the codes functionality = All modules and function in the script work without any error.   
# 5.	The command-line syntax to run the script and what is expected as output = All menu work perfectly
# 6.	A brief statement of what could be added, subtracted or modified in future versions with a view to improvement and/or enhancement = 
#       In future add function to delete user data in text file, update user details in text file.
