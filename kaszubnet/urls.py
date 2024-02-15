"""kaszubnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kaszubnet_app.views import *

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(), name="index"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('user_menu/', UserMenuView.as_view(), name="user-menu"),
    path('main_menu/<str:name>/', MainMenuView.as_view(), name="main-menu"),
    path('character_editor/', CharacterEditorView.as_view(), name="character-editor"),
    path('faction_menu/', FactionMenuView.as_view(), name="faction-menu"),
    path('members/', FactionMembersView.as_view(), name="members"),
    path('hierarchy/', FactionHierarchyView.as_view(), name="hierarchy"),
    path('faction_law/', FactionLawView.as_view(), name="faction-law"),
    path('chronicle_menu/', ChronicleMenuView.as_view(), name="chronicle-menu"),
    path('chronicle_chronology/', ChronicleChronologyView.as_view(), name="chronicle-chronology"),
    path('artefacts_menu/', ArtefactsMenuView.as_view(), name="artefacts-menu"),
    path('artefact/<str:name>/', ArtefactView.as_view(), name="artefact"),
    path('warehouse_menu/', WarehouseMenuView.as_view(), name="warehouse-menu"),
    path('warehouse_status/', WarehouseStatusView.as_view(), name="warehouse-status"),
    path('warehouse_action_add/', WarehouseActionAddView.as_view(), name="warehouse-action-add"),
    path('warehouse_action_update/', WarehouseActionUpdateView.as_view(), name="warehouse-action-update"),
    path('expansion_map/', ExpansionMapView.as_view(), name="expansion-map"),
    ]
urlpatterns += staticfiles_urlpatterns()
