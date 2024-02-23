# todo_list/todo_app/views.py
from django.views.generic import ListView
from .models import ToDoList,ToDoItem


class ListListView(ListView):
    model = ToDoList
    template_name = "index.html"
    context_object_name="todo_lists"
    
class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_list.html"
    context_object_name="todo_items"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context
    
