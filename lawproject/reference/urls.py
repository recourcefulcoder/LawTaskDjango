from django.urls import path

from . import views

app_name = "reference"
urlpatterns = [
    path("", views.do_nothing, name="index"),
    path("docs-meta/", views.get_documents_metadata, name="docs_meta"),
    path(
        "doc-meta/<int:document_id>/",
        views.get_document_metadata,
        name="doc_meta"
    ),
    path("docs/", views.get_documents, name="docs"),
    path("doc/<int:document_id>/", views.get_document, name="doc"),
    path("category/", views.get_category, name="category"),
]
