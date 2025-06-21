from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('yazi-ekle/', views.yazi_ekle, name='yazi_ekle'),
    path('yazi/<int:pk>/duzenle/', views.yazi_duzenle, name='yazi_duzenle'),
    path('yazi/<int:pk>/sil/', views.yazi_sil, name='yazi_sil'),

]
