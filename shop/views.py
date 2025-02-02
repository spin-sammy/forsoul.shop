from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product, Slide
from cart.forms import CartAddProductForm


def main(request):
    categories = Category.objects.order_by('pk').all()
    subcategories = SubCategory.objects.all()
    products = Product.objects.filter(available=True)
    slides = Slide.objects.filter(active=True)
    return render(request,
                  'shop/main.html',
                  {'categories': categories, 'subcategories': subcategories, 'products': products, 'slides': slides})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


