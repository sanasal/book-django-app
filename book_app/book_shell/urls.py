from django import views
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static      
from django.conf import settings       
from . import views   

app_name='book_shelf'
   
urlpatterns = [          
    path('' , views.home , name='home'),     
    path('log_in/' , views.log_in , name= 'log_in'),
    path('sign_in/' , views.sign_in , name='sign_in'),
    path('log_out/' , views.log_out , name='log_out'),
    path('Mystry and police/' , views.police_view , name = 'police'),
    path('Sciences/' , views.Sciences_view , name = 'sciences'),     
    path('Programming/' , views.Programming_view, name = 'programming'),
    path('Languages/' , views.Languages_view , name = 'languages'),
    path('Islam/' , views.Islam_view , name = 'islam'),
    path('Psychology/' , views.Psychology_view , name = 'psychology'),
    path('Reoprt issue/' , views.report_issue , name='report_issue'),
    path('Add Comment/' , views.add_comment , name='add_comment'),
    path('Islam/<str:name>/' , views.book_islam_detail , name= 'book_islam_detail'),
    path('Programming/<str:name>/' , views.book_prog_detail , name = 'book_prog_detail'),
    path('Languages/<str:name>/' , views.book_lang_detail , name = 'book_lang_detail'),
    path('Sciences/<str:name>/' , views.book_sci_detail , name = 'book_sci_detail'),
    path('Psychology/<str:name>/' , views.book_psy_detail , name = 'book_psy_detail'),
    path('Mystry and ploice/<str:name>/' , views.book_mystry_detail , name = 'book_mystry_detail'),
    path('pdf/<str:name>/' , views.pdf , name= 'pdf'),
    path('search_islam/' , views.Islam_search , name='search_islam'),
    path('search_police/' , views.police_search , name='search_police'),
    path('search_programming/' , views.prog_search , name='search_prog'),
    path('search_sciences/' , views.sci_search , name='search_sci'),
    path('search_languages/' , views.lang_search , name='search_lang'),
    path('search_psychyologist/' , views.psy_search , name='search_psy'),
]