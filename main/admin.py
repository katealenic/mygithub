from attachments.admin import AttachmentInlines
from django.contrib.admin import site
from main.models import Membership, News, Project, Comment, Discussions, Developer, Wiki, Files
from django.contrib import admin

class CoometInline(admin.TabularInline):
    model = Comment

class DiscussionAdmin(admin.ModelAdmin):
    inlines = [CoometInline, ]

class CommentAdmin(admin.ModelAdmin):
    pass

class WikiAdmin(admin.ModelAdmin):
    pass

class ProjectInline1(admin.TabularInline):
    model = Discussions

class ProjectInline2(admin.TabularInline):
    model = Files

class ProjectInline3(admin.TabularInline):
    model = Developer

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectInline1, ProjectInline2, ProjectInline3, ]

site.register(Files)
site.register(News)
site.register(Project, ProjectAdmin)
site.register(Membership)
site.register(Comment, CommentAdmin)
site.register(Discussions,  DiscussionAdmin)
site.register(Developer)
site.register(Wiki, WikiAdmin)

