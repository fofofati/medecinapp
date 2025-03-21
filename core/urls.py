# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Dashboard et authentification
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_custom, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Médecins
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    path('doctors/import/', views.import_doctors, name='doctor_import'),

    # Commentaires
    path('doctors/<int:pk>/comments/', views.doctor_comments, name='doctor_comments'),
    path('doctors/<int:pk>/comments/add/', views.comment_create_for_doctor, name='comment_create_for_doctor'),
    path('comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comments/<int:comment_id>/analyse/', views.comment_analyse, name='comment_analyse'),
    path('comments/<int:comment_id>/annotate/', views.annotate_comment, name='annotate_comment'),
    path('doctors/<int:pk>/comments/import/', views.comment_import_for_doctor, name='comment_import_for_doctor'),

    # Sélection d'un médecin pour voir ses commentaires
    path('comments/', views.select_doctor_for_comments, name='select_doctor_for_comments'),

    # CRUD Aspects (Aborder) – saisie manuelle
    path('comments/<int:comment_id>/aborder/add/', views.aborder_add, name='aborder_add'),
    path('comments/aspect/<int:aborder_id>/edit/', views.aborder_edit, name='aborder_edit'),
    path('comments/aspect/<int:aborder_id>/delete/', views.aborder_delete, name='aborder_delete'),

    path('aspects/create_ajax/', views.aspect_create_ajax, name='aspect_create_ajax'),
]

