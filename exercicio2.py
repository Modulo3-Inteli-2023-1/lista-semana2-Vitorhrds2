#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui
def is_anagram(string1, string2):
    # Remove espaços em branco e converte as strings em minúsculas
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    # Verifica se os comprimentos das strings são iguais
    if len(string1) != len(string2):
        return False

    # Converte as strings em listas e as ordena
    lista1 = sorted(list(string1))
    lista2 = sorted(list(string2))

    # Compara as listas ordenadas para verificar se são iguais
    if lista1 == lista2:
        return True
    else:
        return False






# Teste a sua função aqui (caso ache necessário)











