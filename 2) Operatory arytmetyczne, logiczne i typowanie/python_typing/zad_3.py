def czy_parzysta(liczba: int) -> bool:
    return liczba % 2 == 0

if __name__ == '__main__':
    wynik = czy_parzysta(4)
    if wynik:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")