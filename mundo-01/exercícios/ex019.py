from random import choice

student1 = str(input('First student: '))
student2 = str(input('Second student: '))
student3 = str(input('Third student: '))
student4 = str(input('Fourth student: '))
student_list = [student1, student2, student3, student4]
chosen_student = choice(student_list)
print('The chosen student is {}'.format(chosen_student))
