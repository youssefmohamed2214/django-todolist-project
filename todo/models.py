from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=400)
    complete = models.BooleanField(default=False)
    task_image = models.ImageField(upload_to="todo_images/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']



@receiver(post_delete, sender=Todo)
def delete_task_image_on_delete(sender, instance, **kwargs):
    """
    Deletes the task_image file from the filesystem
    when a Todo object is deleted.
    """
    # The 'instance' is the Todo object that was just deleted.
    if instance.task_image:
        instance.task_image.delete(save=False)

