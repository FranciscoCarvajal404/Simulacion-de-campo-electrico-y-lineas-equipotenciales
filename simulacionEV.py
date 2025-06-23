#@author: franciscocarvajal
import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt

q1 = [(-1e-9,0,0)]
q2 = [(-1e-9,-1,0),(-1e-9,1,0)]
q3 = [(-1e-9,0,2),(-1e-9,-1,0), (-1e-9, 1,0)]
q4 = [(-1e-9,-1,-1),(-1e-9,-1,1), (-1e-9, 1,1), (-1e-9, 1, -1)]

def EV(cargas, R = 5,n = 30, scale = 20):
    
    c = 1/(4*np.pi*sc.epsilon_0) #1/4πε_0
    
    #Inicializamos la cuadricula
    x = np.linspace(-R, R, n) #Recta en x
    y = np.linspace(-R, R, n) #Recta en y
    X, Y = np.meshgrid(x,y) #Devuelve una lista de matrices de coordenadas a partir de vectores de coordenadas
    
    #Iniciamos los campos con matrices de coordenas vacias
    V = np.zeros_like(X)
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(X)
    
    #Calculamos los valores de las componetes del campo y del potencial
    for qi, xi, yi in cargas:
        rx = X - xi #Vector de posicion en x
        ry = Y - yi #Vector de posicion en y
        
        r = np.sqrt(rx**2 + ry**2) #Magnitud del vector posicion 
        r[r == 0] = 1e-20 #Cambia el valor r=0 si es que existe
    
        Ex += c * qi * (rx / r**3)
        Ey += c * qi * (ry / r**3)
        
        V = c * (qi / r)
        
        '''
        Notemos que para las componentes del campo electrico usamos 
        las componentes del vector r (r_x o r_y), mientras que para 
        el potencial usamos la magnitud de r
        '''
        
    #Calculamos la magnitud de E y sus vectores unitarios para graficar
    E = np.sqrt(Ex**2 + Ey**2)
    Exu = Ex / E
    Eyu = Ey / E
        
    #Trazado de lineas equipotenciales
    r_min = 0.5 #A partir de donde se empiezan a dibujar las lineas equipotenciales
    r_max = R #El valor maximo, que sera R
    num_niveles = 10 #Total de lineas que se dibujaran 
    radios = np.linspace(r_min, r_max, num_niveles)
    
    niveles = []
    for q in [q for q, _, _ in cargas]:
        niveles_q = c * q / radios #Calculamos V solo donde queremos graficarlo
        niveles.extend(niveles_q) #Los guardamos
        s
    
    #Iniciamos la gráfica
    plt.figure(figsize=(8,6))
    
    #Solo se grafica el potencial 
    if len(cargas) == 1:
        plt.contour(X, Y, V, levels = niveles, colors = "blue", linestyles = "solid")
        plt.title("Campo eléctrico y lìneas equipotenciales")
    else: 
        plt.title("Campo eléctrico")
        
    #Agregamos las flechas de campo electrico
    plt.quiver(X, Y, Exu, Eyu, E, cmap = "viridis", scale = scale)
    
    #Agregamos puntos en donde va cada carga
    for qi, xi, yi in cargas:
        color = "ro" if qi > 0 else "bo"
        plt.plot(xi, yi, color, label= f'q = {qi:1e} C')
        
    #Agregamos cuadricula e iniciamos
    plt.grid(True)        
    #plt.axis("equal")
    plt.show()
