class Employee:
    def __init__(self, full_name, phone, salary_day):
        self.full_name = full_name
        self.phone = phone
        self.salary_day = salary_day

    def __lt__(self, other):  # - x < y
        result = True
        if self.salary_day >= other.salary_day:
            result = False
        return result

    def __le__(self, other):  # - x <= y
        result = True
        if self.salary_day > other.salary_day:
            result = False
        return result

    def __eq__(self, other):  # - x == y
        result = True
        if self.salary_day != other.salary_day:
            result = False
        return result

    def __ne__(self, other):  # - x != y
        result = True
        if self.salary_day == other.salary_day:
            result = False
        return result

    def __gt__(self, other):  # - x > y
        result = True
        if self.salary_day <= other.salary_day:
            result = False
        return result

    def __ge__(self, other):  # - x >= y
        result = True
        if self.salary_day < other.salary_day:
            result = False
        return result

    def work(self):
        return 'I come to office.'

    # check_salary returns how much does an employee urned
    def check_salary(self, days=None):
        if days is None:
            # days calculate
            pass
        return self.salary_day * days


class Candidate:
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return f'{self.full_name} is a candidate with technologies {self.technologies}.' \
               f'His main skill is {self.main_skill} with grade {self.main_skill_grade}.' \
               f'She has an email: {self.email}'


class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
