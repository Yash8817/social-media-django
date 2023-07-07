import profile
from django.contrib import admin
from core.views import like_post
from .models import Post, Profile , LikePost,FollowerCount

# Register your models here.


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowerCount)



