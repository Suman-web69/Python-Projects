# print("STUDENT MANAGEMENT SYSTEM")

# import os
# import json

# students={}
# if os.path.exists("info.json"):
#    with open("info.json","r") as f :
#       rd=json.load(f)
#       for rol,info1 in rd.items():
#         #  print((roll,info))                
#             students[rol]=info1
        
# if not os.path.exists("info.json") :
#    students={1:{"Ramu":45},2:{"Gyanu":78}}

#    with open("info.json","w") as g :
#       wd=json.dump(students,g)   

# class Student:
#     def __init__(self,name,marks,roll):
#         self.name=name
#         self.marks=marks
#         self.roll=roll
                            
#         students[self.roll]={self.name:self.marks}
          
#     def display(self):
#         return (self.roll,{self.name:self.marks})
    
# print("Adding Student ")
# nam=input('Enter Student Name("Enter q if not Adding):')
# if nam.lower()!="q":
#  mark=int(input("Enter Student Marks:"))
#  rollno=int(input("Enter Roll No:"))
#  s1=Student(nam,mark,rollno)
#  with open("info.json","w") as e:
#          json.dump(students,e)
# print(f"Student Successfully Added:info-{s1.display()}")


# print("Searching Student.")
# search=int(input("Enter Roll No to search"))
# with open("info.json","r") as p :
#       pd=json.load(p)
#       found=False
#       for roll,inf in pd.items():
#             roll=int(roll)
#             if roll==search:
#                found=True
#                print(f"Student Found..(info)={inf}")
#                break
# if not found:
#              print("Not found first Add ")

# print("Deleting Student..")
# delete=int(input("Enter Student Roll No to Delete:"))
# try:
#  with open("info.json","r") as q :
#       qd=json.load(q)
# except FileNotFoundError:
#       qd={}
#       found=False
# for rollo,infoo in qd.items():
         
#             rollo=int(rollo)
#             if rollo==delete:
#                found=True
#                qd.pop(rollo)
#                print(f'Student wit Roll No{rollo} deleted.')
#                with open("info.json","w") as zx:
#                   json.dump(qd,zx)
#                   break
# if not found:
#     print("Student Doesn't Exists.")


            
               
   

















