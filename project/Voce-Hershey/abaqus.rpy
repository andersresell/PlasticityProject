# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2022 replay file
# Internal Version: 2021_09_15-19.57.30 176069
# Run by anders on Wed Nov  1 20:37:49 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=364.331237792969, 
    height=208.409271240234)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o1 = session.openOdb(
    name='/home/anders/Documents/H2023/PlasticityTheory/PlasticityProject/project/unit_exp.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#* OdbError: Cannot open file 
#* /home/anders/Documents/H2023/PlasticityTheory/PlasticityProject/project/unit_exp.odb. 
#* *** ERROR: No such file: 
#* /home/anders/Documents/H2023/PlasticityTheory/PlasticityProject/project/unit_exp.odb.
o1 = session.openOdb(
    name='/home/anders/Documents/H2023/PlasticityTheory/PlasticityProject/project/MJC-Hershey/unit_shear.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/anders/Documents/H2023/PlasticityTheory/PlasticityProject/project/MJC-Hershey/unit_shear.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       2
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
odb = session.odbs['/home/anders/Documents/H2023/PlasticityTheory/PlasticityProject/project/MJC-Hershey/unit_shear.odb']
xyList = xyPlot.xyDataListFromField(odb=odb, outputPosition=INTEGRATION_POINT, 
    variable=(('S', INTEGRATION_POINT, ((INVARIANT, 'Mises'), )), ), 
    elementPick=(('REF', 1, ('[#1 ]', )), ('VUMAT', 1, ('[#1 ]', )), ), )
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
curveList = session.curveSet(xyData=xyList)
chart.setValues(curvesToPlot=curveList)
session.charts[chartName].autoColor(lines=True, symbols=True)
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['/home/anders/Documents/H2023/PlasticityTheory/PlasticityProject/project/MJC-Hershey/unit_shear.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=odb)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
x = session.xyPlots['XYPlot-1']
session.viewports['Viewport: 1'].setValues(displayedObject=x)
c1 = session.curves['_S:Mises PI: REF E: 1 IP: 1']
session.charts['Chart-1'].removeCurve(curve=(c1, ))
