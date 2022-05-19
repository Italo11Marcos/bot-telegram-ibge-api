import requests
import re

url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

class frequenciaPorNome:
    def __init__(self, nome: str) -> None:
        self.periodos = {}
        req = requests.get(url.format(nome=nome)).json()
        for dados in req[0]['res']:
            self.periodos[dados['periodo']] = dados['frequencia']
        self.periodo = max(self.periodos, key=self.periodos.get)
        self.quantidade = self.periodos[self.periodo]

if __name__ == '__main__':
    nome = 'Italo'
    
    freq = frequenciaPorNome(nome)
    print(freq.periodo)
    print(freq.quantidade)