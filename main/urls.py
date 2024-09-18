from django.urls import path
from main.views import show_main, create_mood_entry, show_xml,show_json,show_json_by_id,show_xml_by_id,register,login_user,logout_user


app_name = 'main'

urlpatterns = [
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('json/', show_json, name='show_json'),
    path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]