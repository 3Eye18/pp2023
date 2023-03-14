import time
import math

class Student():
    def __init__(self, top_right_window, bot_window, all_student):
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
    def __init__(self, top_right_window, bot_window, all_course):
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
    def __init__(self, top_right_window, bot_window, all_course, all_student):
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