# creating class and objects

# class Student:
#     name = "prathmesh"
#     id = 101
# s1 = Student()
# print(s1.name, s1.id)

# creating init function
# class Stud:
#     def __init__(self,name):
#         self.name = name

# s1= Stud("prathmesh")
# print(s1.name)


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hii", self.name,"Your Avg Score is :",sum/3)

s1 = Student("prathmesh", [88,87,86])
s1.get_avg()        
    



