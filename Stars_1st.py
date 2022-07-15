# star : n(n+1)/2 = s
# spaces : n-1
class formula:
    def set_var(self , num1):
        self.num1 = num1
    def odd_formula(self):
        x = self.num1
        result = (2 * x) - 1
        return int(result)
class running:
    def set_var(self,num1):
        self.num1 = num1
    def returning(self):
        y = self.num1
        spaces = y
        obj_f = formula()
        for i in range(1 , y+1):
            obj_f.num1 = i
            spaces = spaces - 1
            print(spaces * " " , end="")
            print(obj_f.odd_formula() * "*")


#getting input
obj = running()


#Printing Summary of the work of the app
print("   *")
print("  ***")
print(" *****")
print("*******")
#print("\n")
print("_______")
print("This is example of output. the number of column is 4")


try:

    #input
    obj.num1 = int(input("Enter number of column : "))

    #the number size
    if obj.num1 > 1000 :
        inp_l = input("This number is very large. Do you wanna continue [y/n]")
        if inp_l == "y" or inp_l == "Y":
            obj.returning()
        elif inp_l == "n" or inp_l == "N":
            print("Good bye!")
        else:
            print("Error")
    else:
        obj.returning()
except:
    print("Error")