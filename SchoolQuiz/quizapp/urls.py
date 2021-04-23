from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home,name="home"),
    path('signup/', views.signup,name="signup"),
    path('login/', views.userlogin,name="userlogin"),
    path('logout/', views.userlogout,name="userlogout"),
    path('quizhistory/', views.quizhistory,name="userlogout"),
    path('quiz/<str:category>/<int:num>/', views.quizpage,name="quizpage"),
    path('quiz/results/', views.result,name="result"),
    path('check/<str:queid>/', views.check,name="check"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
