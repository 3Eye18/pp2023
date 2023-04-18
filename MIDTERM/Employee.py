class Employee:
    def __init__(self, name, id, dob, phone, mail):
        self.__name = name
        self.__id = id
        self.__dob = dob
        self.__phone = phone
        self.__mail = mail

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_dob(self):
        return self.__dob

    def get_phone(self):
        return self.__phone

    def get_mail(self):
        return self.__mail

    def get_salary(self):
        return self.__salary

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_dob(self, dob):
        self.__dob = dob

    def set_phone(self, phone):
        self.__phone = phone

    def set_mail(self, mail):
        self.__mail = mail







