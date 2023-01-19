import linecache
#from MSD2 import filtxyz
# Este primer programa crea todos los archivos steps separados de la particula la cual 
# se va a calcular el MSD

# step final, n es el numero de moleculas para MSD
# nt numero de moleculas totales 
def MSD(steptotal,n,nt,step,a_xyz):
    
    i = 0
    while i*step < steptotal:
        #line_numbers = range((nt - n + 3) + (nt+2)*i,(nt + 3) + (nt+2)*i)
        line_numbers = range(3 + (n+2)*i, (n + 2) + (n+2)*i)
        #lines = []

        new = open("Timestep{}".format(i*step), "a")

        for k in line_numbers:
            x = linecache.getline(r"{}".format(a_xyz), k)
            
            #lines.append(x)
            new.writelines(x)
        
        new.close()
        
        #lines.clear()
        #print("Timestep:",i*step)
        #print(line_numbers)
        #print(lines)
        i += 1

#nt = 1000000 #particulas totales 
# a_xyz = archivo xyz
#n = 1024 #particulas
#step = 1000  # Periodo de 100, se actualiza cada 100
#stepF = 100000 # Step final 
#MSD(stepF + step,n,nt,step)    




