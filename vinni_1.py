class BusRoute:
    """Класс, представляющий отдельный рейс автобуса."""
    def __init__(self, bus_number, departure_time, station):
        self.bus_number = bus_number
        self.departure_time = departure_time
        self.station = station

class BusStationCounter:
    """Класс, для подсчета количества рейсов до каждой станции."""
    def __init__(self):
        # Словарь для хранения количества рейсов до каждой станции
        self.station_counts = {}

    def add_route(self, bus_route):
        """Метод для добавления рейса и обновления словаря."""
        station = bus_route.station
        if station in self.station_counts:
            self.station_counts[station] += 1
        else:
            self.station_counts[station] = 1

    def read_routes_from_file(self, input_file):
        """Метод для чтения маршрутов из файла и создания объектов BusRoute."""
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split("-")
                bus_number = parts[0]
                departure_time = parts[1]
                station = parts[2]
                bus_route = BusRoute(bus_number, departure_time, station)
                self.add_route(bus_route)

    def write_station_counts_to_file(self, output_file):
        """Метод для записи результатов в выходной файл."""
        with open(output_file, 'w', encoding='utf-8') as file:
            for station in sorted(self.station_counts):
                file.write(f"{station} {self.station_counts[station]}\n")

# Основная функция для работы с классами
def main():
    
    counter = BusStationCounter()
  
    input_file = 'in.txt'
    output_file = 'out.txt'

    # Читаем маршруты из файла и записываем результаты
    counter.read_routes_from_file(input_file)
    counter.write_station_counts_to_file(output_file)

if __name__ == "__main__":
    main()
