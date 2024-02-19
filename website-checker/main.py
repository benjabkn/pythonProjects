import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1:
                if 'https://' not in row[1]:
                    websites.append(f'https://{row[1]}')
                else:
                    websites.append(row[1])
    return websites

def get_userAgent() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status_description(status_code: int) -> str:
    for value in HTTPStatus:
        if value.value == status_code:
            return f'{value.value} {value.name}'

def check_website(website: str, user_agent: str):
    try:
        response = requests.get(website, headers={'User-Agent': user_agent})
        print(f'{website}: {get_status_description(response.status_code)}')
    except requests.RequestException as e:
        print(f'{website} No se puede obtener información del sitio  (???) unknown status code')

def main():
    sites: list[str] = get_websites('websites.csv')
    user_agent: str = get_userAgent()

    for site in sites:
        check_website(site, user_agent)

if __name__ == '__main__':
    main()
