all_student = []
all_course = []
all_mark = []

class Student():
    def __init__(self):
        self.__name = input("-Enter name: ")
        self.__id  = input("-Enter id: ")
        self.__DoB  = input("-Enter DoB: ")

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_DoB(self):
        return self.__DoB
    
class Course():
    def __init__(self):
        self.__name = input("-Enter name: ")
        self.__id = input("-Enter id: ")

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

class Mark():
    def __init__(self):
        #Check if this course exists or not
        course_id_state = True
        while course_id_state:
            self.__course_id = input("Enter course id: ")
            for i in range(len(all_course)):
                if all_course[i].get_id() == self.__course_id:
                    course_id_state = False
                    break
            if course_id_state == True:
                print("This course doesn't exist")

        #Same as above but for student
        student_id_state = True
        while student_id_state:
            self.__student_id = input("Enter student id: ")
            for i in range(len(all_student)):
                if all_student[i].get_id() == self.__student_id:
                    student_id_state = False
                    break
                if student_id_state == True:
                    print("This student doesn't exist")

        self.__mark = input("Enter mark: ")
    
    def get_course_id(self):
        return self.__course_id
    
    def get_student_id(self):
        return self.__student_id
    
    def get_mark(self):
        return self.__mark

def input_students():
    num_of_student = int(input("Enter number of student: "))
    for i in range(num_of_student):
        print(f"Student #{i+1}")
        all_student.append(Student())

def input_courses():
    num_of_course = int(input("Enter number of course: "))
    for i in range(num_of_course):
        print(f"Course #{i+1}")
        all_course.append(Course())

def input_mark():
    all_mark.append(Mark())

def list_students():
    for Student in all_student:
        print(f"Student name: {Student.get_name} ,id: {Student.get_id}, DoB: {Student.get_DoB}")

def list_courses():
    for Course in all_course:
        print(f"Course name: {Course.get_name} ,id: {Course.get_id}")

def search_mark():
    if len(all_mark) == 0:
        print("There are no marks yet!")
    else:
        #check for the course and save the index of all the result
        search_course = input("Enter course id")
        indexes = []
        for i in range(len(all_course)):
            if all_mark[i].get_course_id() == search_course:
                indexes.append(i)
        if len(indexes) == 0:
            print("This course doesn't exist or don't have any marks yet")
        else:
            #check for the student and remove the result that satisfies
            before_search_student = len(indexes)
            search_student = input("Enter student id: ")
            for i in indexes:
                if all_mark[i].get_student_id() == search_student:
                    print(f"This student mark: {all_mark[i].get_mark()}")
                    indexes.remove(i)
                if len(indexes) == before_search_student:
                    print("This student doesn't exist or doesn't have any mark yet")

#creating an user interface (i think?)
def main_menu(current_choice):
    current_choice = int(input('''
Please select what to do next:
1: Input mark
2: Show students
3: Show courses
4: Show mark of a student
0: exit
Enter your choice: '''))
    return current_choice

if __name__ == "__main__":
    print("Initializing students and courses.....")
    input_students()
    input_courses()
    print("Initialize complete!")
    current_choice = 0
    current_choice = main_menu(current_choice)
    while current_choice!= 0:
        match current_choice:
            case 1:
                input_mark()
                current_choice = main_menu(current_choice)
            case 2: 
                list_students()
                current_choice = main_menu(current_choice)
            case 3:
                list_courses()
                current_choice = main_menu(current_choice)
            case 4:
                search_mark()
                current_choice = main_menu(current_choice)
            case _:
                print("Invalid choice!")
                current_choice = main_menu(current_choice)
    if current_choice == 0:
        print("Exited program")

