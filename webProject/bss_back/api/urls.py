from django.urls import path

# from api.views import ProductListAPIView, ProductDetailAPIVIEW, catergory_list, catergory_detail, catergory_products

from rest_framework_simplejwt.views import TokenObtainPairView  # ← добавь вот это
from api.views import *




urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIVIEW.as_view()),
    path('categories/<int:pk>/products/', category_products),

    path('categories/<int:pk>/products/<int:product_id>/', category_product),


    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIVIEW.as_view()),

    path('products/<int:pk>/comments/', comment_list),
    path('products/<int:pk>/comments/<int:comment_id>/', comment_detail),


    path('orders/', order_list),
    path('orders/<int:order_id>/', order_detail),

]
