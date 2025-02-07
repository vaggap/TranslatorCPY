#Apostolakis Evangelos AM:4318

#NOTES:



import os
import sys
from typing import Tuple

abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']

file = open(sys.argv[1],'r',encoding='utf8')

#characters

blank = 0
letter = 1
number = 2
plus = 3
minus = 4
mult = 5
div = 6
mod = 7
less_than = 8
more_than = 9
equal = 10
excl = 11
comma = 12
colon = 13
left_parentheses = 14
right_parentheses = 15
left_curly = 16
right_curly = 17
hashtag = 18
unkown_symbol = 19
EOF = 20
change_line = 21


#situations

situation_start = 0
situation_letter = 1
situation_number = 2
situation_less = 3
situation_more = 4
situation_equal = 5
situation_hashtag = 6
situation_comment = 7
situation_closing_comment = 8
situation_slash = 9
situation_exclamation = 10

#tokens

keyword_tk = 210
number_tk = 211
plus_tk = 212
minus_tk = 213
mult_tk = 214
div_tk = 215
mod_tk = 216
less_than_tk = 217
more_than_tk = 218
equal_tk = 219
excl_tk = 220
comma_tk = 221
colon_tk = 222
left_parentheses_tk = 223
right_parentheses_tk = 224
left_curly_tk = 225
right_curly_tk = 226
less_equal_tk = 227
more_equal_tk = 228
not_equal_tk = 229
hashtag_tk = 230
EOF_tk = 231
change_line_tk = 232
assign_tk = 233

#reserved_words

reserved_words = ['main' , 'def' , '#def' , '#int' , 'global' , 'if' , 'elif' , 'else' , 'while' , 'print' ,
 'return' , 'input' , 'int' , 'and' , 'or' , 'not']

main_tk = 110
def_tk = 111
hash_def_tk = 112
hash_int_tk = 113
global_tk = 114
if_tk = 115
elif_tk = 116
else_tk = 117
while_tk = 118
print_tk = 119
return_tk = 120
input_tk = 121
int_tk = 122
and_tk = 123
or_tk = 124
not_tk = 125

#errors

ERROR_UNIDENTIFIED_CHAR = 310
ERROR_LETTER_AFTER_NUM = 311
ERROR_OUT_OF_BOUNDS = 312
ERROR_LIMIT_30 = 313
ERROR_UNCLOSED_COMMENT = 314
ERROR_PLAIN_HASHTAG = 315
ERROR_PLAIN_SLASH = 316
ERROR_PLAIN_LEFT_CURLY = 317
ERROR_PLAIN_RIGHT_CURLY = 318
ERROR_PLAIN_EXCL = 319


#automatic situations managment

SituationBoard = [
    #start
        [situation_start , situation_letter , situation_number , plus_tk , minus_tk , mult_tk , situation_slash , mod_tk , situation_less , situation_more , situation_equal , situation_exclamation , comma_tk , colon_tk , 
         left_parentheses_tk , right_parentheses_tk , ERROR_PLAIN_LEFT_CURLY , ERROR_PLAIN_RIGHT_CURLY , situation_hashtag , ERROR_UNIDENTIFIED_CHAR , EOF_tk , situation_start],

    #letter
        [keyword_tk , situation_letter , situation_letter , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , keyword_tk , 
         keyword_tk, keyword_tk , keyword_tk , keyword_tk , ERROR_UNIDENTIFIED_CHAR , keyword_tk ,keyword_tk],

    #number
        [number_tk , ERROR_LETTER_AFTER_NUM , situation_number , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk , number_tk ,
         number_tk , number_tk , number_tk , ERROR_UNIDENTIFIED_CHAR , number_tk , number_tk],

    #less
        [less_than_tk , less_than_tk , less_than_tk , less_than_tk , less_than_tk , less_than_tk , less_than_tk , less_than_tk , less_than_tk , less_than_tk , less_equal_tk , less_than_tk , less_than_tk , less_than_tk , less_than_tk ,
         less_than_tk , less_than_tk , less_than_tk , less_than_tk , ERROR_UNIDENTIFIED_CHAR , less_than_tk , less_than_tk],

    #more
        [more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_than_tk , more_equal_tk , more_than_tk , more_than_tk , more_than_tk ,
         more_than_tk , more_than_tk , more_than_tk , more_than_tk , ERROR_UNIDENTIFIED_CHAR , more_than_tk , more_than_tk],

    #equal
        [assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , equal_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk , assign_tk,
         assign_tk , ERROR_UNIDENTIFIED_CHAR , assign_tk , assign_tk],
    
    #hashtag
        [ERROR_PLAIN_HASHTAG , situation_letter , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG, 
         ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG ,  left_curly_tk , right_curly_tk , situation_comment , ERROR_UNIDENTIFIED_CHAR ,
         ERROR_PLAIN_HASHTAG , ERROR_PLAIN_HASHTAG],
    
    #comments
        [situation_comment , situation_comment , situation_comment , situation_comment, situation_comment , situation_comment , situation_comment , situation_comment , situation_comment , situation_comment , situation_comment , situation_comment ,
         situation_comment , situation_comment , situation_comment , situation_comment, situation_comment , situation_comment , situation_closing_comment , ERROR_UNIDENTIFIED_CHAR , situation_comment , situation_comment],
    
    #closing_comments
        [situation_comment , situation_comment , situation_comment , situation_comment, situation_comment , situation_comment , situation_comment , situation_comment , situation_comment , situation_comment , situation_comment , situation_comment ,
         situation_comment , situation_comment , situation_comment , situation_comment, situation_comment , situation_comment , situation_start , ERROR_UNIDENTIFIED_CHAR , situation_comment , situation_comment],
    
    #slash
        [ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , div_tk , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH ,
         ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH , ERROR_UNIDENTIFIED_CHAR , ERROR_PLAIN_SLASH , ERROR_PLAIN_SLASH],

    #exclamation
        [ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , not_equal_tk ,
         ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL , ERROR_UNIDENTIFIED_CHAR , ERROR_PLAIN_EXCL , ERROR_PLAIN_EXCL ]
    
        ]


