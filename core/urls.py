from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Save that day',
        description='Благотворительный агрегатор',
        default_version='v1'
    ), public=True
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('docs/', schema_view.with_ui('swagger')),
    path('api/v1/', include('charity_programs.urls')),
    path('api/v1/', include('program_categories.urls')),
    path('api/v1/', include('reports.urls')),
    path('api/v1/', include('payment.urls')),
    path('paypal/', include('paypal.standard.ipn.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
