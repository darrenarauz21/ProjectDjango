from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

 #clase que maneja los datos del perfil de usuario   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.TextField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    #devuelve usuario
    def __str__(self):
        return str(self.user)
    
#clase que maneja los datos para las publicaciones del Blog
class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    content=models.TextField()
    image = models.ImageField(upload_to="blogs_img", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    #devuelve el autor y el titulo del blog
    def __str__(self):
        return str(self.author) +  " Titulo del Blog: " + self.title
    #devuelve la direccion del blog
    def get_absolute_url(self):
        return reverse('blogs')

#clase que maneja los datos para las publicaciones del review 
class ReviewPost(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130)
    content=models.TextField()
    image = models.ImageField(upload_to="reviews_img", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    #devuelve el autor y el titulo del review
    def __str__(self):
        return str(self.author) +  " Titulo de la review: " + self.title
    #devuelve la direccion del
    def get_absolute_url(self):
        return reverse('reviews')   

#clase Para los comentarios del Blog    
class CommentBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)
    #devuelve el usuario y comentario
    def __str__(self):
        return self.user.username +  " Comentario: " + self.content
 #Clase para las review   
class CommentReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    review = models.ForeignKey(ReviewPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(default=now)
    #devuelve el usuario y comentario de la review
    def __str__(self):
        return self.user.username +  " Comentario: " + self.content
    
    