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