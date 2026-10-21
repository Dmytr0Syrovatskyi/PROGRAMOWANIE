def wyswietl_co_drugi(liczby):
    # Użycie wycinków (slicing) [start:stop:step]
    for liczba in liczby[::2]:
        print(liczba)

if __name__ == '__main__':
    # Użycie funkcji range do wygenerowania 10 liczb (0-9)
    dziesiec_liczb = list(range(10))
    wyswietl_co_drugi(dziesiec_liczb)