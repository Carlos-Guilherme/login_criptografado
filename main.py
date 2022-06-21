import cryptocode
import os

# criador: Carlos Emanoel
# insta: carlos_guilherme_18

# login padrão: carlos
# senha padrão: carlos123

login = open('login.txt', 'r')
login_txt = login.readline()
login = login_txt

senha = open('senha.txt', 'r')
senha_txt = senha.readline()
senha = senha_txt


opc = str(input('[1] - Login\n[2] - Mudar login\n[3] - Mudar senha\n:'))

if opc == '1':
    input_login = str(input('Login: '))
    login_decript = cryptocode.decrypt(login, input_login)
    if login_decript == 'login':
        print('login ok')
        
    else:
        print('Login incorreto!')
    input_senha = str(input('Senha: '))
    senha_decript = cryptocode.decrypt(senha, input_senha)
    if senha_decript == 'senha':
        print('Senha ok')
    else:
        print('senha incorreta!')
    
elif opc == '2':
    login_atual = str(input('Digite o login atual: '))
    login_decript = cryptocode.decrypt(login, login_atual)
    if login_decript == 'login':
        novo_login = str(input('Digite o novo login: '))
        novo_login_encript = cryptocode.encrypt('login', novo_login)
        login = open('login.txt', 'r')
        login.close()
        os.remove('login.txt')
        login = open('login.txt', 'a')
        login.write(novo_login_encript)
        print('Login alterado com sucesso!')
    else:
        print('Login incorreto!')

elif opc == '3':
    senha_atual = str(input('Digite a senha atual: '))
    senha_decript = cryptocode.decrypt(senha, senha_atual)
    if senha_decript == 'senha':
        nova_senha = str(input('Digite a nova senha: '))
        nova_senha_encript = cryptocode.encrypt('senha', nova_senha)
        senha = open('senha.txt', 'r')
        senha.close()
        os.remove('senha.txt')
        senha = open('senha.txt', 'a')
        senha.write(nova_senha_encript)
        print('Senha alterada com sucesso!')
    else:
        print('Senha incorreta!')
