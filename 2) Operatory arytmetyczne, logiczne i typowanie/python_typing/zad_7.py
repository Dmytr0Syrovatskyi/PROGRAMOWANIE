import requests
from typing import Optional

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, city: Optional[str], country: Optional[str]):
        self.id: str = id
        self.name: str = name
        self.brewery_type: str = brewery_type
        self.city: Optional[str] = city
        self.country: Optional[str] = country

    def __str__(self) -> str:
        return f"Browar: {self.name} | Typ: {self.brewery_type} | Lokalizacja: {self.city}, {self.country}"

def main() -> None:
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
    response = requests.get(url)
    response.raise_for_status()
    dane = response.json()

    lista_browarow: list = []
    
    for b in dane:
        obiekt_brewery = Brewery(
            id=b.get("id", ""),
            name=b.get("name", "Brak nazwy"),
            brewery_type=b.get("brewery_type", "Nieznany"),
            city=b.get("city"),
            country=b.get("country")
        )
        lista_browarow.append(obiekt_brewery)

    for browar in lista_browarow:
        print(browar)

if __name__ == '__main__':
    main()