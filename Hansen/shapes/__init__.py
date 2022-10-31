#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# base class shape
class shape(object):
    def __init__(self, dimension:float=None):
        self.shape_type = self.__class__.__name__.capitalize()
        self.dim = dimension
        return
    
    def diameter(self):
        raise Exception("Unimplmented method error.")
    
    def volume(self):
        raise Exception("Unimplmented method error.")
        
    def surface(self):
        raise Exception("Unimplmented method error.")
    
    def type(self):
        return(self.shape_type)





class cube(shape):
    def __init__(self, dim:float):
        super().__init__(dim)
        return
    
    def diameter(self):
        return (3 * self.dim**2)**(1/2)




class sphere(shape):
    def __init__(self, dim:float):
        super().__init__(dim)
        return
    
    def diameter(self):
        return self.dim*2





class pyramid(shape):
    
    is_haunted = True
    
    def __init__(self, dim:float):
        super().__init__(dim)
        self.shape_type = 'Regular Pyramid'
        return
    
    def has_mummies(self):
        return self.is_haunted




class tpyramid(pyramid):
    
    is_haunted = False
    
    def __init__(self, dim:float):
        super().__init__(dim)
        self.shape_type = "Triangular Pyramid"
        return



