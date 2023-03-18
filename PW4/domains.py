import time, math

class Student():
    def __init__(self, name, id, dob, gpa):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__gpa = gpa

    def input_name(self, top_right_window, bot_window, all_student):
        top_right_window.erase()
        top_right_window.addstr(f"Student #{len(all_student)+1}\n")
        top_right_window.addstr("-Enter name: ")
        top_right_window.refresh()
        bot_window.erase()
        self.__name = str(bot_window.getstr().strip())[2:-1]
        top_right_window.addstr(f"{self.__name}\n")
        top_right_window.refresh()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    #ID input and check for existence
    def input_id(self, top_right_window, bot_window, all_student):
        id_existed = True
        while id_existed:
            top_right_window.move(2, 0)
            top_right_window.clrtoeol()
            top_right_window.addstr("-Enter id: ")
            top_right_window.refresh()
            bot_window.erase()
            self.__id = str(bot_window.getstr().strip())[2:-1]
            id_existed = False
            if len(all_student)!=0:
                for Student in all_student:
                    if Student.get_id() == self.__id:
                        id_existed = True
                        top_right_window.addstr("This ID already exists!")
                        top_right_window.refresh()
                        time.sleep(0.5)
        top_right_window.addstr(f"{self.__id}\n")
        top_right_window.refresh()

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    #dob enter (year, month then date) and check for error
    def input_dob(self, top_right_window, bot_window):
        #year
        year = 0
        while True:
            top_right_window.move(3, 0)
            top_right_window.clrtoeol()
            top_right_window.addstr("-Enter year (from 1950 to 2023): ")
            top_right_window.refresh()
            bot_window.erase()
            try:
                year = int(bot_window.getstr().strip())
            except:
                top_right_window.addstr("Not an integer!")
                top_right_window.refresh()
                time.sleep(0.5)
            else:
                if year >= 1950 and year <= 2023:
                    top_right_window.addstr(f"{year}\n")
                    break
                else:
                    top_right_window.addstr("Invalid!")
                    top_right_window.refresh()
                    time.sleep(0.5)
        #month
        month = 0
        while True:
            top_right_window.move(4, 0)
            top_right_window.clrtoeol()
            top_right_window.addstr("-Enter month (from 1 to 12): ")
            top_right_window.refresh()
            bot_window.erase()
            try:
                month = int(bot_window.getstr().strip())
            except:
                top_right_window.addstr("Not an integer!")
                top_right_window.refresh()
                time.sleep(0.5)
            else:
                if month >= 1 and month <= 12:
                    top_right_window.addstr(f"{month}\n")
                    break
                else:
                    top_right_window.addstr("Invalid!")
                    top_right_window.refresh()
                    time.sleep(0.5)
        #date
        date = 0
        while True:
            top_right_window.move(5, 0)
            top_right_window.clrtoeol()
            top_right_window.addstr("-Enter date: ")
            top_right_window.refresh()
            bot_window.erase()
            try:
                date = int(bot_window.getstr().strip())
            except:
                top_right_window.addstr("Not an integer!")
            else:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    if date >= 1 and date <= 31:
                        top_right_window.addstr(f"{date}\n")
                        break
                    else:
                        top_right_window.addstr("Invalid!")
                if month in [4, 6, 9, 11]:
                    if date >= 1 and date <= 30:
                        top_right_window.addstr(f"{date}\n")
                        break
                    else:
                        top_right_window.addstr("Invalid!")
                if month == 2:
                    if year % 4 == 0:
                        if date >= 1 and date <= 29:
                            top_right_window.addstr(f"{date}\n")
                            break
                        else:
                            top_right_window.addstr("Invalid!")
                    else:
                        if date >= 1 and date <= 28:
                            top_right_window.addstr(f"{date}\n")
                            break
                        else:
                            top_right_window.addstr("Invalid!")   
            top_right_window.refresh()
            time.sleep(0.5)
        self.__dob = f"{date}/{month}/{year}"

    def set_dob(self, dob):
        self.__dob = dob

    def get_dob(self):
        return self.__dob
    
    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa
    
class Course(): 
    def __init__(self, name, id):
        self.__name = name          
        self.__id = id
    
    def input_name(self, top_right_window, bot_window, all_course):
        top_right_window.erase()
        top_right_window.addstr(f"Course #{len(all_course)+1}\n")
        top_right_window.addstr("-Enter name: ")
        top_right_window.refresh()
        bot_window.erase()
        self.__name = str(bot_window.getstr().strip())[2:-1]
        top_right_window.addstr(f"{self.__name}\n")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    #Course id and check for existence
    def input_id(self, top_right_window, bot_window, all_course):
        id_existed = True
        while id_existed:
            top_right_window.move(2, 0)
            top_right_window.clrtoeol()
            top_right_window.addstr("-Enter id: ")
            top_right_window.refresh()
            bot_window.erase()
            self.__id = str(bot_window.getstr().strip())[2:-1]
            id_existed = False
            if len(all_course)!=0:
                for Course in all_course:
                    if Course.get_id() == self.__id:
                        id_existed = True
                        top_right_window.addstr("This ID already exists!")
                        top_right_window.refresh()
                        time.sleep(0.5)
        top_right_window.addstr(f"{self.__id}\n")
        top_right_window.refresh()

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

class Mark():
    def __init__(self, course_id, student_id, mark):
        self.__course_id = course_id
        self.__student_id = student_id
        self.__mark = mark

    #Input course id and check for its existence
    def input_course_id(self, top_right_window, bot_window, all_course):
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

    def set_course_id(self, course_id):
        self.__course_id = course_id
    
    def get_course_id(self):
        return self.__course_id
    
    #Input student id and check for its existence
    def input_student_id(self, top_right_window, bot_window, all_student): 
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

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id
    
    #input mark and check if it's in range [0,20] or not
    def input_mark(self, top_right_window, bot_window):
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

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark