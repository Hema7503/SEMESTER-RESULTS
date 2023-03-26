'''from django.urls import path,include
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('details/',views.get_details,name='get_details')
]'''

from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
path('',views.webpage1,name='webpage1'),
path('result2',views.webpage2,name='webpage2'),
path('result3',views.webpage3,name='webpage3'),
#path('result4',views.webpage4,name='webpage4'),

path('index',views.index,name='index'),
path('result/',views.result,name='result'),
path('admin_login/',views.admin_login,name='admin_login'),
path('admin_panel/',views.admin_panel,name='admin_panel'),
path('delete-student/<int:id>/',views.delete_student,name='delete-student'),
path('edit-student/<int:id>/',views.edit_student,name='edit-student'),
path('edit-confirm/<int:id>/',views.edit_confirm,name='edit_confirm'),
path('logout/',views.admin_logout,name='admin-logout'),
path('add_student/',views.add_student,name='add_student'),
path('add_confirm/',views.add_confirm,name='add_confirm'),
#path('Index/',views.Index,name='Index'),
#path('details/',views.get_details,name='get_details'),
]

