from django.core.exceptions import PermissionDenied

def user_is_seller(function):

    def wrap(request, *args, **kwargs):   

        if request.user.role == 'seller':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap



def user_is_shopper(function):

    def wrap(request, *args, **kwargs):    

        if request.user.role == 'shopper':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap