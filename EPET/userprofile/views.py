from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Userprofile
from django.contrib.auth.decorators import login_required
from store.forms import ProductForm
from django.utils.text import slugify
from store.models import Product, OrderItem, Order
from django.contrib import messages
from .forms import CustomSignupForm

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from verify_email.email_handler import send_verification_email


def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVE)
    return render(request, 'userprofile/vendor_detail.html', {'user': user, 'products': products})


@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


@login_required
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'Your product have been added!')

            return redirect('my_store')
    else:

        form = ProductForm()
    return render(request, 'userprofile/product_form.html', {'title': 'Add product', 'form': form})


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes was saved!')

            return redirect('my_store')
    else:
        form = ProductForm(instance=product)
    return render(request, 'userprofile/product_form.html', {'title': 'Edit product', 'product': product, 'form': form})


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()
    messages.success(request, 'Product was deleted!')
    return redirect('my_store')


@login_required
def my_store(request):
    products = request.user.products.exclude(status=Product.DELETED)
    order_items = OrderItem.objects.filter(product__user=request.user)
    return render(request, 'userprofile/my_store.html', {'products': products, 'order_items': order_items})


@login_required
def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)

    return render(request, 'userprofile/my_store_order_detail.html', {'order': order})


def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():

            user = form.save()

            login(request, user)
            userprofile = Userprofile.objects.create(user=user)
            inactive_user = send_verification_email(request, form)
            return redirect('frontpage')
    else:
        form = CustomSignupForm()

    return render(request, 'userprofile/signup.html', {'form': form})
