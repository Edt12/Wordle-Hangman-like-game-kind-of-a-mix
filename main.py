

import pygame
import random

pygame.init()
screen_width = (1200)
screen_height = (700)
screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)
pygame.display.set_caption("Word Check Game")
clock = pygame.time.Clock()
background= pygame.image.load("Background.jpg")
#defining colours
black=(0,0,0)
white=(255,255,255)
Red=(255,0,0)
#finding word to display from list
words=("adduct","absurd","acquit","adjust","badger","bangle","becalm","bicker","bought","bounce","bowler","branch",
     "bright","calmer","canter","carpet","catkin","chapel","choral","common","damson","dancer","deacon","depart",
     "deputy","detail","dinghy","dismay","dollar","earwig","eating","fabric","facing","factor","family","figure",
     "firmly","flower","flying","foiled","garlic","garnet","gasped","gerbil","golden","guitar","halved","harmed",
     "hearty","hockey","housed","lawyer","learnt","lizard","longer","magnet","magpie","manger","marble","neatly")
currentWord=random.sample(words,1)#selects random word from list 1 is how many to select
currentWord=str(currentWord)
currentWord=currentWord.replace("[","")#gets rid of brackets and apostraphes because strings from random sample command  are bracketet
currentWord=currentWord.replace("]","")#example ['lawyer']
currentWord=currentWord.replace("'","")
#setting text font and creating on screen letters
font=pygame.font.Font("freesansbold.ttf",100)#font=font,Font=size
letter1=font.render("_",True,black)#""=text,true= if antialiasing or not,black = colour
letter2=font.render("_",True,black)
letter3=font.render("_",True,black)
letter4=font.render("_",True,black)
letter5=font.render("_",True,black)
letter6=font.render("_",True,black)
#creates a surface for the text to go on to for each letter
letter1Rect=letter1.get_rect()
letter2Rect=letter2.get_rect()
letter3Rect=letter3.get_rect()
letter4Rect=letter4.get_rect()
letter5Rect=letter5.get_rect()
letter6Rect=letter6.get_rect()
#creates font for text input box
userFont=pygame.font.Font("freesansbold.ttf",50)
#creates font for things other than the text box
generalSmallFont=pygame.font.Font("freesansbold.ttf",30)
#defining user text e.g what user types in
userText=""
#creates a rect for a user input box
Inputrect=pygame.Rect(screen_width/2,screen_height/2+100,25,50)#x,y,width,hieght
#creating a sign at the below the text box to tell the user to type in only lower case letters
lowercaseSign=generalSmallFont.render("Please type in only lowercase letters",True,black)
lowercaseSignRect=lowercaseSign.get_rect()
#making a limit to number of guesses and creating guess number on screen
guessNum=0
guessNumgraphic=font.render(str(guessNum),True,black)#first updating graphic
guessNumgraphicRect=guessNumgraphic.get_rect()

guessNumgraphic2=font.render("/10",True,black)#second static one
guessNumgraphic2Rect=guessNumgraphic2.get_rect()

guessSign=generalSmallFont.render("Guesses Remaining",True,black)#creating a sign to say what the numbers mean
guessSignRect=guessSign.get_rect()
#creating a win or lose graphic
winMessage=generalSmallFont.render("",True,black)
winMessageRect=winMessage.get_rect()

#creating a string of letters from a to z so user can see which letters have been guessed
a=generalSmallFont.render("a",True,black)
aRect=a.get_rect()
b=generalSmallFont.render("b",True,black)
bRect=b.get_rect()
c=generalSmallFont.render("c",True,black)
cRect=c.get_rect()
d=generalSmallFont.render("d",True,black)
dRect=d.get_rect()
e=generalSmallFont.render("e",True,black)
eRect=e.get_rect()
f=generalSmallFont.render("f",True,black)
fRect=f.get_rect()
g=generalSmallFont.render("g",True,black)
gRect=g.get_rect()
h=generalSmallFont.render("h",True,black)
hRect=h.get_rect()
i=generalSmallFont.render("i",True,black)
iRect=i.get_rect()
j=generalSmallFont.render("j",True,black)
jRect=j.get_rect()
k=generalSmallFont.render("k",True,black)
kRect=k.get_rect()
l=generalSmallFont.render("l",True,black)
lRect=l.get_rect()
m=generalSmallFont.render("m",True,black)
mRect=m.get_rect()
n=generalSmallFont.render("n",True,black)
nRect=n.get_rect()
o=generalSmallFont.render("o",True,black)
oRect=o.get_rect()
p=generalSmallFont.render("p",True,black)
pRect=p.get_rect()
q=generalSmallFont.render("q",True,black)
qRect=q.get_rect()
r=generalSmallFont.render("r",True,black)
rRect=r.get_rect()
s=generalSmallFont.render("s",True,black)
sRect=s.get_rect()
t=generalSmallFont.render("t",True,black)
tRect=t.get_rect()
u=generalSmallFont.render("u",True,black)
uRect=u.get_rect()
v=generalSmallFont.render("v",True,black)
vRect=v.get_rect()
w=generalSmallFont.render("w",True,black)
wRect=w.get_rect()
x=generalSmallFont.render("x",True,black)
xRect=x.get_rect()
y=generalSmallFont.render("y",True,black)
yRect=y.get_rect()
z=generalSmallFont.render("z",True,black)
zRect=z.get_rect()




