from django.test import LiveServerTestCase
from selenium import webdriver
import os

class AnimaisTestesCase(LiveServerTestCase):
    
    def setUp(self):

        a = os.path.dirname(__file__)
        self.browser = webdriver.Chrome(executable_path=f'{a}/chromedriver')

    def tearDown(self):
        self.browser.quit()


    def teste_buscando_um_novo_animal(self):
        # Ele encontra o busca animal de descide usar o site
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)


