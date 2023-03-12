import math
import numpy
import curses
from curses.textpad import rectangle
import time

all_student = []
all_course = []
all_mark = []

class Student():
    def __init__(self, top_right_window, bot_window):
        top_right_window.erase()
        top_right_window.addstr(f"Student #{len(all_student)+1}\n")
        top_right_window.addstr("-Enter name: ")
        top_right_window.refresh()
        bot_window.erase()
        self.__name = str(bot_window.getstr().strip())[2:-1]
        top_right_window.addstr(f"{self.__name}\n")

        top_right_window.addstr("-Enter id: ")
        top_right_window.refresh()
        bot_window.erase()
        self.__id = str(bot_window.getstr().strip())[2:-1]
        top_right_window.addstr(f"{self.__id}\n")

        top_right_window.addstr("-Enter DoB: ")
        top_right_window.refresh()
        bot_window.erase()
        self.__DoB = str(bot_window.getstr().strip())[2:-1]
        top_right_window.addstr(f"{self.__DoB}\n")
        top_right_window.refresh()
        time.sleep(0.5)

        self.__GPA = 0

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_DoB(self):
        return self.__DoB
    
    def set_GPA(self, value):
        self.__GPA = value

    def get_GPA(self):
        return self.__GPA
    
class Course():
    def __init__(self, top_right_window, bot_window):
        top_right_window.erase()
        top_right_window.addstr(f"Course #{len(all_course)+1}\n")
        top_right_window.addstr("-Enter name: ")
        top_right_window.refresh()
        bot_window.erase()
        self.__name = str(bot_window.getstr().strip())[2:-1]
        top_right_window.addstr(f"{self.__name}\n")

        top_right_window.addstr("-Enter id: ")
        top_right_window.refresh()
        bot_window.erase()
        self.__id = str(bot_window.getstr().strip())[2:-1]
        top_right_window.addstr(f"{self.__id}\n")
        top_right_window.refresh()
        time.sleep(0.5)

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

class Mark():
    def __init__(self, top_right_window, bot_window):
        #Check if this course exists or not
        course_id_state = True
        while course_id_state:
            top_right_window.erase()
            top_right_window.addstr("-Enter course id: ")
            top_right_window.refresh()
            bot_window.erase()
            self.__course_id = str(bot_window.getstr().strip())[2:-1]
            top_right_window.addstr(f"{self.__course_id}\n")
            for i in range(len(all_course)):
                if all_course[i].get_id() == self.__course_id:
                    course_id_state = False
                    break
            if course_id_state == True:
                top_right_window.addstr("This course doesn't exist")
                top_right_window.refresh()
                time.sleep(0.5)

        #Same as above but for student
        student_id_state = True
        while student_id_state:
            top_right_window.move(1, 0)
            top_right_window.clrtoeol()
            top_right_window.move(2, 0)
            top_right_window.clrtoeol()
            top_right_window.addstr(1, 0, "-Enter student id: ")
            top_right_window.refresh()
            bot_window.erase()
            self.__student_id = str(bot_window.getstr().strip())[2:-1]
            top_right_window.addstr(f"{self.__student_id}\n")
            for i in range(len(all_student)):
                if all_student[i].get_id() == self.__student_id:
                    student_id_state = False
                    break
            if student_id_state == True:
                top_right_window.addstr("This student doesn't exist")
                top_right_window.refresh()
                time.sleep(0.5)

        #check for mark to be in [0,20]
        while True:
            top_right_window.move(2, 0)
            top_right_window.clrtoeol()
            top_right_window.addstr("-Enter mark: ")
            top_right_window.refresh()
            bot_window.erase()
            try:
                dummy = float(bot_window.getstr().strip())
                self.__mark = math.floor(dummy * 10) / 10
            except:
                top_right_window.addstr("Invalid!")
                top_right_window.refresh()
                time.sleep(0.5)
            else:
                if type(self.__mark) == float and self.__mark >= 0 and self.__mark <= 20:
                    top_right_window.addstr(f"{self.__mark}\n")
                    break
                else:
                    top_right_window.addstr("Must be in range [0; 20]!")
                    top_right_window.refresh()
                    time.sleep(0.5)
        top_right_window.addstr("Enter mark done!")
        top_right_window.refresh()
        time.sleep(0.5)

    def get_course_id(self):
        return self.__course_id
    
    def get_student_id(self):
        return self.__student_id
    
    def get_mark(self):
        return self.__mark

