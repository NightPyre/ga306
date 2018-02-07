import maya.cmds


def make_function(int) :
    radius = num *.5
    sphere = maya.cmds.polySphere(r = radius)[0]
    cube = maya.cmds.polyCube(d = num, h = num, w = num)[0]



    maya.cmds.connectAttr(cube+'.ry', sphere+'.ty')
    maya.cmds.select(cube)

make_function(1)

