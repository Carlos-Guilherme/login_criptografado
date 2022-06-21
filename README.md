# login_criptografado

um sistema de login criptografado. Esse sistema de login não armazena nenhum dado (login ou senha) de forma "crua". Nos arquivos "login.txt" e "senha.txt"
é onde ficam a senha, só que de forma criptografada.
ao colocar um login o sistema ira verificar se com o login que foi colocado no input é possivel decifrar a mensagem criptgrafada no arquivo de texto.
se for possivel; ele retorna "ok", indicado que o login é compativel com a mensagem criptografada no arquivo de texto.
caso não seja possivel; ele retorna que o login está incorreto, ja que, para que o login esteja certo é necessario que o login passado no input seja decifravel para
o dado do arquivo de texto.

Para usa é necessário importar as seguntes bibliotecas:

import os
import cryptocode

é necessário fazer a instalação da biblioteca cryptocode pois ela não faz parte do pacote pradrão do python.
