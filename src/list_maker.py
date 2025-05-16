import csv
from .ip_info import get_ip_info


class IPList:
    def __init__(self):
        self.ip_list = []
        self.countries = []
        self.cities = []
        self.isps = []
        self.lat_lons = []

    def get_ips(self, txt):
        try:
            file = open(txt)
            ips = [i.replace('\n','') for i in file]
            file.close()
            self.ip_list += ips
        except FileNotFoundError as _ex:
            print(f'Error: {_ex}')


    def list_processing(self):
        for ip in self.ip_list:
            country, city, isp, lat_lon = get_ip_info(ip)[1:]
            self.countries.append(country)
            self.cities.append(city)
            self.isps.append(isp)
            self.lat_lons.append(lat_lon)

    def append_csv(self, csv_name):
        with open(f'./csv/{csv_name}.csv', 'a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=';')
            for ip, country, city, isp, lat_lon in zip(self.ip_list, self.countries, self.cities, self.isps, self.lat_lons):
                writer.writerow([ip, country, city, isp, lat_lon])

    def write_csv(self, csv_name):
        with open(f'./csv/{csv_name}.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow('IP Страна Город Провайдер Координаты'.split())
        self.append_csv(csv_name)