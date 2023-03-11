
class MinhaClasse:
   def __init__(self,name,location):
      self.name = name
      self.location = location

   def __str__(self):
        return f'O nome da classe e {self.name} e o local da classe e {self.location}'
   
# we can implement the __eq__ dunder method in the Person class.

# Python automatically calls the __eq__ method of a class when you use
# the == operator to compare the instances of the class. By default, Python uses 
# the is operator if you don’t provide a specific implementation for the __eq__ method.

# The following shows how to implement the __eq__ method in the Person class that
# returns True if two person objects have the same age:

   def __eq__(self,other):
       
       if not isinstance(other,MinhaClasse):
       # don't attempt to compare against unrelated types
         return NotImplemented
       
       return self.name == other.name and self.location == other.location
   

   def __len__(self):
        return len(self.name) + len(self.location)
   
   # def __eq__(self,other):
   #    if (self.name and self.location == other.name and other.location):
   #        return True
   #    else:
   #        return False
   
   
objeto = MinhaClasse("Yuri","Victoria")

objeto1 = MinhaClasse("Yuri","Victoria")


print(objeto)  # => invoca o método objeto.__str__()
#print(objeto.location)


print(objeto1)

print(len(objeto))  # => invoca o método objeto.__len__()

print(len(objeto1))

# In this example, the object and object1 objects are not the same object.
# And you can check it using the is operator:

print(objeto is objeto1) #returns False

#Also, when you compare objeto with objeto1 using the equal operator (==), you’ll get the result of False:

#print(objeto == objeto1)

#After implementing our def __eq__() method let's objects equality once again fingers crossed

print (objeto == objeto1) #Agora retornou True Yaayy funcionou


#print(objeto1.name)
# print(objeto1)  # => invoca o método objeto.__str__()
#print(objeto1.location)

#Aplicando métodos especiais
# Para fazer com que sua classe tenha alguns comportamentos específicos,
# você pode implementar o que chamamos de métodos especiais, como __len__, __str__ e __eq__.
# Cada um desses métodos é chamado indiretamente pelo próprio interpretador Python quando executamos
# algumas instruções específicas.

#Por exemplo:
# objeto = MinhaClasse()

# print(objeto)  # => invoca o método objeto.__str__()
#len()  # => invoca o método objeto.__len__()

# outro_objeto = MinhaClasse()
# objeto == outro_objeto  # => invoca o método objeto.__eq__(outro_objeto)


     