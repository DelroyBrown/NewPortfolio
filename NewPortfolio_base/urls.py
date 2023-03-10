from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Home.views import home, welcome_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home, name='home'),
    path('', welcome_page, name='welcome-page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
