#1.Listar ciudades y radares

def list_ciu_radar(arbol1,arbol2):
	dict1={}
	codprov1=arbol1.xpath('//PROVINCIA/NOMBRE/text()')
	codprov2=arbol2.xpath('//provincia/@id')	
	for cod2 in codprov2:
		cod1=cod2
		prov=arbol2.xpath('//provincia[@id="{}"]/text()'.format(cod2))
		nomprov=prov[0]
		carreteras=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA/DENOMINACION/text()'.format(cod1))
		dict1[nomprov]={}
		for carretera in carreteras:
			dict1[nomprov][carretera]={}
			dict1[nomprov][carretera]["PI"]={}
			pipk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/PK/text()'.format(cod1,carretera))
			dict1[nomprov][carretera]["PI"]["PK"]=pipk[0]
			pilat=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LATITUD/text()'.format(cod1,carretera))
			dict1[nomprov][carretera]["PI"]["LAT"]=pilat[0]
			pilon=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'.format(cod1,carretera))
			dict1[nomprov][carretera]["PI"]["LON"]=pilon[0]
			dict1[nomprov][carretera]["PF"]={}
			pfpk=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/PK/text()'.format(cod1,carretera))
			dict1[nomprov][carretera]["PF"]["PK"]=pfpk[0]
			pflat=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/LATITUD/text()'.format(cod1,carretera))
			dict1[nomprov][carretera]["PF"]["LAT"]=pflat[0]
			pflon=arbol1.xpath('//PROVINCIA[NOMBRE="{}"]/CARRETERA[DENOMINACION="{}"]/RADAR/PUNTO_FINAL/LONGITUD/text()'.format(cod1,carretera))
			dict1[nomprov][carretera]["PF"]["LON"]=pflon[0]
	return dict1


#2.Contar ciudades y radares

#3.Buscar ciudades por la que pase una carretera y muestre radares

#4.Buscar una ciudad y muestra sus radares, Busca una carretera y muestra sus radares

#5.Mostrar las coordenadas de los radares que tienen una carretera