from django.contrib import admin
from django.urls import path

from test_pages_app.views import page0, page1, page2, page3, page4, page2_1, page2_1_1, info0, info1

app_name = 'test_pages_app'

urlpatterns = [
    path('', page0, name='page0'),
    path('page1/', page1, name='page1'),
    path('page2_1/', page2_1, name='page2_1'), 
    path('page2_1_1/', page2_1_1, name='page2_1_1'),
    path('page2/', page2, name='page2'),
    path('page3/', page3, name='page3'),
    path('page4/', page4, name='page4'),
    
    path('info0/', info0, name='info0'), 
    path('info1/', info1, name='info1'),
]
