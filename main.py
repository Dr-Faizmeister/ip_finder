import requests


def get_info_by_ip(ip_addr='127.0.0.1'):
    """
    Получение информации по IP-адресу
    :param ip_addr: (str) ip-адрес
    :return:
    """
    try:
        # начальный запрос
        response = requests.get(url=f'http://ip-api.com/json/{ip_addr}').json()
        print(response)
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    # запрос ip-адреса от пользователя
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip_addr=ip)


if __name__ == '__main__':
    main()
