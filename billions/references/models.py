from django.db import models

class Season(models.Model):
    number = models.IntegerField()
    year = models.IntegerField()
    poster = models.ImageField(blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        ordering = ['number']


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
    img_small = models.ImageField(blank=True)
    img_large = models.ImageField(blank=True)
    actor = models.CharField(max_length=50)

    def __str__(self):
        return self.aka


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
    time = models.TimeField()
    image = models.ImageField(blank=True)
    dialog = models.TextField(max_length=500)
    explanation = models.TextField(max_length=1500)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['season', 'episode', 'time']