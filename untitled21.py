import pygame,  sys
from button import Button


pygame.init()

SCREEN = pygame.display.set_mode((1300, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("sp.jpeg")

def sb():
    while True:
        
        OPTIONS_TEXT = get_font(70).render('SUN', True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(100, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        pygame.display.update()
def hb():
    print('sun')
def vb():
    print('sun')
def eb():
    print('sun')
def mb():
    print('sun')
def ab():
    print('sun')
def jb():    
    print('sun')
def satb():
    print('sun')
def ub():
    print('sun')
def nb():
    print('sun')


def get_font(size): 
    return pygame.font.Font("exon.otf", size)

s=pygame.transform.scale(pygame.image.load("sun.png"),(200,200))
hg=pygame.transform.scale(pygame.image.load("mercury.png"),(20,20))
v=pygame.transform.scale(pygame.image.load("Venus.png"),(40,40))
e=pygame.transform.scale(pygame.image.load("earth.png"),(40,40))
m=pygame.transform.scale(pygame.image.load("mars.png"),(30,30))
asb=pygame.transform.scale(pygame.image.load("asb.png"),(650,650))
j=pygame.transform.scale(pygame.image.load("Jupiter.png"),(120,120))
sa=pygame.transform.scale(pygame.image.load("saturn.png"),(120,90))
u=pygame.transform.scale(pygame.image.load("uranus.png"),(90,90))
n=pygame.transform.scale(pygame.image.load("neptune.png"),(65,50))

sun=Button(image=s, pos=(650, 450), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
HG=Button(image=hg, pos=(790, 450), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
venus=Button(image=v, pos=(840, 500), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
earth=Button(image=e, pos=(600, 270), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
mars= Button(image=m, pos=(415, 440), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
a=Button(image=asb, pos=(650, 450), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
jup=Button(image=j, pos=(260, 500), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
sat=Button(image=sa, pos=(230, 110), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
ur=Button(image=u, pos=(1100, 600), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")
nep=Button(image=n, pos=(1200, 200), text_input="", font=get_font(50), base_color="#68838B", hovering_color="White")




MENU_MOUSE_POS = pygame.mouse.get_pos()
while True:
    SCREEN.blit(BG, (0, 0))

    for button in [sun,HG, venus,earth,mars,a,jup,sat,ur,nep]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sun.checkForInput(MENU_MOUSE_POS):
                sb()
            if HG.checkForInput(MENU_MOUSE_POS):
                hb()
            if venus.checkForInput(MENU_MOUSE_POS):
                vb()
            if earth.checkForInput(MENU_MOUSE_POS):
                eb()
            if mars.checkForInput(MENU_MOUSE_POS):
                mb()
            if a.checkForInput(MENU_MOUSE_POS):
                ab()
            if jup.checkForInput(MENU_MOUSE_POS):
                jb()
            if sat.checkForInput(MENU_MOUSE_POS):
                satb()
            if ur.checkForInput(MENU_MOUSE_POS):
                ub()
            if nep.checkForInput(MENU_MOUSE_POS):
                nb()
            
        
    pygame.display.update()