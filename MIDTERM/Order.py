class Order:
    def __init__(self, id, employee_id, time, status, deadline):
        self.__id = id
        self.__employee_id = employee_id
        self.__time = time
        self.__status = status
        self.__deadline = deadline

    def get_id(self):
        return self.__id

    def get_employee_id(self):
        return self.__employee_id

    def get_time(self):
        return self.__time

    def get_status(self):
        return self.__status

    def get_deadline(self):
        return self.__deadline

    def set_id(self, id):
        self.__id = id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_time(self, time):
        self.__time = time

    def set_status(self, status):
        self.__status = status

    def set_deadline(self, deadline):
        self.__deadline =  deadline