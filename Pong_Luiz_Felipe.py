import pygame
import os

#inicializa o módulo pygame
pygame.init()

#define a largura_tela e altura_tela da tela
largura_tela, altura_tela = 1000, 600

#define a raquete(x , y)
largura_raquete, altura_raquete = 30, 120

#contagem de gols
pontos_player_esq = 0
pontos_player_dir = 0

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong_Luiz_Felipe")
rodando = True
pontos_maximos = 5

#cores
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AZUL_CLARO = (135, 206, 250)
VERMELHO_CLARO = (255, 102, 102)
#fontes
fonte = pygame.font.SysFont("Arial", 50)

#fundo
fundo = pygame.image.load("ufsc.png")  #substitua pelo caminho correto
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))  #redimensiona para o tamanho da tela

#imagens setinha
caminho_imagem_es = os.path.join("minha_setinha_es.png")
caminho_imagem_dr = os.path.join("minha_setinha_dr.png")
seta_imagem_es = pygame.image.load(caminho_imagem_es)
seta_imagem_dr = pygame.image.load(caminho_imagem_dr)
minha_imagem_es = pygame.transform.scale(seta_imagem_es, (18, 20))  # Ajusta o tamanho da imagem na esquerda
minha_imagem_dr = pygame.transform.scale(seta_imagem_dr, (18, 20))  # Ajusta o tamanho da imagem na direita

#parâmetros da bola
raio = 15
bola_x, bola_y = largura_tela / 2 - raio, altura_tela / 2 - raio
velocidade_x, velocidade_y = 0.5, 0.5

#parâmetros da spawn da raquete
raquete_y = raquete_y1 = altura_tela / 2 - altura_raquete / 2
raquete_x, raquete_X = 100 - largura_raquete / 2, largura_tela - (100 - largura_raquete / 4)
velocidade_raquete = velocidade_raquete1 = 0

#parâmetros dos gadgets
gad = act = 0 

