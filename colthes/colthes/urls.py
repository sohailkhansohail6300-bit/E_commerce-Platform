"""
URL configuration for colthes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('serv/',views.serv,name='serv'),
    path('cantact/',views.contact,name='contact'),
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.login_e,name='login'),
    path('user/',views.user_data,name='user1'),
    path('cart_page/<int:id>',views.cart1,name='cart_page'),
    # path('cart_page1/<int:id>',views.review,name='rating'),
    # path('cart_page2/<int:id>',views.revive,name='revive'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)