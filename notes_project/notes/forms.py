from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'understanding', 'what_learned', 'what_not_understood', 'category', 'subcategory']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите тему'}),
            'description': forms.Textarea(attrs={'placeholder': 'О чём была тема?', 'rows': 4}),
            'understanding': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
            'what_learned': forms.Textarea(attrs={'placeholder': 'Что вы изучили нового?', 'rows': 2}),
            'what_not_understood': forms.Textarea(attrs={'placeholder': 'Что осталось непонятным?', 'rows': 2}),
            'category': forms.Select(choices=[('IT', 'IT'), ('Languages', 'Языки')]),
            'subcategory': forms.TextInput(attrs={'placeholder': 'Подкатегория'}),

        }
