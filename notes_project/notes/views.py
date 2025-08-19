from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Note
import numpy as np
from .forms import NoteForm
import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/add_note.html', {'form': form})

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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect("home")
    return render(request, "notes/delete_note.html", {"note": note})

def home(request):
    category = request.GET.get('category')
    if category:
        notes = Note.objects.filter(category=category).order_by('-id')
    else:
        notes = Note.objects.all().order_by('-id')
    return render(request, 'notes/home.html', {'notes': notes, 'selected_category': category})


def ai_advice_view(request, note_id):
    if request.method == 'POST':
        note = get_object_or_404(Note, id=note_id)
        note_text = (
            f"Тема: {note.title}\n"
            f"Описание: {note.description}\n"
            f"Понятность: {note.get_understanding_display()}\n"
            f"Что изучено: {note.what_learned}\n"
            f"Что непонятно: {note.what_not_understood}\n"
            f"Категория: {note.category}\n"
            f"Подкатегория: {note.subcategory}"
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Ты помогаешь студенту с советами по обучению."},
                    {"role": "user", "content": note_text + "\n\nДай совет, что почитать или посмотреть, чтобы лучше понять материал."}
                ],
                max_tokens=300,
                temperature=0.7
            )
            advice = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            advice = f"Ошибка при работе с ИИ: {e}"

        return JsonResponse({'prediction': advice})
    else:
        return HttpResponseBadRequest('Метод запроса должен быть POST.')

#def infer_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        if not user_input:
            return HttpResponseBadRequest('No input data provided.')

        # Example: converting user_input into a 2D numpy array
        # In a real scenario, handle input parsing and preprocessing carefully
        input_array = np.array([[float(x) for x in user_input.split(",")]])

        prediction_result = predict(input_array)

        # Convert numpy array to list for JSON serialization
        prediction_list = prediction_result.tolist()

        return JsonResponse({'prediction': prediction_list})
    else:
        return HttpResponseBadRequest('Invalid request method.')
