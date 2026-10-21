def sprawdz_zawartosc(lista: list, wartosc: int) -> bool:
    return wartosc in lista

if __name__ == '__main__':
    moja_lista = [10, 20, 30, 40]
    print(sprawdz_zawartosc(moja_lista, 30))