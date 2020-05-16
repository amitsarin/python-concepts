data_valid=False
while data_valid == False:
    grade1=input("type the grade of first test: ")
    try:
        grade1=float(grade1)
    except:
        print("invalid input. only number is accepted")
        continue
    if grade1<0 or grade1>10:
        print("grade should be between 0 and 10")
        continue
    else:
        data_valid=True

data_valid=False
while data_valid == False:
    grade2=input("type the grade of second test: ")
    try:
        grade2=float(grade2)
    except:
        print("invalid input. Only numbers is accepted")
        continue
    if grade2<0 or grade2>10:
        print("grade should be between 0 and 10")
        continue
    else:
        data_valid=True
        
data_valid=False
while data_valid == False:
    total_classes=int(input("input the total number of classes: "))
    if total_classes<=0:
        print("total classes should be greater than 0")
        continue
    else:
        data_valid=True
        
data_valid=False
while data_valid == False:
    absences=int(input("input the number of absences: "))
    if absences<0 or absences >total_classes:
        print("absences cant be less than 0 or greater than total classes")
        continue
    else:
        data_valid=True        

avg_grade= (grade1+grade2)/2
attendence= (total_classes-absences)/total_classes

print("average grade: ", round(avg_grade,2))
print("attendence rate: ", str(round((attendence*100),2))+"%")

if(avg_grade >=6 and attendence >= 0.8):
    print(" student is approved: ")
elif(avg_grade < 6 and attendence < 0.8):
    print("failed due to average grade less than 6 and less attendence")
elif(attendence >=0.8):
    print(" failed due to average grade less than 6")
else:
    print(" failed due to less attendence")
