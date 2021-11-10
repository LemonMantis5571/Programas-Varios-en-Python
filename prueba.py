
class humano:

    def __init__(self, peso,altura):
        self.peso = peso
        self.altura = altura
   
    def imc(self):
        self.kilos = self.peso / (self.altura ** 2)
        print(self.kilos)


    def rango(self):
        if self.kilos < 18.5:
            print("Bajo peso")

        elif self.kilos >= 18.5 and self.kilos <= 24.9:
            print("Normal")


        elif self.kilos >= 25 and self.kilos <= 29.9:
            print("Sobrepeso")  

        else: 
            print("Obesidad")

# Definir una clase llamada animal con atributos de raza, edad, peso y altura. 
class animal:
    
    def __init__(self, raza, edad, peso, altura):
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
    def descripcion(self):
        print("Raza: ", self.raza, "Edad: ", self.edad, "Peso: ", self.peso, "Altura: ", self.altura)

    def rango(self):
        if self.peso < 10:
            print("Bajo peso")

        elif self.peso >= 10 and self.peso <= 20:
            print("Normal")


        elif self.peso >= 20 and self.peso <= 30:
            print("Sobrepeso")  

        else: 
            print("Obesidad")
          

john = humano(120,1.80)
john.imc()
john.rango()

jennie = animal("Gato", "5 meses", 10, 0.30)
jennie.descripcion()
jennie.rango()

#