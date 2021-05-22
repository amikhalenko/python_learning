# Задание № 1. Наследование
#
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и
# класс студентов (вы можете взять этот код за основу или написать свой). Студентов пока оставим без изменения,
# а вот преподаватели бывают разные, поэтому теперь класс Mentor должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список
# закрепленных курсов логично реализовать на уровне родительского класса. А чем же будут специфичны
# дочерние классы? Об этом в следующих заданиях.

# Задание № 2. Атрибуты и взаимодействие классов.
#
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
# Теперь это могут делать только Reviewers (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student
# (оценки по 10-балльной шкале, хранятся в атрибуте-списке).
# Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

# Задание № 3. Полиморфизм и магические методы
#
#     Перегрузите магический метод __str__ у всех классов.
#
# У проверяющих он должен выводить информацию в следующем виде:
#
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
#
# У лекторов:
#
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
#
# А у студентов так:
#
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
#
#Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней
# оценке за лекции и студентов по средней оценке за домашние задания.
#
# Задание № 4. Полевые испытания
#
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
#
#     для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
#     для подсчета средней оценки за лекции всех лекторов в рамках конкретного курса (в качестве аргументов принимаем список лекторов и название курса).
#
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
#
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

all_lectures = {}
all_students = {}
mid_student = {}
mid_lecturer = {}
list_values_lecturers = []
lecturer_course_grades = {}
name_surname_lecturer=[]
name_surname_student=[]

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_list = list(range(1,11))
        print(self.grades_list)
        compare_mid_student = 0

    def grades_lecturer(self, lecturer, course, grade_lecturer):
         if grade_lecturer in self.grades_list:
             if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
                 if course in lecturer.grade_lecturer:
                    lecturer.grade_lecturer[course] += grade_lecturer
                 else:
                    lecturer.grade_lecturer[course] = grade_lecturer
             else:
                return('Ошибка')
         else:
            return('Ошибка')

    def __str__(self):
         name_surname_student.append(self.name + ' ' + self.surname)
         count = 0
         _sum = 0
         for key in self.grades:
             count += 1
             _sum += self.grades[key]
         mid_grades = _sum/count

         n = '\n'

         courses_in_progress = self.courses_in_progress
         student_courses_in_progress = ', '.join(courses_in_progress)

         finished_courses = self.finished_courses
         student_finished_courses = ', '.join(finished_courses)

         mid_student.update({self.name + ' ' + self.surname: mid_grades})
         all_students.update({self.name + ' ' + self.surname: student.__dict__})
         self.compare_mid_student = mid_student[self.name + ' ' + self.surname]
         return (f"Имя: {self.name}{n}Фамилия: {self.surname}{n}Средняя оценка за домашние задания:"
                 f"{mid_grades}{n}Курсы в процессе изучения: {student_courses_in_progress}{n}"
                 f"Завершенные курсы: {student_finished_courses}")

    def __lt__(self, student2):
        return self.compare_mid_student < student2

    def __gt__(self, student2):
        return self.compare_mid_student > student2

    def __eq__(self, student2):
        return self.compare_mid_student == student2

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __str__(self):
        n = '\n'
        return (f"Имя: {self.name}{n}Фамилия: {self.surname}" )

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    grade_lecturer = {}
    compare_mid_lecturer = 0
    def __str__(self):
        name_surname_lecturer.append(self.name + ' ' + self.surname)
        count = 0
        _sum = 0
        for key in self.grade_lecturer:
            count += 1
            _sum += self.grade_lecturer[key]
        mid_grade_lecturer = _sum/count
        mid_lecturer.update({self.name + ' ' + self.surname : mid_grade_lecturer})
        n = '\n'
        all_lectures.update({self.name + ' ' + self.surname: lecturer.__dict__})
        self.compare_mid_lecturer = mid_lecturer[self.name + ' ' + self.surname]
        return (f"Имя: {self.name}{n}Фамилия: {self.surname}{n}Средняя оценка за лекции:{mid_grade_lecturer}")

    def __lt__(self, lecturer2):
        return self.compare_mid_lecturer < lecturer2

    def __gt__(self, lecturer2):
        return self.compare_mid_lecturer > lecturer2

    def __eq__(self, lecturer2):
        return self.compare_mid_lecturer == lecturer2

student = Student('Федя', 'Фёдоров', 'male')
reviewer = Reviewer('Дима', 'Дмитриев')
lecturer = Lecturer('Сидор', 'Сидоров')
reviewer.courses_attached = ['Java','Python', 'Oracle']
lecturer.courses_attached = ['Oracle','Java', 'Python']
student.finished_courses = ['Beginner','Oracle', 'Java', 'Python']
student.courses_in_progress += ['Python', 'Git']
student.grades = {'Beginner': 7}
reviewer.rate_hw(student, 'Python', 8)
lecturer.grade_lecturer = {'Beginner': 7}
student.grades_lecturer(lecturer, 'Python', 2)


