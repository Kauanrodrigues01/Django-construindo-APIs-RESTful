from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']   

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'  # Pega todos os campos


# 1 - Serializer de Matricula
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []  # Não exclui nenhum campo, ou seja, pega todos os campos
        
# 2 - Serializer de Matricula por Estudante
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    '''
    ➤ serializers.ReadOnlyField() diz para API que o campo é somente leitura, ou seja, não pode ser modificado.
    ➤ source='curso.descricao' é uma forma de acessar o campo descrição do curso, em vez de retornar o id do curso.
    
    ➤ O nome do método que será chamado pelo serializers.SerializerMethodField() segue essa convenção: get_ + nome da variável. Se a variável fosse chamada x, o método deveria ser get_x(self, obj).
    
    ➤ O obj é a instância do modelo Matricula.
    
    ➤ O método get_periodo_display() é uma função do Django que retorna o valor "por extenso" de um campo que utiliza escolhas (choices) no modelo.
    '''
    curso = serializers.ReadOnlyField(source='curso.descricao') 
    
    periodo = serializers.SerializerMethodField()
    
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()


# 3 - Serializer de Matricula por Curso
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    
    class Meta:
        model = Matricula
        fields = ['estudante_nome']