line = 1

def lex():
        global line
        read_word = ''
        cr = situation_start #cr = current situation
        
        LineCounter = line
        LexResult = []
        while(cr>=0 and cr<=10):
                char = file.read(1)  #read next character (only one)
                
                
                if (char == ' '):
                        char_tk = blank
                elif (char in abc):
                        char_tk = letter
                elif (char in numbers):
                        char_tk = number
                elif (char == '+'):
                        char_tk = plus
                elif (char == '-'):
                        char_tk = minus
                elif (char == '*'):
                        char_tk = mult
                elif (char == '/'):
                        char_tk = div
                elif (char == '%'):
                        char_tk = mod
                elif (char == '<'):
                        char_tk = less_than
                elif (char == '>'):
                        char_tk = more_than
                elif (char == '='):
                        char_tk = equal
                elif (char == '!'):
                        char_tk = excl
                elif (char == ','):
                        char_tk = comma
                elif (char == ':'):
                        char_tk = colon
                elif (char == '('):
                        char_tk = left_parentheses
                elif (char == ')'):
                        char_tk = right_parentheses
                elif (char == '{'):
                        char_tk = left_curly
                elif (char == '}'):
                        char_tk = right_curly
                elif (char == '#'):
                        char_tk = hashtag
                elif (char == ''):
                        char_tk = EOF
                elif (char == '\t'):
                        char_tk = blank                        
                elif (char == '\n'):
                        LineCounter=LineCounter+1
                        char_tk = change_line
                else:
                        char_tk = unkown_symbol
                
                
                #print('Current Situation ', cr )
                #print('read_word= ', char )
                
                
                cr=SituationBoard[cr][char_tk]
                
                #print('New situation ', cr)
                #input("Press Enter to continue...")
                
                if(len(read_word)<30):
                        if(cr != situation_start and cr != situation_comment and cr != situation_closing_comment):
                              read_word+=char
                        else:
                              read_word=''

                else:
                        cr=ERROR_LIMIT_30
              

        if(cr == keyword_tk or cr == number_tk or cr == less_than_tk or cr == more_than_tk or cr == assign_tk):
                if (char == '\n'):
                        LineCounter -= 1
                char=file.seek(file.tell()-1,0)  #This line is moving the file pointer back by one position.

                read_word = read_word[:-1]        #This line is removing the last character from read_word.(To properly identify keywords, it could be reoved latter but just to be sure)

        if(cr == keyword_tk):
                if(read_word in reserved_words):
                        if(read_word == 'main'):
                                cr = main_tk
                        elif(read_word == 'def'):
                                cr = def_tk
                        elif (read_word == '#def'):
                                cr = hash_def_tk
                        elif (read_word == '#int'):
                                cr = hash_int_tk
                        elif (read_word == 'global'):
                                cr = global_tk
                        elif (read_word == 'if'):
                                cr = if_tk
                        elif (read_word == 'elif'):
                                cr = elif_tk
                        elif (read_word == 'else'):
                                cr = else_tk
                        elif (read_word == 'while'):
                                cr = while_tk
                        elif (read_word == 'print'):
                                cr = print_tk
                        elif (read_word == 'return'):
                                cr = return_tk
                        elif (read_word == 'input'):
                                cr = input_tk
                        elif (read_word == 'int'):
                                cr = int_tk
                        elif (read_word == 'and'):
                                cr = and_tk
                        elif (read_word == 'not'):
                                cr = not_tk
                        elif (read_word == 'or'):
                                cr = or_tk
        
        #ERROR CHECK
        if (cr == number_tk):
                if (int(read_word) >= 32767):
                    cr = ERROR_OUT_OF_BOUNDS
                    
        if(cr == ERROR_UNIDENTIFIED_CHAR):
                print("ERROR: This symbol cannot be used")
                
        elif(cr == ERROR_LETTER_AFTER_NUM):
                print("ERROR: A letter cant be placed after a number")
        
        elif(cr == ERROR_OUT_OF_BOUNDS):
                print("ERROR: The number you provided is bigger that this programm limit(32767)")
        
        elif(cr == ERROR_LIMIT_30):
                print("ERROR: The provided string was longer than the acceptable limit(30)")
        
        elif(cr == ERROR_UNCLOSED_COMMENT):
                print("ERROR: You started a comments section without ever closing it")
        
        elif(cr == ERROR_PLAIN_HASHTAG):
                print("ERROR: A # cant be used as a completed command")
        
        elif(cr == ERROR_PLAIN_SLASH):
                print("ERROR: The divide symbol is // not /")
        
        elif(cr == ERROR_PLAIN_LEFT_CURLY):
                print("ERROR: A { cant be used as a completed command")
        
        elif(cr == ERROR_PLAIN_RIGHT_CURLY):
                print("ERROR: A } cant be used as a completed command")
                
        elif(cr == ERROR_PLAIN_EXCL):
                print("ERROR: A ! cant be used as a completed command")
              
        LexResult.append(cr)
        LexResult.append(read_word)
        LexResult.append(LineCounter)
        line=LineCounter
        
        #print(LexResult)
        return LexResult

#Intermediate code

global listOfAllQuads
listOfAllQuads = []
countQuad = 1

def nextQuad():
        global countQuad
        return countQuad

FinalQuadsList = []

def genQuad(op,x,y,z):
        global countQuad
        global listOfAllQuads
        global FinalQuadsList
        list = []

        list = [nextQuad()]
        list.extend([op, x, y, z])

        countQuad += 1
        listOfAllQuads.append(list)
        FinalQuadsList.append(list)
        return list
