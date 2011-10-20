#!/usr/bin/python
from django.contrib import admin
from QPaperGenerator.QP.models import *

RTF = True


class CommonMedia:
        js = (
        '/site_media/dojo-toolkit/dojo/dojo.js',
        '/site_media/js/editor.js',
        )
        css = {
        'all': ('/site_media/css/editor.css',),
        }
        # let's add it to this model
        #admin.site.register(models.Category,
        #        list_display  = ('full_name',),
        #        search_fields = ['full_name',],
        #        Media = CommonMedia,
        #        )

class InlineSubjectAdmin(admin.TabularInline):
    model = Subject
    extra = 2
    if RTF:
        Media = CommonMedia

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [InlineSubjectAdmin,]
    fields = ('name', 'description') 
    list_filter = ('name', )
    search_fields = ('name','description')
    if RTF:
        Media = CommonMedia

class QuestionInlineAdmin(admin.TabularInline):
    model = Question
    extra = 7
    if RTF:
        Media = CommonMedia

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name' , 'subject_code' , 'department' , )
    list_display_links = ('name' ,)
    list_editable = ('subject_code' , 'department')
    fields = ('department' , 'name' , 'subject_code' , 'description' , )
    list_filter = ( 'department' , 'name' , 'subject_code' , )
    search_fields = ('name', 'department' , 'subject_code' , 'description')
    inlines = [QuestionInlineAdmin]
    if RTF:
        Media = CommonMedia
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question' , 'question_type' , 'unit_number', 'subject' )
    
    list_display_links = ('question' ,)
    list_editable = ('question_type' ,'unit_number' ,  'subject')
    list_filter = ('question_type' , 'unit_number' , 'subject')
    if RTF:
        Media = CommonMedia
 

######################################################################################3




admin.site.register(Department , DepartmentAdmin )
admin.site.register(Subject , SubjectAdmin,  )
admin.site.register(Question , QuestionAdmin ,  )  



