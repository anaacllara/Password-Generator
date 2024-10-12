import random
import string 
#show on user's screen the permissions 
print("Bem vindo ao gerador de senhas.")
letra = (int(input("É permitido letras?\n Digite 1 para sim, 2 para não: "))) 
numero = (int(input("É permitido numeros? \n Digite 1 para sim, 2 para não: ")))
caEspeciais = (int(input("É permitido caracteres especiais? \n Digite 1 para sim, e 2 para não: ")))
tam = (int(input("Digite o tamanho da senha: ")))

# passwords combinations
tipo1 = string.ascii_letters + string.digits + string.punctuation 
tipo2 = string.ascii_letters + string.digits 
tipo3 = string.ascii_letters + string.punctuation 
tipo4 = string.digits + string.punctuation 

# function to make random passwords
def senhaGerada(tam):
    senha = ''.join(random.choice(tipo1) for i in range(tam))
    return senha
def senhaGerada2(tam):
    senha =''.join(random.choice(tipo2) for i in range(tam))
    return senha
def senhaGerada3(tam):
    senha =''.join(random.choice(tipo3) for i in range(tam))
    return senha
def senhaGerada4(tam):
    senha =''.join(random.choice(tipo4) for i in range(tam))
    return senha

# the passwords agreeing with the user's condition
if ((letra == 1) and (numero == 1) and (caEspeciais==1)):
    senha = senhaGerada(tam)
    print("Sua senha é ", senha)
elif ((letra == 1) and (numero == 1) and (caEspeciais ==2)):
    senha = senhaGerada2(tam)
    print("Sua senha é ", senha)
elif ((letra == 1) and (numero == 2) and (caEspeciais == 1)):
    senha = senhaGerada3(tam)
    print("Sua senha é ", senha)
elif ((letra == 2) and (numero == 1) and (caEspeciais == 1)):
    senha = senhaGerada4(tam)
    print("Sua senha é ", senha)
else: 
    print("Não é possível gerar uma senha. ")
