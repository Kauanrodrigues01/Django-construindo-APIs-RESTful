from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasCursoSerializer, ListaMatriculasEstudanteSerializer
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# IsAdminUser: Só quem é admin pode acessar
# IsAuthenticatedOrReadOnly: Qualquer usuário autenticado pode acessar para leitura(GET), mas só quem é admin pode acessar para(POST, PUT, DELETE)

class EstudanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication] # Autentificação
    permission_classes = [IsAuthenticated] # Qualquer usuario logado tem permissão de acessar está view
    
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class ListaMatriculaEstudante(generics.ListAPIView):
    '''
    
    '''
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk_estudante'])
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer
    
class ListaMatriculaCurso(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk_curso'])
        return queryset
        
    serializer_class = ListaMatriculasCursoSerializer