def generaMatriz(renglon,columna):
  matriz=[]
  for reng in range(renglon):
    lista=[]
    for col in range(columna):
      num=int(input())
      lista.append(num)
    matriz.append(lista)
  return (matriz)

def sumaColumnas(matriz,renglon,columna):
  deflist=[]
  renglon_suma=0
  columna_suma=-1
  b=0
  c=0
  z=0
  for i in range(columna):
    columna_suma+=1
    z=0
    c=0
    b=0
    renglon_suma=0
    for n in range(renglon):
      c=c+b
      b=matriz[renglon_suma][columna_suma]
      renglon_suma=renglon_suma+1
    z=c+b
    deflist.append(z)
  return (deflist)

def main():
  renglon=int(input())
  columna=int(input())
  if renglon<=0 or columna<=0:
    print("Error")
  else:
    matriz=generaMatriz(renglon,columna)
    print(sumaColumnas(matriz,renglon,columna))

if _name_ == '_main_':
    main()
