from models.base import Employee


class Recruiter(Employee):

    def __init__(self, full_name: object, phone: object, salary_day: object) -> object:
        super().__init__(full_name, phone, salary_day)

    def __str__(self):
        return F'Recruiter: {self.full_name}'

    def work(self):
        var = super().work()
        return var[:len(var) - 1] + ' and start hiring.'


class Programmer(Employee):

    def __init__(self, full_name, phone, salary_day):
        super().__init__(full_name, phone, salary_day)

    def __str__(self):
        return F'Programmer: {self.full_name}'

    def work(self):
        var = super().work()
        return var[:len(var) - 1] + ' and start codding.'
