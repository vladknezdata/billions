from django.shortcuts import render, get_object_or_404
from .models import Season, Episode, Reference, ReferenceCategory, Character
from taggit.models import Tag

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

def list_view(request, tag_slug=None, episode_number=None):
    references = Reference.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        references = references.filter(tags__in=[tag])
    if episode_number:
        references = references.filter(episode=episode_number)
    for reference in references:
        reference.faces = reference.characters.all()
        print(reference.faces)
        print(reference.characters.all())
    return render(request,
                  'references/reference/list.html',
                  {'references': references})


def season_list_view(request):
    seasons = Season.objects.all()
    return render(request,
                  'references/seasons/list.html',
                  {'seasons': seasons})

def season_detail_view(request, season_number=None):
    season = Season.objects.get(number=season_number)
    episodes = Episode.objects.filter(season=season_number)
    return render(request,
                  'references/seasons/detail.html',
                  {'season': season,
                   'episodes': episodes})

def character_detail_view(request, aka):
    character = Character.objects.get(aka=aka)
    return render(request,
                  'references/characters/detail.html',
                  {'charachter': character})

def character_list_view(request):
    characters = Character.objects.all()
    return render(request,
                  'references/characters/list.html',
                  {'characters': characters})

