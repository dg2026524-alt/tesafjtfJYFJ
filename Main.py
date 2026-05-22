uranus = sphere(pos = vec(0,0,0),color=vec(201/255,239/255,252/255),radius=20)
ariel = sphere(pos = vec(50,0,0),color=vec(137/255,130/255,130/255),radius=9)  
umbriel = sphere(pos = vec(-50,0,0),color=vec(181/255,178/255,178/255),radius=5)
sun = sphere(pos = vec(-1200,0,0),color=vec(248/255,86/255,17/255),radius=50)
ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=50, thickness=0.4)
ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=30, thickness=0.1)
t=0
while True :
    rate(200)
    t+=0.001
    ariel.pos = vec(50*cos(t), 50*sin(t), 1)
    umbriel.pos = vec(-50*cos(t), -50*sin(t), -1)
    uranus.pos = vec(0*cos(t), 0*sin(t), 0.1) 
