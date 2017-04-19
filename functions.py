from treelib import Node, Tree


def condition_for_continue(leaf_str,user_str):
    my_character=""
    i=0    
    while(i<len(leaf_str)):
        if(leaf_str[i]>='a' and leaf_str[i]<='z'):
            my_character=my_character+leaf_str[i]
        i=i+1
    if(len(my_character) == len(user_str) or len(my_character)<len(user_str)):
        return True
    else:
        return False
        
def is_equal(leaf_str,user_str):
    if(leaf_str == user_str):
        return True
    else:
        return False

def get_leaf(tree):
    leaf_list=[]  
    list_node=tree.all_nodes()
    for item in list_node:
        if(Node.is_leaf(item)):
            leaf_list.append(item)
    return leaf_list
    
def create_children(leaf,grammer_list):
    copy_grammer_list=[]
    copy_list_function(grammer_list, copy_grammer_list)
    node_string=leaf.identifier         #reshteye morede nazar
    children_list=[]                    #list farzand haye reshteye morede nazar
    switch_for_variable=1   
    low_list=[]                         # list halat haye yek ghanon khas ke baraye tabe loop_func_for_variable ersal mmishavad
    # tahie list ke har motaghaier be chand halat rafte ast.
    variable_num_state=[]           
    for i in range(0,len(grammer_list)):
        first=grammer_list[i][0]
        second=len(grammer_list[i])-1
        variable_num_state.append([first,second])
    # mohasebeye tedade kole farzand ha 
    number_of_children=1
    flag_for_exist_children=0
    for i in range( 0 , len(node_string) ):
        for j in range(0 , len(variable_num_state)):
            if(variable_num_state[j][0]==node_string[i]):
                flag_for_exist_children=1
                number_of_children=number_of_children*variable_num_state[j][1]
    if(flag_for_exist_children==0):
        number_of_children=0
    children_list=create_children_list(number_of_children , children_list)
    # be andazeye size node_string peimayesh mikonim     
    for i in range(0 , len(node_string)):
        # agar character bod 
        if(node_string[i] >= 'a' and node_string[i] <= 'z'):
            children_list = loop_func_for_character(number_of_children , children_list , node_string[i] )
        # agar motaghaier bod 
        else:
            # create low_list            
            for j in range (0 , len(grammer_list)):               
                if(node_string[i] in grammer_list[j]):
                    low_list=grammer_list[j]
                    del low_list[0]
                    copy_list_function(copy_grammer_list,grammer_list )
            switch_for_variable = switch_for_variable * len(low_list)   # 1*3*3*2=18
            children_list=loop_func_for_variable(number_of_children , children_list , low_list , number_of_children/switch_for_variable)
    return children_list  
   
def create_children_list(number_of_children , children_list):
    for i in range(0 , number_of_children):
        children_list.append('')
    return children_list
    
   
def loop_func_for_character(number_of_loop , children_list , character):
    for i in range(0 , number_of_loop):
        children_list[i]=children_list[i] + character
    return children_list
    
    
    
def loop_func_for_variable(number_of_loop , children_list , low_list , switch ):
    j=0
    for i in range(1 , number_of_loop+1):
        if(low_list[j] != '?'):        
            children_list[i-1]=children_list[i-1] + low_list[j]        
        if(i % switch == 0):
            j=j+1
        if(j == len(low_list)):
            j=0
    return children_list

def is_there_any_variable(leaf_str):
    for i in range( 0 , len(leaf_str)):
        if(leaf_str[i] >= 'A' and leaf_str[i]<='Z'):
            return False
    return True
    
def copy_list_function( main_list ,copy_list ):
    while len(copy_list) > 0 : copy_list.pop()
    for i in range(0,len(main_list)):
        copy_list.append([])
        for j in range(0,len(main_list[i])):
            copy_list[i].append(main_list[i][j])
    
    
    
    
    
    
    
    






















    
    
    
    
    
    
    
    
    
    
    
    
    