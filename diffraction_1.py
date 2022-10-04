from numpy import cos, sin, sqrt, pi, meshgrid, linspace, zeros
import matplotlib.pyplot as plt

def J(m,x): #Bessel's function
    def f(theta):
        return 1/pi*cos(m*theta-x*sin(theta))
    #SIMPSON'S METHOD:
    N = 1000 #numero de divisiones
    a = 0.0 #limite inferior
    b = pi  #limite superior
    h = (b-a)/N #tamaño de las divisiones
    s = 1/3*(f(a) + f(b))
    for k in range(1,N,2): #terminos impares
        s += 1/3*(4*f(a+k*h))
    for k in range(2,N,2): #terminos pares
        s += 1/3*(2*f(a+k*h))
    return h*s

x = linspace(0,20,100)
plt.title("Bessel's functions")
plt.xlabel('x')
plt.ylabel('Jm(x)')
plt.grid(True)
plt.plot(x,J(0,x),'b-',label='J0(x)')
plt.plot(x,J(1,x),'r-',label='J1(x)')
plt.plot(x,J(2,x),'g-',label='J2(x)')
plt.legend()
plt.show()

#INTENSITY AS FUNCTION OF RADIUS
def I(r):
    k = 2*pi/0.5 #numero de onda, 500 nm a micrometros
    return (J(1,k*r)/(k*r))**2

N = 1000 #precision
matrix = zeros((N,N))

x = y = linspace(-1.0, 1.0, N)
X, Y = meshgrid(x, y)
R = sqrt(X*X+Y*Y)

plt.title("Diffraction pattern")
plt.xlabel('x')
plt.ylabel('y')
plt.imshow(I(R),vmax=0.01)
plt.hot()
plt.show()