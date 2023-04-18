import tkinter
from tkinter import ttk
import output
import input
import os.path

def clear_tree():
    for item in tree.get_children():
        tree.delete(item)

def delete():
    # Get selected item to Delete
    selected_item = tree.selection()[0]
    match current_tab:
        case "employee":
            for employee in employee_list:
                if employee.get_id() == tree.item(selected_item)['values'][1]:
                    employee_list.remove(employee)
        case "order":
            for order in order_list:
                if order.get_id() == tree.item(selected_item)['values'][0]:
                    order_list.remove(order)
        case "attendance":
            for attend in attendance_list:
                if attend.get_dtime() == tree.item(selected_item)['values'][1]:
                    attendance_list.remove(attend)
        case "performance":
            for perform in performance_list:
                if perform.get_employee_id() == tree.item(selected_item)['values'][1] and perform.get_month() == tree.item(selected_item)['values'][0]:
                    performance_list.remove(perform)
    tree.delete(selected_item)
   

# Changing tabs
def employee_gui():
    global current_tab
    current_tab = "employee"
    label1.config(text="Name*")
    label2.config(text="ID*")
    label3.config(text="Date of birth*")
    label4.config(text="Phone number")
    label5.config(text="Email*")
    insert_button.config(command=lambda:input.add_employee(employee_list, entry1, entry2, entry3, entry4, entry5, tree))
    tree.config(columns=employee_columns)
    label1.grid(row=0, column=0)
    entry1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    entry2.grid(row=3, column=0)
    label3.grid(row=4, column=0)
    entry3.grid(row=5, column=0)
    label4.grid(row=6, column=0)
    entry4.grid(row=7, column=0)
    label5.grid(row=8, column=0)
    entry5.grid(row=9, column=0)
    tree.heading('Name', text='Name')
    tree.heading('ID', text='ID')
    tree.heading('DoB', text='DoB')
    tree.heading('Phone', text='Phone')
    tree.heading('Email', text='Email')
    clear_tree()
    for employee in employee_list:
        tree.insert('', 0, values = [employee.get_name(), employee.get_id(), employee.get_dob(), employee.get_phone(), employee.get_mail()])

def order_gui():
    global current_tab
    current_tab = "order"
    label1.config(text="ID*")
    label2.config(text="Employee ID*")
    label3.config(text="Deadline*")
    insert_button.config(command=lambda:input.add_order(order_list, entry1, entry2, entry3, tree))
    tree.config(columns=order_columns)
    label1.grid(row=0, column=0)
    entry1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    entry2.grid(row=3, column=0)
    label3.grid(row=4, column=0)
    entry3.grid(row=5, column=0)
    label4.grid_forget()
    entry4.grid_forget()
    label5.grid_forget()
    entry5.grid_forget()
    tree.heading('ID', text='ID')
    tree.heading('Employee ID', text='Employee ID')
    tree.heading('Time', text='Time')
    tree.heading('Status', text='Status')
    tree.heading('Deadline', text='Deadline')
    clear_tree()
    for order in order_list:
        tree.insert('', 0, values = [order.get_id(), order.get_employee_id(), order.get_time(), order.get_status(), order.get_deadline()])

def attendance_gui():
    global current_tab
    current_tab = "attendance"
    label1.config(text="Employee ID*")
    insert_button.config(command=lambda:input.make_attendance(attendance_list, entry1, tree))
    tree.config(columns=attendance_columns)
    label1.grid(row=0, column=0)
    entry1.grid(row=1, column=0)
    label2.grid_forget()
    entry2.grid_forget()
    label3.grid_forget()
    entry3.grid_forget()
    label4.grid_forget()
    entry4.grid_forget()
    label5.grid_forget()
    entry5.grid_forget()
    tree.heading('Employee ID', text='Employee ID')
    tree.heading('DateTime', text='DateTime')
    tree.heading('Attendance', text='Attendance')
    clear_tree()
    for attendance in attendance_list:
        tree.insert('', 0, values = [attendance.get_employee_id(), attendance.get_dtime(), attendance.get_attendance()])

def performace_gui():
    global current_tab
    current_tab = "performance"
    label1.config(text="Month*")
    label2.config(text="Employee ID*")
    insert_button.config(command=lambda:input.add_performance(order_list, attendance_list, performance_list, entry1, entry2, tree))
    tree.config(columns=performance_columns)
    label1.grid(row=0, column=0)
    entry1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    entry2.grid(row=3, column=0)
    label3.grid_forget()
    entry3.grid_forget()
    label4.grid_forget()
    entry4.grid_forget()
    label5.grid_forget()
    entry5.grid_forget()
    tree.heading('Month', text='Month')
    tree.heading('Employee ID', text='Employee ID')
    tree.heading('Order Rating', text='Order Rating')
    tree.heading('Attend Rating', text='Attend Rating')
    tree.heading('Salary', text='Salary')
    clear_tree()
    for performance in performance_list:
        tree.insert('', 0, values = [performance.get_month(), performance.get_employee_id(), performance.get_order_perform(), performance.get_attend_perform(), performance.get_employee_salary()])

