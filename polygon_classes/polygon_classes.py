import numpy as np
import csv
import sys
import random
from math import *
import time

class Line(object):
    
    def __init__(self,start,end,properties = {}):
        self.start = start
        self.end = end       
        self.length = sqrt((self.start[0]-self.end[0])**2 + (self.start[1]-self.end[1])**2)
        self.properties = properties
    
    def dot(self,L):
        return ((self.end[0]-self.start[0])*(L.end[0] - L.start[0]) + 
        (self.end[1] - self.start[1])*(L.end[1] - L.start[1]))
        
    def distancepoint(self,point):
        #if the line segment is itself just a point, then take Euclidean distance
        if self.end == self.start:
            return (sqrt((self.end[1]-point[1])**2 + (self.end[0] - point[0])**2))
            
        v = Line(self.start,point)
        if self.dot(v)/self.length**2 < 0:
            return Line(point,self.start).length
        elif self.dot(v)/self.length**2 <= 1:
            return ( abs((self.end[1]-self.start[1])*point[0] - 
                    (self.end[0] - self.start[0])*point[1] + 
                    self.end[0]*self.start[1] - self.end[1]*self.start[0]) /
                    sqrt((self.end[1]-self.start[1])**2 + (self.end[0] - self.start[0])**2) )
        else:
            return Line(point,self.end).length
            
    def intersect(self,L,eps = 10**-5):
        #General strategy: check what point the two lines containing each line segment intersect at
        #then see if that point is on both line segments
        #Note that horizontal and vertical line segments are special cases which must be dealt with
        #individually.
        
        if self.start[0] == self.end[0]:
            if L.start[0] == L.end[0]:
                if (self.distancepoint(L.start) > eps and self.distancepoint(L.end) > eps and
                    L.distancepoint(self.start) > eps and L.distancepoint(self.end) > eps):
                    return False
                    
            elif L.start[1] == L.end[1]:
                solution = (self.start[0],L.start[1])
                if (self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                    return False
            else:
                slopeL = float(L.start[1] - L.end[1])/float(L.start[0]-L.end[0])
                intL = L.start[1] - slopeL*L.start[0]
                solution = (self.start[0],slopeL*self.start[0] + intL)
                if (self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                    return False
                    
        elif self.start[1] == self.end[1]:
            if L.start[1] == L.end[1]:
                if (self.distancepoint(L.start) > eps and self.distancepoint(L.end) > eps and
                    L.distancepoint(self.start) > eps and L.distancepoint(self.end) > eps):
                    return False
                    
            elif L.start[0] == L.end[0]:
                solution = (L.start[0],self.start[1])
                if (self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                    return False
            else:
                slopeL = float(L.start[1] - L.end[1])/float(L.start[0]-L.end[0])
                intL = L.start[1] - slopeL*L.start[0]
                solution = ((self.start[1] - intL)/slopeL,self.start[1])
                if (self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                    return False
        else:
            slopeself = float((self.start[1] - self.end[1])/float((self.start[0]-self.end[0])))
            intself = self.start[1] - slopeself*self.start[0]
            
            if L.start[1] == L.end[1]:
                solution = ((L.start[1] - intself)/slopeself,L.start[1])
                if (self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                    return False
            elif L.start[0] == L.end[0]:        
                solution = (L.start[0],slopeself*L.start[0] + intself)
                if (self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                    return False
            else:
                slopeL = float(L.start[1] - L.end[1])/float(L.start[0]-L.end[0])
                intL = L.start[1] - slopeL*L.start[0]
                if slopeL == slopeself:
                    if (self.distancepoint(L.start) > eps and self.distancepoint(L.end) > eps and
                    L.distancepoint(self.start) > eps and L.distancepoint(self.end) > eps):
                        return False
                else:
                    x = (intL - intself)/(slopeself-slopeL)
                    y = slopeself*x + intself
                    solution = (x,y)
                    if(self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                        return False
        
        return True
        
class Polygon(object):
    def __init__(self,points):
        #raise an exception if two sides without mutual points intersect
        if len(points) > 3:
            for i in range(len(points)):
                pointA = points[i]
                pointB = points[(i+1) % len(points)]
                side = Line(pointA,pointB)
                for j in range(i+2,i+len(points)-1):
                    pointC = points[j % len(points)]
                    pointD = points[(j+1) % len(points)]
                    segment = Line(pointC,pointD)
                    if segment.intersect(side):
                        raise ValueError('Invalid shape specified')
        self.points = points
    
    def number_of_sides(self):
        return len(self.points)
        
    def perimeter(self):
        perimeter = 0
        for i in range(self.number_of_sides()):
            side = Line(self.points[i],self.points[(i+1) % self.number_of_sides()])
            perimeter += side.length
        
        return perimeter
    
    def area(self):
    #in general, divide the shape into triangles, compute the area of each triangle
    #then add them up
    #Note: this only works for convex polygons. Seems like a pretty difficult problem
    #for totally arbitrary polygon.
        area = 0
        if self.number_of_sides() == 3:
            for i in range(self.number_of_sides()):
                pointA = self.points[i]
                pointB = self.points[(i+1) % self.number_of_sides()]
                pointC = self.points[(i+2) % self.number_of_sides()]
                side = Line(pointA,pointB)
                if (side.distancepoint(pointC) < Line(pointA,pointC).length and
                    side.distancepoint(pointC) < Line(pointB,pointC).length):
                        base = side.distancepoint(pointC)
                        height = side.length
                        area = .5*base*height
        else:
            start_point = self.points[0]
            for i in range(1,self.number_of_sides()):
                pointA = self.points[i]
                pointB = self.points[(i+1) % self.number_of_sides()]
                area = area +  Triangle([start_point,pointA,pointB]).area()
        
        return area

class Pentagon(Polygon):
    def __init__(self,points):
        if len(points) != 5:
            raise ValueError("Not a pentagon")
        else:
            Polygon.__init__(self,points)
            
class Quadrilateral(Polygon):
    def __init__(self,points):
        if len(points) != 4:
            raise ValueError("Not a quadrilateral")
        else:
            Polygon.__init__(self,points)

class Triangle(Polygon):
    def __init__(self,points):
        if len(points) != 3:
            raise ValueError("Not a triangle")
        else:
            Polygon.__init__(self,points)
            
#~ Triangle([(0,0),(5,0),(2,0)]).number_of_sides()

#~ try:
    #~ Quadrilateral([(0,0),(5,0),(0,2),(4,4)]).number_of_sides()
#~ except ValueError:
    #~ print "caught it"
    
#~ print Quadrilateral([(0,0),(5,0),(4,4),(0,2)]).number_of_sides()
