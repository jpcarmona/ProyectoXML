
# Si existe provincia

def provincia_existe(arbol,provincia):
	"""Dada la provincia(str)
	y el arbol(lxml.etree)
	de 'provincias.xml',
	verifica si existe(bool)"""
	provincias=arbol.xpath('//provincia/text()')
	for prov in provincias:
		if prov.upper()==provincia.upper():
			return prov
	return False

# Si existe carretera

def carretera_existe(arbol,carretera):
	"""Dada la carretera(str)
	y el arbol(lxml.etree)
	de 'radares.xml',
	verifica si existe(bool)"""
	carreteras=arbol.xpath('//CARRETERA/DENOMINACION/text()')
	for carre in carreteras:
		if carre.upper()==carretera.upper():
			return carre
	return False 

# Lista de carreteras

def list_carre(arbol):
	"""Dada el arbol(lxml.etree)
	de 'radares.xml', devuelve 
	lista de carreteras(list)"""
	carreteras1=arbol.xpath('//CARRETERA/DENOMINACION/text()')
	carreteras2=[]
	for carre in carreteras1:
		if carre not in carreteras2:
			carreteras2.append(carre)
	return carreteras2

# Código provincia

def get_cod_prov(arbol,provincia):
	"""Dada la provincia(str)
	y el arbol(lxml.etree)
	de 'provincias.xml',
	devuelve codigo(str)"""
	codprov=arbol.xpath('/provincias/provincia[contains(text(),"{}")]/@id'.format(provincia))
	return codprov[0]

# Diccionario de provincia y radares

def dict_radar(arbol1,arbol2,codigo):
	"""Dado el arbol1(lxml.etree)
	de 'radares.xml', el arbol2(lxml.etree)
	de 'provincias.xml' y el codigo(str) de provincia
	devuelve dict1(dict)"""
	dict1={}
	prov=arbol2.xpath('/provincias/provincia[@id="{}"]/text()'.format(codigo))
	nomprov=prov[0]
	carreteras=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA/DENOMINACION/text()'.format(codigo))
	dict1[nomprov]={}
	for carretera in carreteras:
		dict1[nomprov][carretera]={}
		dict1[nomprov][carretera]["PI"]={}
		pipk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/PK/text()'.format(codigo,carretera))
		dict1[nomprov][carretera]["PI"]["PK"]=pipk[0]
		pilat=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LATITUD/text()'.format(codigo,carretera))
		dict1[nomprov][carretera]["PI"]["LAT"]=pilat[0]
		pilon=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'.format(codigo,carretera))
		dict1[nomprov][carretera]["PI"]["LON"]=pilon[0]
		dict1[nomprov][carretera]["PF"]={}
		pfpk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/PK/text()'.format(codigo,carretera))
		dict1[nomprov][carretera]["PF"]["PK"]=pfpk[0]
		pflat=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/LATITUD/text()'.format(codigo,carretera))
		dict1[nomprov][carretera]["PF"]["LAT"]=pflat[0]
		pflon=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/LONGITUD/text()'.format(codigo,carretera))
		dict1[nomprov][carretera]["PF"]["LON"]=pflon[0]
	return dict1

# Si existe provincia devuelve el diccionario de provincias y radares:

def dictprov(provincia,arbol1,arbol2):
	if not provincia_existe(arbol2,provincia):
		print("No existe la provincia, inténtelo de nuevo")
		return False
	else:
		prov=provincia_existe(arbol2,provincia)
		cod=get_cod_prov(arbol2,prov)
		dict1=dict_radar(arbol1,arbol2,cod)
		return dict1

#1.Listar ciudades y radares

# listamos provincias y radares

def list_radar(dict1):
	"""Dado dict1(dict)
	devuelve una salida"""
	provincia=list(dict1.keys())[0]
	print(provincia)
	print("")
	for carretera in dict1[provincia].keys():
		print(carretera)
		print("")
		carr=dict1[provincia][carretera]
		print("Punto Inicial:")
		print(carr["PI"]["PK"],carr["PI"]["LAT"],carr["PI"]["LON"])
		print("Punto Final:")
		print(carr["PF"]["PK"],carr["PF"]["LAT"],carr["PF"]["LON"])
		print("")
	print("")