employee_list = []
order_list = []
attendance_list = []
performance_list = []

# Decompressing
if os.path.isfile("datafile.pkl"):
    employee_list, order_list, attendance_list, performance_list = input.decompress()

#Window
window = tkinter.Tk()
window.title("Workplace Management System")
current_tab = "employee"


style = ttk.Style()
style.configure("Treeview", rowheight=25, font=("Arial", 12), background="#E1E1E1", fieldbackground="#E1E1E1", foreground="black")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#C1C1C1", foreground="black")


# Frames
button_frame = tkinter.Frame(window)
button_frame.grid(row=0, column=0, padx=20, pady=10)

info_frame = tkinter.Frame(window)
info_frame.grid(row=1, column=0, padx=20)

input_frame = tkinter.Frame(info_frame)
input_frame.grid(row=1, column=1) 


# Button frame widgets
employee_button = tkinter.Button(button_frame, text="Employee", width=40, command=employee_gui)
employee_button.grid(row=0, column=1, sticky="ew")

order_button = tkinter.Button(button_frame, text="Order", width=40, command=order_gui)
order_button.grid(row=0, column=2, sticky="ew")

attendance_button = tkinter.Button(button_frame, text="Attendance", width=40, command=attendance_gui)
attendance_button.grid(row=0, column=3, sticky="ew")

performance_button = tkinter.Button(button_frame, text="Performance", width=40, command=performace_gui)
performance_button.grid(row=0, column=4, sticky="ew")


# Input frame widgets
label1 = tkinter.Label(input_frame, text="Name*")
label1.grid(row=0, column=0)
entry1 = tkinter.Entry(input_frame)
entry1.grid(row=1, column=0)

label2 = tkinter.Label(input_frame, text="ID*")
label2.grid(row=2, column=0)
entry2 = tkinter.Entry(input_frame)
entry2.grid(row=3, column=0)

label3 = tkinter.Label(input_frame, text="Date of birth*")
label3.grid(row=4, column=0)
entry3 = tkinter.Entry(input_frame)
entry3.grid(row=5, column=0)

label4 = tkinter.Label(input_frame, text="Phone number")
label4.grid(row=6, column=0)
entry4 = tkinter.Entry(input_frame)
entry4.grid(row=7, column=0)

label5 = tkinter.Label(input_frame, text="Email*")
label5.grid(row=8, column=0)
entry5 = tkinter.Entry(input_frame)
entry5.grid(row=9, column=0)

insert_button = tkinter.Button(input_frame, text="Insert", command=lambda:input.add_employee(employee_list, entry1, entry2, entry3, entry4, entry5, tree))
insert_button.grid(row=10, column=0, pady=5)
del_button = tkinter.Button(input_frame, text="Delete", command=delete)
del_button.grid(row=11, column=0)


# Treeview code
employee_columns = ('Name', 'ID', 'DoB', 'Phone', 'Email')
order_columns = ('ID', 'Employee ID', 'Time', 'Status', 'Deadline')
attendance_columns = ('Employee ID', 'DateTime', 'Attendance')
performance_columns = ('Month', 'Employee ID', 'Order Rating', 'Attend Rating', 'Salary')
tree = ttk.Treeview(info_frame, columns=employee_columns, show="headings", style="mystyle.Treeview")
tree.heading('Name', text='Name')
tree.heading('ID', text='ID')
tree.heading('DoB', text='DoB')
tree.heading('Phone', text='Phone')
tree.heading('Email', text='Email')
for employee in employee_list:
    tree.insert('', 0, values = [employee.get_name(), employee.get_id(), employee.get_dob(), employee.get_phone(), employee.get_mail()])

# Placing the treeview in the right side of the frame
tree.grid(row=1, column=2, padx=20, pady=10, columnspan=3, sticky='nsew')  
style.configure("mystyle.Treeview", rowheight=25, font=("Arial", 12), background="#E1E1E1", fieldbackground="#E1E1E1", foreground="black")
style.configure("mystyle.Treeview.Heading", font=("Arial", 12, "bold"), background="#C1C1C1", foreground="black")


window.mainloop()
output.compress_file(employee_list, order_list, attendance_list, performance_list)