T_i = 1
TempVarList = []

def newTemp():
        global T_i
        global TempVarList
        temp = 'T_' + str(T_i)
        T_i += 1
        TempVarList.append(temp)
        
        entity = Entity()
        entity.name = temp
        entity.type = 'TEMP'
        entity.tempVar.offset = compute_offsets()
        new_entity(entity)
        
        return temp

def emptyList():
        return []


def makeList(x):
        return [x]

def merge(list1, list2):
        return list1 + list2

def backpatch(list, z):
        global listOfAllQuads
        for i in range(len(list)):
                for j in range(len(listOfAllQuads)):
                        if(list[i] == listOfAllQuads[j][0] and listOfAllQuads[j][4] == '_'):
                                listOfAllQuads[j][4] = z
                                break; #didnt enter next i(next loop)
        return

#Symbols Table
class Argument():
        #triangle
        def __init__(self):
                self.name = ''
                self.type = 'Int'

class Entity():
        #yellow box
        def __init__(self, name = None, type = None):
                self.name = name
                self.type = type
                self.variable = self.Variable()
                self.subprogram = self.SubProgram()
                self.parameter = self.Parameter()
                self.tempVar = self.TempVar()
        
        class Variable():
                def __init__(self):
                        self.type = 'Int'
                        self.offset = 0
        
        class SubProgram():
                def __init__(self):
                        self.type = 'Function'
                        self.startQuad = 0
                        self.frameLength = 0
                        self.arguments = []
                        self.nestingLvl = 0

        class Parameter():
                def __init__(self):
                        self.mode = 'CV'
                        self.offset = 0

        class TempVar():
                def __init__(self):
                        self.type = 'Int'
                        self.offset = 0

class Scope():
        #Red circle
        def __init__(self, enclosingScope=None): 
                self.enclosingScope = enclosingScope
                self.entityList = []
                self.name = ''
                self.nestingLvl = 0
                #self.enclosingScope = None
                #self.entityList = []

def new_argument(object):
        global topScope
        topScope.entityList[-1].subprogram.arguments.append(object)

def new_entity(object):
        global topScope
        topScope.entityList.append(object)

topScope = None

def new_scope(name):
        global topScope
        nextScope = Scope()
        nextScope.name = name
        nextScope.enclosingScope = topScope

        if(topScope == None):
                nextScope.nestingLvl = 0
        else:
                nextScope.nestingLvl = topScope.nestingLvl + 1
        
        topScope = nextScope

def delete_scope():
        global topScope

        freeScope = topScope
        topScope = topScope.enclosingScope
        del freeScope

def compute_offsets():
        global topScope
        counter = 0
        if topScope.entityList:
                for entity in topScope.entityList:
                        if (entity.type == 'VAR' or entity.type == 'TEMP' or entity.type == 'PARAM'):
                                counter += 1
        offset = (4*counter) + 12       
        
        return offset

def compute_startQuad():
        global topScope
        topScope.enclosingScope.entityList[-1].subprogram.startQuad = nextQuad()

def compute_frameLength():
        global topScope
        topScope.enclosingScope.entityList[-1].subprogram.frameLength = compute_offsets()

def add_parameter():
        global topScope
        for arg in topScope.enclosingScope.entityList[-1].subprogram.arguments:
                entity = Entity()
                entity.type = 'PARAM'
                entity.name = arg.name
                entity.parameter.mode = 'CV'
                entity.parameter.offset = compute_offsets()
                new_entity(entity)


def find_entity(name):
        global topScope
        #print(f"Looking for entity: {name}")
        #print(f"Current scope: {topScope}")
        #print(f"All entities in current scope: {[e.name for e in topScope.entityList]}")
        
        currentScope = topScope
        while currentScope != None:
                for entity in currentScope.entityList:
                        if entity.name == name:
                                return currentScope,entity
                currentScope = currentScope.enclosingScope
        print("Error: Entity not found. Name: " + str(name))
        exit()


                                
#Final Code

ascFile = open('ascFile.asm', 'w')
ascFile.write('        \n\n\n')

def gnlvcode(var):

        global topScope
        global ascFile
        ascFile.write('lw t0,-4(sp)\n')
        
        (scope, entity) = find_entity(var)

        level = topScope.nestingLvl - scope.nestingLvl
        level = level-1

        for i in range(0, level):
                ascFile.write('lw t0,-4(t0)\n')

        if entity.type == 'VAR':
                ascFile.write('addi t0,t0,-' + str(entity.variable.offset) + '\n')
        elif entity.type == 'PARAM':
                ascFile.write('addi t0,t0,-' + str(entity.parameter.offset) + '\n')

def loadvr(v,r):
        global topScope
        global ascFile

        if v is not None and v.isdigit():
                ascFile.write('li t' + str(r) + ', ' + v + '\n')

        elif v is not None:
                (scope, entity) = find_entity(v)
        

                if scope.nestingLvl == topScope.nestingLvl:
                        if entity.type == 'VAR':
                                ascFile.write('lw t' + str(r) + ', -' + str(entity.variable.offset) + '(sp)\n')
                        elif entity.type == 'PARAM' and entity.parameter.mode == 'CV':
                                ascFile.write('lw t' + str(r) + ', -' + str(entity.parameter.offset) + '(sp)\n')
                        elif entity.type == 'TEMP':
                                ascFile.write('lw t' + str(r) + ', -' + str(entity.tempVar.offset) + '(sp)\n')
                
                elif scope.nestingLvl == 0 and entity.type == 'VAR':
                        ascFile.write('lw t' + str(r) + ', -' + str(entity.variable.offset) + '(s0)\n')
                
                elif scope.nestingLvl == 0 and entity.type == 'TEMP':
                        ascFile.write('lw t' + str(r) + ',-' + str(entity.tempVar.offset) + '(s0)\n')

                elif scope.nestingLvl < topScope.nestingLvl:
                        if entity.type == 'VAR':
                                gnlvcode(v)
                                ascFile.write('lw t' + str(r) + ', 0(t0)\n')
                        elif entity.type == 'PARAM' and entity.parameter.mode == 'CV':
                                gnlvcode(v)
                                ascFile.write('lw t' + str(r) + ', 0(t0)\n')
                
                
                

