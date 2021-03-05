from enum import Enum
import inspect

# interface to create ast nodes
# and decouple the grammar of these nodes 
class AstFactory:
    def __call__(self, key_name_node : str ) : 
        return self.Builder(key_name_node, self)
    
    class Builder:
        def __init__(self, knn, obj):
            self.knn = knn
            self.obj = obj

        # synteticed is a list with tokens and nodes 
        def build(self, synteticed_list : list):
            for name, func in inspect.getmembers(self.obj, predicate=inspect.ismethod):
                if self.knn in name:
                    return func(synteticed_list)
                

   
