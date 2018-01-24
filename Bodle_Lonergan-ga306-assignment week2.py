import maya.cmds;
spher = maya.cmds.polySphere()[0];
locate = maya.cmds.spaceLocator()[0];
maya.cmds.connectAttr(locate+'.tx', spher+'.scaleX')
maya.cmds.connectAttr(locate+'.ty', spher+'.scaleY')
maya.cmds.connectAttr(locate+'.tz', spher+'.scaleZ')
maya.cmds.select(locate)