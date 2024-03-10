'''3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
tekst "Liczba parzysta" / "Liczba nieparzysta"'''

def check_if_even(a: int) -> bool:
    if a%2==0:
        return True
    else:
        return False

number = check_if_even(14)

if number:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
