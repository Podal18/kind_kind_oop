class Genre:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return f"Genre(code={self.code}, name={self.name})"


class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __repr__(self):
        return f"Country(code={self.code}, name={self.name})"


class Stamp:
    def __init__(self, code, country_code, genre_code, year, price, album_number):
        self.code = code
        self.country_code = country_code
        self.genre_code = genre_code
        self.year = year
        self.price = price
        self.album_number = album_number

    def __repr__(self):
        return (f"Stamp(code={self.code}, country_code={self.country_code}, genre_code={self.genre_code}, "
                f"year={self.year}, price={self.price}, album_number={self.album_number})")


class StampCollection:
    def __init__(self):
        self.genres = []
        self.countries = []
        self.stamps = []

    def add_genre(self, genre):
        self.genres.append(genre)

    def add_country(self, country):
        self.countries.append(country)

    def add_stamp(self, stamp):
        self.stamps.append(stamp)

    def find_most_expensive_stamp(self):
        if not self.stamps:
            return None
        most_expensive_stamp = self.stamps[0]
        for i in self.stamps:
            if i.price > most_expensive_stamp.price:
                most_expensive_stamp = i
        return most_expensive_stamp


collection = StampCollection()

collection.add_genre(Genre(code=1, name="Historical"))
collection.add_genre(Genre(code=2, name="Art"))

collection.add_country(Country(code=1, name="USA"))
collection.add_country(Country(code=2, name="Germany"))

collection.add_stamp(Stamp(code=101, country_code=1, genre_code=1, year=1990, price=10.5, album_number=1))
collection.add_stamp(Stamp(code=102, country_code=2, genre_code=2, year=1985, price=20.0, album_number=2))
collection.add_stamp(Stamp(code=103, country_code=1, genre_code=2, year=2000, price=15.0, album_number=3))

most_expensive = collection.find_most_expensive_stamp()
print("The most expensive stamp:", most_expensive)
