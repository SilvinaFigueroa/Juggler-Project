from django.db import models


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Project Name")

    def __str(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100,
                             help_text="Task Title")
    description = models.TextField(max_length=300,
                                   verbose_name="Describe Task")

    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str(self):
        return self.title
