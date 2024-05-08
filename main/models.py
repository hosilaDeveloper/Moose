from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class SocialMedia(TimeStampedModel):
    icon_name = models.CharField(max_length=212)
    link = models.CharField(max_length=212)

    def __str__(self):
        return self.icon_name


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to="author/")
    occupation = models.CharField(max_length=212)
    social_media = models.ManyToManyField(SocialMedia)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    second_title = models.CharField(max_length=212, blank=True, null=True)
    second_description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to="comment/")
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class About(TimeStampedModel):
    title = models.CharField(max_length=212)
    description = models.TextField()
    second_title = models.CharField(max_length=212, blank=True, null=True)
    second_description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
