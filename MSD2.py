
# funcion filtro, luego de hacer los archivos Timesteps, ahora se van a separar en diferentes arrays para
# cada posicion
def filtxyz(filename,xyz):
   
    f = open(filename,"r")
    x = []
    y = []
    z = []
    for line in f:
        a,b,c,d = line.split(" ")
        x.append(float(b))
        y.append(float(c))
        z.append(float(d))

    if xyz == 'x':
        return x   
    elif xyz == 'y': 
        return y
    elif xyz == 'z':
        return z      
#---------------------------------------------------------------------------------------------------------------------------------
particulas = 1000000
step = 1000
stepF = 10000 # final step
# To obtain the MSD we need the inital positions and the final positions  
x0,y0,z0 = filtxyz("Timestep0","x"), filtxyz("Timestep0","y"), filtxyz("Timestep0","z")
xf,yf,zf = filtxyz("Timestep{}".format(stepF),"x"),filtxyz("Timestep{}".format(stepF),"y"),filtxyz("Timestep{}".format(stepF),"z") 
#---------------------------------------------------------------------------------------------------------------------------------
# funcion para sacar el MSD de una dimension (x, y o z)
# The next loop is for calculate the MSD de x y z 
def MSDD(xyz):
    l = 0 # contador
    deltax_squared, deltay_squared, deltaz_squared = 0,0,0 

    while l < particulas:
        if xyz == 'x':
            deltax_squared = (x0[l] - xf[l])**2 + deltax_squared
        elif xyz == "y":    
            deltay_squared = (y0[l] - yf[l])**2 + deltay_squared
        elif xyz == 'z':
            deltaz_squared = (z0[l] - zf[l])**2 + deltaz_squared

        l += 1

    if xyz == "x":
        MSD = (1/particulas)*deltax_squared
        
    elif xyz == "y":    
        MSD = (1/particulas)*deltay_squared
        
    elif xyz == "z":    
        MSD = (1/particulas)*deltaz_squared
        
    return MSD

# Coeficiente de difusion program
t = stepF/step
Dx = MSDD("x")/(6*t)
print(Dx)

