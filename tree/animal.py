from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, specie):
        self.name = name
        self.specie = specie

    @abstractmethod
    def speak(self):
        "speak method"

    @abstractmethod
    def walk(self):
        "walk method abstract"

    def print_name():
        print(self.name)


class Cachorro(Animal):

    def speak(self):
        print("barking")
    
    def walk(self):
        print("dogs walk")

""" 
as sentenças abaixo jamais vão funcionar, pois eu estou instanciando (Atraves de Animal("tody, "cao"))
um objeto do tipo Animal, que é abstrato. Eu só posso instanciar objetos do tipo Animal que implementar as funções abstrata
speak and walk
animal = Animal("tody", "cao")
animal.speak() """

cao = Cachorro("Tody", "cao")
cao.speak()
print(isinstance(cao, Cachorro))
print(isinstance(cao, Animal))


class FormaGeografica(ABC):

    @abstractmethod
    def calcula_area(self):
        pass

    @abstractmethod
    def calcula_perimeter(self):
        pass


class Country(ABC):

    def __init__(self, name, population, states, capital, current_coin):
        self.name = name
        self.population = population
        self.states = states # [], lista com os nomes dos estados
        self.capital = capital
        self.current_coin = current_coin


brasil = Country("Brasil", 200000000, ["Acre", "Amapa", "Amazonas"], "Brasilia", "Real")