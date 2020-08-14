
#problemas secuenciales
'''capinv=int(input("ingrese su capital invertido"))
gan=capinv * 0.02
print(f"la ganancia total es de:  {gan}")


sb:int(input("ingrese el sueldo base"))
v1=float(input("ingrese el total de la venta1"))
venta2=int(input("ingrese el total de la venta2"))
venta3=float(input("ingrese el total de la venta3"))

tot_vta=(v1+venta2+venta3)
com=tot_vta*0.10
tpag=tot_vta+com

print(f"el total de las compras:{com}")
print(f"el total  a pagar  es  de :{tpag}")

compratotal=int(input("ingrese el total de la compra"))
des=compratotal*0.15
tot_pag=compratotal - des
print(f"total a pagar es :{tot_pag}")

c1=float(input("ingrese calificacion uno"))
c2=float(input("ingrese calificacion dos "))
c3=float(input("ingrese calificacion tres "))
ef=float(input("ingrese examen final"))
tf=float(input("ingrese  trabajo final"))
prom=(c1+c2+c3)/3
ppar=-prom*0.55
pef=ef*0.30
ptf=tf*0.15
cf=ppar+pef+ptf
print(f"la calificacion final es :{cf}")

nm=int(input("ingrese cantidad de mujeres"))
nh=int(input("ingrese cantidad de hombres"))
total=nh+nm
phom=nh*100/total
pmu=nm*100/total
print(f"el promdeio de hombres son:{phom}")
print(f"el promedio de las mujeres  son :{pmu}")

fnac=int(input("ingrese fecha de su nacimiento"))
fact=int(input("ingrese fecha actual"))
edad=fnac -fact
print(f"su edad como tal es {edad}")

#problemas propuestos

masa=str(input("ingrese la cantidad de  masa "))
presion=int(input("ingrese la presion"))
volumen=int(input("ingrese el volumen de la masa"))
temperatura=float(input("ingrese la temperatura de la masa"))
masa=(presion*volumen)/(0.37*(temperatura + 460))

print(f"el resultado de la masa es :{masa}")

num1=int(input("ingrese el numero"))
valor_abs=num1/num1
print(f"el valor absoluto del numero es:{num1}")



num_pulsaciones=int(input("ingrese numero de pulsaciones"))
edad=int(input("ingrese edad"))
num_pulsaciones=(220-edad)/100
print(f"la cantidad de pulsaciones por minutos son :{num_pulsaciones}")

sb=float(input("ingrese el salario base"))
valo_horas=int(input("ingrese el valor de las horas"))
horas_tra=int(input("ingrese las horas que trabajo"))
sb=valo_horas+horas_tra
sf=sb*0.25
print(f"el salario final de obrero es :{sf}")

area=str(input("ingrese el numero del area 1-pediatra,2-traumatologia,3-ginecologica"))
if area==1:
    print("su descuento sera del :40%")
elif area==2:
    print("su descuento sera del  40:")
elif area==3:
    print("su area es la 3 y su /n descuento es del :30")

porcentaje=area/100
print(f"la cantidad de dinero a pagar es {porcentaje}")

capital1=str(input("ingrese su capital invertido"))
capital2=str(input("ingrese su capital invertido"))
capital3=str(input("ingrese su capital invertido"))
porcentaje=(int)(capital1+capital2+capital3)/100
print(f"el capital invertido de cada  persona es del:{porcentaje}")


cat_pesos=str(input("ingrese la cantidad de pesos"))
cat_dolar=int(input("ingrese la cantidad en dolar"))
cat_pesos,cat_dolar=cat_dolar,cat_pesos
print(f"la cantidad es :{cat_pesos}")
print(f"la cantidad es :{cat_dolar}")

precio_inicial=int(input("ingresio el precio inicial"))
gan=precio_inicial/100'''


materias=str(input("ingrese la materia 1-matematicas 2-fisica 3-quimica"))
notas=any(input("ingrese las notas obtenidas"))
por=any(input("ingrese el porcentaje que equivale "))
examen=any(input("ingrese porcentaje del examen"))

if por==0.90 and examen==0.10:
    print("gano")

elif por==0.80 and examen==0.20:
    print("gano")
else :por==0.85 and examen==0.15

pro_final=(notas / examen /por)*100

print(f"el promedio final del estudiante es del:{pro_final}")





