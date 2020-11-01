from django.urls import path
from . import views
from orders.views import OrderList
from orders.views import OrderDetail
from orders.views import OrderUpdate
from orders.views import CreateOrder

urlpatterns = [
    path('list/', OrderList.as_view(), name='order-list'),
    path('create', CreateOrder.as_view(), name='create-order'),
    path('update/<slug:slug>/', OrderUpdate.as_view(success_url="/orders/list"), name='order-update'),
    path('<slug:slug>/', OrderDetail.as_view(), name='order-detail'),
]