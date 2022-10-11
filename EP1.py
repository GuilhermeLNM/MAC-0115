#!/usr/bin/env python
# coding: utf-8

# In[10]:

N=int(input("Digite o número de pokébolas: "))

g=int(input("Digite o valor da gravidade: "))

xp=int(input("Digite a coordenada x (inteiro >= 0) do pokemon: "))

yp=int(input("Digite a coordenada y (inteiro >= 0) do pokemon: "))

acertou=False

errou=False

t=0

n=1

vx=1

while N>=n and acertou==False:
    
    print("Tentativa: ", n)
    
    xt=int(input("Digite a coordenada x (inteiro >= 0) do treinador: "))
    yt=int(input("Digite a coordenada y (inteiro >= 0) do treinador: "))
    vy=int(input("Digite a componente y da velocidade de lancamento: "))
    
    yb=yt+vy*t-(t*t*g//2)
    xb=xt+vx*t
    vb=vy-g*t
    
    print("t =" ,t, ", vy =" ,vb, ", x =" ,xb, ", y =" ,yb)
    
    t+=1
    
    while acertou==False and errou==False:
        
        yb=yt+vy*t-(t*t*g//2)
        xb=xt+vx*t
        vb=vy-g*t
        
        print("t =" ,t, ", vy =" ,vb, ", x =" ,xb, ", y =" ,yb)
        
        if xb==xp and yb==yp:
            acertou=True
            print("A pokebola atingiu o pokemon.")
        elif xb>=xp or yb<=0:
            errou=True
            print("A pokebola não atingiu o pokemon.")
        t+=1    
    n+=1
    t=0
    errou=False


# In[ ]:




