def pomnoz_for(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik

def pomnoz_skladana(liczby):
    return [liczba * 2 for liczba in liczby]

if __name__ == '__main__':
    moje_liczby = [1, 2, 3, 4, 5]
    
    print("Pętla for:", pomnoz_for(moje_liczby))
    print("Lista składana:", pomnoz_skladana(moje_liczby))