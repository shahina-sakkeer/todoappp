from . import views
from django.urls import path

urlpatterns = [
    path("",views.add,name="added"),
    path("delete/<int:taskid>/",views.delete,name="deleted"),
    path("update/<int:id>/",views.update,name="remove"),
    path("list/",views.TodoListView.as_view(),name="listing"),
    path("detail/<int:pk>/",views.TodoDetailView.as_view(),name="detailed"),
    path("update/<int:pk>/",views.TodoUpdateView.as_view(),name="edit"),
    path("delete/<int:pk>/",views.TodoDeleteView.as_view(),name="deleting")  
]
