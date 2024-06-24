

lista=[{"codigo":23,"nombre":"car"},{"codigo":235,"nombre":"carl"},{"codigo":234,"nombre":"carlo"}]
codigo=235

print(lista)
for i in range(len(lista)):
    listaIn=lista[i]    
    if {"codigo":235,"nombre":"carl"} == listaIn:
        lista[i]={"codigo":235,"nombre":"carlitrox"}

print(lista)