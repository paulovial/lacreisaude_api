from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from profissionais.models import Profissional

class ProfissionalAPITests(APITestCase):
    def setUp(self):
        self.profissional_data = {
            "nome_social": "Dra. Luma de Oliveira",
            "profissao": "Psicóloga",
            "endereco": "Rua das Orquídeas, 123",
            "contato": "(11) 98765-4321"
        }

    def test_criar_profissional(self):
        url = reverse('profissional-list')
        response = self.client.post(url, self.profissional_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profissional.objects.count(), 1)
        self.assertEqual(Profissional.objects.first().nome_social, "Dra. Luma de Oliveira")