#Enter student info for the 1st time
def initialize_students(top_left_window, top_right_window, bot_window):
    while True:
        bot_window.clear()
        bot_window.refresh()
        top_right_window.clear()
        top_right_window.addstr("Enter number of student: ")
        top_right_window.refresh()
        try:
            num_of_student = int(bot_window.getstr().strip())
        except:
            top_right_window.addstr("Invalid!")
            top_right_window.refresh()
            time.sleep(0.5)
        else:
            if type(num_of_student) == int and num_of_student > 0:
                break
            else:
                top_right_window.addstr("Invalid!")
                top_right_window.refresh()
                time.sleep(0.5)
    top_left_window.addstr(f"Total students: {num_of_student}\n")
    top_left_window.refresh()
    for i in range(num_of_student):
        add_student(top_right_window, bot_window)
    top_left_window.addstr("Initialize students done!\n")
    top_left_window.refresh()

#Enter student info once
def add_student(top_right_window, bot_window):
    top_right_window.clear()
    top_right_window.refresh()
    all_student.append(Student(top_right_window, bot_window))

#Enter courses for the 1st time
def initialize_courses(top_left_window, top_right_window, bot_window):
    while True:
        bot_window.clear()
        bot_window.refresh()
        top_right_window.clear()
        top_right_window.addstr("Enter number of courses: ")
        top_right_window.refresh()
        try:
            num_of_course = int(bot_window.getstr().strip())
        except:
            top_right_window.addstr("Invalid!")
            top_right_window.refresh()
            time.sleep(0.5)
        else:
            if type(num_of_course) == int and num_of_course > 0:
                break
            else:
                top_right_window.addstr("Invalid!")
                top_right_window.refresh()
                time.sleep(0.5)
    top_left_window.addstr(f"Total courses: {num_of_course}\n")
    top_left_window.refresh()
    for i in range(num_of_course):
        add_course(top_right_window, bot_window)
    top_left_window.addstr("Initialize courses done!\n")
    top_left_window.refresh()

#Enter course info once
def add_course(top_right_window, bot_window):
    top_right_window.clear()
    top_right_window.refresh()
    all_course.append(Course(top_right_window, bot_window))

#Enter mark for a specific student in a specific course
def add_mark(top_right_window, bot_window):
    all_mark.append(Mark(top_right_window, bot_window))

#Show all students
def list_students(top_right_window):
    top_right_window.erase()
    for Student in all_student:
        top_right_window.addstr(f"Student name: {Student.get_name()} ,id: {Student.get_id()}, DoB: {Student.get_DoB()}, GPA: {Student.get_GPA()}\n")
        top_right_window.refresh()

#Show all courses
def list_courses(top_right_window):
    top_right_window.erase()
    for Course in all_course:
        top_right_window.addstr(f"Course name: {Course.get_name()} ,id: {Course.get_id()}\n")
        top_right_window.refresh()

#Calculate GPA of all students and then sort all students by GPA
def sort_GPA(top_right_window):
    top_right_window.erase()
    if len(all_mark) != 0:
        for Student in all_student:
            temporary = []
            for Mark in all_mark:
                if Student.get_id() == Mark.get_student_id():
                    temporary.append(Mark.get_mark())
            Student.set_GPA(math.floor(float(numpy.average(temporary) * 10)) / 10)

        if len(all_student) == 1:
            top_right_window.addstr("Only 1 student, please add more!")
        else:
            for i in range(len(all_student)-1):
                if all_student[i].get_GPA() < all_student[i+1].get_GPA():
                    dum = all_student[i]
                    all_student[i] = all_student[i+1]
                    all_student[i+1] = dum
                top_right_window.addstr("Sort done!")
    else:
        top_right_window.addstr("There are no marks!")
    top_right_window.refresh()

