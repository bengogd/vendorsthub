from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse, reverse_lazy

from account.forms import *
from vendorapp.permission import user_is_shopper 


def get_success_url(request):

    """
    Handle Success Url After LogIN

    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('index')



def shopper_registration(request):

    """
    Handle Shopper Registration

    """
    form = ShopperRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('login')
    context={
        
            'form':form
        }

    return render(request,'shopper-registration.html',context)


def seller_registration(request):

    """
    Handle Seller Registration 

    """

    form = SellerRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('login')
    context={
        
            'form':form
        }

    return render(request,'seller-registration.html',context)


@login_required(login_url=reverse_lazy('login'))
@user_is_shopper
def shopper_edit_profile(request, id=id):

    """
    Handle Shopper Profile Update Functionality

    """

    user = get_object_or_404(User, id=id)
    form = ShopperProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form = form.save()
        messages.success(request, 'Your Profile Was Successfully Updated!')
        return redirect(reverse("account:edit-profile", kwargs={
                                    'id': form.id
                                    }))
    context={
        
            'form':form
        }

    return render(request,'shopper-edit-profile.html',context)



def user_logIn(request):

    """
    Provides users to logIn

    """

    form = UserLoginForm(request.POST or None)
    

    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            if form.is_valid():
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_url(request))
    context = {
        'form': form,
    }

    return render(request,'login.html',context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')