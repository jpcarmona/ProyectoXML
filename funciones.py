# Menu

def menuxml():
	print("""Elija una opción de las siguientes 5 (\"0\" para salir)\n
1.Listar radares de una provincia.
2.Contar radares que tiene una provincia.
3.Muestra los radares y las provincias por las que pasa una carretera.
4.Muestra el radar dada una provincia y carretera.
5.Muestra los radares de una carretera.\n""")
	opcion=input("Opcion: ")
	return opcion

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

#1.Listar ciudades y radares

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


#2.Contar ciudades y radares

#3.Buscar ciudades por la que pase una carretera y muestre radares

#4.Buscar una ciudad y muestra sus radares, Busca una carretera y muestra sus radares

#5.Mostrar las coordenadas de los radares que tienen una carretera