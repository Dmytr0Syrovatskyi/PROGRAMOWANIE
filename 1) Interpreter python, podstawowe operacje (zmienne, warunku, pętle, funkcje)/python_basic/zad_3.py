def wyswietl_parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)

if __name__ == '__main__':
    # Użycie funkcji range do wygenerowania 10 liczb (0-9)
    dziesiec_liczb = list(range(10))
    wyswietl_parzyste(dziesiec_liczb)