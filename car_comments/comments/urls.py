from django.urls import path
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

import car_comments.settings
from . import views, export_views

router_country = SimpleRouter()
router_country.register(r'country', viewset=views.CountryViewset)

router_producer = SimpleRouter()
router_producer.register(r'producer', viewset=views.ProducerViewset)

router_car = SimpleRouter()
router_car.register(r'car', viewset=views.CarViewset)

router_comment = SimpleRouter()
router_comment.register(r'comment', viewset=views.CommentViewset)


urlpatterns = [
    path('country/export/', name='country_export', view=export_views.CountryExportiew.as_view()),
    path('producer/export/', name='producer_export', view=export_views.ProducerExportiew.as_view()),
    path('car/export/', name='car_export', view=export_views.CarExportiew.as_view()),
    path('comment/export/', name='comment_export', view=export_views.CommentExportiew.as_view()),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
