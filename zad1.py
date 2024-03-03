'''2. Dla osób posiadających podstawową wiedzę o pythonie:
a. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
wyświetli każde z nich.
c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
jedynie parzyste elementy.
d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
(rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
drugi element.
Wykonane zadania należy umieścić w repozytorium na gałęzi python_basic
Każde zadanie należy rozbijać na osobne pliki lub jeśli ktoś potrzebuje to na
osobne katalogi z zachowaniem nazewnictwa zad_1 , zad_2 ... zad_n .'''

def print_list_names(names):
    for name in names:
        print(name)

names = ["Marcel", "Dawid", "Filip", "Kriss", "Adam"]

print_list_names(names)
