import numpy as np
import matplotlib.pyplot as plt

# Valores de x
x = np.linspace(1, 100, 100)

# Funciones
g_x = x**2 + x + 1
o_x2 = x**2         
o_x = x           

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(x, g_x, label=r'$x^2 + x + 1$', color='blue')
plt.plot(x, o_x2, label=r'$x^2$', linestyle='--', color='green')
plt.plot(x, o_x, label=r'$x$', linestyle='--', color='red')

# Títulos y leyendas
plt.title('Comparación entre $x^2 + x + 1$, $O(x^2)$ y $O(x)$')
plt.xlabel('x')
plt.ylabel('Valores')
plt.legend()

# Mostrar gráfico
plt.grid(True)
plt.show()
