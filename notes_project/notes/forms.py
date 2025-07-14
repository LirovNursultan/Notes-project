from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description', 'understanding']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите тему'}),
            'description': forms.Textarea(attrs={'placeholder': 'О чём была тема?', 'rows': 4}),
            'understanding': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
        }
