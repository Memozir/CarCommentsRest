from django.contrib import admin
from django.urls import path, include

from comments.urls import router_country, router_producer, router_car, router_comment 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_country.urls)),
    path('api/', include(router_producer.urls)),
    path('api/', include(router_car.urls)),
    path('api/', include(router_comment.urls)),
    # path('api/', include('comments.urls')),
]
