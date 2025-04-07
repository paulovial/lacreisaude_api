from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profissional']

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Consulta

@api_view(['POST'])
def mock_pagamento(request):
    consulta_id = request.data.get('consulta_id')
    valor_total = request.data.get('valor_total')

    if not consulta_id or not valor_total:
        return Response(
            {"erro": "consulta_id e valor_total são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        consulta = Consulta.objects.get(id=consulta_id)
    except Consulta.DoesNotExist:
        return Response({"erro": "Consulta não encontrada."}, status=404)

    # Simula o split
    valor_total = float(valor_total)
    valor_profissional = round(valor_total * 0.8, 2)
    valor_lacrei = round(valor_total * 0.2, 2)

    return Response({
        "status_pagamento": "RECEBIDO",
        "consulta_id": consulta.id,
        "valor_total": valor_total,
        "split_pagamento": {
            "profissional": {
                "id": consulta.profissional.id,
                "nome": consulta.profissional.nome_social,
                "valor_recebido": valor_profissional
            },
            "plataforma": {
                "nome": "Lacrei Saúde",
                "valor_recebido": valor_lacrei
            }
        }
    }, status=status.HTTP_200_OK)

