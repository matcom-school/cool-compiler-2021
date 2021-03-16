from cool_compiler.table_regex import Token as Token
import cool_compiler.cmp.visitor as visitor

from cool_compiler.cmp.semantic import Context as Context 
from cool_compiler.cmp.semantic import SemanticError as SemanticError
from cool_compiler.cmp.semantic import ErrorType as ErrorType
from cool_compiler.cmp.semantic import Type as Type


from cool_compiler.errors import errors_compose as errors_compose
from cool_compiler.errors import ErrorType as EType 

from cool_compiler.semantic_ast import Program as ProgramNode
from cool_compiler.semantic_ast import Class as ClassNode
from cool_compiler.semantic_ast import Attribute as AttrNode
from cool_compiler.semantic_ast import Function as FuncNode

