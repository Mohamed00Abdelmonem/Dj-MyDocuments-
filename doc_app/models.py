from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

class Section(models.Model):
    title = models.CharField(max_length=100)
    intro = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='section_author')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
    

class Subject(models.Model):
    section = models.ForeignKey(Section, on_delete=models.SET_NULL,null=True, related_name='subject_section')
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title
    


# class detail_subject(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True, related_name='detail_subject_subject')
#     author = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
#     created_at = models.DateTimeField(default=timezone.now)

#     def __str__(self) -> str:
#         return self.content.split()[:10]
    