#Encrypted-database
#Highly secured database using python
print '---------------------------------------------------------------------------\n'
print '                          ENCRYPTED DATABASE 1.0                          '
print '---------------------------------------------------------------------------\n'
print 'Admin login :'
key1 =[["",""]]
Id1 = raw_input("\t\tEnter UserID :")
Pin1 = raw_input("\t\tEnter Password :")
if [Id1,Pin1] in key1 : i = int(raw_input("Enter no of data :"))
for i in range(i):
    emp_name = raw_input("Enter Employee Name :")
    emp_id = raw_input("Enter Employee Id :")
    emp_Address = raw_input("Enter Employee Address :")
#From Above line of code is for storing database
key2 = [["",""]]
print "Admin Login"
Id2 = raw_input("\t\tEnter UserId :")
Pin2 = raw_input("\t\tEnter Password :")
if [Id2,Pin2] in key2 :print "1. Add data"
print "2  Display data"
print "3  Back up data"
print "4  Enrypt data"
inp = raw_input("Enter your choice : ")

add_data = "1"

if(inp == "1"):
    del inp
    i = int(raw_input("Enter no of data :"))
for i in range(i):
    inp = raw_input("Enter number of data")
    emp_name = raw_input("Enter Employee Name :")
    emp_id = raw_input("Enter Employee Id :")
    emp_Address = raw_input("Enter Employee Address :")





