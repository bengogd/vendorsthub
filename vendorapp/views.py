from django.contrib import messages
from multiprocessing import context
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
#------------------------------------------------------------
from account.models import User
from vendorapp.forms import *
from vendorapp.models import *
from vendorapp.permission import *
User = get_user_model()
from vendorapp.models import *


from .models import Product

def index(request):

    listings = Product.objects.filter(is_published=True, available=True).order_by('-timestamp') #get all published listings, ordered by newest first

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'index.html', context)


@login_required(login_url=reverse_lazy('account:login'))
@user_is_seller
def create_product_View(request):
    """
    Provide the ability to create product post
    """
    form = ProductForm(request.POST or None)

    user = get_object_or_404(User, id=request.user.id)
    categories = Category.objects.all()

    if request.method == 'POST':

        if form.is_valid():

            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            # for save tags
            form.save_m2m()
            messages.success(
                    request, 'You are successfully posted your product! Please wait for review.')
            return redirect(reverse("single-product", kwargs={
                                    'id': instance.id
                                    }))

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'post-product.html', context)
