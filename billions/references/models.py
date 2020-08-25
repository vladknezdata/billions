from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager

class Season(models.Model):
    number = models.IntegerField()
    year = models.IntegerField()
    poster = models.ImageField(blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        ordering = ['-number']


class Episode(models.Model):
    number = models.IntegerField()
    season = models.ForeignKey(Season,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    aired = models.DateField()

    def __str__(self):
        return str(self.number)

    class Meta:
        ordering = ['number']


class ReferenceCategory(models.Model):
    category = models.CharField(max_length=25)

    def __str(self):
        return self.type


class Character(models.Model):
    name = models.CharField(max_length=50)
    aka = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25,
                            blank=True)
    img_small = models.ImageField(blank=True)
    img_large = models.ImageField(blank=True)
    actor = models.CharField(max_length=50)
    imdb_link = models.URLField(max_length=200,
                                blank=True)

    def __str__(self):
        return self.aka

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.aka)
        super().save(*args, **kwargs)


class Reference(models.Model):
    season = models.ForeignKey(Season,
                               on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode,
                                on_delete=models.CASCADE)
    characters = models.ManyToManyField(Character)
    category = models.ForeignKey(ReferenceCategory,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,
                           blank=True)
    time = models.TimeField()
    image = models.ImageField(blank=True)
    dialog = models.TextField(max_length=1000)
    explanation = models.TextField(max_length=2000)
    tags = TaggableManager(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['season', 'episode', 'time']