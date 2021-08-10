from os import name
from django.contrib import admin
from django.urls import path
from piapp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('kpi', views.KPIModelView.as_view(), name='kpi'),
    path('per', views.RetrieveStoryPointsData.as_view(), name='per'),
    path('sprint', views.RetrieveIncomeandFixedPointsData.as_view())
]
