# Importan la biblioteca
import numpy as np  

# Una forma de crear arreglos ndarray es usando una lista

miLista={3,5,7,9}

miArreglo=np.array(miLista)
# Arreglo unidimensional a partir de una lista de python 

#Dimensiones 
print(miArreglo.ndim)
print(miArreglo.shape)
print(miArreglo.size)
print(miArreglo.dtype)

miArreglo= np.zeros((2,2))

print(miArreglo)

  

