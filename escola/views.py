from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Emprego, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, EmpregoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class EmpregosViewSet(viewsets.ModelViewSet): 
    """Exibindo todos os Empregos"""
    queryset = Emprego.objects.all()
    serializer_class = EmpregoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class MatriculaViewSet(viewsets.ModelViewSet): 
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    
class ListaMatriculasAluno(generics.ListAPIView): 
    """Listando todas as matriculas"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView): 
    def get_queryset(self):
        query_set = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return query_set
    serializer_class = ListaAlunosMatriculadosSerializer