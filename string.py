import functions
from treelib import Node, Tree
import main


'''
grammer = main.readFromFile("grammar.txt")
if main.isContexFreeGrammer(grammer):
        print("is a cfg...")
else:
        print("grammer is not a cfg ...")
'''

grammer_list=[
[ 'S' , 'aSb' ,  'A' , 'bB' , ''],
['A' , 'aA' , ''],
['B' , 'bB' , ''],
]

# Variable List
leaf_list=[]    # liste barghaye har marhale
unvalid_leaf_list=[]    # list barg haye gheire mojaze 
father_node=''      # node pedar ke dar marhaleye farzand sazi estefade mishavad
children_list=[]    # liste farzand ha baraye har pedar
unvalid_leaf_list_for_continue=[]
checked_list_for_duplicated=[]
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
print "Please Enter Your String For Check:"
user_str=raw_input()
print "____________________________________________________\n"

tree = Tree()
tree.create_node("S", "S")  # root node
tree.create_node("aSb", "aSb", parent="S"  )
tree.create_node("A", "A", parent="S" )
tree.create_node("bB", "bB", parent="S" )
tree.create_node("", "", parent="S" )

checked_list_for_duplicated.append("aSb")
checked_list_for_duplicated.append("A")
checked_list_for_duplicated.append("bB")
checked_list_for_duplicated.append("")

#print functions.create_children(functions.get_leaf(tree)[0],grammer_list)
j=0
while(1):
    leaf_list=functions.get_leaf(tree)    
    # baresie inke reshteye karbar ba reshteye barg ha barabar ast ya na .
    for i in range(0 , len(leaf_list)):
        if(functions.is_equal(leaf_list[i].identifier,user_str)):
            print "Derakhte Eshteghagh:\n"
            tree.show()
            print "____________________________________________________\n"
            print "Reshte Yaft Shod."
            exit()
    # tahiieye listi az barg haye gheire mojaz baraye edame derakht.
    for i in range (0 , len(leaf_list)):
        if((leaf_list[i].identifier in unvalid_leaf_list)== False):
            if(functions.condition_for_continue( leaf_list[i].identifier , user_str) == False):
                unvalid_leaf_list.append(leaf_list[i].identifier)
    # tahiieye listi az barg haye gheire mojaz baraye edame ye while.
    for i in range(0 , len(unvalid_leaf_list_for_continue)):
        unvalid_leaf_list_for_continue.pop()
    for i in range(0 , len(leaf_list)):
        if(functions.condition_for_continue( leaf_list[i].identifier , user_str) == False):
            unvalid_leaf_list_for_continue.append(leaf_list[i])
        elif(functions.is_there_any_variable(leaf_list[i].identifier)==True):
            unvalid_leaf_list_for_continue.append(leaf_list[i])
    if(leaf_list == unvalid_leaf_list_for_continue):
        tree.show() 
        print "____________________________________________________\n"
        print "Reshteye Yaft Nashod."
        break
    # sakhtan farzand va gharar dadane anha dar derakht
    for i in range( 0 , len(leaf_list)): 
        if(functions.is_there_any_variable(leaf_list[i].identifier)==False):    # baressie inke barg motaghaier dashte bashad
            if((leaf_list[i].identifier in unvalid_leaf_list)== False):     # barresie inke barg mojaz bashad az lahaze tedad
                    father_node=leaf_list[i]
                    children_list=functions.create_children(father_node , grammer_list)
                    for item in children_list:
                        if((item in checked_list_for_duplicated) == False):        # barresie inke farzand tekrari nabashad. 
                            tree.create_node(item , item , parent= father_node.identifier)
                        checked_list_for_duplicated.append(item)
    j=j+1


















