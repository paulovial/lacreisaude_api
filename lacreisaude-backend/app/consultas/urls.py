from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaViewSet, mock_pagamento

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('pagamentos/mock/', mock_pagamento, name='mock_pagamento'),
]

