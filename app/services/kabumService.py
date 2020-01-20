import requests
from config import config
import os

class KabumService():
    URL_KABUM_API = "https://servicespub.prod.api.aws.grupokabum.com.br/descricao/v1/descricao/produto/"

    def getProduct(self, idProduct):
        product = None
        res = requests.get(self.URL_KABUM_API + str(idProduct))
        if res.ok:
            product = res.json()

        return product