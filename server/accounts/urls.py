
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from .views import RegisterRecruiter, RegisterUser,RegisterCompany


urlpatterns = [
  
    path('js_register/', RegisterUser.as_view()),
    path('rec_register/', RegisterRecruiter.as_view()),
    path('owner_register/', RegisterCompany.as_view()),
    
    



]