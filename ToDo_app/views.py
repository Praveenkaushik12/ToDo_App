# todo_list/todo_app/views.py
# from typing import Any
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from .models import ToDoList,ToDoItem


class ListListView(ListView):
    model = ToDoList
    template_name = "index.html"
    context_object_name="todo_lists"
    
class ItemListView(ListView):
    model = ToDoItem
    template_name = "account/todo_list.html"
    context_object_name="todo_items"
    
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
    
class ListCreate(CreateView):
    model=ToDoList
    fields=["title"]
    template_name="account/todolist_form.html"
    
    def get_context_data(self):
        context=super(ListCreate,self).get_context_data()
        context["title"]="Add a new list"
        return context
    
class ItemCreate(CreateView):
    model=ToDoItem
    fields=[
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    template_name="account/todoitem_form.html"
    
    def get_initial(self):
        initial_data=super(ItemCreate,self).get_initial()
        todo_list=ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"]=todo_list
        return initial_data
    
    def get_context_data(self):
        context=super(ItemCreate,self).get_context_data()
        todo_list=ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"]=todo_list
        context["title"]="Create a new item"
        return context
    
    def get_success_url(self):
        return reverse("list",args=[self.object.todo_list_id])
    
class ItemUpdate(UpdateView):
    model=ToDoItem
    fields=[
        "todo_list",
        "title",
        "description",
        "due_date",
    ]
    template_name="account/todoitem_form.html"
    
    def get_context_data(self):
        context=super(ItemUpdate,self).get_context_data()
        context["todo_list"]=self.object.todo_list
        context["title"]="Edit item"
        return context
    
    def get_success_url(self):
        return reverse("list",args=[self.object.todo_list_id])        
