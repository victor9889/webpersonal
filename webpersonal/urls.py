"""
URL configuration for webpersonal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core import views as views_core
from portfolio import views as views_portfolio
from experiencia import views as views_experiencia
# Para poder ver las imagenes sin estar en producción
from django.conf import settings

urlpatterns = [
    path('', views_core.home, name="home"),
    path('about-me/', views_core.about, name="about"),
    path('portfolio/', views_portfolio.portfolio, name="portfolio"),
    path('contact/', views_core.contact, name="contact"),
    path('experiencia/', views_experiencia.experiencia, name="experiencia"),
    path('admin/', admin.site.urls),
]
# Para poder ver las imagenes sin estar en producción
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)