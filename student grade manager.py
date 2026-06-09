student={
    "ram":90,
    "sita":95,
    "gits":56,
}
higest=0
higest_student=""
while True:
 quetion=input("do you want to add a student (yes/no):")
 if quetion.lower() == "yes":
    name2=input("enter the name of student :")
    student[name2]=int(input("enter the marks of student: "))
    print(student)
 else:
    break
while True:
 question2=input("Do you want to remove student (yes/no):")
 
 if question2.lower() == "yes":
    q2=input("which student you want to remove:")
    if q2 in student:
     student.pop(q2)
     print(student)
    else:
       print("student doesnt exixt:")
 else:
    break
for i,j in student.items():
    if j>higest:
        higest=j
        higest_student=i
print(f"the higest grade is {higest} scored by {higest_student}")
avg=0
n=0
for i,j in student.items():
    avg=j+avg
    n+=1
average=avg/n
print("the average grade is ",average)

name=input("you want to check the grade of which student :")
print(f"the grade of {name} is {student[name]}")

