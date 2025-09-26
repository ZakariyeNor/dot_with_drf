from django.db import models
from django.contrib.auth.models import User

# Note model to store notes
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('title', 'owner')
        
        
    def __str__(self):
        return self.title
