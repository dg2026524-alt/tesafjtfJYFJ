uranus = sphere(pos = vec(0,0,0),color=vec(201/255,239/255,252/255),radius=20)
ariel = sphere(pos = vec(50,0,0),color=vec(137/255,130/255,130/255),radius=9)  
umbriel = sphere(pos = vec(-50,0,0),color=vec(181/255,178/255,178/255),radius=5)
sun = sphere(pos = vec(-900,0,0),color=vec(248/255,86/255,17/255),radius=50,emissive=True)
ring(pos=vector(-900,0,0), axis=vector(0,1,0), radius=900, thickness=0.2)
ring(pos=vector(0,0,0), axis=vector(0,0,1), radius=30, thickness=0.1)
ring(pos=vector(0,0,0), axis=vector(0,1,0), radius=50, thickness=0.4)
t=0
c=0
v=0
lamp = local_light(pos=vector(-900,0,0),color=color.white)
while True :
    rate(200)
    t+=0.001
    ariel.pos = vec(50*cos(t),0,50*sin(t))
    umbriel.pos = vec(-50*cos(t),0,-50*sin(t))
    uranus.pos = vec(0*cos(t), 0*sin(t), 0.1) 
