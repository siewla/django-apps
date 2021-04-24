from bookstore.models import Book
from reviews.models import Review
from reviews.forms import ReviewForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def create(request, book):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # form.save()
            # review = Review(
            #     name=request.POST['name'], review=request.POST['review'], book=book)
            # review.save()
            book = Book.objects.get(pk=book)
            book.reviews.create(
                name=request.POST['name'], review=request.POST['review'])
            return redirect('bookstore:show', book.id)

    if request.GET.get('action') == 'del':
        review = Review.objects.get(pk=request.GET.get('pk'))
        review.delete()
        return redirect('bookstore:index')

    # if request.method == 'POST' and request.GET['action'] == 'edit':
    #     form = ReviewForm(request.POST, instance=review)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('bookstore:show', book.id)

    # if request.GET.get('action') == 'edit':
    #     form = ReviewForm(instance=review)
    #     context = {"review": review, "edit": True, "form": form}
    #     return render(request, 'bookstore/show.html', context)

    return HttpResponse({"message": "works"})
