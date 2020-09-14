from django.urls import path
from form import views
urlpatterns = [

    path('', views.home_view, name='home'),
    path('form/', views.form_view, name='form'),
    path('member_page/', views.members_view, name='member'),
    path('reply_form/<int:id>', views.reply_form, name='reply'),
    path('delete_form/<int:id>', views.delete_form, name='delete'),
    # path('error_email', views.delete_form, name='delete'),

   
    
   
]