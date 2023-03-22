from django.urls import path
from django.conf.urls.static import static
from ..car_comments import settings


# Добавить для каждой модели эндпоинт с возможностью забрать все записи
# Пример: 'get/country'
# Использовать ViewSets
urlpatterns = [
    path('get/country/', name='get_country'),
    path('get/country/xlx', name='get_country_xlx'),
    path('get/country/csv', name='get_country_csv'),
    path('create/country', name='create_country'),
    path('update/country', name='update_country'),
    path('delete/country', name='delete_country'),

    path('get/producer', name='get_producer'),
    path('get/producer/xlx', name='get_producer_xlx'),
    path('get/producer/csv', name='get_producer_csv'),
    path('get/producer', name='create_producer'),
    path('get/producer', name='update_producer'),
    path('get/producer', name='delete_producer'),

    path('get/car', name='get_car'),
    path('get/car/xlx', name='get_car_xlx'),
    path('get/car/csv', name='get_car_csv'),
    path('create/car', name='create_car'),
    path('update/car', name='update_car'),
    path('delete/car', name='delete_car'),

    path('get/comment', name='get_comment'),
    path('get/comment/xlx', name='get_comment_xlx'),
    path('get/comment/csv', name='get_comment_csv'),
    path('create/comment', name='create_comment'),
    path('update/comment', name='update_comment'),
    path('delete/comment', name='delete_comment'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
