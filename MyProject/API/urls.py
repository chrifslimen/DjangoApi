from django.urls import path
from .views import Artical_list
from .views import apiOverview
from .views import taskList,taskDetail,taskCreate,taskUpdate,taskDelete,taskDetailTitle
from .views import compteList,compteDetail,compteCreate
from .views import photoList,photoUpload
urlpatterns = [
    path('', apiOverview, name='apiOverview'),
    path('article/', Artical_list),
    path('task-list/', taskList, name="task-list"),
    path('task-detail/<str:pk>/', taskDetail, name="task-detail"),
    path('task-detail-title/<str:pk>/', taskDetailTitle, name="task-detail"),
    path('task-create/', taskCreate, name="task-create"),
    path('task-update/<str:pk>/', taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', taskDelete, name="task-delete"),
    path('compte-list/', compteList, name="compte-list"),
    path('compte-detail/', compteDetail, name="compte-detail"),
    path('compte-create/', compteCreate, name="compte-create"),
    path('photo-list/', photoList, name="photo-list"),
    path('photo-upload/', photoUpload, name="photo-upload"),

]