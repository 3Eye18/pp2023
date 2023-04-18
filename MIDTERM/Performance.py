class Performance:
    def __init__(self, month, employee_id, order_perform, attend_perform, employee_salary):
        self.__month = month
        self.__employee_id = employee_id
        self.__order_perform = order_perform
        self.__attend_perform = attend_perform
        self.__employee_salary = employee_salary

    def get_month(self):
        return self.__month

    def get_employee_id(self):
        return self.__employee_id

    def get_order_perform(self):
        return self.__order_perform

    def get_attend_perform(self):
        return self.__attend_perform
    
    def get_employee_salary(self):
        return self.__employee_salary

    def set_month(self, month):
        self.__month = month

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_order_perform(self, order_perform):
        self.__order_perform = order_perform

    def set_attend_perform(self, attend_perform):
        self.__attend_perform = attend_perform

    def set_employee_salary(self, employee_salary):
        self.__employee_salary = employee_salary