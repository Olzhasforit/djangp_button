from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import AwsBucketModel
import boto3
import fitz


s3 = boto3.client('s3')

# Create your views here.
def htmlform(request):
    return render(request, 'my_app/htmlform.html')

def add_record(request):
    upload_file_path = 'test_dir/a.jpg'
    s3.upload_fileobj(open(request.POST['file'], 'rb'), request.POST['name'], upload_file_path)
    return HttpResponseRedirect(reverse('htmlform'))

def pdfform(request):
    return render(request, 'my_app/pdfform.html')

def pdf_find(request):
    doc = fitz.open(request.POST['file'])
    search_word = request.POST['word']

    for page in doc:
        areas = page.search_for(search_word)
        higlight = page.add_highlight_annot(areas)
        higlight.set_colors(stroke=[1, 0, 0])
        higlight.update()
        print(1)
    doc.save("x.pdf")
    return HttpResponseRedirect(reverse('pdfform'))
