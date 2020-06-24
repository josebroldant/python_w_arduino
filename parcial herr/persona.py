class Persona:

	def __init__(self,nombre,edad,cedula,sexo,peso,altura):
		self.nombre=nombre
		self.edad=edad
		self.cedula=cedula
		self.sexo=sexo
		self.peso=peso
		self.altura=altura
	def imprimir(self):
		print(self.nombre)
		print(self.edad)
		print(self.cedula)
		print(self.sexo)
		print(self.peso)
		print(self.altura)
	def esMayorDeEdad(self,edad):
		if edad >= 18:
			return True
		if edad < 18:
			return False
	def calcularIMC(self,peso,altura):
		IMC=peso/(altura*altura)
		if IMC < 20:
			print(-1)
		if 20 <= IMC <= 25:
			print(0)
		if IMC > 25:
			print(1) 
