import os
### EXISTENCIAS #########################################################################

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

### VARIOS #############################################################################

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

### CREACION DE DICCIONARIOS CON XML ###################################################

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
		dict1[nomprov][carretera]["PF"]={}
		pfpk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/PK/text()'.format(codigo,carretera))
		dict1[nomprov][carretera]["PF"]["PK"]=pfpk[0]
	return dict1

# Diccionario de provincias y radares dada una carretera

def dict_radar2(carretera,arbol1,arbol2):
	dict1={}
	cod_provincia=arbol1.xpath('//CARRETERA[DENOMINACION="{}"]/../NOMBRE/text()'.format(carretera))
	for cod in cod_provincia:
		provin=arbol2.xpath('/provincias/provincia[@id="{}"]/text()'.format(cod))
		prov=provin[0]
		dict1[prov]={}
		pipk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/PK/text()'.format(cod,carretera))
		dict1[prov]["PIPK"]=[]
		for i in pipk:
			dict1[prov]["PIPK"].append(i)
		pilat=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LATITUD/text()'.format(cod,carretera))
		dict1[prov]["PILAT"]=[]
		for i in pilat:
			dict1[prov]["PILAT"].append(i)
		pilon=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'.format(cod,carretera))
		dict1[prov]["PILON"]=[]
		for i in pilon:
			dict1[prov]["PILON"].append(i)
		pfpk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/PK/text()'.format(cod,carretera))
		dict1[prov]["PFPK"]=[]
		for i in pfpk:
			dict1[prov]["PFPK"].append(i)
		pflat=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LATITUD/text()'.format(cod,carretera))
		dict1[prov]["PFLAT"]=[]
		for i in pflat:
			dict1[prov]["PFLAT"].append(i)
		pflon=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'.format(cod,carretera))
		dict1[prov]["PFLON"]=[]
		for i in pflon:
			dict1[prov]["PFLON"].append(i)
	return dict1


### EXISTENCIAS 2 #########################################################################

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

# Si existe carretera devuelve el provincias y radares dada una carretera:

def dictcar(carretera,arbol1,arbol2):
	if not carretera_existe(arbol1,carretera):
		print("No existe la carretera, inténtelo de nuevo")
		return False
	else:
		carr=carretera_existe(arbol1,carretera)
		dict1=dict_radar2(carr,arbol1,arbol2)
		return dict1


### RESULTADOS FINALES DE LAS OPCIONES #####################################################

#1.Listar ciudades y radares

def list_radar(dict1):
	"""Dado dict1(dict)
	devuelve una salida"""
	provincia=list(dict1.keys())[0]
	print("Radares en la Provincia de {}".format(provincia))
	print("")
	for carretera in dict1[provincia].keys():
		carr=dict1[provincia][carretera]
		pipk=carr["PI"]["PK"]
		pfpk=carr["PF"]["PK"]
		print("Radar en carretera {} ".format(carretera))
		print("Punto Kilometrico Inicial {}".format(round(float(pipk),1)))
		print("Punto Kilometrico Final {}".format(round(float(pfpk),1)))
		print("")
	print("")

#2.Contar ciudades y radares

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

def list_car(dict1):
	"""Dado dict1(dict)
	devuelve una salida"""
	provincias=list(dict1.keys())
	for provincia in provincias:
		print(provincia)
		print("")
		num=0
		for x,y in zip(dict1[provincia]["PIPK"],dict1[provincia]["PFPK"]):
			num+=1
			print("Radar {}".format(num))
			print("Punto Kilometrico Inicial {} y Punto Kilometrico Final {}".format(round(float(x),1),round(float(y),1)))
		print("")

#4.Buscar una Provincia y muestra sus radares, Busca una carretera y muestra sus radares

def list_rad(dict1,provincia):
	"""Dado dict1(dict)
	y provincia(str)
	devuelve una salida"""
	provincias=list(dict1.keys())
	for prov in provincias:
		if prov==provincia:
			num=0
			for x,y in zip(dict1[provincia]["PIPK"],dict1[provincia]["PFPK"]):
				num+=1
				print("Radar {}".format(num))
				print("Punto Kilometrico Inicial {} y Punto Kilometrico Final {}".format(round(float(x),1),round(float(y),1)))
			print("")		


#5.Mostrar las coordenadas de los radares que tienen una carretera

def fire_maps(url):
	urlfull='https://www.google.es/maps/dir/'+url+'data=!4m2!4m1!3e0'
	os.system("firefox --new-window {} 2> /dev/null".format(urlfull))

def map_rad(dict1):
	provincias=list(dict1.keys())
	num=0
	url=''
	for provincia in provincias:
		print(provincia)
		print("")		
		for x,y,z,w in zip(dict1[provincia]["PILAT"],dict1[provincia]["PFLAT"],dict1[provincia]["PILON"],dict1[provincia]["PFLON"]):
			num+=1
			print("Radar {}".format(num))
			print("Latitud Inicial {} y Longitud Inicial {}".format(x,z))
			print("Latitud Final {} y Longitud Final {}".format(y,w))
			print("")
			latlon=x+','+z+'/'+y+','+w+'/'
			url+=latlon
		print("En total tiene {} Radares".format(num))
		return url	
		print("")

#def abrir_maps():	


### MENUS ##################################################################################

# Menu Carreteras

def menucar(arbol1,arbol2,opcion,provincia='0'):
	while True:
		carretera=input("¿Carretera?(\"0\" para volver): ")
		print("")
		if carretera=="0":
			break
		if not dictcar(carretera,arbol1,arbol2):
			continue
		if opcion=="3":
			carre=carretera_existe(arbol1,carretera)
			print("Radares y provincias que pasan por la carretera {}".format(carre))
			print("")
			list_car(dictcar(carretera,arbol1,arbol2))
		if opcion=="4":
			list_rad(dictcar(carretera,arbol1,arbol2),provincia)
			break
		if opcion=="5":
			carre=carretera_existe(arbol1,carretera)
			print("Radares que pasan por la carretera {}".format(carre))
			print("")
			control=input("Desea abrir firefox y ver los radares: (y/n)")
			if control=='y':
				fire_maps(map_rad(dictcar(carretera,arbol1,arbol2)))
			else:
				map_rad(dictcar(carretera,arbol1,arbol2))
		print("")

# Menu Provincias

def menuprov(arbol1,arbol2,opcion):
	while True:
		provincia=input("¿Provincia?(\"0\" para volver): ")
		print("")
		if provincia=="0":
			break
		if not dictprov(provincia,arbol1,arbol2):
			continue
		if opcion=="1":
			list_radar(dictprov(provincia,arbol1,arbol2))
		if opcion=="2":
			cont_radar(dictprov(provincia,arbol1,arbol2))
		if opcion=="4":
			prov=provincia_existe(arbol2,provincia)
			menucar(arbol1,arbol2,opcion,prov)
		print("")

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
			menucar(arbol1,arbol2,opcion)
		if opcion=="4":
			print("Elija Provincia y Carretera:")
			print("")
			menuprov(arbol1,arbol2,opcion)
		if opcion=="5":
			menucar(arbol1,arbol2,opcion)
		if opcion not in ["1","2","3","4","5"]:
			print("Por favor elija una opcion correcta")
		opcion=menuxml()