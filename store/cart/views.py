from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem


def index(request):
    products_list = Product.objects.all()
    
    return render(request,'homepage.html',{"products_list": products_list})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': product.price * quantity})
        total_price += product.price * quantity

    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