print(student.__dict__)
print(reviewer.__dict__)
print(lecturer.__dict__)
print(student.grades)
print(lecturer.grade_lecturer)
print(reviewer)
print(lecturer)
print(student)

student = Student('Вася', 'Васильев', 'male')
reviewer = Reviewer('Иван', 'Иванов')
lecturer = Lecturer('Серафим', 'Серафимов')
reviewer.courses_attached = ['Java','Python', 'Oracle']
lecturer.courses_attached = ['Oracle','Java', 'Python']
student.finished_courses = ['Beginner','Oracle', 'Java', 'Python']
student.courses_in_progress += ['Python', 'Git']
student.grades = {'Beginner': 10}
reviewer.rate_hw(student, 'Python', 3)
lecturer.grade_lecturer = {'Beginner': 7}
student.grades_lecturer(lecturer, 'Python', 10)

print(student.__dict__)
print(reviewer.__dict__)
print(lecturer.__dict__)
print(student.grades)
print(lecturer.grade_lecturer)
print(reviewer)
print(lecturer)
print(student)

student = Student('Пётр', 'Петров', 'male')
reviewer = Reviewer('Алексей', 'Алексеев')
lecturer = Lecturer('Александр', 'Александров')
reviewer.courses_attached = ['Java','Python', 'Oracle']
lecturer.courses_attached = ['Oracle','Java', 'Python']
student.finished_courses = ['Beginner','Oracle', 'Java', 'Python']
student.courses_in_progress += ['Python', 'Git']
student.grades = {'Beginner': 6}
reviewer.rate_hw(student, 'Python', 8)
lecturer.grade_lecturer = {'Beginner': 4}
student.grades_lecturer(lecturer, 'Python', 2)


print(student.__dict__)
print(reviewer.__dict__)
print(lecturer.__dict__)
print(student.grades)
print(lecturer.grade_lecturer)
print(reviewer)
print(lecturer)
print(student)

print('Средняя оценка у каждого лектора: ',mid_lecturer)
print('Средняя оценка у каждого студента: ',mid_student)

lecturer2 = mid_lecturer['Сидор Сидоров']
compare_lect = (lecturer < lecturer2)
if compare_lect is True:
    print('Верно')
else:
    print('Неверно')

lecturer2 = mid_lecturer['Сидор Сидоров']
compare_lect = (lecturer > lecturer2)
if compare_lect is True:
    print('Верно')
else:
    print('Неверно')

lecturer2 = mid_lecturer['Сидор Сидоров']
compare_lect = (lecturer == lecturer2)
if compare_lect is True:
    print('Верно')
else:
    print('Неверно')


student2 = mid_student['Пётр Петров']
compare_stud = (student < student2)
if compare_stud is True:
    print('Верно')
else:
    print('Неверно')

student2 = mid_student['Пётр Петров']
compare_stud = (student > student2)
if compare_stud is True:
    print('Верно')
else:
    print('Неверно')

student2 = mid_student['Пётр Петров']
compare_stud = (student == student2)
if compare_stud is True:
    print('Верно')
else:
    print('Неверно')

def lecturer_coursegrades(name_surname_lecturer, course):
    _sum = 0
    count = 0
    for name in name_surname_lecturer:
        tmp_lect = all_lectures[name]
        if course in tmp_lect['courses_attached']:
            try:
                tmpI = tmp_lect['grade_lecturer'][course]
                _sum += tmp_lect['grade_lecturer'][course]
                count += 1
            except Exception:
                print('error')
        else:
            print('error')
    try:
        mid_course_lecturer = _sum / count
    except ZeroDivisionError:
        mid_course_lecturer = 0

    print("Средняя оценка лекторов по курсу " + course + ": " + str(mid_course_lecturer))

lecturer_coursegrades(name_surname_lecturer, course='Python')


def student_coursegrades(name_surname_student, course):
    _sum = 0
    count = 0
    for name in name_surname_student:
        tmp_student = all_students[name]
        if course in tmp_student['finished_courses']:
            try:
                tmpI = tmp_student['grades'][course]
                _sum += tmp_student['grades'][course]
                count += 1
            except Exception:
                print('error')
        else:
            print('error')
    try:
        mid_course_student = _sum / count
    except ZeroDivisionError:
        mid_course_student = 0

    print("Средняя оценка студентов по курсу " + course + ": " + str(mid_course_student))

student_coursegrades(name_surname_student, course='Python')

