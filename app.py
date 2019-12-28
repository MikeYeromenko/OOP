from models.base import Employee, Candidate, Vacancy
from models.custom import Recruiter, Programmer


def main():
    recruiter1 = Recruiter('Vasya', '5050654646', 10)
    print(recruiter1.work())

    programmer = Programmer('Sofia', '5050654646', 25)
    print(programmer.work() + ' ' + str(programmer.check_salary(20)))
    # print(str(progr1.salary_day(20)))
    print(programmer)

    programmer2 = Programmer('Marina', '505060666', 30)

    candidate1 = Candidate('Olena', 'email1.sd', ('tech1', 'tech2', 'tech3'), 'main_skill1', 'main_skill_level1')
    print(candidate1)
    candidate2 = Candidate('Svetlana', 'email2.sd', ('tech1', 'tech2', 'tech3'), 'main_skill2', 'main_skill_level2')
    candidate3 = Candidate('Galina', 'email3.sd', ('tech1', 'tech2', 'tech3'), 'main_skill3', 'main_skill_level3')

    vacancy1 = Vacancy('Vac1', 'main_skill1', 'main_skill_level1')
    vacancy2 = Vacancy('Vac2', 'main_skill2', 'main_skill_level2')

# print(__name__)


if __name__ == '__main__':
    main()
