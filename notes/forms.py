from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "category", "link"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Give your note a clear title...",
                    "class": "form-input",
                    "aria-label": "Note title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "placeholder": "Write something worth remembering...",
                    "rows": 8,
                    "class": "form-input",
                    "aria-label": "Note content",
                    "spellcheck": "true",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-input",
                    "aria-label": "Note category",
                }
            ),
            "link": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com",
                    "class": "form-input",
                    "aria-label": "Reference link",
                    "inputmode": "url",
                }
            ),
        }
