from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # CRUD Médecin
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    path('doctors/import/', views.import_doctors, name='doctor_import'),

    # Gestion des commentaires pour un médecin
    path('doctors/<int:pk>/comments/', views.doctor_comments, name='doctor_comments'),
    path('doctors/<int:pk>/comments/add/', views.comment_create_for_doctor, name='comment_create_for_doctor'),
    path('doctors/<int:pk>/comments/import/', views.comment_import_for_doctor, name='comment_import_for_doctor'),

    # CRUD Commentaire (édition, suppression, analyse)
    path('comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comments/<int:comment_id>/analyse/', views.comment_analyse, name='comment_analyse'),

    # Pour la navbar "Comments" : sélection d'un médecin
    path('comments/', views.select_doctor_for_comments, name='select_doctor_for_comments'),

    # Authentification
    path('login/', views.login_custom, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
