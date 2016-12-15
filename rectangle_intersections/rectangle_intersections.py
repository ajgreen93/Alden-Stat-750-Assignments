import numpy as np
import csv
import sys
import random
from math import *
import time


##Note: the intersectCircle function in Rectangle is what we use
##to test whether Rectangles and Circles intersect
##The rest is just copied from my RTree work.
def boundingBox(shapes):
    left = np.inf
    right = -np.inf
    bottom = np.inf
    top = -np.inf
    if shapes != []:
        for shape in shapes:
            left = min(shape.rectangle().left[0],left)
            right = max(shape.rectangle().right[0],right)
            bottom = min(shape.rectangle().bottom[1], bottom)
            top = max(shape.rectangle().top[1],top)
            
    return Rectangle((left,bottom),(right,top),
                     (right,bottom),(left,top))

class Rectangle(object):
    def __init__(self,left = (0,0),right = (0,0),bottom = (0,0),top = (0,0),
                 properties = {}):
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
        self.properties = properties

        self.area  = Line(left,bottom).length * Line(left,top).length
        
        #the four line segments which make up the rectangle
        self.lines = [Line(bottom,left),Line(left,top),Line(top,right),Line(right,bottom)]
        
    def rectangle(self):
        
        #axis-aligned rectangle is its own bounding box
        if (self.left[1] == self.bottom[1] and self.left[0] == self.top[0]):
            return self
        else:
            return boundingBox(self.left,self.right,self.bottom,self.top)
    
    def __eq__(self,F):
        if type(self) is not type(F):
            return False
        
        if(self.left == F.left and self.right == F.right and
           self.top == F.top and self.bottom == F.bottom and self.properties == F.properties):
                return True
        
        return False
    
    def intersect(self,F):
        
        #axis-aligned rectangles are a special (easy) case, so we take care of them
        #seperately. (This isn't necessary, but speeds things up)
        if (self.left[1] == self.bottom[1] and self.left[0] == self.top[0] and
            F.left[1] == F.bottom[1] and F.left[0] == F.top[0]):
            if (self.right[0] < F.left[0] or F.right[0] < self.left[0] or
                self.top[1] < F.bottom[1] or F.top[1] < self.bottom[1]):
                return False
            else:
                return True
                
        #in general, two rectangles intersect if one of the border segments of one
        #of them crosses into the other
        else:        
            
            for line in self.lines:
                if F.inRectangle(line):
                    return True
                    
            for line in F.lines:
                if self.inRectangle(line):
                    return True
            
            return False
            
    def intersectCircle(self,circle):
        #if the rectangle intersects the circle, one of the borders of the rectangle
        #intersects the circle, which happens if the distance from that line segment
        #to the circle is 
        for line in self.lines:
            if (line.distancepoint(circle.center) <= circle.radius and not
               (Line(line.start,circle.center).length < circle.radius and 
                Line(line.end,circle.center).length < circle.radius)):
                return True
        else:
            return False
            
    def inRectangle(self,L):
    #if a line segment L is at least partly in the rectangle,
    #for each boundary segment B of the rectangle,
    #the distance from L to B should be no more than the length
    #of the perpendicular line segments
        for i in range(4):
            line = self.lines[i]
            if line.distanceline(L) > self.lines[(i+1) % 4].length:
                return False
        
        return True
                

class Line(object):
    def __init__(self,start,end,properties = {}):
        self.start = start
        self.end = end       
        self.length = sqrt((self.start[0]-self.end[0])**2 + (self.start[1]-self.end[1])**2)
        self.properties = properties
    
    def __eq__(self,L):
        if type(self) is not type(L):
            return False
        
        if (self.start == L.start and self.end == L.end and 
            self.properties == L.properties):
            return True
        
        return False
        
    def rectangle(self):
        left = min(self.start[0],self.end[0])
        right = max(self.start[0],self.end[0])
        bottom = min(self.start[1],self.end[1])
        top = max(self.start[1],self.end[1])
        return Rectangle((left,bottom),(right,top),(right,bottom),(left,top))
    
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
                    
    def distanceline(self,L):
        if self.intersect(L):
            return 0
        else:
        #distance between two non-intersecting line segments in 2D is the minimum distance
        #between the endpoints of one and the other line
            return min(self.distancepoint(L.start),self.distancepoint(L.end),
                       L.distancepoint(self.start),L.distancepoint(self.end))
    
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
                slopeL = (L.start[1] - L.end[1])/(L.start[0]-L.end[0])
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
                slopeL = (L.start[1] - L.end[1])/(L.start[0]-L.end[0])
                intL = L.start[1] - slopeL*L.start[0]
                solution = ((self.start[1] - intL)/slopeL,self.start[1])
                if (self.distancepoint(solution) > eps or L.distancepoint(solution) > eps):
                    return False
        else:
            slopeself = (self.start[1] - self.end[1])/(self.start[0]-self.end[0])
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
                slopeL = (L.start[1] - L.end[1])/(L.start[0]-L.end[0])
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
            
                 
class Point(object):
    def __init__(self,point = (0,0),properties = {}):
        self.point = point
        self.properties = properties
        
    def __eq__(self,P):
        if type(self) is not type(P):
            return False
        
        if (self.point == P.point and
            self.properties == P.properties):
            return True
        
        return False
            
    def rectangle(self):
        return Rectangle(self.point,self.point,self.point,self.point)

class Circle(object):
    def __init__(self,center = (0,0),radius = 1,properties = {}):
        self.center = center
        self.radius = radius
        self.properties = properties
        
    def __eq__(self,C):
        if type(self) is not type(C):
            return False
        
        if (self.center == C.center and self.radius == C.radius and 
            self.properties == C.properties):
            return True
        
        return False    
        
    def rectangle(self):
        left = self.center[0] - self.radius
        right = self.center[0] + self.radius
        bottom = self.center[1] - self.radius
        top = self.center[1] + self.radius
        
        return Rectangle((left,bottom),(right,top),(right,bottom),(left,top))
