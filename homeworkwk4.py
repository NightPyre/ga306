import maya.cmds

def rename_objects(new) :
    selected = maya.cmds.ls (sl = True)
    objectname = selected(0)
    maya.cmds.rename(objectname, new)
    print(rename_objects)
rename_objects("shoot")
