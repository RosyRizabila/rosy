# def http_status(status):
#       match status:
#           case 400:
#               return "Bad request"
#           case 404:
#               return "Not found"
#           case 418:
#               return "I'm a teapot"
#           case _:
#               return "Something's wrong with the internet"
#  print(http_status(404))

class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 0))

# def http_nilai(point):
#     match point:
#        case (0, 0):
#           print("Origin")
#         case (0, y):
#             print(f"Y={y}")
#         case (x, 0):
#           print(f"X={x}")
#         case (x, y):
#           print(f"X={x}, Y={y}")
#         case _:
#             raise ValueError("Not a point")
# http_nilai((0, 3))



# from enum import Enum
# class Color(Enum):
#      RED = 'red'
#      GREEN = 'green'
#      BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#      case Color.RED:
#          print("I see red!")
#      case Color.GREEN:
#          print("Grass is green")
#      case Color.BLUE:
#          print("I'm feeling the blues :(")


