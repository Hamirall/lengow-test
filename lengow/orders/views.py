from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views import View
from orders.models import Order
from .forms.order import OrdersForm
from django.http import HttpResponseRedirect
from datetime import date


class OrderList(ListView):
    model = Order

class OrderDetail(DetailView):
    model = Order
    slug_field = 'id'

class OrderUpdate(UpdateView):
    model = Order
    slug_field = 'id'
    fields = ['marketplace', 'id_flux', 'order_amount']
    template_name_suffix = '_update_form'


class CreateOrder(View):

    def get(self, request):
        form = OrdersForm()
        return render(request, 'orders/create.html', {'form': form})

    def post(self, request):
        form = OrdersForm(request.POST)

        if form.is_valid():
            marketplace = form.cleaned_data['marketplace']
            id_flux = form.cleaned_data['id_flux']
            order_amount = form.cleaned_data['order_amount']

        order = Order.objects.create(
            marketplace = marketplace,
            id_flux = id_flux,
            order_purchase_date = date.today(),
            order_amount = order_amount
        )

        return HttpResponseRedirect('/orders/list') 





# def update_order(request, **kwargs):
#     order = Order.objects.get(id=kwargs['slug'])
#     form = OrdersForm(request.POST or None, instance=order)

#     return render(request, 'orders/update_order.html', { 'form': form })
