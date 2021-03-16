from .ast0_semantic import *

class Program(Node):
    def __init__(self, dicc_types, class_list) :
        self.dicc_types = dicc_types
        self.class_list = class_list

