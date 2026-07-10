# Attendance Shortage Alert — Capstone Project
# Complete this file by following docs/STUDENT_GUIDE.md

DATA_FILE = "data/students.txt"
SHORTAGE_LIMIT = 75


# Calculate average attendance from a list like ["English:60", "Maths:72"]
def calculate_average(subject_list):
    # Your code will go here
    pass


# Print each subject with OK or SHORTAGE WARNING if below 75%
def check_shortage(subject_list):
    # Your code will go here
    pass


# Ask for student details and save one line to the file (type 'done' to go back)
def add_student():
     while True:
        roll = input("\nRoll no (or 'done' to go back): ")
        if roll == "done":
            break


        name   = input("Name   : ")
        stream = input("Stream : ")
        n      = int(input("Number of subjects: "))


        subjects = []
        for i in range(n):
            sub = input("  Subject name : ")
            pct = input("  Attendance % : ")
            subjects.append(sub + ":" + pct)

        subjects_str = " ".join(subjects )
        line = roll+" "+name+" "+stream+" "+subjects_str
        with open(DATA_FILE, "a") as f:
            f.write(line + "\n")
        print("Record saved for", name)
# Search student by roll number and show attendance report
def search_student():
    # Your code will go here
    pass

# Show main menu and handle user choice in a loop
def main():
  while True:
    print("\n===attendence alert system===")
    print("1.add student record")
    print("2.search student")
    print("3.exit")
    choice=input("enter choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        print("you chiced 2")
    elif choice=="3":
        print("goodbye!")
        break
    else:
        print("invalid choice.please enter 1,2 or 3.")
        
if __name__ == "__main__":
    main()
