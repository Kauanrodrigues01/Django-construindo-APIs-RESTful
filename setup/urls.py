from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # Todas as rotas vão estar dentro do router
    path('estudantes/<int:pk_estudante>/matriculas/', ListaMatriculaEstudante.as_view()), # Tem que colocar o .as_view() quando tiver usando o generics.ListAPIView
    path('cursos/<int:pk_curso>/matriculas/', ListaMatriculaCurso.as_view()) 
]
