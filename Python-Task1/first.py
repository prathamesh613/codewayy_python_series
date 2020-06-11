print("=+" * 30) # Asthetics
# Operations on Numbers
class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        # Assign num1 and num2
    #Addition
    def add(self):
        return num1 + num2
    #Subtraction
    def sub(self):
        return num1 - num2
    #Subtraction with absolute value
    def sub_abs(self):
        return abs(num1 - num2)
    #Multiplication
    def mul(self):
        return num1 * num2
    #Division
    def div(self):
        return (num1/num2)
    #Division with floor value
    def div_floor(self):
        return num1//num2
    #Exponent
    def pow(self):
        return num1 ** num2

#Integers
print("Integers".upper())

num1, num2 = (int(x) for x in input("Enter Two Integers : ").split())
# Input 2 Numbers and perform operations
Int = Numbers(num1, num2)
integer_operations = {'Addition' : Int.add(), 'Subtraction' : Int.sub(), 'Absolute_Subtracion' : Int.sub_abs(),
                'Multiplication' : Int.mul(), 'Division' : Int.div(), 'Floor_Division' : Int.div_floor(),
                'Power' : Int.pow()}
# print(help({})) #Taking Help from Dictionary Class
# Print All Integer Operations
print(integer_operations)
print("=+" * 30) # Asthetics

#Floating Point Numbers
print("Floating Point Numbers".upper())

num1, num2 = (float(x) for x in input("Enter Two Floating Point Numbers : ").split())
Float = Numbers(num1, num2)
floating_operations = {'Addition' : Float.add(), 'Subtraction' : Float.sub(), 'Absolute_Subtracion' : Float.sub_abs(),
                'Multiplication' : Int.mul(), 'Division' : Float.div(), 'Floor_Division' : Float.div_floor(),
                'Power' : Float.pow()}
print(floating_operations)
print("=+" * 30) # Asthetics
