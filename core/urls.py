from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.urls import re_path, include
from graphene_django.views import GraphQLView

urlpatterns = [
    re_path(r"^$", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    re_path(
        r"^about/$",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    re_path(settings.ADMIN_URL, admin.site.urls),
    # User management
    re_path(r"^users/", include("users.urls", namespace="users")),
    re_path(r"^accounts/", include("allauth.urls")),
    # Third party apps here
    re_path(r"^comments/", include("django_comments.urls")),
    re_path(r"^graphql", GraphQLView.as_view(graphiql=True)),
    re_path(r"^markdownx/", include("markdownx.urls")),
    # Local apps here
    re_path(
        r"^notifications/",
        include("notifications.urls", namespace="notifications"),
    ),
    re_path(r"^articles/", include("articles.urls", namespace="articles")),
    re_path(r"^notebooks/", include("notebooks.urls", namespace="notebooks")),
    re_path(r"^news/", include("news.urls", namespace="news")),
    re_path(r"^messages/", include("messager.urls", namespace="messager")),
    re_path(r"^qa/", include("qa.urls", namespace="qa")),
    re_path(r"^search/", include("search.urls", namespace="search")),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development
    urlpatterns += [
        re_path(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        re_path(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        re_path(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        re_path(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [re_path(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
