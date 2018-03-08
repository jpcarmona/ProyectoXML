from lxml import etree
from funciones import menu

arbol1=etree.parse("radares.xml")
arbol2=etree.parse("provincias.xml")

menu(arbol1,arbol2)

#https://www.google.es/maps/dir/37.282015,-5.9381587/37.2709883,-5.9294977

