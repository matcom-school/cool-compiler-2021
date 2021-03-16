from ..__dependency import visitor
from ..__dependency import EType, errors_compose
from ..__dependency import Type

from ..ASTs import ast0_semantic as InitAST
from ..ASTs import ast1_collector as ReturnAST

class RecolectorDeTipos():
    def __init__(self, build_in_types : dict = {}, errors : list = []):
        self.errors = errors
        self.dicc_types = build_in_types

    @visitor.on("node")
    def visit(self,node):
        pass

    @visitor.when( InitAST.Program )
    def visit ( self, node : InitAST.Program ):
        for cl in node.class_list:
            self.visit(cl)

        return ReturnAST.Program( self.dicc_types, node.class_list )

    @visitor.when ( InitAST.Class )
    def visita ( self, node : InitAST.Class ):
        if node.name in self.dicc_types :
            self.errors.append( errors_compose( node.get_ubi_to['Class'], EType.SE, 
                f"class {node.name} already definded"
            ) )
        
        self.dicc_types[node.name] = Type(node.name)
