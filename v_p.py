
class Bus:
    def __init__(self, nomber, time, station):
        self.nomber = nomber
        self.time = time
        self.station = station


def read_from_file(filename):
    calls = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            nomber, time, staition = line.strip().split()
            calls.append(Bus(nomber, time, staition))
    return calls


def calcul(calls):
    station_bus = {}
    coll = 1
    for Bus in calls:
        if Bus.station in station_bus:
            station_bus[Bus.station] += coll
        else:
            station_bus[Bus.station] = coll
    return station_bus


def write_to_file(station_bus, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for staition, total_cost in sorted(station_bus.items()):
            file.write(f"{staition}\t{total_cost}\n")


calls = read_from_file('in.txt')
station_cost = calcul(calls)
write_to_file(station_cost, 'out.txt')



class Tovar:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self. price = price

def read_from_file(filename):
    calls = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            id, name, price = line.strip().split()
            calls.append(Tovar(id, name, price))
    return calls

def calcul(calls):
    return sorted(calls, key=lambda Tovar: Tovar.price)

def write_to_file(calls, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for Tovar in calls:
            file.write(f"{Tovar.id} {Tovar.name} {Tovar.price}\n")

calls = read_from_file('in.txt')
sorted_file = calcul(calls)
write_to_file(sorted_file, 'out.txt')


111
class Perevozka:
    def __init__(self, punct, fio, car, time):
        self.punct = punct
        self.fio = fio
        self.car = car
        self.time = time

def read_from_file(filename):
    calls = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            punct, fio, car, time = line.strip().split()
            if fio == "Винни-Пух":
                calls.append(Perevozka(punct, fio, car, time))
    return calls

def calculc(calls):
    return sorted(calls, key=lambda Perevozka: Perevozka.time)

def write_to_file(calls, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for Perevozka in calls:
            file.write(f"{Perevozka.punct} {Perevozka.fio} {Perevozka.car} {Perevozka.time}\n")

calls = read_from_file('in.txt')
sorted_file = calculc(calls)
write_to_file(sorted_file, 'out.txt')

