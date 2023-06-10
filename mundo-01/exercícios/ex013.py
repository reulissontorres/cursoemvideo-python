salary = float(input('What is the employee\'s salary? R$'))
new_salary = salary + (salary * 15 / 100)
print('An employee who earned R${:.2f}, with a 15% raise, now earns R${:.2f}'.format(salary, new_salary))