#Search mark for a specific student in a specific course
def search_mark(top_right_window, bot_window):
    top_right_window.erase()
    if len(all_mark) == 0:
        top_right_window.addstr("There are no marks yet!")
        top_right_window.refresh()
    else:
        #check for the course and save the index of all the result
        course_id_state = True
        while course_id_state:
            top_right_window.erase()
            top_right_window.addstr("Enter course id: ")
            top_right_window.refresh()
            bot_window.erase()
            search_course = str(bot_window.getstr().strip())[2:-1]
            top_right_window.addstr(f"{search_course}\n")
            for i in range(len(all_course)):
                if all_course[i].get_id() == search_course:
                    course_id_state = False
                    break
            if course_id_state == True:
                top_right_window.addstr("This course doesn't exist")
                top_right_window.refresh()
                time.sleep(0.5)

        indexes = []
        for i in range(len(all_mark)):
            if all_mark[i].get_course_id() == search_course:
                indexes.append(i)
        if len(indexes) == 0:
            top_right_window.addstr("This course doesn't exist or don't have any marks yet")
            top_right_window.refresh()
        else:
            #check for the student and remove the result that satisfies
            top_right_window.addstr("Enter student id: ")
            top_right_window.refresh()
            search_student= str(bot_window.getstr().strip())[2:-1]
            top_right_window.addstr(f"{search_student}\n")
            not_found = True
            for i in indexes:
                if all_mark[i].get_student_id() == search_student:
                    top_right_window.addstr(f"Mark #{i+1}: {all_mark[i].get_mark()}\n")
                    top_right_window.refresh()
                    not_found = False
            if not_found:
                top_right_window.addstr("This student doesn't exist or doesn't have any mark yet")
                top_right_window.refresh()

#Creating an user interface
def main_menu(current_choice, top_left_window):
    top_left_window.clear()
    top_left_window.addstr('''Please select what to do next:
1: Input mark
2: Show students
3: Show courses
4: Show mark of a student
5: Calculate GPA and sort
0: exit
Enter your choice: ''')
    top_left_window.refresh()
    try:
        current_choice = int(top_left_window.getstr().strip())
    except:
        current_choice = -1
    return current_choice

#Main function
def main(stdscr):
    curses.echo()
    stdscr.clear() 
    top_left_window = curses.newwin(20, 50, 2, 2)
    top_right_window = curses.newwin(20, 50, 2, 53)
    bot_window = curses.newwin(6, 100, 23, 2)
    rectangle(stdscr, 1, 1, 22, 52)
    rectangle(stdscr, 1, 52, 22, 103)
    rectangle(stdscr, 22, 1, 29, 103)
    stdscr.refresh()

    top_left_window.addstr("Initializing students and courses.....\n")
    top_left_window.refresh()
    initialize_students(top_left_window, top_right_window, bot_window)
    initialize_courses(top_left_window, top_right_window, bot_window)
    top_left_window.addstr("Initialize complete!\n")
    top_left_window.refresh()
    time.sleep(1.5)
    current_choice = 0
    current_choice = main_menu(current_choice, top_left_window)

    while current_choice!= 0:
        match current_choice:
            case 1:
                add_mark(top_right_window, bot_window)
                current_choice = main_menu(current_choice, top_left_window)
            case 2: 
                list_students(top_right_window)
                current_choice = main_menu(current_choice, top_left_window)
            case 3:
                list_courses(top_right_window)
                current_choice = main_menu(current_choice, top_left_window)
            case 4:
                search_mark(top_right_window, bot_window)
                current_choice = main_menu(current_choice, top_left_window)
            case 5:
                sort_GPA(top_right_window)
                current_choice = main_menu(current_choice, top_left_window)
            case _:
                top_left_window.addstr("Invalid choice!")
                top_left_window.refresh()
                time.sleep(0.5)
                current_choice = main_menu(current_choice, top_left_window)
    if current_choice == 0:
        print("Exited program")

curses.wrapper(main)