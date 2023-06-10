salary = float(input('What is the employee\'s salary? R$'))
if salary <= 1250:
    new_salary = salary + (salary * 15 / 100)
else:
    new_salary = salary + (salary * 10 / 100)

print('The employee who earned R${:.2f} now earns R${:.2f}.'.format(salary, new_salary))
