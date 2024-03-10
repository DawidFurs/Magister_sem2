'''2. Dla osób posiadających podstawową wiedzę o pythonie:
a. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
wyświetli każde z nich.
'''

def print_list_names(names):
    for name in names:
        print(name)

names = ["Marcel", "Dawid", "Filip", "Kriss", "Adam"]

print_list_names(names)

'''b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
zwróci. Zadanie należy wykonać w 2 wersjach:
i. Wykorzystując pętle for .
ii. Wykorzystując listę składaną.'''

def multiple_list_by_two(numbers, is_loop_true):
    if is_loop_true:
        multipled_numbers = []
        for number in numbers:
            number = number*2
            multipled_numbers.append(number)
        return multipled_numbers
    else:
        multipled_numbers = [number * 2 for number in numbers]
        return(multipled_numbers)

numbers = [4,5,3,2,1]

print(multiple_list_by_two(numbers, True))
print(multiple_list_by_two(numbers, False))

'''c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
jedynie parzyste elementy.'''


def print_even_numbers(numbers):
    for number in numbers:
        if number%2 == 0:
            print(number)

numbers = range(0,10)

print_even_numbers(numbers)

'''d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
drugi element.'''


def print_every_second_number(numbers):
    for i in range(0, len(numbers)-1, 2):
            print(numbers[i])

numbers = range(1,20,2)
print_every_second_number(numbers)
