from django.contrib import admin
from .models import Comments, Posts, Likes, Follwers 

# Register your models here.
admin.site.register(Comments)
admin.site.register(Posts)
admin.site.register(Likes)
admin.site.register(Follwers)
