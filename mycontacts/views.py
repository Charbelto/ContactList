from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def index(request):
  contacts = Contact.objects.all()
  return render(request, 'index.html', {'contacts': contacts})

def add_contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = ContactForm()

  return render(request, 'add_contact.html', {'form': form})

def edit_contact(request, pk):
  contact = Contact.objects.get(id=pk)
  
  if request.method == 'POST':
    form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
      form.save()
      return redirect('index')
      
  else:
    form = ContactForm(instance=contact)
    
  return render(request, 'edit_contact.html', {'form': form})
  
def delete_contact(request, pk):
  contact = Contact.objects.get(id=pk)
  contact.delete()
  return redirect('index')