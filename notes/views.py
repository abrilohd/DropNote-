from django.contrib import messages
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def note_list(request):
    notes = Note.objects.all()

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    if query:
        notes = notes.filter(
            models.Q(title__icontains=query) | models.Q(content__icontains=query)
        )

    if category:
        notes = notes.filter(category=category)

    paginator = Paginator(notes, 12)
    page_obj = paginator.get_page(request.GET.get("page"))
    query_params = request.GET.copy()
    query_params.pop("page", None)

    category_counts = dict(
        Note.objects.values("category")
        .annotate(count=Count("id"))
        .values_list("category", "count")
    )
    folders = [
        {
            "value": "",
            "label": "All notes",
            "count": Note.objects.count(),
            "description": "Everything saved",
        }
    ]
    folders.extend(
        {
            "value": value,
            "label": label,
            "count": category_counts.get(value, 0),
            "description": "Saved notes",
        }
        for value, label in Note.CATEGORY_CHOICES
    )

    context = {
        "notes": page_obj,
        "page_obj": page_obj,
        "total_notes": paginator.count,
        "pagination_query": query_params.urlencode(),
        "folders": folders,
        "query": query,
        "selected_category": category,
    }

    return render(request, "notes/index.html", context)


def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(
        request,
        "notes/detail.html",
        {"note": note},
    )


def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save()
            messages.success(request, "Note created successfully.")
            return redirect("notes:detail", pk=note.pk)
    else:
        form = NoteForm()

    return render(
        request,
        "notes/create.html",
        {"form": form},
    )


def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            messages.success(request, "Note updated successfully.")
            return redirect("notes:detail", pk=note.pk)
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "notes/edit.html",
        {
            "form": form,
            "note": note,
        },
    )


def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        messages.success(request, "Note deleted successfully.")
        return redirect("notes:index")

    return render(
        request,
        "notes/detail.html",
        {
            "note": note,
            "confirm_delete": True,
        },
    )
