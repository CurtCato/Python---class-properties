# Practice: Solid Student
class Student():

    def __str__(self):
        return f"{self.full_name} is a {int(self.age)} year old student in cohort {int(self.cohort)}."

    @property #Getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return ""

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return ""

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @property
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0

    @first_name.setter # The setter
    def first_name(self, new_first):
        if type(new_first) is str:
            self.__first_name = new_first
        else:
            raise TypeError('Please provide a string for the first name')

    @last_name.setter # The setter
    def last_name(self, new_last):
        if type(new_last) is str:
            self.__last_name = new_last
        else:
            raise TypeError('Please provide a string for the last name')

    @age.setter # The setter
    def age(self, new_age):
        if type(new_age) is float:
            self.__age = new_age
        else:
            raise TypeError('Please provide a floating value for the age')

    @cohort.setter # The setter
    def cohort(self, new_cohort):
        if type(new_cohort) is float:
            self.__cohort = new_cohort
        else:
            raise TypeError('Please provide a floating value for the cohort')

jo = Student()
jo.first_name = "Jo"
jo.last_name = "Kennerly"
jo.age = 30.0
jo.cohort = 33.0
print(jo)


# Practice: Sensitive Information
class Patient():
    def __init__(self, ssn, dob, insurance, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__insurance = insurance
        self.__first_name = first_name
        self.__last_name = last_name
        self.address = address

    @property
    def ssn(self):
        try:
            return self.__ssn
        except AttributeError:
            return ""

    @property
    def dob(self):
        try:
            return self.__dob
        except AttributeError:
            return ""

    @property
    def insurance(self):
        try:
            return self.__insurance
        except AttributeError:
            return ""

    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return ""
    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string for the address')

danny = Patient("123-12-123", "8/30/2019", 123123123, "Danny", "Barker", "123 Sesame St")

danny.address = "456 pick up sticks"




