from django.contrib import admin
from board.models import Post
# Register your models here.


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}
