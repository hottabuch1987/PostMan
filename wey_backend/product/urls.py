from django.urls import path, include
from product  import views


urlpatterns = [
    path('latest-products/', views.LatesProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    # path('api/payment/', views.payment_view, name='payment_api'),
    # path('payment/', views.payment_form_view, name='payment_form'),
]