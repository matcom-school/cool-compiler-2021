class Node:
    pass

####################################################
class Program (Node):
    def __init__(self, build_in_type, class_list, class_info ) -> None:
        self.bit = build_in_type
        self.class_list = class_list
        self.class_info = class_info

class Class (Node):
    def __init__(self, name, inherits_type, feature_list):
        self.name = name
        self.parent = inherits_type
        self.feature_list = feature_list

####################################################
class ClassFeature (Node):
    pass

class Attribute (ClassFeature):
    def __init__(self, name, atype, expr = None):
        self.name = name
        self.type = atype
        self.expr = expr

class Function (ClassFeature):
    def __init__(self, name, parameter_list, ftype, body):
        self.name = name
        self.params = parameter_list
        self.return_type = ftype
        self.expr = body

####################################################
class Expression (Node):
    pass

class Dispatch (Expression):
    def __init__(self, fname, expr_list):
        self.name = fname
        self.expr_list = expr_list

class IntanceDispatch (Dispatch):
    def __init__(self, expr, fname, expr_list):
        self.expr = expr
        super().__init__(fname, expr_list)

class CastingDispatch (IntanceDispatch):
    def __init__(self, expr, casting_type ,fname, expr_list):
        super().__init__(expr, fname, expr_list)
        self.cast_type = casting_type

####################################################
class Statement (Expression):
    pass 

class Assignation (Statement):
    def __init__(self, idx, expr):
        self.id = idx
        self.expr = expr

class IfThenElse (Statement):
    def __init__(self, condiction, then_expr, else_expr):
        self.condiction = condiction
        self.then_expr = then_expr
        self.else_expr = else_expr

class WhileLoop (Statement):
    def __init__(self, condiction, expr):
        self.condiction = condiction
        self.expr = expr

class Block (Statement):
    def __init__(self, expr_list):
        self.expr_list = expr_list

class LetIn (Statement):
    def __init__(self, assign_list , in_expr ):
        self.assign_list = assign_list
        self.in_expr = in_expr

class Case (Statement):
    def __init__(self, expr, case_list):
        self.expr = expr
        self.case_list = case_list

####################################################
class Unary (Expression):
    def __init__(self, expr):
        self.expr = expr

        
class NewType (Expression):
    def __init__(self, ntype):
        self.type = ntype

class Negaction (Unary):
    pass

class FuncionIsVoid(Unary):
    pass

class Complemento(Unary):
    pass

#####################################################
class Binary (Expression):
    def __init__(self, left, right ):
        self.left = left
        self.right = right

#####################################################
class Comparation (Binary):
    pass

class LessOrEquals (Comparation):
    pass

class Equals (Comparation):
    pass

class Less (Comparation):
    pass

#####################################################
class Arithmetic (Binary):
    pass

class Sum (Arithmetic):
    pass

class Minus (Arithmetic):
    pass

class Multiplication (Arithmetic):
    pass

class Division (Arithmetic):
    pass

#####################################################
class Atomic (Expression):
    def __init__(self, lex):
        self.lex = lex

class Int (Atomic):
    pass

class String (Atomic):
    pass

class Bool (Atomic):
    pass

class Identifier (Expression):
    def __init__(self, lex):
        self.id = lex

