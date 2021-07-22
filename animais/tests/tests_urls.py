from django.test import TestCase, RequestFactory
from django.urls import reverse
from animais.views import index


class AnimaisURLSTestCase(TestCase):


    def setUp(self):
        self.factory = RequestFactory() 
        

    def test_rotas_url_ultiliza_veiw_index(self):
        """Teste se a home da aplocação ultiliza a função index"""
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)

    