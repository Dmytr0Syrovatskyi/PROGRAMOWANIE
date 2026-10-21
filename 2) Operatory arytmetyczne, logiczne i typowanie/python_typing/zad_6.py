def polacz_i_poteguj(lista1: list, lista2: list) -> list:
    # Połączenie list i usunięcie duplikatów za pomocą rzutowania na set
    unikalne = list(set(lista1 + lista2))
    # Podniesienie każdego elementu do potęgi 3
    return [x ** 3 for x in unikalne]

if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [2, 3, 4]
    print(polacz_i_poteguj(l1, l2))