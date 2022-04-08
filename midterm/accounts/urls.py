from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("create_order/<str:pk>", views.createOrder, name="create_order"),
    path("update_order/<str:pk>", views.updateOrder, name="update_order"),
    path("customers/<str:pk_test>/", views.customer, name="customers"),
    path("delete_order/<str:pk>/", views.deleteOrder, name="delete_order"),

    path('account/', views.accountSettings, name='account'),

    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
    path('user/', views.userPage,name='user_page'),
    path('logout/', views.logoutUser, name="logout"),
]
