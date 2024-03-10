'''4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
informację jako typ logiczny bool'''

def is_2_first_numbers_bigger_than_3(a: int, b: int, c: int) -> bool:
    if a+b >= c:
        return True
    else:
        return False

print(is_2_first_numbers_bigger_than_3(2,2,3))