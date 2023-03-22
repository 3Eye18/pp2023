import time, pickle
from domains import Student, Course, Mark

#Enter courses for the 1st time
def initialize_courses(top_left_window, top_right_window, bot_window, all_course):
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
        add_course(top_right_window, bot_window, all_course)
    top_left_window.addstr("Initialize courses done!\n")
    top_left_window.refresh()

#Enter course info once
def add_course(top_right_window, bot_window, all_course):
    top_right_window.clear()
    top_right_window.refresh()
    new_course = Course("", "")
    new_course.input_name(top_right_window, bot_window, all_course)
    new_course.input_id(top_right_window, bot_window, all_course)
    all_course.append(new_course)
    #write course info into courses.txt
    name = new_course.get_name()
    id = new_course.get_id()
    f = open("./courses.txt","a")
    f.write(f"c: {name} | {id}\n")
    f.close()

#Enter student info for the 1st time
def initialize_students(top_left_window, top_right_window, bot_window, all_student):
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
        add_student(top_right_window, bot_window, all_student)
    top_left_window.addstr("Initialize students done!\n")
    top_left_window.refresh()
    

#Enter student info once
def add_student(top_right_window, bot_window, all_student):
    top_right_window.clear()
    top_right_window.refresh()
    new_student = Student("", "", "", 0.0)
    new_student.input_name(top_right_window, bot_window, all_student)
    new_student.input_id(top_right_window, bot_window, all_student)
    new_student.input_dob(top_right_window, bot_window)
    all_student.append(new_student)
    #write student info into students.txt
    name = new_student.get_name()
    id = new_student.get_id()
    dob = new_student.get_dob()
    gpa = new_student.get_gpa()
    f = open(f"./students.txt","a")
    f.write(f"s: {name} | {id} | {dob} | {gpa}\n")
    f.close()

#Enter mark for a specific student in a specific course
def add_mark(top_right_window, bot_window, all_course, all_student, all_mark):
    new_mark = Mark("", "", 0.0)
    new_mark.input_course_id(top_right_window, bot_window, all_course)
    new_mark.input_student_id(top_right_window, bot_window, all_student)
    new_mark.input_mark(top_right_window, bot_window)
    all_mark.append(new_mark)
    #write mark info into marks.txt
    course_id = new_mark.get_course_id()
    student_id = new_mark.get_student_id()
    mark = new_mark.get_mark()
    f = open("./marks.txt","a")
    f.write(f"m: {course_id} | {student_id} | {mark}\n")
    f.close()

#Creating an user interface
def main_menu(current_choice, top_left_window):
    top_left_window.clear()
    top_left_window.addstr('''Please select what to do next:
1: Add a mark for a student in a course
2: Add a student
3: Add a course
4: Show all students
5: Show all courses
6: Show all marks of a student in a course
7: Calculate gpa and sort student descendingly by gpa
0: exit
Enter your choice: ''')
    top_left_window.refresh()
    try:
        current_choice = int(top_left_window.getstr().strip())
    except:
        current_choice = -1
    return current_choice

#decompress using pickle
def decompress():
    with open('data.pkl', 'rb') as f2:
        all_student, all_course, all_mark = pickle.load(f2)
        return all_student, all_course, all_mark