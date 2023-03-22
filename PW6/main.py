import curses, time, input, output, os
from curses.textpad import rectangle

all_student = []
all_course = []
all_mark = []

#Main function
def main(stdscr):
    global all_student, all_course, all_mark
    curses.echo()
    stdscr.clear() 
    top_left_window = curses.newwin(20, 50, 2, 2)
    top_right_window = curses.newwin(20, 50, 2, 53)
    bot_window = curses.newwin(6, 100, 23, 2)
    rectangle(stdscr, 1, 1, 22, 52)
    rectangle(stdscr, 1, 52, 22, 103)
    rectangle(stdscr, 22, 1, 29, 103)
    stdscr.refresh()

    if os.path.exists("./data.pkl"):
        # Read the compressed data from the file
        all_student, all_course, all_mark = input.decompress()
    else:
        top_left_window.addstr("Initializing students and courses.....\n")
        top_left_window.refresh()
        input.initialize_students(top_left_window, top_right_window, bot_window, all_student)
        input.initialize_courses(top_left_window, top_right_window, bot_window, all_course)
        top_left_window.addstr("Initialize complete!\n")
        top_left_window.refresh()
        time.sleep(1.5)
    current_choice = 0
    current_choice = input.main_menu(current_choice, top_left_window)

    while current_choice!= 0:
        match current_choice:
            case 1:
                input.add_mark(top_right_window, bot_window, all_mark, all_course, all_student)
                current_choice = input.main_menu(current_choice, top_left_window)
            case 2:
                input.add_student(top_right_window, bot_window, all_student)
                current_choice = input.main_menu(current_choice, top_left_window)
            case 3:
                input.add_course(top_right_window, bot_window, all_course)
                current_choice = input.main_menu(current_choice, top_left_window)
            case 4: 
                output.list_students(top_right_window, all_student)
                current_choice = input.main_menu(current_choice, top_left_window)
            case 5:
                output.list_courses(top_right_window, all_course)
                current_choice = input.main_menu(current_choice, top_left_window)
            case 6:
                output.search_mark(top_right_window, bot_window, all_mark, all_course)
                current_choice = input.main_menu(current_choice, top_left_window)
            case 7:
                output.sort_gpa(top_right_window, all_mark, all_student)
                current_choice = input.main_menu(current_choice, top_left_window)
            case _:
                top_left_window.addstr("Invalid choice!")
                top_left_window.refresh()
                time.sleep(0.5)
                current_choice = input.main_menu(current_choice, top_left_window)
    if current_choice == 0:
        print("Exited program")

curses.wrapper(main)
output.compress(all_student, all_course, all_mark)
