from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about',views.about, name = 'about'),
    path('program', views.program, name = 'program'),
    path('manual', views.manual, name = 'manual')
]