def storerv(r,v):

        global topScope
        global ascFile

        (scope,entity) = find_entity(v)

        if scope.nestingLvl == topScope.nestingLvl:
                if entity.type == 'VAR':
                        ascFile.write('sw t' + str(r) + ', -' + str(entity.variable.offset) + '(sp)\n')
                elif entity.type == 'PARAM' and entity.parameter.mode == 'CV':
                        ascFile.write('sw t' + str(r) + ', -' + str(entity.parameter.offset) + '(sp)\n')
                elif entity.type == 'TEMP':
                        ascFile.write('sw t' + str(r) + ', -' + str(entity.tempVar.offset) + '(sp)\n')
        
        elif scope.nestingLvl == 0 and entity.type == 'VAR':
                ascFile.write('sw t' + str(r) + ', -' + str(entity.variable.offset) + '(sp)\n')
        elif scope.nestingLvl == 0 and entity.type == 'TEMP':
                ascFile.write('sw t' + str(r) + ', -' + str(entity.tempVar.offset) + '(sp)\n')

        elif scope.nestingLvl < topScope.nestingLvl:
                if entity.type == 'VAR':
                        gnlvcode(v)
                        ascFile.write('sw t' + str(r) + ', 0(t0)\n')
                elif entity.type == 'PARAM' and entity.parameter.mode == 'CV':
                        gnlvcode(v)
                        ascFile.write('sw t' + str(r) + ', 0(t0)\n')

Cntr = -1 #i


def final():

        global topScope
        global listOfAllQuads
        global ascFile
        global Cntr                        

        
        for i in range(len(listOfAllQuads)): 

                ascFile.write('label' + str(listOfAllQuads[i][0]) + ': \n') #label(quad num): (ex. label 24)

                if listOfAllQuads[i][1] == 'jump':
                        ascFile.write('j label' + str(listOfAllQuads[i][4]) + '\n') #4 as jump target
                
                elif listOfAllQuads[i][1] == '==':
                        loadvr(listOfAllQuads[i][2],1) #(x,1)
                        loadvr(listOfAllQuads[i][3],2) #(x,2)
                        ascFile.write('beq t1,t2,label' + str(listOfAllQuads[i][4]) + '\n')

                elif listOfAllQuads[i][1] == '!=':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2) 
                        ascFile.write('bne t1,t2,label' + str(listOfAllQuads[i][4]) + '\n')
                
                elif listOfAllQuads[i][1] == '>':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2) 
                        ascFile.write('bgt t1,t2,label' + str(listOfAllQuads[i][4]) + '\n')
                
                elif listOfAllQuads[i][1] == '<':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2) 
                        ascFile.write('blt t1,t2,label' + str(listOfAllQuads[i][4]) + '\n')

                elif listOfAllQuads[i][1] == '>=':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2) 
                        ascFile.write('bge t1,t2,label' + str(listOfAllQuads[i][4]) + '\n')
                
                elif listOfAllQuads[i][1] == '<=':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2) 
                        ascFile.write('ble t1,t2,label' + str(listOfAllQuads[i][4]) + '\n')
                
                elif listOfAllQuads[i][1] == ':=':
                        loadvr(listOfAllQuads[i][2],1)
                        storerv(1,listOfAllQuads[i][4])
                
                elif listOfAllQuads[i][1] == '+':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2)
                        ascFile.write('add t1,t1,t2\n')
                        storerv(1,listOfAllQuads[i][4])
                
                elif listOfAllQuads[i][1] == '-':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2)
                        ascFile.write('sub t1,t1,t2\n')
                        storerv(1,listOfAllQuads[i][4])
                
                elif listOfAllQuads[i][1] == '*':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2)
                        ascFile.write('mul t1,t1,t2\n')
                        storerv(1,listOfAllQuads[i][4])
                
                elif listOfAllQuads[i][1] == '//':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2)
                        ascFile.write('div t1,t1,t2\n')
                        storerv(1,listOfAllQuads[i][4])

                elif listOfAllQuads[i][1] == '%':
                        loadvr(listOfAllQuads[i][2],1)
                        loadvr(listOfAllQuads[i][3],2)
                        ascFile.write('mod t1,t1,t2\n')
                        storerv(1,listOfAllQuads[i][4])
                
                elif listOfAllQuads[i][1] == 'out':
                        loadvr(listOfAllQuads[i][2],1)
                        ascFile.write('mv a0,t1\n')
                        ascFile.write('li a7,1\n')
                        ascFile.write('ecall\n')
                
                elif listOfAllQuads[i][1] == 'inp':
                        ascFile.write('li a7,5\n') # in assembly a7=5 is the system call for reading an integer from the user.In assembly, the a7 register is used to specify the system call number when making a system call. Stackoverflow told me so.
                        ascFile.write('ecall\n')
                        ascFile.write('mv t1,a0\n')
                        storerv(1,listOfAllQuads[i][2])
                
                elif listOfAllQuads[i][1] == 'retv':
                        loadvr(listOfAllQuads[i][2],1)
                        ascFile.write('lw t0,-8(sp)\n')
                        ascFile.write('sw t1,(t0)\n')
                
                elif listOfAllQuads[i][1] == 'par':
                        if Cntr == -1:
                                x = 0
                                while x < len(listOfAllQuads): # loop till it find call or reach end of list
                                        
                                        if listOfAllQuads[x][1] == 'call':
                                                result = str(listOfAllQuads[x][2]) #2 for the name
                                                break

                                        x += 1
                                (scope,entity) = find_entity(result)
                                ascFile.write('addi fp,sp,-' + str(entity.subprogram.frameLength) + '\n')
                                Cntr = 0

                        if listOfAllQuads[i][3] == 'CV':
                                loadvr(listOfAllQuads[i][2],0)
                                
                                ascFile.write('sw t0,-' + str(12 + 4*Cntr) + '(sp)\n')
                                
                        
                        #elif listOfAllQuads[i][3] == 'REF':
                                #loadvr(listOfAllQuads[i][2],0)
                                #gnlvcode(listOfAllQuads[i][2])
                                #ascFile.write('sw t0,-' + str(12 + 4*Cntr) + '(sp)\n')

                        elif listOfAllQuads[i][1] == 'RET':
                                (scope,entity) = find_entity(listOfAllQuads[i][2])
                                ascFile.write('addi t0,sp' + str(entity.tempVar.offset) +'\n')
                                ascFile.write('sw t0,-8(fp)\n')
                        
                elif listOfAllQuads[i][1] == 'call':
                        Cntr = -1
                        (scope,entity) = find_entity(listOfAllQuads[i][2])
                        if topScope.nestingLvl == entity.subprogram.nestingLvl:
                                ascFile.write('lw t0,-4(sp)\n')
                                ascFile.write('sw t0,-4(fp)\n')
                        
                        elif topScope.nestingLvl < entity.subprogram.nestingLvl:
                                ascFile.write('sw sp,-4(fp)\n')
                        
                        ascFile.write('addi sp,sp,' + str(entity.subprogram.frameLength) + '\n')
                        ascFile.write('jal label' + str(entity.subprogram.startQuad) + '\n')
                        ascFile.write('addi sp,sp,-' + str(entity.subprogram.frameLength) + '\n')

                elif listOfAllQuads[i][1] == 'begin_block' and topScope.nestingLvl == 0:
                        ascFile.seek(0, os.SEEK_SET)
                        ascFile.write('j label' + str(listOfAllQuads[i][0]) + '\n')
                        ascFile.seek(0, os.SEEK_END)
                        #This will move the pointer to thestart of the file then label to main and the return to where it was.
                        ascFile.write('addi sp,sp,' + str(compute_offsets()) + '\n')
                        ascFile.write('move gp,sp\n')

                elif listOfAllQuads[i][1] == 'begin_block' and topScope.nestingLvl != 0:
                        ascFile.write('sw ra,-4(sp)\n')


                elif listOfAllQuads[i][1] == 'end_block' and topScope.nestingLvl != 0:
                        ascFile.write('lw ra,(sp)\n')
                        ascFile.write('jr ra\n')
                        
        def intCode(intF):
                #this writes the list of quads to the intermediate code file named intFile.int
                for i in range(len(listOfAllQuads)):
                        intF.write(str(listOfAllQuads[i][0]) + ' ' + str(listOfAllQuads[i][1]) + ' ' + str(listOfAllQuads[i][2]) + ' ' + str(listOfAllQuads[i][3]) + ' ' + str(listOfAllQuads[i][4]) + '\n')
        intF = open('intCodeFile.int','a')
        intCode(intF)
        intF.close()
        listOfAllQuads = []


                

        

