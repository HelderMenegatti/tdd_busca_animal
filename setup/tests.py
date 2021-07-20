from django.test import LiveServerTestCase
from selenium import webdriver
import os

class AnimaisTestesCase(LiveServerTestCase):
    
    def setUp(self):

        a = os.path.dirname(__file__)
        self.driver = webdriver.Chrome(executable_path=f'{a}/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_abre_janela_do_chrome(self):
        self.driver.get(self.live_server_url)
