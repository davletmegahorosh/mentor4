from django.contrib import admin
from django.urls import path
from catalog.views import main, pizza_view, pizza_detail_view, create_pizza
from users.views import auth_view, logout_view, register_view
from django.conf.urls.static import static
from mentor_4.settings import MEDIA_URL, MEDIA_ROOT
# from mentor_4.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('pizza/', pizza_view),
    path('pizza/<int:id>/', pizza_detail_view),
    path('create/', create_pizza),

    path('users/login/', auth_view),
    path('users/logout/', logout_view),
    path('users/register/', register_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)