from django.shortcuts import render, get_object_or_404
from .models import Season, Episode, Reference, ReferenceCategory, Character

def detail_view(request, slug):
    reference = get_object_or_404(Reference, slug=slug)
    characters = reference.characters.all()
    if not reference.slug:
        refrence.slug = slugify(reference.title)

    context = {'reference': reference,
               'characters': characters}
    return render(request,
                  'references/reference/detail.html',
                  context)

def list_view(request):
    references = Reference.objects.all()
    for reference in references:
        reference.faces=reference.characters.all()
    # characters = reference.characters.all()
    return render(request,
                  'references/reference/list.html',
                  {'references': references})