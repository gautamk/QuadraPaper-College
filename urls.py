from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^QuestionPaperFrom/', 'QPaperGenerator.QP.views.GenerateQuestionPaperGetDetails'),
    (r'^GenerateQPaper/','QPaperGenerator.QP.views.GenerateQuestionPaperFromDetails'),
    # Example:
    # (r'^QPaperGenerator/', include('QPaperGenerator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$','QPaperGenerator.QP.views.Root_url'),
    (r'^photologue/', include('photologue.urls')),
    


)
