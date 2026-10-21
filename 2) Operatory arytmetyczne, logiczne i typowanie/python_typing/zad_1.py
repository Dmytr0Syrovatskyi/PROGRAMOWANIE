def powitanie(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"

if __name__ == '__main__':
    wynik = powitanie("Jan", "Kowalski")
    print(wynik)