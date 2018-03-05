from lxml import etree
from funciones import menuxml,provincia_existe,get_cod_prov,dict_radar,list_radar

arbol1=etree.parse("radares.xml")
arbol2=etree.parse("provincias.xml")

opcion=menuxml()

while opcion!="0":
	if opcion=="1":
		provincia="1"
		while provincia!="0":
			provincia=input("¿Provincia?(\"0\" para salir): ")
			if not provincia_existe(arbol2,provincia):
				print("No existe la provincia, inténtelo de nuevo")
			else:
				prov=provincia_existe(arbol2,provincia)
				cod=get_cod_prov(arbol2,provincia)
				dict1=dict_radar(arbol1,arbol2,cod)
				list_radar(dict1)
	if opcion=="2":
		print("opcion2")
	if opcion=="3":
		print("opcion3")
	if opcion=="4":
		print("opcion4")
	if opcion=="5":
		print("opcion5")
	if opcion not in ["1","2","3","4","5"]:
		print("Por favor elija una opcion correcta")
	opcion=menuxml()






#https://www.google.es/maps/dir/37.282015,-5.9381587/37.2709883,-5.9294977

