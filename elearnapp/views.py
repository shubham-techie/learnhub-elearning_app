from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
from django.views import generic
from youtubesearchpython import VideosSearch
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def notes(request):
   if request.method=="POST":
      form=NotesForm(request.POST)
      if form.is_valid():
         notes=Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
         notes.save()
         messages.success(request, "Notes Added Successfully")
         return redirect('notes')

   else:
      form=NotesForm()

   notes=Notes.objects.filter(user=request.user)
   context={
      'notes':notes,
      'form':form,
   }
   return render(request, 'notes.html',context)

@login_required
def delete_note(request,pk=None):
   Notes.objects.get(id=pk).delete()
   return redirect('notes')

class NotesDetailView(generic.DetailView):
   model=Notes
   template_name='notes_detail.html'


@login_required
def assignment(request):
   if request.method=="POST":
      form=AssignmentsForm(request.POST)
      if form.is_valid():
         try:
            finished=request.POST['is_finished']
            finished=True if finished=='on' else False
         except:
            finished=False

         assignment=Assignments(
            user=request.user,
            subject=request.POST['subject'],
            title=request.POST['title'],
            description=request.POST['description'],
            due=request.POST['due'],
            is_finished=finished
         )
         assignment.save()
         messages.success(request, "Assignment Added Successfully")
         return redirect('assignment')
   
   else:
      form=AssignmentsForm()

   assignments=Assignments.objects.filter(user=request.user)
   ALL_ASSIGNS_DONE=True if len(assignments)==0 else False
   context={
      'assignments':assignments,
      'ALL_ASSIGNS_DONE':ALL_ASSIGNS_DONE,
      'form': form,
   }
   return render(request, 'assignment.html', context)

@login_required
def update_assignment(request,pk=None, page='assignment'):
   assignment=Assignments.objects.get(id=pk)
   assignment.is_finished=not  assignment.is_finished
   assignment.save()
   return redirect(page)

@login_required
def delete_assignment(request, pk=None, page='assignment'):
   Assignments.objects.get(id=pk).delete()
   return redirect(page)



def youtube(request):
   if request.method=='POST':
      form=DashboardForm(request.POST)
      text=request.POST['text']
      video=VideosSearch(text, limit=20)
      result_list=[]
      
      for i in video.result()['result']:
         result_dict={
            'input':text,
            'title':i['title'],
            'duration':i['duration'],
            'thumbnail':i['thumbnails'][0]['url'],
            'channel':i['channel']['name'],
            'link':i['link'],
            'views':i['viewCount']['short'],
            'published':i['publishedTime']
         }

         desc=''
         if i['descriptionSnippet']:
            for j in i['descriptionSnippet']:
               desc +=j['text']
         result_dict['description']=desc

         result_list.append(result_dict)

         context={
            'form':form,
            'results':result_list
         }

   else:
      form=DashboardForm()
      context={
         'form':form,
      }
   return render(request, 'youtube.html',context)


@login_required
def todo(request):
   if request.method=='POST':
      form=TodoForm(request.POST)
      if form.is_valid():
         try:
            status=request.POST['status']
            status=True if status=='on' else False
         except:
            status=False

         todo=Todo(
            user=request.user,
            task=request.POST['task'],
            status=status
         )
         todo.save()
         messages.success(request, "Todo Task Added Successfully")
         return redirect('todo')
   else:
      form=TodoForm()

   tasks=Todo.objects.filter(user=request.user)
   ALL_TASKS_DONE=False if len(tasks)>0 else True
   context={
      'tasks':tasks,
      'ALL_TASKS_DONE': ALL_TASKS_DONE,
      'form':form
   }
   return render(request, 'todo.html', context)

@login_required
def update_todo_status(request, pk=None, page='todo'):
   todo=Todo.objects.get(id=pk)
   todo.status=not todo.status
   todo.save()
   return redirect(page)

@login_required
def delete_todo(request,pk=None, page='todo'):
   Todo.objects.get(id=pk).delete()
   return redirect(page)



def books(request):
   if request.method=='POST':
      form=DashboardForm(request.POST)
      text=request.POST['text']
      url = "https://www.googleapis.com/books/v1/volumes?q="+text
      res=requests.get(url).json()

      result_list=[]
      
      for i in range(10):
         book=res['items'][i]['volumeInfo']

         result_dict={
            'title':book['title'],
            'subtitle':book.get('subtitle'),
            'description':book.get('description'),
            'pageCount':book.get('pageCount'),
            'categories':book.get('categories'),
            'rating':book.get('pageRating'),
            'thumbnail':book.get('imageLinks').get('thumbnail'),
            'preview':book.get('previewLink'),
         }
         result_list.append(result_dict)

         context={
            'form':form,
            'results':result_list
         }

   else:
      form=DashboardForm()
      context={
         'form':form,}
   return render(request, 'books.html',context)



def dict(request):
   if request.method=='POST':
      form=DashboardForm(request.POST)
      input=request.POST['text']
      url="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+input
      res=requests.get(url).json()

      phonetics=res[0]['phonetics'][0]
      meanings=res[0]['meanings'][0]['definitions'][0]
      definition=meanings['definition']

      try:
         phonetic_text=phonetics['text']
         audio=phonetics['audio']

         example=meanings['example']
         synonyms=meanings['synonyms']
         
         context={
            'form':form,
            'input':input,
            'phonetic_text':phonetic_text,
            'audio':audio,
            'definition':definition,
            'example':example,
            'synonyms':synonyms
         }
      except:
         context={
            'form':form,
            'input':input,
            'definition':definition,
         }
   
   else:
      form=DashboardForm()
      context={'form':form}

   return render(request, 'dictionary.html', context)



def register(request):
   if request.method=='POST':
      form=UserRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         username=form.cleaned_data['username']
         messages.success(request, f"Account created successfully for {username}!!")
         return redirect('login')
      else:
         if request.POST['password1']!=request.POST['password2']:
               messages.success(request, f"Both passwords must be same.")
         else:
            username=request.POST['username']
            try:
               User.objects.get(username=username)
               messages.success(request,f"Account with {username} already exists!!")
            except:
               messages.success(request,"Follow the instructions for password!!")
         return redirect('register')
   else:
      form=UserRegistrationForm()

   context={
      'form':form
   }
   return render(request, 'register.html', context)


@login_required
def profile(request):
   assignments=Assignments.objects.filter(is_finished=False, user=request.user)
   todos=Todo.objects.filter(user=request.user, status=False)
   
   ASSIGNMENTS_DONE= True if len(assignments)==0 else False
   TODOS_DONE= True if len(todos)==0 else False

   context={
      'assignments':assignments,
      'todos':todos,
      'ASSIGNMENTS_DONE':ASSIGNMENTS_DONE,
      'TODOS_DONE':TODOS_DONE
   }
      
   return render(request, 'profile.html', context)
