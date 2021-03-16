from .abstract_ast_factory import AstFactory
from . import ast as Ast


class SemanticAstFactory (AstFactory):
    def __init__(self, build_in_type):
        self.bit = build_in_type
    
    def __Program__(self, synted):
        return Ast.Program()
    