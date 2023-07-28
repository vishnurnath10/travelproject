from .import views
from django.urls import path
app_name='ecommerceapp'

urlpatterns = [

    path('',views.AllProductCategory,name='AllProductCategory'),
    path('<slug:c_slug>/',views.AllProductCategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProductDetail,name='prodcatedetail'),

]