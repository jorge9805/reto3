from math import sqrt
class Point:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        
class Line:
    def __init__(self,start:Point,end:Point):
        self.start=start
        self.end=end
        self.distance_x=self.end.x-self.start.x
        self.distance_y=self.end.y-self.start.y
    def compute_slope(self):
        slope=self.distance_y/self.distance_x
        return slope
    def compute_length(self):
        return sqrt(self.distance_x**2+self.distance_y**2)
    def compute_horizontal_cross(self):
        if(self.start.y*self.end.y<=0):
            return True
        else:
            return False
    def compute_vertical_cross(self):
        if(self.start.x*self.end.x<=0):
            return True
        else:
            return False    
line1=Line(Point(2,2),Point(3,3))
line2=Line(Point(-2,-3),Point(2,3))
print(line1.compute_slope())
print(line1.compute_length())
print(line1.compute_horizontal_cross())
print(line1.compute_vertical_cross())
print(line2.compute_horizontal_cross())
print(line2.compute_vertical_cross())



class Rectangle:
    def __init__(self,method,*args):
        #bottom left corner (point) width height
        if method==1:
            self.bottom_left=args[0]
            self.width=args[1]
            self.height=args[2]
            self.top_right=Point(self.bottom_left.x+self.width,self.bottom_left.y+self.height)
        #center point width height
        elif method==2:
            self.center=args[0]
            self.width=args[1]
            self.height=args[2]
            self.bottom_left=Point(self.center.x-self.width/2,self.center.y-self.height/2)
            self.top_right=Point(self.center.x+self.width/2,self.center.y+self.height/2)
        #two opposite points
        elif method==3:
            self.bottom_left=args[0]
            self.top_right=args[1]
            self.width=self.top_right.x-self.bottom_left.x
            self.height=self.top_right.y-self.bottom_left.y
        # 4 lines
        elif method==4:
            self.bottom=args[0]
            self.top=args[1]
            self.left=args[2]
            self.right=args[3]
            self.width=self.right.compute_length()
            self.height=self.top.compute_length()
            self.bottom_left=self.bottom.start
            self.top_right=self.top.end
    def compute_area(self):
        return self.width*self.height
    def compute_perimeter(self):
        return 2*(self.width+self.height)
rectangle1=Rectangle(1,Point(2,2),3,4)
rectangle2=Rectangle(2,Point(2,2),3,4)
rectangle3=Rectangle(3,Point(2,2),Point(5,6))
rectangle4=Rectangle(4,Line(Point(2,2),Point(5,2)),Line(Point(5,2),Point(5,6)),Line(Point(5,6),Point(2,6)),Line(Point(2,6),Point(2,2)))
print(rectangle1.compute_area())
print(rectangle1.compute_perimeter())
print(rectangle2.compute_area())
print(rectangle2.compute_perimeter())
print(rectangle3.compute_area())
print(rectangle3.compute_perimeter())
print(rectangle4.compute_area())
print(rectangle4.compute_perimeter())
