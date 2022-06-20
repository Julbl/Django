from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogListView, BlogDetailView, AddPostView, UpdatePostView, AddCategoryView, CategoryView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('post/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('category/<str:Cats>/', CategoryView, name='category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