#Parser

def parser():
        global LexRes
        global line
        global global_id_table
        global_id_table = {}
        LexRes = lex()
        line = LexRes[2]
        

        def startRule():
                new_scope('main')
                def_main_part()
                call_main_part()
            
           
            

        def def_main_part():
                global LexRes
                global line
                def_function()
                while(LexRes[0] != hash_def_tk):
                        def_function()
                
                
                

        def def_function():
                global LexRes
                global line
                global topScope
                declarations()
                if(LexRes[0] == def_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        if(LexRes[0] == keyword_tk):
                                name = LexRes[1]
                                LexRes = lex()
                                line = LexRes[2]
                                if(LexRes[0] == left_parentheses_tk):
                                        LexRes = lex()
                                        line = LexRes[2]
                                        
                                        newScope = Scope(enclosingScope=topScope)
                                        topScope = newScope

                                        while True:
                                                #print(f'Current LexRes[0]: {LexRes[1]}')  # Debugging print statement
                                                if LexRes[0] == right_parentheses_tk:
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                        break
                                                elif LexRes[0] == keyword_tk:
                                                        newEntity = Entity(name=LexRes[1], type='VAR')
                                                        topScope.entityList.append(newEntity)
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                elif LexRes[0] == comma_tk:
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                

                                        entity = Entity()
                                        entity.name = name
                                        entity.type = 'SUBPROGRAM'
                                        entity.subprogram.nestingLvl = topScope.nestingLvl + 1
                                        entity.subprogram.type = 'Function'
                                        new_entity(entity)
                                        id_list(0)
                                        #if(LexRes[0] == right_parentheses_tk):
                                                #LexRes = lex()
                                                #line = LexRes[2]
                                        if(LexRes[0] == colon_tk):
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                        if(LexRes[0] == left_curly_tk):
                                                                LexRes = lex()
                                                                line = LexRes[2]
                                                                new_scope(name)
                                                                add_parameter()
                                                                global_id_list(0)
                                                                declarations()
                                                                while(LexRes[0] == def_tk):
                                                                        def_function()
                                                                        
                                                                compute_startQuad()
                                                                
                                                                genQuad('begin_block',name,'_','_')
                                                                code_blocks()
                                                                compute_frameLength()
                                                                genQuad('end_block',name,'_','_')
                                                                
                                                                final()
                                                                delete_scope()

                                                                if(LexRes[0] == right_curly_tk):
                                                                        LexRes = lex()
                                                                        line = LexRes[2]
                                                                else:
                                                                        print("Missing: '#}'",line)
                                                                        exit(-1)
                                                                if(LexRes[0] == hash_int_tk or LexRes[0] == global_tk):
                                                                        declarations()
                                                        else:
                                                                print("Missing: '#{'",line)
                                                                exit(-1)
                                        else:
                                                        print("No ':' aftre calling function",line)
                                                        exit(-1)
                                        #else:
                                                #print("Missing: ')'",line)
                                                #exit(-1)
                                else:
                                        print("Missing: '('",line)
                                        exit(-1)
                        else:
                                print("Missing function name",line)
                                exit(-1)
                else:
                         print("Please start with def for function",line)
                         exit(-1)
        
        
        
        def declarations():
                global LexRes
                global line
                while(LexRes[0] == hash_int_tk or LexRes[0] == global_tk):
                        declaration_line()
        
        def declaration_line():
                global LexRes
                global line
                if(LexRes[0] == hash_int_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        id_list(1)
                elif(LexRes[0] == global_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        global_id_list(1)
                else:
                        print("Please start with '#int' or 'global' for declaration", line)
                        exit(-1)
        
        def id_list(flag):
                global LexRes
                global line
                if(LexRes[0] == keyword_tk):
                        name = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                        
                        if flag == 1:
                                entity = Entity()
                                entity.name = name
                                entity.type = 'VAR'
                                entity.variable.offset = compute_offsets()
                                new_entity(entity)
                        
                        else:
                                argument = Argument()
                                argument.name = name
                                argument.parMode = 'CV'
                                new_argument(argument)


                        while(LexRes[0] == comma_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                if(LexRes[0] == keyword_tk):
                                        LexRes = lex()
                                        line = LexRes[2]
                                        name = LexRes[1]
                                        if flag == 1:
                                                entity = Entity()
                                                entity.name = name
                                                entity.type = 'VAR'
                                                entity.variable.offset = compute_offsets()
                                                new_entity(entity)
                        
                                        else:
                                                argument = Argument()
                                                argument.name = name
                                                argument.parMode = 'CV'
                                                new_argument(argument)

                                else:
                                        print("Keyword expected after ','. Nothing found", line)
                                        exit(-1)
                

        def global_id_list(flag):
                global LexRes
                global line
                global global_id_table
                if(LexRes[0] == keyword_tk):
                        identifier = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                        global_id_table[identifier] = None
                        name = LexRes[1]

                        if flag == 1:
                                entity = Entity()
                                entity.name = name
                                entity.type = 'VAR'
                                entity.variable.offset = compute_offsets()
                                new_entity(entity)
                        
                        else:
                                argument = Argument()
                                argument.name = name
                                argument.parMode = 'CV'
                                new_argument(argument)


                        while(LexRes[0] == comma_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                if(LexRes[0] == keyword_tk):
                                        identifier = LexRes[1]
                                        LexRes = lex()
                                        line = LexRes[2]
                                        global_id_table[identifier] = None
                                        name = LexRes[1]
                                        if flag == 1:
                                                entity = Entity()
                                                entity.name = name
                                                entity.type = 'VAR'
                                                entity.variable.offset = compute_offsets()
                                                new_entity(entity)
                        
                                        else:
                                                argument = Argument()
                                                argument.name = name
                                                argument.parMode = 'CV'
                                                new_argument(argument)
                                else:
                                        print("Keyword expected after ','. Nothing found", line)
                                        exit(-1)
        
        def code_block():
                global LexRes 
                global line
                if(LexRes[0] == keyword_tk or LexRes[0] == print_tk or LexRes[0] == return_tk):
                        simple_code_block()
                elif(LexRes[0] == if_tk or LexRes[0] == while_tk):
                        structured_code_block()
                else:
                        print("Keywords Error", line)
                        exit(-1)
        
        def code_blocks():
                global LexRes
                
                code_block()
                while(LexRes[0] == keyword_tk or LexRes[0] == print_tk or LexRes[0] == return_tk or LexRes[0] == if_tk or LexRes[0] == while_tk):
                        code_block()
        
        def simple_code_block():
                global LexRes
                global global_id_table
                if(LexRes[0] == keyword_tk):
                        identifier = LexRes[1]
                        if(identifier in global_id_table):
                                LexRes = lex()  
                                if(LexRes[0] == assign_tk):
                                    LexRes = lex()
                                    value = expression()  
                                    global_id_table[identifier] = value  
                        else:
                            assignment_stat()
                            
                elif(LexRes[0] == print_tk):
                        print_stat()
                elif(LexRes[0] == return_tk):
                        return_stat()
        def structured_code_block():
                global LexRes
                if(LexRes[0] == if_tk):
                        if_stat()
                elif(LexRes[0] == while_tk):
                        while_stat()
        
        def assignment_stat():
                global LexRes
                global line
                if(LexRes[0] == keyword_tk):
                        thisId = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                        if(LexRes[0] == assign_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                if(LexRes[0] == int_tk):
                                        LexRes = lex()
                                        line = LexRes[2]

                                        genQuad('inp',thisId,'_','_')

                                        if(LexRes[0] == left_parentheses_tk):
                                                LexRes = lex()
                                                line = LexRes[2]
                                                if(LexRes[0] == input_tk):
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                        if(LexRes[0] == left_parentheses_tk):
                                                                LexRes = lex()
                                                                line = LexRes[2]
                                                                if(LexRes[0] == right_parentheses_tk):
                                                                        LexRes = lex()
                                                                        line = LexRes[2]
                                                                        if(LexRes[0] == right_parentheses_tk):
                                                                                LexRes = lex()
                                                                                line = LexRes[2]
                                                                                
                                                                        else:
                                                                                print("Missing: ')'",line)
                                                                                exit(-1)
                                                                else:
                                                                        print("Missing: ')'",line)
                                                                        exit(-1)
                                                        else:
                                                                print("Missing: '('",line)
                                                                exit(-1)
                                                else:
                                                        print("No input in assignment_stat",line)
                                                        exit(-1)
                                        else:
                                                print("Missing: '('",line)
                                                exit(-1)
                                else:
                                        #expression()
                                        Eplace = expression()
                                        genQuad(':=',Eplace,'_',thisId)
                                    
                                        
                        else:
                                print("Missing: '='",line)
                                exit(-1)
                else:
                        print("Missing keyword")
                        exit(-1)
  
        def print_stat():
                global LexRes
                global line
                if(LexRes[0] == print_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        if(LexRes[0] == left_parentheses_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                #expression()
                                Eplace = expression()
                                genQuad('out',Eplace,'_','_')

                                if(LexRes[0] == right_parentheses_tk):
                                        LexRes = lex()
                                        line = LexRes[2]
                                        if(LexRes[0] == EOF_tk):
                                                pass
                                else:
                                        print("Missing: ')' in print_stat",line)
                                        exit(-1)
                        else:
                                print("Missing: '(' in print_stat", line)
                                exit(-1)
                else:
                        print("Missing print",line)
                        exit(-1)
        def return_stat():
                global LexRes
                global line
                if(LexRes[0] == return_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        
                        #expression()
                        Eplace = expression()
                        genQuad('retv',Eplace,'_','_')
                        
                else:
                        print("Missing return",line)
                        exit(-1)
        
        
        def if_stat():
                global LexRes
                global line
                if(LexRes[0] == if_tk):
                        
                        LexRes = lex()
                        line = LexRes[2]
                        #condition()
                        C = condition()
                        backpatch(C[0], nextQuad())
                        
                        if(LexRes[0] == colon_tk):
                                                LexRes = lex()
                                                line = LexRes[2]
                                                
                                                code_blocks()

                                                backpatch(C[1],nextQuad())
                                                ListIf = makeList(nextQuad())
                                                genQuad('jump','_','_',ListIf[0])
                                                
                                                
                                                while(LexRes[0] == elif_tk):
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                        #conditon()
                                                        C = condition()
                                                        if(LexRes[0] == colon_tk):
                                                                                LexRes = lex()
                                                                                line = LexRes[2]
                                                                                
                                                                                code_blocks()
                                                                                ListIf = makeList(nextQuad())
                                                                                backpatch(C[1],nextQuad())
                                                                                genQuad('jump','_','_',ListIf[0])
                                                                                

                                                        else:
                                                                print("Missing: ':' after elif",line)
                                                                exit(-1)
                                                if(LexRes[0] == else_tk):
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                        if(LexRes[0] == colon_tk):
                                                                LexRes = lex()
                                                                line = LexRes[2]
                                                                
                                                                code_blocks()
                                                                backpatch(C[1],nextQuad())
                                                        else:
                                                                print("Missing ':' after else statement")
                                                                exit(-1)
                        else:
                                print("Missing ':' after if statement")
                                exit(-1)
                else:
                        print("Missing if statement")
                        exit(-1)
        
        def while_stat():
                global LexRes
                global line
                if(LexRes[0] == while_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        
                        Cquad = nextQuad()
                        C = condition()
                        backpatch(C[0], nextQuad())
                        #condition()
                                
                        if(LexRes[0] == colon_tk):
                                             LexRes = lex()
                                             line = LexRes[2]
                                             if(LexRes[0] == left_curly_tk):
                                                    LexRes = lex()
                                                    line = LexRes[2]
                                                    code_blocks()

                                                    genQuad('jump','_','_',Cquad)
                                                    backpatch(C[1],nextQuad())
                                                    if(LexRes[0] == right_curly_tk):
                                                        LexRes = lex()
                                                        line = LexRes[2]
                                                    else:
                                                        print("Missing '#}' after while statement",line)
                                                        exit(-1)
                                             else:
                                                    code_block()

                                                    genQuad('jump','_','_',Cquad)
                                                    backpatch(C[1],nextQuad())
                        else:
                                              print("Missing ':' after while statement",line)
                                              exit(-1)
                                
                else:
                        print("Missing while statement",line)
                        exit(-1)
        
        def expression():
                global LexRes
                global line
                optional_sign()
                T1p = term()
                while(LexRes[0] == plus_tk or LexRes[0] == minus_tk):
                        Plus_or_Minus = ADD_OP()
                        T2p = term()

                        w = newTemp()
                        genQuad(Plus_or_Minus,T1p,T2p,w)
                        T1p = w
                Eplace = T1p
                return Eplace
       
        def term():
                global LexRes
                global line
                F1p = factor()
                while(LexRes[0] == mult_tk or LexRes[0] == div_tk or LexRes[0] == mod_tk):
                        Mul_Or_Div = MUL_OP()
                        F2p = factor()

                        w = newTemp()
                        genQuad(Mul_Or_Div,F1p,F2p,w)
                        F1p = w
                Tp = F1p
                return Tp
        
        def factor():
                global LexRes
                global line
                if(LexRes[0] == number_tk):
                        Fact = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == left_parentheses_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        #expression()
                        Fact = expression() #Eplace
                        if(LexRes[0] == right_parentheses_tk):
                                LexRes = lex()
                                line = LexRes[2]
                        else:
                                print("Missing ')' after calling FACTOR ",line)
                                exit(-1)
                elif(LexRes[0] == keyword_tk):
                        Temp_Fact = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                        Fact  = idtail(Temp_Fact)
                else:
                        print("Missing constant either expression either variable when calling FACTOR",line)
                        exit(-1)
                return Fact
        
        def idtail(name):
                global LexRes
                global line
                if(LexRes[0] == left_parentheses_tk ):
                        LexRes = lex()
                        line = LexRes[2]
                        actual_par_list()
                        w = newTemp()
                        genQuad('par',w,'RET','_')
                        genQuad('call',name,'_','-')

                        if(LexRes[0] == right_parentheses_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                return w
                        else:
                                print("Missing ')' idtail")
                                exit(-1)
                if(LexRes[0] == right_parentheses_tk):
                        pass
                else:
                        return name
        
        def actual_par_list():
                global LexRes
                global line 
                if(LexRes[0] == number_tk or LexRes[0] == left_parentheses_tk or LexRes[0] == keyword_tk):
                    #expression()
                    thisExpression = expression()
                    genQuad('par',thisExpression,'CV','_')


                    while(LexRes[0] == comma_tk):
                        LexRes  = lex()
                        line = LexRes[2]
                        #expression()
                        thisExpression = expression()
                        genQuad('par',thisExpression,'CV','_')
                

        def optional_sign():
                global LexRes
                global line
                if(LexRes[0] == plus_tk or LexRes[0] == minus_tk):
                        ADD_OP()

        def ADD_OP():
                global LexRes 
                global line
                if(LexRes[0] == plus_tk):
                        Add_Op_Symb = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == minus_tk):
                        Add_Op_Symb = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                return Add_Op_Symb
        
        def MUL_OP():
                global LexRes 
                global line
                if(LexRes[0] == mult_tk):
                        Mul_Op_Symb = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == div_tk):
                        Mul_Op_Symb = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == mod_tk):
                        Mul_Op_Symb = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                return Mul_Op_Symb
        
        def condition():
                global LexRes
                global line

                Btrue = emptyList()
                Bfalse = emptyList()

                B1 = bool_term()

                Btrue = B1[0]
                Bfalse = B1[1]
                #bool_term()
                while(LexRes[0] == or_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        backpatch(Bfalse,nextQuad())
                        #bool_term()
                        B2 = bool_term()

                        Btrue = merge(Btrue,B2[0])
                        Bfalse = B2[1]
                return [Btrue,Bfalse]
        
        def bool_term():
                global LexRes
                global line
                #bool_factor()

                Btrue = emptyList()
                Bfalse = emptyList()

                B1 = bool_factor()

                Btrue = B1[0]
                Bfalse = B1[1]

                while(LexRes[0] == and_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        backpatch(Btrue,nextQuad())
                        #bool_factor()

                        B2 = bool_factor()

                        Bfalse = merge(Bfalse,B2[1])
                        Btrue = B2[0]
                
                return [Btrue,Bfalse]
        
        def bool_factor():
                global LexRes
                global line

                Btrue = emptyList()
                Bfalse = emptyList()

                if(LexRes[0] == not_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        if(LexRes[0] == left_parentheses_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                #condition()
                                C = condition()
                                if(LexRes[0] == right_curly_tk):
                                        LexRes = lex()
                                        line = LexRes[2]

                                        Btrue = C[1]
                                        Bfalse = C[0]

                                else:
                                        print("Missing ')' at boolfactor")
                                        exit(-1)
                        else:
                                print("Missing '(' at boolfactor")
                elif(LexRes[0] == left_parentheses_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        #condition()
                        C = condition()

                        if(LexRes[0] == right_parentheses_tk):
                                LexRes = lex()
                                line = LexRes[2]

                                Btrue = C[0]
                                Bfalse = C[1]
                                
                        else:
                                print("Missing ')' in boolfactor")
                                exit(-1)
                else:
                        #expression()
                        E1 = expression()
                        #REAL_OP()
                        R = REL_OP()
                        #expression()
                        E2 = expression()
                        
                        Btrue = makeList(nextQuad())
                        genQuad(R,E1,E2,'_')
                        Bfalse = makeList(nextQuad())
                        genQuad('jump','_','_','_')

                return [Btrue,Bfalse]
        
        def REL_OP():
                global LexRes
                global line
                if(LexRes[0] == equal_tk):
                        r = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == less_than_tk):
                        r = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == more_than_tk):
                        r = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == less_equal_tk):
                        r = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == more_equal_tk):
                        r = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                elif(LexRes[0] == not_equal_tk):
                        r = LexRes[1]
                        LexRes = lex()
                        line = LexRes[2]
                else:
                        print("PLease use one of (=, <, >, <=, >=, !=)")
                        exit(-1)
                return r
        
        def call_main_part():
                global LexRes
                global line
                
                if(LexRes[0] == hash_def_tk):
                        LexRes = lex()
                        line = LexRes[2]
                        if(LexRes[0] == main_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                
                                genQuad('begin_block','main','_','_')
                                main_function_call()
                                
                                while(LexRes[0] == keyword_tk):
                                        main_function_call()
                                genQuad('halt','_','_','_')
                                genQuad('end_block','main','_','_')

                                final()
                                delete_scope()
                        else:
                                print("Missing 'main' call")
                                exit(-1)
                else:
                        print("Missing '#def' call")
                        exit(-1)
        
        def main_function_call():
                global LexRes 
                global line
                while(LexRes[0] != EOF_tk):
                        if(LexRes[0] == hash_int_tk):
                                LexRes = lex()
                                line = LexRes[2]
                                id_list(0)
                        
                        
                        elif(LexRes[0] == keyword_tk):
                                assignment_stat() 
                        
                        elif(LexRes[0] == print_tk):
                                print_stat()

                        elif(LexRes[0] == while_tk):
                                while_stat()

                        
                else:
                        pass
                        
                                

        startRule() 


parser()
print("Parser Working")

print("Intermediate Code Working (File Created Named intCodeFile)")
print("Symbol Table created")
print("Assembly Code Working (File Created Named ascFile)")
ascFile.close()
