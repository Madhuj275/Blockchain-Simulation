from django.urls import path
from . import views

urlpatterns = [
    path('chain/', views.get_chain, name='get_chain'),
    path('transactions/', views.add_transaction, name='add_transaction'),
    path('tamper/<int:index>/', views.tamper_block, name='tamper_block'),
    path('validate/', views.validate_chain, name='validate_chain'),
]