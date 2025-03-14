from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .extra_views import *

project_router = DefaultRouter()
project_router.register(r'projects', views.ProjectViewSet, basename='project')

file_router = DefaultRouter()
file_router.register(r'files', views.FileViewSet, basename='file')

project_assignment_router = DefaultRouter()
project_assignment_router.register(r'project_assignments', views.ProjectAssignmentViewSet,
                                   basename='project_assignment')

stage_assignment_router = DefaultRouter()
stage_assignment_router.register(r'stage_assignments', views.StageAssignmentViewSet, basename='stage_assignment')

stage_router = DefaultRouter()
stage_router.register(r'stages', views.StageViewSet, basename='stage')

stage_report_router = DefaultRouter()
stage_router.register(r'stages_reports', views.StageViewSet, basename='stage_report')

project_report_router = DefaultRouter()
stage_router.register(r'project_reports', views.StageViewSet, basename='project_report')

# API
urlpatterns = [
    path('test_assign/<uuid:project_id>/<uuid:stage_id>/', views.test_assign, name='test_assign'),  # Тест
    # принадлежности пользователя к данной сущности
    path('', include(project_router.urls)),  # Проекты
    path('', include(file_router.urls)),  # Файлы
    path('', include(project_assignment_router.urls)),  # Назначения для проектов
    path('', include(stage_assignment_router.urls)),  # Назначения для этапов
    path('', include(stage_router.urls)),  # Этапы
    path('', include(stage_report_router.urls)),
    path('', include(project_report_router.urls)),
    path('e/ms/', project_from_file),
    path('e/user_projects/', get_user_projects, name='user-projects'),
    path('e/project_stages/<uuid:project_id>/', get_project_stages),
    path('e/stage_substages/<uuid:stage_id>/', get_stage_substages),
    path('e/project_files/<uuid:project_id>/<str:type>/', get_project_files),
    path('e/stage_files/<uuid:stage_id>/<str:type>/', get_stage_files),
]
