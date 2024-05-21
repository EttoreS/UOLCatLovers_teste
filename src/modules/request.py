import requests
import csv

def get_data_from_api():

    url = "https://cat-fact.herokuapp.com/facts"

    response = requests.get(url)

    if response.status_code == 200:
        data =  response.json()
        with open('data/raw/raw_data_cats.csv', 'w', newline='') as csvfile:
            # Criar o objeto do escritor CSV
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())

            # Escrever o cabeçalho do CSV
            writer.writeheader()

            # Escrever cada item do JSON como uma linha no CSV
            for item in data:
                writer.writerow(item)

        print('JSON salvo em users.csv com sucesso!')
    else:
        print(f'Erro na requisição: {response.status_code}')