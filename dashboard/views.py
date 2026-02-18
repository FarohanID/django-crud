from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# READ: Menampilkan semua produk
def product_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/index.html', {'products': products})

# CREATE: Menambah produk
def product_create(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            stock=request.POST['stock']
        )
        return redirect('product_list')
    return render(request, 'dashboard/form.html')

# UPDATE: Mengedit produk
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.save()
        return redirect('product_list')
    return render(request, 'dashboard/form.html', {'product': product})

# DELETE: Menghapus produk
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')