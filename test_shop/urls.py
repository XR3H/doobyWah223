from django.urls import path, include
from .views import *

art_router = routers.DefaultRouter()
art_router.register(prefix='article', viewset=TestViewSet, basename='popa')
art_router.register(prefix='category', viewset=TestCatViewSet)

zakr_router = routers.DefaultRouter()
zakr_router.register(prefix='article', viewset=ZakrViewSet, basename='zakr')

penis_router = routers.DefaultRouter()
penis_router.register(r'article', viewset=PenisViewSet, basename='article')
penis_router.register(r'article2', viewset=AnusViewSet, basename='article')
penis_router.register(r'article3', viewset=ModelAnusViewSet, basename='article')

urlpatterns = [
    path('article/<int:pk>/', ArticleAPIView.as_view()),
    path('clear_article/<int:pk>/', ArticleClearAPIView.as_view()),
    path('articles/', ArticlesCRAPIView.as_view()),
    path('test/', PenisView.as_view()),
    path('test/<int:id>/', PenisView.as_view()),
    path('penis/', include(penis_router.urls)),





    # path('api/gen/', RestGenView.as_view()),
    # path('api/gen/<int:id>/', RestGenView.as_view()),
    # path('testatview/', RestAtView.as_view()),
    # path('testudview/<int:pk>/', RestUdView.as_view()),
    # path('controllers/', include(art_router.urls)),
    # path('zakr/', include(zakr_router.urls)),

    # path('test_vs/', TestViewSet.as_view({'get':'list', 'post':'create'})),
    # path('test_vs/<int:pk>/', TestViewSet.as_view({'put':'update', 'get':'retrieve', 'delete':'destroy'})),
]