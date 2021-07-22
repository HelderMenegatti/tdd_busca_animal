from django.test import LiveServerTestCase
from selenium import webdriver
import os
from animais.models import Animal


class AnimaisTestesCase(LiveServerTestCase):
    
    def setUp(self):

        a = os.path.dirname(__file__)
        self.browser = webdriver.Chrome(executable_path=f'{a}/chromedriver')
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não',
        )

    def tearDown(self):
        self.browser.quit()


    def teste_buscando_um_novo_animal(self):
        # Ele encontra o busca animal de descide usar o site
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: Leão')

        buscar_animal_input.send_keys('Leão')
        self.browser.find_element_by_css_selector('form button').click()


        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)