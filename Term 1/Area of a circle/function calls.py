#Logan Nelson
#9/13/18

#get a usuers name
##def get_name():
##
### step one ask user for name
## name = input("what's your name?")
### step two display the name back for user
## print("the name you entered was", name)
### step three verify the name
## input("is this correct yes or no")
##
##print("this is our function")
##get_name()


# calculate the area of a circle
# radius*radius*pi
def area_of_circle():
    pi=3.141592653
#1 get a radius
     radius = input("what is the radius")   
#2 calculate the area
     radius = float(radius)
     area = radius*radius*pi
#3 display the area
     print("the area of the circle is: ",area)

area_of_circle()
