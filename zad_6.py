'''6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.'''


def join_list(list_1: list, list_2: list) -> list:
    list_1.extend(list_2)
    list_3 = set(list_1)
    list_4 = [number**3 for number in list_3]
    return list_4
list_1 = list(range(1,20))
list_2 = list(range(1,20,2))

print(join_list(list_1,list_2))
