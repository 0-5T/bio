import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, render_to_response
from proteinWeb.forms import DocumentForm, PDBNameForm
import requests
import urllib
import urllib.request
from django.http import HttpResponse


# Create your views here.
def home(request):
    title = "Site Home"
    welcome = "Welcome to MD Web"
    form = PDBNameForm()
    return render(request, "home.html", {
        'form': form
    })


'''def upload(request):
    if request.method == "POST" and request.FILES['pdb']:
        pdb = request.FILES['pdb']
        fs = FileSystemStorage()
        filename = fs.save(pdb.name, pdb)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')
'''


'''def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})
'''


def uploadpage(request):
    form = DocumentForm()
    return render(request, 'upload.html', {"form": form})


def upload(request):
    if request.method == "POST":
        myFile = request.FILES.get("myfile", None)
        uploadFile = myFile.name
        destination = open(os.path.join("media/document", myFile.name), 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
    return render(request, 'uploadVis.html', locals())




def download(request):
    '''    if request.method == 'POST':
        name_form = PDBNameForm(request.POST, initial={'name': 'pdbIndex'})
        if name_form.is_valid():
            link = 'https://files.rcsb.org/download/' + name_form.name.upper() + '.pdb'
            urllib.request.urlretrieve(link, filename='/media')
    else:
        return render(request, 'download.html')

    return render(request, 'download.html', {'name_form': name_form})
    '''
    form = PDBNameForm()
    return render(request, 'download.html', {
        'form': form
    })


def downloadPDB(request):
    if request.method == 'POST':
        name_form = PDBNameForm(request.POST)
        if name_form.is_valid():
            #pdbIndex = name_form.cleaned_data['pdbName']
            downloadFile = name_form.cleaned_data['pdbName'] + '.pdb'
            link = 'https://files.rcsb.org/download/' + name_form.cleaned_data['pdbName'] + '.pdb'
            req = requests.get(link)
            with open("media/document/"+name_form.cleaned_data['pdbName']+".pdb", "wb") as f:
                f.write(req.content)
    else:
        name_form = PDBNameForm()
    return render(request, 'downloadVis.html', locals())


def test(request):
    main = "eudic_win.exe"
    f = os.popen(main)
    return render(request, 'test.html', locals())


