from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from profissionais.models import Profissional
from consultas.models import Consulta

class ConsultaAPITests(APITestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome_social="Dr. Érico Andrade",
            profissao="Psiquiatra",
            endereco="Av. Paulista, 2000",
            contato="(11) 99999-8888"
        )
        self.consulta_data = {
            "data": "2025-04-10T10:00:00Z",
            "profissional": self.profissional.id
        }

    def test_criar_consulta(self):
        url = reverse('consulta-list')
        response = self.client.post(url, self.consulta_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consulta.objects.count(), 1)
        print(response.data)

    def test_filtrar_por_profissional(self):
        Consulta.objects.create(
            data="2025-04-10T10:00:00Z",
            profissional=self.profissional
        )
        url = reverse('consulta-list')
        response = self.client.get(f"{url}?profissional={self.profissional.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)




