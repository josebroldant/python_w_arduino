import persona

personasRegistradas=[]
opcion=0

def AgregarPersona():
	global personasRegistradas
	nom=input("Nombre de la persona: ")
	ed=input("Edad de la persona: ")
	sex=input("Sexo de la persona: ")
	pes=input("Peso de la persona en Kg: ")
	altu=input("Altura de la persona en metros: ")
	nuevaPersona=persona.Persona(nom,ed,sex,[],pes,altu)
	personasRegistradas.append(nuevaPersona)
	return nuevaPersona
def imprimirPersonas():
	for p in personasRegistradas:
		p.imprimir()
def MayorDeEdad():
	nombrePers=input("Ingrese el nombre de la persona: ")
	persona.esMayorDeEdad()
	if edad >= 18:
		ced=input("Ingrese la cedula de la persona: ")
	if edad < 18:
		return False
def CalcIMC():
	nombrePerso=input("Ingrese el nombre de la persona: ")
	persona.calcularIMC()
while(opcion!="4"):
  print("Bienvenido al sistema de personas")
  print("Menu:")
  print("1. Agregar Persona")
  print("2. Calcular IMC")
  print("3. Imprimir Personas")
  print("4. Salir")
  opcion=input("Ingrese una opcion:")
  if(opcion=="1"):
    AgregarPersona()
  elif(opcion=="2"):
    CalcIMC()
  elif(opcion=="3"):
    imprimirPersonas()
  elif(opcion=="4"):
    print("Salir")
  else:
    print("Error")
