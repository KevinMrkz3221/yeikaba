from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    title = models.CharField(max_length = 200)
    class Tag(models.TextChoices):
        fantasy = 'fantasy', 'fantasy'
        bodypaint = 'bodypaint', 'bodypaint'
        effects = 'effects', 'effects'
        hair_color = 'hair_color', 'hair_color'

    category = models.CharField(
        max_length=10,
        choices=Tag.choices,
        default=Tag.fantasy
    )
    description = models.TextField()
    client = models.CharField(max_length=200)

    image=models.ImageField(upload_to='static/images/projects/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/projects/', blank=True, null=True)

    def __str__(self) -> str:
        return self.project.title