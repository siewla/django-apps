from reviews.forms import ReviewForm
from django.shortcuts import redirect, render
from bookstore.forms import BookForm
from bookstore.models import *
from django.contrib import messages
# from django.http import Http404

# Create your views here.


def index(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book has been successfully added')
            return redirect('bookstore:index')
        else:
            messages.error(request, 'Error')
            return redirect('bookstore:index')

    books = Book.objects.all()
    context = {"form": form, "books": books}
    return render(request, 'bookstore/index.html', context)


def show(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return redirect('bookstore:index')

    if request.GET.get('action') == 'del':
        book.delete()
        return redirect('bookstore:index')

    if request.method == 'POST' and request.GET['action'] == 'edit':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('bookstore:show', book.id)

    if request.GET.get('action') == 'edit':
        form = BookForm(instance=book)
        context = {"book": book, "edit": True, "form": form}
        return render(request, 'bookstore/show.html', context)

    review_form = ReviewForm()
    context = {"book": book, "edit": False, "review_form": review_form}
    return render(request, 'bookstore/show.html', context)
