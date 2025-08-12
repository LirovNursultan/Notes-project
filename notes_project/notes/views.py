from django.conf import settings
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})

def home(request):
    notes = Note.objects.all().order_by('-id')
    return render(request, 'notes/home.html', {'notes': notes})

from django.shortcuts import get_object_or_404

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/view_note.html', {'note': note})

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            note.delete()
            return redirect('home')
        else:
            return redirect('home')
    return render(request, 'notes/delete_note.html', {'note': note})

def home(request):
    category = request.GET.get('category')
    if category:
        notes = Note.objects.filter(category=category).order_by('-id')
    else:
        notes = Note.objects.all().order_by('-id')
    return render(request, 'notes/home.html', {'notes': notes, 'selected_category': category})



