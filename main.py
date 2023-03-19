import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip_addr='127.0.0.1'):
    """
    Получение информации по IP-адресу
    :param ip_addr: (str) ip-адрес
    :return:
    """
    try:
        # начальный запрос
        response = requests.get(url=f'http://ip-api.com/json/{ip_addr}').json()
        # print(response)

        # формируем словарь для вывода информации
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP code]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        print('-------------------------')

        for k, v in data.items():
            print(f'{k} : {v}')

        # запрашиваем местоположение на карте
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'area/{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    # Превью с оформлением
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP FINDER'))

    # запрос ip-адреса от пользователя
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip_addr=ip)


if __name__ == '__main__':
    main()
