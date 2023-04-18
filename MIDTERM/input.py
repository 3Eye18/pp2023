from Attendance import *
from Employee import *
from Performance import *
from Order import *
import datetime
from tkinter import messagebox
import output
import pickle

#tạo instance của class Attend dựa trên thời gian chấm công
def make_attendance(attendance_list, entry1, tree):
    employee_id = check_empty(entry1.get())
    dtime = datetime.datetime.now()
    time1 = dtime.time()
    if employee_id != False:
        if time1 < datetime.time(8, 0, 0):
            attendance_list.append(Attendance(employee_id, dtime, "On time"))
            tree.insert('', 0, values = [employee_id, dtime, "On time"])
        else:
            attendance_list.append(Attendance(employee_id, dtime, "Late"))
            tree.insert('', 0, values = [employee_id, dtime, "Late"])
    else:
        messagebox.showerror(title="Empty entry", message="Please fill all * entries")

#tạo instance class Employee
def add_employee(employee_list, entry1, entry2, entry3, entry4, entry5, tree):
    name = check_empty(entry1.get())
    id = check_empty(entry2.get())
    dob = check_empty(entry3.get())
    phone = entry4.get()
    mail = check_empty(entry5.get())
    if False in [name, id, dob, phone, mail]:
        messagebox.showerror(title="Empty entry", message="Please fill all * entries")
    else:
        employee_list.append(Employee(name, id, dob, phone, mail))
        tree.insert('', 0, values = [name, id, dob, phone, mail])

#tương tự cho Order
def add_order(order_list, entry1, entry2, entry3, tree):
    id = check_empty(entry1.get())
    employee_id = check_empty(entry2.get())
    time = datetime.datetime.now()
    status = "Not finished"
    deadline = check_empty(entry3.get())
    if False in [id, employee_id, time, status, deadline]:
        messagebox.showerror(title="Empty entry", message="Please fill all * entries")
    else:
        order_list.append(Order(id, employee_id, time, status, deadline))
        tree.insert('', 0, values = [id, employee_id, time, status, deadline])
    
#tạo instance class Performance
def add_performance(order_list, attend_list, perform_list, entry1, entry2, tree):
    month = check_empty(entry1.get())
    employee_id = check_empty(entry2.get())
    order_perform = output.order_performance(order_list, employee_id, month)
    attend_perform = output.attend_performance(attend_list, employee_id, month)
    salary = output.cal_salary(order_list, attend_list, employee_id, month)
    if False in [month, employee_id]:
        messagebox.showerror(title="Empty entry", message="Please fill all * entries")
    else:
        perform_list.append(Performance(month, employee_id, order_perform, attend_perform, salary))
        tree.insert('', 0, values = [month, employee_id, order_perform, attend_perform, salary])

#check xem có cái input nào bị trống không
def check_empty(text):
    if text != '':
        return text
    else:
        return False

#giải nén
def decompress():
    with open("./datafile.pkl", "rb") as f:
        [employee_list, order_list, attend_list, performance_list] = pickle.load(f)
    return [employee_list, order_list, attend_list, performance_list]