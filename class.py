import maya.cmds

print("Input Height, Width, Length")



sphere = maya.cmds.polySphere()[0]
cube = maya.cmds.polyCube()[0]

maya.cmds.connectAttr(cube+'.ry', sphere+'.ty')
maya.cmds.select(cube)