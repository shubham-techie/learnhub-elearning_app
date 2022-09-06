from django.urls import path
from . import views

urlpatterns =[
    path('',views.home, name='home'),

    path('notes/',views.notes, name="notes"),
    path('delete_note/<int:pk>',views.delete_note, name="delete_note"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name="notes_detail"),
    
    path('assignment/',views.assignment, name="assignment"),
    path('update_assignment/<int:pk>/<str:page>', views.update_assignment, name="update_assignment"),
    path('delete_assignment/<int:pk>/<str:page>',views.delete_assignment, name="delete_assignment"),

    path('youtube/',views.youtube, name="youtube"),

    path('todo/',views.todo, name="todo"),
    path('delete_todo/<int:pk>/<str:page>', views.delete_todo, name="delete_todo"),
    path('update_todo_status/<int:pk>/<str:page>', views.update_todo_status, name="update_todo_status"),
   
    path('books/',views.books, name="books"),

    path('dict/',views.dict, name="dict"),

]