while rodando:
    #desenha a imagem de fundo
    tela.blit(fundo, (0, 0))
    
    #captura os eventos de entrada do usuário
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:                     #lembrete:  Um número positivo faz o objeto se mover para a direita (em X) ou para baixo (em Y).
            if evento.key == pygame.K_UP:                       #           Um número negativo faz o objeto se mover para a esquerda (em X) ou para cima (em Y).
                velocidade_raquete = -2
            
            if evento.key == pygame.K_DOWN:
                velocidade_raquete = 2
            
            if evento.key == pygame.K_w:
                velocidade_raquete1 = -2
            
            if evento.key == pygame.K_s:
                velocidade_raquete1 = 2
                
            if evento.key == pygame.K_RIGHT:
                gad = 1  #ativa o gadget para a raquete direita
                
            if evento.key == pygame.K_d:
                act = 1  #ativa o gadget para a raquete esquerda
                
        elif evento.type == pygame.KEYUP:
            velocidade_raquete = 0 
            velocidade_raquete1 = 0 
    
    if pontos_player_esq + pontos_player_dir == pontos_maximos:
        if pontos_player_esq > pontos_player_dir:
            texto_vencedor = "PLAYER ESQUERDO GANHOU!"
        elif pontos_player_dir > pontos_player_esq:
            texto_vencedor = "PLAYER DIREITO GANHOU!"

        #exibe virou e aguarda o botao
        while True:
            tela.fill(PRETO)
            mensagem = fonte.render(texto_vencedor, True, BRANCO)
            instrucoes = fonte.render("Pressione ENTER para sair", True, BRANCO)
            tela.blit(mensagem, (largura_tela // 2 - mensagem.get_width() // 2, altura_tela // 2 - 50))
            tela.blit(instrucoes, (largura_tela // 2 - instrucoes.get_width() // 2, altura_tela // 2 + 50))
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                    rodando = False
                    break
            if not rodando:
                break
            
    #controles do movimento da bola(          
    #bola teto/chao
    if (bola_y <= 0 + raio) or (bola_y >= altura_tela - raio):
        velocidade_y *= -1  #inverte a direção vertical da bola se é + vai -, - vai pra +
    
    #difiniçoes para reset do jogo(gols)
    
    if (bola_x >= largura_tela - raio):
        pontos_player_esq += 1
        bola_x, bola_y = largura_tela / 2 - raio, altura_tela / 2 - raio
        velocidade_x, velocidade_y = 0.5, 0.5
        velocidade_x *= -1 #)
    
    if (bola_x <= 0 + raio):
        pontos_player_dir += 1
        bola_x, bola_y = largura_tela / 2 - raio, altura_tela / 2 - raio
        velocidade_x, velocidade_y = 0.5, 0.5 
        
        

    #controles do movimento das raquetes
    if raquete_y >= altura_tela - altura_raquete:
        raquete_y = altura_tela - altura_raquete
    if raquete_y <= 0:
        raquete_y = 0
    if raquete_y1 >= altura_tela - altura_raquete:
        raquete_y1 = altura_tela - altura_raquete
    if raquete_y1 <= 0:
        raquete_y1 = 0

    #detecta colisão com a raquete direita
    if raquete_X <= bola_x <= raquete_X + largura_raquete:
        if raquete_y <= bola_y <= raquete_y + altura_raquete:
            bola_x = raquete_X
            velocidade_x *= -1  #inverte a direção horizontal da bola
    
    #detecta colisão com a raquete esquerda
    if raquete_x <= bola_x <= raquete_x + largura_raquete:
        if raquete_y1 <= bola_y <= raquete_y1 + altura_raquete:
            bola_x = raquete_x + largura_raquete
            velocidade_x *= -1  

    #controle de movimento do gadget da raquete direita
    if gad == 1:
        if raquete_X <= bola_x <= raquete_X + largura_raquete:
            if raquete_y <= bola_y <= raquete_y + altura_raquete:
                bola_x = raquete_X
                velocidade_x *= -3.5  #aumenta a velocidade da bola ao ativar o gadget
                gad = 0 

    #controle de movimento do gadget da raquete esquerda
    if act == 1:
        if raquete_x <= bola_x <= raquete_x + largura_raquete:
            if raquete_y1 <= bola_y <= raquete_y1 + altura_raquete:
                bola_x = raquete_x + largura_raquete
                velocidade_x *= -3.5  #aumenta a velocidade da bola ao ativar o gadget
                act = 0  
    
    #movimentos básicos
    raquete_y += velocidade_raquete
    raquete_y1 += velocidade_raquete1
    bola_x += velocidade_x
    bola_y += velocidade_y

    #desenho contorno e bola
    pygame.draw.circle(tela, AZUL_CLARO, (bola_x, bola_y), raio + 2)  #contorno da bola
    pygame.draw.circle(tela, AZUL, (bola_x, bola_y), raio)  #bola

    #desenho do contorno e raquetes
    pygame.draw.rect(tela, VERMELHO_CLARO, pygame.Rect(raquete_x - 2, raquete_y1 - 2, largura_raquete + 4, altura_raquete + 4))  #rontorno raquete esquerda
    pygame.draw.rect(tela, VERMELHO, pygame.Rect(raquete_x, raquete_y1, largura_raquete, altura_raquete))  #raquete esquerda
    pygame.draw.rect(tela, VERMELHO_CLARO, pygame.Rect(raquete_X - 2, raquete_y - 2, largura_raquete + 4, altura_raquete + 4))  #contorno raquete direita
    pygame.draw.rect(tela, VERMELHO, pygame.Rect(raquete_X, raquete_y, largura_raquete, altura_raquete))  #raquete direita

    #cria a tabela de gols
    texto_pontos_esq = fonte.render(f"{pontos_player_esq}", True, BRANCO)
    texto_pontos_dir = fonte.render(f"{pontos_player_dir}", True, BRANCO)
    #desenha ela
    tela.blit(texto_pontos_esq, (largura_tela // 4, 20))  #pontos esquerdo
    tela.blit(texto_pontos_dir, (largura_tela * 3 // 4, 20)) #pontos direita
    
    #coloca as imagens dos gadgets nas raquetes
    if gad == 1:
        tela.blit(minha_imagem_dr, (raquete_X+10, raquete_y))  #imagem da raquete direita
    if act == 1:
        tela.blit(minha_imagem_es, (raquete_x, raquete_y1))  #imagem da raquete esquerda

    pygame.display.update()  #atualiza a tela
