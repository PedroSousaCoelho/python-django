from django.contrib import admin
from escola.models import Aluno, Curso, Emprego, Matricula

class Alunos(admin.ModelAdmin): 
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 20
    
admin.site.register(Aluno, Alunos)

class Empregos(admin.ModelAdmin): 
    list_display=('id', 'cargo', 'empresa')
    list_display_links = ('id', 'cargo')
    
admin.site.register(Emprego, Empregos)

class Cursos(admin.ModelAdmin): 
    list_display=('id', 'codigo_curso', 'descricao',)
    list_display_liks = ('id', 'codigo_curso')
    search_fields = ("codigo_curso",)
    list_per_page = 20
    
admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin): 
   list_display = ('id', 'aluno', 'curso', 'periodo')
   list_display_links = ('id',)
    
admin.site.register(Matricula, Matriculas)