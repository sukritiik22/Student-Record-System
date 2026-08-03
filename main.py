class Student:
    def __init__(self, Name, RollNumber, CGPA):
        self.Name = Name
        self.RollNumber = RollNumber
        self.CGPA = CGPA

studentlist = []
branches = ["EE", "MT", "CS", "ME", "CE", "TT"]

def valid_roll_number(roll):
    if(len(roll) == 10 and roll[0:4] == "2022" and (roll[4:6] in branches) and (roll[6:10].isdigit()) and (int(roll[6:10]) > 0) and  (int(roll[6:10]) < 1800)):
        return True
    
    return False
    

while(True):
    print("====== Student Record System ======\n\n1. Add Student\n2. Display Students\n3. Search Student\n4. Delete Student\n5. Exit")

    a = input()

    if(a != "1" or a != "2" or a != "3" or a != "4" or a != "5"):
        print("Enter Valid Input")
        continue

    a = int(a)

    if(a == 1):
        print("Enter Name")
        name = input()

        print("Enter Roll Number")
        roll = input()

        valid_roll = False

        for i in range(1,6):
            if(valid_roll_number(roll)):
                valid_roll = True
                break

            else:
                print("Enter a valid roll number\nIt should be 2022 Entry with a valid branch and following number")
                roll = input()            
    
        if not valid_roll:
            print("Too many invalid attempts")
            continue

        existing = False

        for val in studentlist:
            if roll == val.RollNumber:
                existing = True
        
        if existing:
            print("This user already exists")
            continue

        print("Enter CGPA")
        cgpa = float(input())

        valid_cg = False

        for i in range(1,6):
            if(cgpa >= 0 and cgpa <= 10):
                valid_cg = True
                break

            else:
                print("Enter a valid cgpa")
                cgpa = float(input())           
    
        if not valid_cg:
            print("Too many invalid attempts")
            continue

        s1 = Student(name, roll, cgpa)
        studentlist.append(s1)



    elif(a == 2):
        if(len(studentlist) == 0):
            print("No Students Found")
        else:
            for val in studentlist:
                print("Name:", val.Name, "RollNo:", val.RollNumber, "CGPA:", val.CGPA)
            

    elif(a == 3):
        print("Enter the name and roll no of the student to be searched")
        x = input()

        found = False

        for val in studentlist:
            if(val.RollNumber == x):
                print("Student Found")
                print("Name:", val.Name, "RollNo:", val.RollNumber, "CGPA:", val.CGPA)
                found = True
                break
            
        if(found == False):
            print("Student Not Found")

            

    elif(a == 4):
        print("Enter the name and roll no of the student to be deleted")
        x = input()

        found = False

        for val in studentlist:
            if(val.RollNumber == x):
                found = True
                studentlist.remove(val)
                break

        if(found == False):
            print("Enter a valid student to be deleted")

    elif(a == 5):
        break