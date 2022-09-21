from django.contrib import admin
from .models import *


admin.site.register(BlogPost)#permiso para crear un nuevo blog
admin.site.register(ReviewPost)#permiso para editar y eliminar blog 
admin.site.register(CommentBlog) #permiso para comentar en blog
admin.site.register(CommentReview) #permiso para comentar en review
admin.site.register(Profile) #permiso para ver perfil
