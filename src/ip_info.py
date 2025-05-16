import requests

def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        if data['status'] == 'success':
            return [ip_address, data['country'], data['city'], data['isp'], f'{data['lat']:.6f}; {data['lon']:.6f}']
        else:
            # print(" Не удалось определить данные.")
            return [ip_address, '-', '-', '-', '-']
    except Exception as _ex:
        return [ip_address, '-', '-', '-', '-']


if __name__ == '__main__':
    print(get_ip_info("1.1.1.1"))
