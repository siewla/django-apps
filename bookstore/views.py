from reviews.forms import ReviewForm
from django.shortcuts import redirect, render
from bookstore.forms import BookForm, CategoryForm
from bookstore.models import *
from django.contrib import messages
# from django.http import Http404

# Create your views here.


def index(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            messages.success(request, 'Book has been successfully added')
            book = Book(title=request.POST['title'],
                        author=request.POST['author'],
                        price=request.POST['price'],
                        description=request.POST['description'],
                        published_year=request.POST['published_year'],
                        cover=request.FILES['cover'])
            book.save()
            categories = form.cleaned_data['categories']
            # one line solution to loop below
            # book.categories.add(*categories)
            for cat in categories:
                book.categories.add(cat)

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


def create_category(request):
    category_form = CategoryForm()
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('bookstore:index')
    context = {"category_form": category_form}
    return render(request, 'bookstore/create_category.html', context)
