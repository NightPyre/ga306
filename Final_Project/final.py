import maya.cmds as cmds
import time
#Select the object you want rotated
selected = cmds.ls(sl= True, long= True)
s = 0
results = []
while s <= 24 :
    s = s + 1 ; 
    
    time.sleep(.25)
    print "s"
    
    cmds.rotate(0, 10, 0, relative=True, componentSpace=True)
    cmds.setAttr("defaultRenderGlobals.imageFormat", 32)
    result = cmds.render('persp', x=512, y=512)
    print results 
    
if s == 25 :
    
    print "reload"