#2.Contar ciudades y radares

# listamos provincias y radares

def cont_radar(dict1):
	"""Dado dict1(dict)
	devuelve una salida"""
	provincia=list(dict1.keys())[0]
	print("")
	num=0
	for carretera in dict1[provincia].keys():
		num+=1
	print("{} tiene {} radares".format(provincia,num))
	print("")

#3.Provincias por la que pase una carretera y muestre radares

def car_prov(carretera,arbol1,arbol2):
	dict1={}
	cod_provincia=arbol1.xpath('//CARRETERA[DENOMINACION="{}}"]/../NOMBRE/text()'.format(carretera))
	for cod in cod_provincia:
		dict1[cod]={}
		pipk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/PK/text()'.format(cod,carretera))
		dict1[cod]["PIPK"]=[]
		for i in pipk:
			dict1[cod]["PIPK"].append(i)
		pfpk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/PK/text()'.format(cod,carretera))
		dict1[cod]["PFPK"]=[]
		for i in pfpk:
			dict1[cod]["PFPK"].append(i)
	return dict1

#4.Buscar una Provincia y muestra sus radares, Busca una carretera y muestra sus radares

#5.Mostrar las coordenadas de los radares que tienen una carretera

# Menu Provincias

def menuprov(arbol1,arbol2,opcion):
	while True:
		provincia=input("¿Provincia?(\"0\" para volver): ")
		if provincia=="0":
			break
		if not dictprov(provincia,arbol1,arbol2):
			continue
		if opcion=="1":
				list_radar(dictprov(provincia,arbol1,arbol2))
		if opcion=="2":
				cont_radar(dictprov(provincia,arbol1,arbol2))
		if opcion=="4":
		print("")

# Menu Carreteras

def menucar(arbol1,arbol2,opcion):
	while True:
		carretera=input("¿Carretera?(\"0\" para volver): ")
		if carretera=="0":
			break
		if not dictprov(provincia,arbol1,arbol2):
			continue
		if opcion=="3":
				list_radar(dictprov(provincia,arbol1,arbol2))
		if opcion=="4":
				cont_radar(dictprov(provincia,arbol1,arbol2))
		if opcion=="5":
			cont_radar(dictprov(provincia,arbol1,arbol2))
		print("")

# Menu 3

def menu3(arbol1,arbol2):
	provincia=input("¿Provincia?(\"0\" para volver): ")
	while provincia!="0":
		opcion1(provincia,arbol1,arbol2)
		provincia=input("¿Provincia?(\"0\" para volver): ")
	exit

# Menu 4

def menu4(arbol1,arbol2):
	provincia=input("¿Provincia?(\"0\" para volver): ")
	while provincia!="0":
		opcion1(provincia,arbol1,arbol2)
		provincia=input("¿Provincia?(\"0\" para volver): ")
	exit

# Menu 5

def menu5(arbol1,arbol2):
	provincia=input("¿Provincia?(\"0\" para volver): ")
	while provincia!="0":
		opcion1(provincia,arbol1,arbol2)
		provincia=input("¿Provincia?(\"0\" para volver): ")
	exit


# Menu Principal texto

def menuxml():
	print("""Elija una opción de las siguientes 5 (\"0\" para salir)\n
1.Listar radares de una provincia.
2.Contar radares que tiene una provincia.
3.Muestra los radares y las provincias por las que pasa una carretera.
4.Muestra el radar de una provincia y una carretera.
5.Muestra los radares de una carretera.\n""")
	opcion=input("Opcion: ")
	return opcion

# Menu Principal

def menu(arbol1,arbol2):
	opcion=menuxml()
	while opcion!="0":
		if opcion=="1":
			menuprov(arbol1,arbol2,opcion)
		if opcion=="2":
			menuprov(arbol1,arbol2,opcion)
		if opcion=="3":
			menu3(arbol1,arbol2)
		if opcion=="4":
			menu4(arbol1,arbol2)
		if opcion=="5":
			menu5(arbol1,arbol2)
		if opcion not in ["1","2","3","4","5"]:
			print("Por favor elija una opcion correcta")
		opcion=menuxml()