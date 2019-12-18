import stripe

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView

from product_app.models import Product, PurchaseOrder


class HomeView(TemplateView):
    '''This will shows the homepage'''
    template_name = 'product_app/home.html'

class CreateProducts(CreateView):
    '''this class is used to insert and create a list of new product'''
    fields = {'id', 'name', 'description', 'price', 'image'}
    model = Product

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(CreateProducts, self).form_valid(form)

class CustomerProdcutList(ListView):
    '''this shows to customer list of product available'''
    model = Product

    def get_context_data(self, **kwargs):
        '''this function shows a payment stripes button with list of products'''
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

class UsersProductsList(ListView):
    '''this shows admin product list to the admin'''
    model = Product
    template_name = 'product_app/list.html'
    context_object_name = 'p'

    def get_context_data(self, *, _=None, **kwargs):
        '''only the logged in admin can view his own products'''
        context = super(UsersProductsList, self).get_context_data(**kwargs)
        print(self.request.user)
        context['p'] = Product.objects.filter(user=self.request.user)
        return context

class UpdateCrudUser(UpdateView):
    '''Updating product through AJAX'''
    model = Product
    fields = ['name', 'description', 'price']

    def get(self, request, *args, **kwargs):
        '''getting objects varibales'''
        self.object = self.get_object()
        form = str(self.get_form())
        return JsonResponse({'form': form})

    def post(self, request, *args, **kwargs):
        obj = self.request.GET.get('name', None)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return JsonResponse({'data': 'success'})


class Delete(View):
    '''this is to delte the the product form list'''
    def  get(self, request):
        '''method to delete the product'''
        product_id = request.GET.get('id', None)
        Product.objects.get(id=product_id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def charge(request, order_pk):
    '''this function svaes the payment token to the purchase order table'''
    purchase_request = PurchaseOrder()
    purchase_request.product = Product.objects.get(id=order_pk)
    purchase_request.user = request.user
    purchase_request.price = purchase_request.product.price
    purchase_request.save()
    return redirect("/PurchasedProducts")


class PurchaseProductsView(ListView):
    '''this shows the purchased order list'''
    model = PurchaseOrder
