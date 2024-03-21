from pickle_store_wrapper_Rakeki.storage import storable

@storable(location='/home/rakeki/Dev/PyPackages/Storage/tests/cache')
class Test:
    def __init__(self, x, y, z):
        if not hasattr(self, 'x'):
            self.x = x
        if not hasattr(self, 'y'):
            self.y = y
        if not hasattr(self, 'z'):
            self.z = z
    
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
test = Test(1, 2, 3)
test.set_x(32)