#creating variable to check whether a letter has been guessed
letter1guessed=False
letter2guessed=False
letter3guessed=False
letter4guessed=False
letter5guessed=False
letter6guessed=False

aguessed=False
bguessed=False
cguessed=False
dguessed=False
eguessed=False
fguessed=False
gguessed=False
hguessed=False
iguessed=False
jguessed=False
kguessed=False
lguessed=False
mguessed=False
nguessed=False
oguessed=False
pguessed=False
qguessed=False
rguessed=False
sguessed=False
tguessed=False
uguessed=False
vguessed=False
wguessed=False
xguessed=False
yguessed=False
zguessed=False

while True:
    halfScreenwidth=screen_width/2
    halfScreenheight=screen_height/2


    #postions text on screen
    letter1Rect.center = (halfScreenwidth   ,halfScreenheight)
    letter2Rect.center = (halfScreenwidth+80,halfScreenheight)
    letter3Rect.center = (halfScreenwidth+160, halfScreenheight)
    letter4Rect.center = (halfScreenwidth+240, halfScreenheight)
    letter5Rect.center = (halfScreenwidth+320, halfScreenheight)
    letter6Rect.center = (halfScreenwidth+400,halfScreenheight)
    guessNumgraphicRect.center= (halfScreenwidth-300,halfScreenheight)
    guessNumgraphic2Rect.center=(halfScreenwidth-150,halfScreenheight)
    guessSignRect.center=(halfScreenwidth-200,halfScreenheight-100)
    winMessageRect.center=(halfScreenwidth,halfScreenheight-200)
    lowercaseSignRect.center=(halfScreenwidth,halfScreenheight+200)
    aRect.center=(100,halfScreenheight-300)
    bRect.center=(150,halfScreenheight-300)
    cRect.center=(200,halfScreenheight-300)
    dRect.center=(250,halfScreenheight-300)
    eRect.center=(300,halfScreenheight-300)
    fRect.center=(350,halfScreenheight-300)
    gRect.center=(400,halfScreenheight-300)
    hRect.center=(450,halfScreenheight-300)
    iRect.center=(500,halfScreenheight-300)
    jRect.center=(550,halfScreenheight-300)
    kRect.center=(600,halfScreenheight-300)
    lRect.center=(650,halfScreenheight-300)
    mRect.center=(700,halfScreenheight-300)
    nRect.center=(750,halfScreenheight-300)
    oRect.center=(800,halfScreenheight-300)
    pRect.center=(850,halfScreenheight-300)
    qRect.center=(900,halfScreenheight-300)
    rRect.center=(950,halfScreenheight-300)
    sRect.center=(1000,halfScreenheight-300)
    tRect.center=(1050,halfScreenheight-300)
    uRect.center=(1100,halfScreenheight-300)
    vRect.center=(1150,halfScreenheight-300)
    wRect.center=(1200,halfScreenheight-300)
    xRect.center=(1250,halfScreenheight-300)
    yRect.center=(1300,halfScreenheight-300)
    zRect.center=(1350,halfScreenheight-300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == pygame.KEYDOWN:
            #defining key presses for letters in text box
            if event.key == pygame.K_a and aguessed==False:
                userText = "a"
            if event.key == pygame.K_RETURN and userText=="a":# turns each letter at the top red when it is guessed by only allowing them to be turned red when enter is pressed and the letters are in the text box
                    a = generalSmallFont.render("a", True, Red)
                    aguessed = True

            if event.key == pygame.K_b and bguessed==False:#two if functions for each letter
                userText = "b"
            if event.key == pygame.K_RETURN and userText == "b":
                b = generalSmallFont.render("b", True, Red)
                bguessed = True

            if event.key == pygame.K_c and cguessed==False:
                userText = "c"
            if event.key == pygame.K_RETURN and userText == "c":
                c = generalSmallFont.render("c", True, Red)
                cguessed = True

            if event.key == pygame.K_d and dguessed==False:
                userText = "d"
            if event.key == pygame.K_RETURN and userText == "d":
                d = generalSmallFont.render("d", True, Red)
                dguessed = True

            if event.key == pygame.K_e and eguessed==False:
                userText = "e"
            if event.key == pygame.K_RETURN and userText == "e":
                e = generalSmallFont.render("e", True, Red)
                eguessed = True

            if event.key == pygame.K_f and fguessed==False:
                userText = "f"
            if event.key == pygame.K_RETURN and userText=="f":
                f = generalSmallFont.render("f", True, Red)
                fguessed = True

            if event.key == pygame.K_g and gguessed==False:
                userText = "g"
            if event.key == pygame.K_RETURN and userText=="g":
                g = generalSmallFont.render("g", True, Red)
                gguessed = True

            if event.key == pygame.K_h and hguessed==False:
                userText = "h"
            if event.key == pygame.K_RETURN and userText=="h":
                h = generalSmallFont.render("h", True, Red)
                hguessed = True

            if event.key == pygame.K_i and iguessed==False:
                userText = "i"
            if event.key == pygame.K_RETURN and userText=="i":
                i = generalSmallFont.render("i", True, Red)
                iguessed = True

            if event.key == pygame.K_j and jguessed==False:
                userText = "j"
            if event.key == pygame.K_RETURN and userText == "j":
                j = generalSmallFont.render("j", True, Red)
                jguessed = True

            if event.key == pygame.K_k and kguessed==False:
                userText = "k"
            if event.key == pygame.K_RETURN and userText=="k":
                k = generalSmallFont.render("k", True, Red)
                kguessed = True

            if event.key == pygame.K_l and lguessed==False:
                userText = "l"
            if event.key == pygame.K_RETURN and userText=="l":
                l = generalSmallFont.render("l", True, Red)
                lguessed = True

            if event.key == pygame.K_m and mguessed==False:
                userText = "m"
            if event.key == pygame.K_RETURN and userText=="m":
                m = generalSmallFont.render("m", True, Red)
                mguessed = True

            if event.key == pygame.K_n and nguessed==False:
                userText = "n"
            if event.key == pygame.K_RETURN and userText == "n":
                n = generalSmallFont.render("n", True, Red)
                nguessed = True

            if event.key == pygame.K_o and oguessed==False:
                userText = "o"
            if event.key == pygame.K_RETURN and userText=="o":
                o = generalSmallFont.render("o", True, Red)
                oguessed = True

            if event.key == pygame.K_p and pguessed==False:
                userText = "p"
            if event.key == pygame.K_RETURN and userText=="p":
                p = generalSmallFont.render("p", True, Red)
                pguessed = True

            if event.key == pygame.K_q and qguessed==False:
                userText = "q"
            if event.key == pygame.K_RETURN and userText=="q":
                q = generalSmallFont.render("q", True, Red)
                qguessed = True

            if event.key == pygame.K_r and rguessed==False:
                userText = "r"
            if event.key == pygame.K_RETURN and userText == "r":
                r = generalSmallFont.render("r", True, Red)
                rguessed = True

            if event.key == pygame.K_s and sguessed==False:
                userText = "s"
                sguessed=True
            if event.key == pygame.K_RETURN and userText=="s":
                s= generalSmallFont.render("s", True, Red)
                sguessed = True

            if event.key == pygame.K_t and tguessed==False:
                userText = "t"
            if event.key == pygame.K_RETURN and userText=="t":
                t = generalSmallFont.render("t", True, Red)
                tguessed = True

            if event.key == pygame.K_u and uguessed==False:
                userText = "u"
            if event.key == pygame.K_RETURN and userText=="u":
                u = generalSmallFont.render("u", True, Red)
                uguessed = True

            if event.key == pygame.K_v and vguessed==False:
                userText = "v"
            if event.key == pygame.K_RETURN and userText=="v":
                v = generalSmallFont.render("v", True, Red)
                vguessed = True

            if event.key == pygame.K_w and wguessed==False:
                userText = "w"
            if event.key == pygame.K_RETURN and userText=="w":
                w = generalSmallFont.render("w", True, Red)
                wguessed = True

            if event.key == pygame.K_x and xguessed==False:
                userText = "x"
            if event.key == pygame.K_RETURN and userText=="x":
                x = generalSmallFont.render("x", True, Red)
                xguessed = True

            if event.key == pygame.K_y and yguessed==False:
                userText = "y"

            if event.key == pygame.K_RETURN and userText=="y":
                 y= generalSmallFont.render("y", True, Red)
                 yguessed = True

            if event.key == pygame.K_z and zguessed==False:
                userText = "z"

            if event.key == pygame.K_RETURN and userText=="z":
                z = generalSmallFont.render("z", True, Red)
                zguessed = True

            if event.key==pygame.K_RETURN and guessNum <10 and userText!=currentWord[0] and userText!= currentWord[1] and userText != currentWord[2] and userText!=currentWord[3] and userText !=currentWord[4] and userText!=currentWord[5] and userText!="":
                guessNum+=1
                guessNumgraphic=font.render(str(guessNum),True,black)#updates the score counter

            if event.key== pygame.K_RETURN and currentWord[0] ==userText and guessNum<10 and letter1guessed==False:
                letter1 = font.render(userText, True, black)
                letter1guessed=True

            if event.key== pygame.K_RETURN and currentWord[1]==userText and guessNum<10 and letter2guessed==False:
                letter2 = font.render(userText, True, black)
                letter2guessed=True

            if event.key == pygame.K_RETURN and currentWord[2] ==userText and guessNum<10and letter3guessed==False:
                letter3 = font.render(userText, True, black)
                letter3guessed=True

            if event.key== pygame.K_RETURN and currentWord[3] ==userText and guessNum<10 and letter4guessed==False:
                letter4 = font.render(userText, True, black)
                letter4guessed=True

            if event.key== pygame.K_RETURN and currentWord[4]==userText and guessNum<10and letter5guessed==False:
                letter5 = font.render(userText, True, black)
                letter5guessed=True

            if event.key== pygame.K_RETURN and currentWord[5] ==userText and guessNum<10and letter6guessed==False :
                letter6 = font.render(userText, True, black)
                letter6guessed=True

            if event.key== pygame.K_BACKSPACE:
                userText = userText[:-1]#tells user text to go del1ete last character this is needed as unicode does not have a backspace function

            if textSurface.get_width()>20:#limits text box to only one character
                userText=userText[:-1]

            if  letter1guessed==True and letter2guessed==True and letter3guessed==True and letter4guessed==True and letter5guessed==True and letter6guessed==True:
                winMessage=generalSmallFont.render("Congratulations you win",True,black)

            if guessNum==10 and (letter1guessed==False or letter2guessed==False or letter3guessed==False or letter4guessed==False or letter5guessed==False or letter6guessed==False ):
                winMessage=generalSmallFont.render("Game over you lost!",True,black)



    pygame.draw.rect(screen, white, Inputrect)#draws text box
    textSurface=userFont.render(userText,True,black)
    screen.blit(textSurface,(Inputrect.x+5,Inputrect.y+5))#renders text surface on Input rect but slightly to side to stop overflow-generates rectangle whever it is typed
    Inputrect.w = max(20, textSurface.get_width()+10)

   #generates letters on screen by updating the screen
    screen.blit(letter1,letter1Rect)
    screen.blit(letter2,letter2Rect)
    screen.blit(letter3,letter3Rect)
    screen.blit(letter4,letter4Rect)
    screen.blit(letter5,letter5Rect)
    screen.blit(letter6,letter6Rect)
    screen.blit(guessNumgraphic,guessNumgraphicRect)
    screen.blit(guessNumgraphic2,guessNumgraphic2Rect)
    screen.blit(guessSign,guessSignRect)
    screen.blit(winMessage,winMessageRect)
    screen.blit(lowercaseSign,lowercaseSignRect)
    screen.blit(a,aRect)
    screen.blit(b, bRect)
    screen.blit(c, cRect)
    screen.blit(d, dRect)
    screen.blit(e, eRect)
    screen.blit(f, fRect)
    screen.blit(g, gRect)
    screen.blit(h, hRect)
    screen.blit(i, iRect)
    screen.blit(j, jRect)
    screen.blit(k, kRect)
    screen.blit(l, lRect)
    screen.blit(m, mRect)
    screen.blit(n, nRect)
    screen.blit(o, oRect)
    screen.blit(p, pRect)
    screen.blit(q, qRect)
    screen.blit(r, rRect)
    screen.blit(s, sRect)
    screen.blit(t, tRect)
    screen.blit(u, uRect)
    screen.blit(v, vRect)
    screen.blit(w, wRect)
    screen.blit(x, xRect)
    screen.blit(y, yRect)
    screen.blit(z, zRect)

    pygame.display.update()  # keeps window open
    screen.blit(background,(0,0))#generates background
    #sets framerate
    clock.tick(60)


