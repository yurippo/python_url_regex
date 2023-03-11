class CarBlueprint:

    #initializer
    def __init__(self,color,style):
     self.color = color
     self.style = style

    

    #class attribute
    wheels = 4

    #print(wheels)

    #Method 1 that shows the description of the car
    def show_description(self):
       print("The car is ",self.color,self.style)

    #Method 2 changes the color of the car
    def change_color(self,color):
       self.color = color
       

c = CarBlueprint("black","sport")

c.show_description()  

c.change_color("red")

print(c.wheels,c.style,c.color)


    
        
 


# The __init__() Method
# __init__() is the special method that initializes an individual object. This method runs automatically each time an object of a class is created.

# The __init__() method is generally used to perform operations that are necessary before the object is created.
#When you define __init__() in a class definition, its first parameter should be self.
# The self parameter refers to the individual object itself. It is used to fetch or set attributes of the particular instance.

# This parameter doesn’t have to be called self, you can call it whatever you want, but it is standard practice, and you should probably stick with it.

    #This is how we would create an object from this class
    #Object #Class
        

    #The attributes of an instance are accessed and assigned to by using dot . notation.

    #Access the Atributes
     


        