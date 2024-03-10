'''5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
drugim.'''

def check_number_exist(list_of_numbers: list, number: int) -> bool:
    return number in list_of_numbers

list_of_numbers = range(1,20)
number1 = 12
number2 = 23

print(check_number_exist(list_of_numbers, number1))
print(check_number_exist(list_of_numbers, number2))