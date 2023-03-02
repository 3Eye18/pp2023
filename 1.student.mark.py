all_students = []
all_courses = []
all_marks = []

#Input student info
def input_student():
    for i in range(int(input("Enter number of students: "))):
        student = []
        student.append(input("-Enter student id: "))
        student.append(input("-Enter student name: "))
        student.append(input("-Enter student dob: "))
        print(f"-Entered student: {student[0]} {student[1]} {student[2]}")
        all_students.append(student)

#Input courses
def input_course():
    for i in range(int(input("Enter number of courses: "))):
        course = []
        course.append(input("-Enter course id: "))
        course.append(input("-Enter course name: "))
        all_courses.append(course)

#Select a course, input marks for student in this course
def input_mark():
    search_course = input("-Enter course id: ")
    found_course = False
    found_student = False
    for course in all_courses:
        if course[0] == search_course:
            found_course = True
            mark = []
            search_student = input("-Enter student id:")
            for student in all_students:
                if student[0] == search_student:
                    found_student = True
                    mark.append(search_course)
                    mark.append(search_student)
                    mark.append(float(input("-Enter mark: ")))
                    all_marks.append(mark)
                    break
            if found_student == False:
                print("There is no such student in the class!")
            break
    if found_course == False:
        print("There is no such course in the curriculum!")

#Show students
def show_students():
    for student in all_students:
        print(f"{student[0]} {student[1]} {student[2]}")

#Show courses
def show_courses():
    for course in all_courses:
        print(f"{course[0]} {course[1]}")

#Show student mark for a given course
def show_student_mark():
    if len(all_marks) != 0:
        search_course = input("-Enter course id: ")
        found_course = False
        found_student = False
        found_mark = False
        for course in all_courses:
            if course[0] == search_course:
                found_course = True
                search_student = input("-Enter student id:")
                for student in all_students:
                    if student[0] == search_student:
                        found_student = True
                        for mark in all_marks:
                            if (mark[0] == search_course) and (mark[1] == search_student):
                                found_mark = True
                                print(f"Student {search_student}'s mark in course {search_course} is: {mark[2]}")
                                break
                        if found_mark == False:
                            print(f"Student {search_student} has no marks in course {search_course} yet")
                            break
                if found_student == False:
                    print("There is no such student in the class!")
                    break
            if found_course == False:
                print("There is no such course in the curriculum!")
    else:
        print("There are no marks in the database yet! Please enter mark first!")

def main_menu(current_choice):
    current_choice = int(input('''
Please select what to do next:
1: Input mark
2: Show students
3: Show courses
4: Show mark
0: exit
Enter your choice: '''))
    return current_choice

if __name__ == "__main__":
    print("Initializing class and curriculum.....")
    input_student()
    input_course()
    print("Initialize complete!")
    current_choice = 0
    current_choice = main_menu(current_choice)
    while current_choice!= 0:
        match current_choice:
            case 1:
                input_mark()
                current_choice = main_menu(current_choice)
            case 2: 
                show_students()
                current_choice = main_menu(current_choice)
            case 3:
                show_courses()
                current_choice = main_menu(current_choice)
            case 4:
                show_student_mark()
                current_choice = main_menu(current_choice)
            case _:
                print("Invalid choice!")
                current_choice = main_menu(current_choice)
    if current_choice == 0:
        print("Exited program")
