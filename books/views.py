from django.shortcuts import render, redirect, get_object_or_404
from .models import Ebook
from .forms import EbookForm


def ebook_list(request):
    ebooks = Ebook.objects.all()
    return render(request, 'books/ebook_list.html', {'ebooks': ebooks})


def ebook_detail(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    return render(request, 'books/ebook_detail.html', {'ebook': ebook})


def ebook_create(request):
    if request.method == "POST":
        form = EbookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EbookForm()
    return render(request, 'books/ebook_form.html', {'form': form})


def ebook_update(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    if request.method == "POST":
        form = EbookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EbookForm(instance=ebook)
    return render(request, 'books/ebook_form.html', {'form': form})


def ebook_delete(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    if request.method == "POST":
        ebook.delete()
        return redirect('ebook_list')
    return render(request, 'books/ebook_confirm_delete.html', {'ebook': ebook})
