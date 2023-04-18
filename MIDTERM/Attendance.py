class Attendance:
    def __init__(self, employee_id, dtime, attendance):
        self.__employee_id = employee_id
        self.__dtime = dtime
        self.__attendance = attendance

    def get_employee_id(self):
        return self.__employee_id

    def get_dtime(self):
        return self.__dtime

    def get_attendance(self):
        return self.__attendance

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_date(self, dtime):
        self.__dtime = dtime

    def set_attendance(self, attendance):
        self.__attendance = attendance