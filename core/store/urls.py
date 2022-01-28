from django.urls import path
from core.store.views import HomeView

app_name = 'store'
urlpatterns = [
    # Home page
    path('', HomeView.as_view(), name = 'index')

]
