import time
import math
import numpy

#Search mark for a specific student in a specific course
def search_mark(top_right_window, bot_window, all_mark, all_course):
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

#Calculate GPA of all students and then sort all students by GPA
def sort_GPA(top_right_window, all_mark, all_student):
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

#Show all students
def list_students(top_right_window, all_student):
    top_right_window.erase()
    for Student in all_student:
        top_right_window.addstr(f"Student name: {Student.get_name()} ,id: {Student.get_id()}, DoB: {Student.get_DoB()}, GPA: {Student.get_GPA()}\n")
        top_right_window.refresh()

#Show all courses
def list_courses(top_right_window, all_course):
    top_right_window.erase()
    for Course in all_course:
        top_right_window.addstr(f"Course name: {Course.get_name()} ,id: {Course.get_id()}\n")
        top_right_window.refresh()