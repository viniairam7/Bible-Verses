import pygame
import webbrowser
from time import sleep
from colorama import Fore, Style
pygame.init()
pygame.mixer.music.load('aeag.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print(Fore.GREEN,'''Olá! Estou aqui para trazer para você soluções bíblicas para o seu dia!
                   Como você está se sentindo hoje?
                   [1] Feliz/Com Alegria
                   [2] Triste/Com Mágoa
                   [3] Ansioso/Com Medo
                   [4] Estressado/Com Raiva
                   [5] Sem Amor/Sem Esperança ''')
opc = int(input('Escolha sua opção:  '))
if opc == 1:
    print(Fore.YELLOW,
          '''         Romanos 12:12 -> "Que a Esperança que vocês tem no Senhor o mantenham Alegres!"

          Filipenses 4:4 -> "Tenham sempre alegria unidos no Senhor."

          João 16:24 -> "Peçam e vocês receberão para que a alegria de vocês sejam completa!"

          Salmos 16:11 -> "A presença do Senhor enche-nos da verdadeira alegria."

          Lucas 2:10 -> "Ele é o motivo da nossa verdadeira alegria!"''')
elif opc == 2:
    print(Fore.BLUE,
          '''         Hebreus 12:2 -> "Fixe seus olhos em Jesus, pois é por meio Dele que nossa fé começa."
    
          Salmos 30:5 -> "Dá-me novamente alegria em tua Salvação e conserva em mim o desejo da obediência!"
                        
          Salmos 5:11 -> "Mas os que buscam abrigo em ti ficarão contentes e sempre cantarão de alegria porque tu os defendes."
                        
          1Pedro 1:6 -> "Talvez vocês fiquem tristes pelos muitos motivos de provações, mas alegrem-se na promessa da vida!"
                        
          Salmos 30:11 -> "Tu mudaste o meu choro em dança alegre. Foi tu Senhor quem afastou de mim a tristeza!"''')
elif opc == 3:
    print(Fore.CYAN,
          '''         Filipenses 4:6 -> "Não andeis ansiosos por coisa alguma. Antes, apresente seus pedidos a Deus e Ele cuidará de você!"

          Salmos 94:19 -> "Quando Estou aflito e preocupado, tu me consolas e me alegras!"

          Filipenses 4:7 -> "E a paz de Deus, que ninguém consegue entender, guardará você, pois você está unido com Deus."

          Habacuque 3:17 -> "Ainda que nada funcione como deve, eu me alegrarei em Ti, Criador dos Céus e da Terra!"

          Josué 1:9-> "Seja Forte e Corajoso! Não temas e não Desanime! Eu sou teu Deus, descanse em mim!"''')
elif opc == 4:
    print(Fore.RED,
          '''         Colossenses 3:15 -> "Que a paz de Deus dirija vocês em seus dias e suas decisões!"

          2Coríntios 12:9 -> "A Minha Graça te Basta!"

          Filipenses 4:9 -> "Ponha em prática tudo o que você ouviu e aprendeu sobre Ele (Jesus)."

          Romanos 12:21 -> "Vençam o mal com o bem!"

          Gálatas 5:16 -> "Deixem que o Espirito de Deus dirija a vida de vocês. É Ele quem te trará a vitória e a paz!"''')
elif opc == 5:
    print(Fore.YELLOW,
          '''         João 3:16 -> "Deus te amou de tal maneira que enviou o seu Único Filho para que fossemos salvos!"

          Romanos 5:8 -> "Deus mostrou seu amor por nós através do Sacrifício de Cristo!"

          1João 4:9 -> "Nós amamos porque Ele nos amou primeiro."

          Romanos 8:38, 39 -> "Nada existente pode nos separar do amor de Deus, que nos comprou com seu sangue imaculado."

          1Coríntios 13:13 -> "Portanto, agora existem essas 3 coisas: a fé, a esperança e o amor, porém o amor é a MAIOR delas!"''')
print('')
abc = int(input('          Esse conteúdo te abençoou? [1] para Sim e [2] para Não:   '))
if abc == 1:
    print('')
    print('°'*100)
    print('')
    print(Fore.YELLOW,'Que Deus continue abençoando seu dia! Espere um pouco para conhecer a página a seguir!')
    sleep(7)
else:
    print('Quer ler outros versículos? Recomece o sistema.')

url = 'https://www.instagram.com/umpi.oz/'
webbrowser.open(url)











