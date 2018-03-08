from lxml import etree
from funciones import menu

arbol1=etree.parse("radares.xml")
arbol2=etree.parse("provincias.xml")

menu(arbol1,arbol2)
