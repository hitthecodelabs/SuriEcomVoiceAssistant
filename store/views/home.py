from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from store.models.product import Products, CMD
from store.models.category import Category
from django.views import View
# from playsound import playsound
# import pygame
# from pydub import AudioSegment
# from pydub.playback import play
# from playsound import playsound
# import vlc
# from glob import glob

# print(glob("*"))

# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        p = Products.objects.filter(id=product)

        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            if quantity := cart.get(product):
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                    p.update(in_stock=p.first().in_stock+1) # type: ignore
                else:
                    in_s = p.first().in_stock-1
                    if in_s >= 0:
                        cart[product]  = quantity+1
                        p.update(in_stock=in_s) # type: ignore
                    else:
                        pass

            else:
                p.update(in_stock=p.first().in_stock-1) # type: ignore
                cart[product] = 1
        else:
            p.update(in_stock=p.first().in_stock-1) # type: ignore
            cart = {product: 1}
        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        url = reverse('product_page', kwargs={'id': int(product)})
        return redirect(url)

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    if categoryID := request.GET.get('category'):
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {'products': products, 'categories': categories}
    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)


def product_page(request, id):
    context = {'product': Products.objects.get(id=id)}
    return render(request, 'product.html', context)



def confirm_payment(request):
    # pygame.init()
    # playsound("bell.mp3")
    # playsound("payment_confirm.mp3")
    # pygame.mixer.init()
    # pygame.mixer.music.load('bell.mp3')
    # pygame.mixer.music.play()
    # pygame.mixer.music.load('../payment_confirm.mp3')
    # playsound('bell.mp3')
    
    ### changes
    #p = vlc.MediaPlayer('bell.mp3')
    #p.play()
    #p = vlc.MediaPlayer('payment_confirm2.mp3')
    #p.play()
    
    # song = AudioSegment.from_mp3("bell.mp3")
    # play(song)
    return HttpResponseRedirect('/store')

def save_cmd(request):
    command = request.GET.get('cmd')
    if command:
        CMD.objects.create(command=command)
        response = "OK"
    else:
        response = "ERROR"
    return HttpResponse(response)





