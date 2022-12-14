from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE
    )  # linking the user as author, as website is only intended to be used by me
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self) -> None:
        """When I hit the 'publish' button I will set the publish date to now()"""
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("blog.Post", related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self) -> None:
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
