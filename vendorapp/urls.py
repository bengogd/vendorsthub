from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='listings'),
    #path('<int:product_id>', views.product_detail, name='product_detail'),
    #path('buy-product/<int:id>/', views.buy_product_view, name='buy-product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)