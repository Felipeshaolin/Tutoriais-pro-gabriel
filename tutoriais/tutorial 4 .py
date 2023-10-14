#agora vamos fazer um progama que torna numeros da base 10 (numeros que agente usa normalmente, como 5,100,400)
#em numeros decimais (10110)
#primeiro temos que descobrir como converter, isso e muito facil
# escolhemos o numero 10
#nos dividimos por 2, isso faz 5. o numero nao tem resto, ou seja nao tem virgula.entao agente escreve um 0
#dividimos 5 por 2. 2,5. nos escrevemos um 1 porque ele tem virgula
# dividimos 2 por 2. isso da 1, entao escrevemos 0
#dividimos 1 por 2 . isso da 0,5 nos ecrevemos 1 e nos terminamos porque chegamos ao numero zero.
#agora se agente coloca os numeros em ordem isso fica (1010) 
#                                                      ^
#                                                   primeiro numero que agente dividiu e dai os outros numeros vem depois
#legal nao? mas como podemos fazer isso?
# tem um peque sujeito que ainda nao falei, os loops.
#loop em ingles quer dizer repetir varias vezess(essa traducao nao é a certa kkkk)
#porque utilisar os loops? porque assim nos podemos refazer algo varias vezes em um pedaço de codigo e nao precisar repetir mil vezes
# o tipo de loop que nos vamos utilisar vem do comando while: ele funciona bem parecido com o if: mas o diferente é que
# ele vai repetir o codigo que ta dentro dele enquanto a condiçao for verdade

# vamos começar?

#começamos por definir un numero com o comando input()
number = int(input("put number here: "))
#         ^
#         este comando esta aqui para mostrar pro progama que este é um numero. o problema é que o comando de input () automaticamente faz as coisas virarem letras e nao numeros
#         entao mesmo se vc colocase um numero, por exemplo 6, ele ia pensar que e a letra 6 do teclado nao o numero 6. um pouco bagunçado mas é importante

rep = " "
# nos criamos uma variavel (algo que vai quardar os numeros) 
while number > 0:
# ^
#  enquanto o numero for maior que 0 o progama vai ser repetido
    if number % 2 ==0:
#     se o restante do numero é igual a zero...
        rep = '0' + rep
#         ^
# agente vai dizer que agora a variavel que agente tinha feito agora que dizer " 0"
# agente tinha definido antes a variavel como a letra espaco " " entao si agente adiciona a letra  "0" para isso, isso da " 0"
#tome cuidado com as armadilhas, "0" nao é a mesma coisa que 0 . o primeiro que dizer a letra 0 e o outro o numero 0
    else:
# se o restante nao for 0 ele vai vir aqui 
        rep = '1' + rep
# agora agente faz a mesma coisa mas com o 1
    number //= 2
# agora nos dividimos o numero por dois para obter o proximo numero
# faça atençao no lugar dos comandos, esse comando nao esta dentro de um if ou else ele esta dentro do while entao ele vai ser feito
# depois do if ou while
print("binary",rep)
#quando o numero for menor que 0 ele vai executar esse codigo, ele esta fora do while
#e assim nos conseguimos nosso numero





