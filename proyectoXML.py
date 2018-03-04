from lxml import etree
from funciones import list_ciu_radar

arbol1=etree.parse("radares.xml")
arbol2=etree.parse("provincias.xml")

dict1=list_ciu_radar(arbol1,arbol2)

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


https://www.google.es/maps/dir/37.282015,-5.9381587/37.2709883,-5.9294977

