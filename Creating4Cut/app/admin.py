from django.contrib import admin
from .models import Post, Photo

#Photo 클래스를 Inline으로 나타낸다.
class PhotoInline(admin.TabularInline):
    model = Photo

#Post 클래스는 해당하는 photo 객체를 리스트로 관리한다.
class PostAdmin(admin.ModelAdmin):
    inlines=[PhotoInline, ]

# Register your models here.
admin.site.register(Post, PostAdmin)