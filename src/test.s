.data
Main_name: .asciiz "Main"

string_0: .asciiz "Hello, World."

.text
.globl main
main:
#Parametro Return $ra en stackpoiner + 16
addi $sp, $sp, -4          #Push local var instance stackpointer 12
addi $sp, $sp, -4          #Push local var type_name@0 stackpointer 8
addi $sp, $sp, -4          #Push local var @result stackpointer 4
addi $sp, $sp, -4          #Push local var $ra stackpointer 0
sw $ra, 0($sp)          #Agrega $ra a la pila para salvar el punto de retorno de la funcion new_ctr_Main
li $a0, 1
li $v0, 9
syscall
sw $v0, 12($sp)          #Reservando memoria para una instancia de tipo Main
la $t0, Main_name
sw $t0, 8($sp)          #Cargando el nombre del tipo desde el data          #Assignando el nombre del tipo en el campo type
lw $t0, 12($sp)          #Saca de la pila instance
addi $sp, $sp, -4
sw $t0, 0($sp)          #Mete para la pila instance
jal Main_main          #Call a la function Main_main
sw $s0, 4($sp)          #Save el resultado de la funcion que esta en $s0 pa la pila
li $v0, 10
syscall

Main_main:
#Parametro Return $ra en stackpoiner + 16
#Parametro self en stackpoiner + 12
addi $sp, $sp, -4          #Push local var param_0_to_out_string@0 stackpointer 8
addi $sp, $sp, -4          #Push local var @result stackpointer 4
addi $sp, $sp, -4          #Push local var $ra stackpointer 0
sw $ra, 0($sp)          #Agrega $ra a la pila para salvar el punto de retorno de la funcion Main_main
la $t0, string_0
sw $t0, 8($sp)          #Fin del paramentro 0 al StaticDispatch out_string
lw $t0, 12($sp)          #Saca de la pila self
addi $sp, $sp, -4
sw $t0, 0($sp)          #Mete para la pila self          #Agrega a la pila el paramentro 0 al StaticDispatch out_string
lw $t0, 12($sp)          #Saca de la pila param_0_to_out_string@0
addi $sp, $sp, -4
sw $t0, 0($sp)          #Mete para la pila param_0_to_out_string@0          #Agrega a la pila el paramentro 1 al StaticDispatch out_string
jal IO_out_string          #Call a la function IO_out_string
sw $s0, 4($sp)          #Save el resultado de la funcion que esta en $s0 pa la pila
lw $s0, 4($sp)          #Envia el resultado de la funcion en $s0
lw $ra, 16($sp)          #Lee el $ra mas profundo de la pila para retornar a la funcion anterior
addi $sp, $sp, 20          #Limpia la pila
jr $ra          #Final de la function main

IO_out_string:
li $v0, 4
lw $a0, 0($sp)
syscall
lw $a0, 4($sp)
addi $sp, $sp, 8
jr $ra
