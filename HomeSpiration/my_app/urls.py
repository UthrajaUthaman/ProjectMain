from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('professional_home',views.professional_dashboard,name='professional_dashboard'),
    path('login/',views.loginnew,name='login'),
    path('signup',views.register_normal_user,name='signup'),
    path('register/professional/',views.register_professional,name='register_professional'),
    path('about',views.about,name='about'),
    path('logout/',views.logoutp,name='logout'),
    path('submit-professional-type-services/', views.submit_professional_type_services, name='submit_professional_type_services'),
    path('submit-professional-website-info/', views.submit_professional_website_info, name='submit_professional_website_info'),
    path('submit-professional-final-details/', views.submit_professional_final_details, name='submit_professional_final_details'),
    #path('addprojects',views.addprojects,name='addprojects'),
    path('Design/', views.generate_image_from_txt, name='Design'),

    path('add_project/', views.add_project, name='add_project'),
    path('show-projects/', views.show_projects, name='show_projects'),
    path('project-detail/<int:project_id>/', views.project_detail, name='project_detail'),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

