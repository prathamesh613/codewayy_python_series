#Details Displaying Program
print("=+" * 30)

class Details:
    #Assign Names
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
        self.total = 0
    #Concatenate Names
    def concat_name(self):
        return self.fname.capitalize() + ' ' + self.lname.capitalize()

    #College Name
    def college(self,name, address,city,state):
        return(f"{name}, {address}, {city}, {state}.")

    #Printing Marks
    def marks(self,subjects):
        for ele in subjects:
            self.total += ele
        return self.total
fname = input("Enter your First Name : ") #Input First Name
lname = input("Enter yout Last  Name : ") #Input Last Name

person = Details(fname,lname)

cname = input("Enter your College Name : ") #Input College Name
caddress = input("Enter your College Address : ") #Input College Address
city = input("Enter your City : ") #Your City
state = input("Enter yout State : ") #Your State
# Take subject marks and calcultae marks
subjects = []
subjects = [int(x) for x in (input("Enter Marks in 5 Subjects (Out of 100) : ").split())]
total = person.marks(subjects)
no_of_subjects = len(subjects)
##print(type(subjects))
# Printing
print("=+" * 30 + '\n' + "Marksheet : ")
print("Name        : " + person.concat_name())
print("College     : " + person.college(cname,caddress,city,state))
print("Total Marks : " + str(total))
print("Percentage  : " + str(total/no_of_subjects))

print("=+" * 30)
