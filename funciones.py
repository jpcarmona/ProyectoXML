
#1.Listar ciudades y radares

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

# Código provincia

def get_cod_prov(arbol,provincia):
	"""Dada la provincia(str)
	y el arbol(lxml.etree)
	de 'provincias.xml',
	devuelve codigo(str)"""
	codprov=arbol.xpath('/provincias/provincia[contains(text(),"{}")]/@id'.format(provincia))
	return codprov[0]

# Creamos diccionario de provincias y radares

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

# listamos provincias y radares

def list_radar(dict1):
	"""Dado dict1(dict)
	devuelve una salida"""
	for provincia in dict1.keys():
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

# Ejecucion final opcion1

def opcion1(provincia,arbol1,arbol2):
	if not provincia_existe(arbol2,provincia):
		print("No existe la provincia, inténtelo de nuevo")
	else:
		prov=provincia_existe(arbol2,provincia)
		cod=get_cod_prov(arbol2,prov)
		dict1=dict_radar(arbol1,arbol2,cod)
		list_radar(dict1)

#2.Contar ciudades y radares

#3.Buscar ciudades por la que pase una carretera y muestre radares

#4.Buscar una ciudad y muestra sus radares, Busca una carretera y muestra sus radares

#5.Mostrar las coordenadas de los radares que tienen una carretera

# Menu 1

def menu1(arbol1,arbol2):
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
			menu1(arbol1,arbol2)
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