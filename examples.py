#dictionary ex

name = 'jane'

def func_name (person_name):
    print(person_name + ' loves complexity')
    
funk_name = func_name

funk_name(name)


#func ex

import maya.cmds

def process_all_textures(*args):
    print(args[0], args[1:])
    
texture = maya.cmds.shadingNode('file' , asTexture=True)

tx1 = maya.cmds.shadingNode('file' , asTexture=True)
tx2 = maya.cmds.shadingNode('file' , asTexture=True)
tx3 = maya.cmds.shadingNode('file' , asTexture=True)

node_list = [tx1, tx2, tx3]

process_all_textures('ur_', *node_list)

#return

import maya.cmds

def mutate_list():
    list_arg = []
    list_arg.append(1)
    list_arg.append(2)
    list_arg.append(2)
    return list_arg
print(mutate_list())