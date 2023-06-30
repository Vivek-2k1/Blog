from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    publication_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
class CommentModel(models.Model):
    post = models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return str(self.post)