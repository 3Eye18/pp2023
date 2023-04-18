import pickle

#tính % order đã hoàn thành
def order_performance(order_list, employee_id, month):
    employee_order = []
    for order in order_list:
        if order.get_employee_id() == employee_id and order.get_time().month == month and order.get_status() == "Finished":
            employee_order.append(order)
    return len(employee_order)

#tính % số ngày đi làm đúng giờ
def attend_performance(attend_list, employee_id, month):
    employee_attend = []
    for attend in attend_list:
        if attend.get_employee_id() == employee_id and attend.get_dtime().month == month and attend.get_attendance() == "On time":
            employee_attend.append(attend)
    return len(employee_attend)

#tính lương
def cal_salary(order_list, attend_list, employee_id, month):
    orders = order_performance(order_list, employee_id, month)
    if orders > 20:
        order_bonus = 0.2
    elif orders >= 17:
        order_bonus = 0
    else:
        order_bonus = -0.1
    attends = attend_performance(attend_list, employee_id, month)
    if attends >= 30:
        attend_bonus = 0.15
    elif attends >= 27:
        attend_bonus = 0
    else:
        attend_bonus = -0.1
    return 200000 * (orders + order_bonus) + 100000 * (attends + attend_bonus)

#nén file
def compress_file(employee_list, order_list, attend_list, performance_list):
    with open("./datafile.pkl", "wb") as f:
        pickle.dump([employee_list, order_list, attend_list, performance_list], f)
    f.close()
    
