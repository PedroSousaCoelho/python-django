from rest_framework import serializers
from escola.models import Aluno, Curso, Emprego, Matricula

class AlunoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class EmpregoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Emprego
        fields = ['cargo', 'empresa']

class CursoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Curso
        fields = '__all__'
        
class MatriculaSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Matricula
        exclude = []
    """Tras todos os itens com exclude[], mas se quiser colocar somente um item para não aparecer"""
    
class ListaMatriculasAlunoSerializer(serializers.ModelSerializer): 
    curso = serializers.ReadOnlyField(source = 'curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta: 
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj): 
        return obj.get_periodo_display()