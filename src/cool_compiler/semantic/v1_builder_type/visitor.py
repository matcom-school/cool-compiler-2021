from ..__dependency import visitor
from ..__dependency import errors_compose, EType

from ..ASTs import ast1_collector as InitAST
from ..ASTs import ast2_builder_type as ReturnAST

class TypeCreator:
    def __init__(self, type_info_list : list, errors : list):
        self.errors = errors
    
    @visitor.on("node")
    def visit (self, node):
        pass
    
    @visitor.when( InitAST.Program )
    def visit ( self, node : InitAST.Program ):
        
        for cl in node.class_list: 
            self.visit(cl)

        return not any(self.errors)

    @visitor.when( InitAST.Class )
    def visit (self, node : InitAST.Class ):
        self.contexto.current_type = self.contexto.get_type( node.name ) 
        this_type : Type = self.contexto.current_type

        if node.parent is not None:
            if node.parent in ["Int","Bool","String"]:
                self.errors.append( 
                    errors_compose( node.get_ubi_to['Inherits'], EType.SE, 
                        f"Can't inherit or redifine {node.parent}"))
            else:
                try:
                   parent_type = self.context.get_type(node.parent)
                   this_type.set_parent(parent_type)
                except SemanticError as se:
                    this_type.set_parent( ErrorType() )
                    self.errors.append(
                        errors_compose( node.get_ubi_to['Inherits'], EType.SE, se.text) )


        for ft in node.feature_list:
            self.visit(ft)

    @visitor.when( InitAST.AttrNode )
    def visit(self, node : InitAST.AttrNode ):
        try:
            attr_type = self.context.get_type(node.type)
        except SemanticError as se:
            attr_type = ErrorType()
            self.errors(
                errors_compose( node.get_ubi_to["Type"], EType.SE, se.text ))
        
        self.context.current_type.define_attribute(node.name, attr_type)
        

    @visitor.when( InitAST.FuncNode )
    def visit (self, node : InitAST.FuncNode ):
        types = []
        names = []
        for name, ptype in node.params:
            try:
                types.append( self.context.get_type(ptype) )
            except SemanticError as se:
                types.append(ErrorType())
                self.errors(
                    errors_compose(node.get_ubi_to[name], EType.SE, se.text))
            names.append( name )
        try:
            return_type = self.context.get_type(node.return_type)
        except SemanticError as se:
            return_type = ErrorType()
            self.errors(errors_compose(node.get_ubi_to["Return"], EType.SE, se.text))
        
        self.context.current_type.define_method(node.name, names,types, return_type)