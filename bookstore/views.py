from django.shortcuts import render

# Create your views here.
def index(request):
    # form = BookForm()
    # if request.method == 'POST':
    #     form = BookForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('books_index')
    # books = Book.objects.all()
    # context = {"form": form, "books": books}
    return render(request, 'bookstore/index.html')
