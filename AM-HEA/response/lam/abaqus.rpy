# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.13-1 replay file
# Internal Version: 2013_05_15-19.56.28 126354
# Run by yzhang951 on Wed Dec 29 13:21:57 2021
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=259.829406738281, 
    height=201.435180664062)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
o1 = session.openOdb(name='/home/yzhang951/AlHEA/response/lam/Job-1.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: /home/yzhang951/AlHEA/response/lam/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          8
#: Number of Steps:              1
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
odb = session.odbs['/home/yzhang951/AlHEA/response/lam/Job-1.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 1 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 2 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy2 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 3 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy3 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 4 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy4 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 5 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy5 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 6 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy6 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 7 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy7 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 8 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy8 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 9 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy9 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 10 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy10 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 11 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy11 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 12 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy12 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 13 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy13 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 14 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy14 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 15 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy15 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 16 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy16 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 17 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy17 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 18 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy18 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 19 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy19 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 20 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy20 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 21 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy21 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 22 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy22 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 23 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy23 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 24 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy24 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 25 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy25 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 26 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy26 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 27 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy27 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 28 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy28 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 29 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy29 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 30 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy30 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 31 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy31 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 32 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy32 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 33 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy33 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 34 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy34 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 35 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy35 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 36 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy36 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 37 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy37 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 38 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy38 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 39 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy39 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 40 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy40 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 41 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy41 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 42 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy42 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 43 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy43 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 44 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy44 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 45 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy45 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 46 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy46 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 47 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy47 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 48 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy48 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 49 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy49 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 50 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy50 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 51 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy51 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 52 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy52 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 53 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy53 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 54 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy54 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 55 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy55 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 56 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy56 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 57 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy57 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 58 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy58 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 59 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy59 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 60 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy60 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 61 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy61 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 62 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy62 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 63 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy63 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 64 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy64 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 65 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy65 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 66 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy66 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 67 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy67 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 68 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy68 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 69 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy69 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 70 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy70 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 71 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy71 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 72 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy72 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 73 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy73 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 74 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy74 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 75 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy75 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 76 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy76 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 77 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy77 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 78 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy78 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 79 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy79 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 80 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy80 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 81 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy81 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 82 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy82 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 83 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy83 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 84 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy84 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 85 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy85 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 86 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy86 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 87 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy87 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 88 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy88 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 89 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy89 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 90 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy90 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 91 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy91 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 92 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy92 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 93 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy93 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 94 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy94 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 95 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy95 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 96 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy96 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 97 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy97 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 98 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy98 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 99 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy99 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 100 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy100 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 101 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy101 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 102 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy102 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 103 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy103 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 104 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy104 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 105 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy105 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 106 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy106 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 107 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy107 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 108 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy108 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 109 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy109 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 110 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy110 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 111 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy111 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 112 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy112 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 113 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy113 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 114 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy114 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 115 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy115 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 116 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy116 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 117 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy117 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 118 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy118 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 119 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy119 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 120 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy120 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 121 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy121 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 122 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy122 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 123 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy123 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 124 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy124 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 125 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy125 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 126 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy126 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 127 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy127 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 128 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy128 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 129 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy129 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 130 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy130 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 131 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy131 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 132 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy132 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 133 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy133 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 134 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy134 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 135 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy135 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 136 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy136 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 137 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy137 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 138 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy138 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 139 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy139 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 140 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy140 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 141 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy141 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 142 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy142 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 143 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy143 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 144 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy144 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 145 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy145 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 146 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy146 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 147 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy147 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 148 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy148 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 149 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy149 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 150 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy150 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 151 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy151 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 152 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy152 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 153 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy153 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 154 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy154 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 155 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy155 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 156 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy156 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 157 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy157 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 158 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy158 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 159 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy159 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 160 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy160 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 161 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy161 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 162 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy162 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 163 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy163 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 164 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy164 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 165 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy165 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 166 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy166 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 167 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy167 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 168 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy168 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 169 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy169 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 170 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy170 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 171 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy171 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 172 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy172 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 173 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy173 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 174 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy174 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 175 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy175 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 176 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy176 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 177 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy177 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 178 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy178 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 179 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy179 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 180 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy180 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 181 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy181 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 182 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy182 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 183 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy183 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 184 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy184 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 185 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy185 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 186 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy186 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 187 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy187 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 188 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy188 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 189 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy189 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 190 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy190 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 191 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy191 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 192 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy192 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 193 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy193 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 194 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy194 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 195 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy195 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 196 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy196 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 197 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy197 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 198 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy198 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 199 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy199 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 200 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy200 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 201 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy201 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 202 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy202 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 203 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy203 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 204 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy204 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 205 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy205 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 206 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy206 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 207 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy207 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 208 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy208 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 209 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy209 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 210 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy210 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 211 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy211 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 212 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy212 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 213 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy213 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 214 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy214 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 215 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy215 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 216 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy216 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 217 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy217 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 218 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy218 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 219 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy219 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 220 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy220 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 221 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy221 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 222 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy222 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 223 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy223 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 224 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy224 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 225 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy225 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 226 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy226 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 227 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy227 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 228 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy228 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 229 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy229 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 230 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy230 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 231 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy231 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 232 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy232 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 233 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy233 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 234 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy234 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 235 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy235 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 236 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy236 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 237 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy237 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 238 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy238 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 239 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy239 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 240 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy240 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 241 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy241 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 242 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy242 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 243 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy243 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 244 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy244 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 245 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy245 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 246 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy246 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 247 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy247 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 248 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy248 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 249 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy249 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 250 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy250 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 251 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy251 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 252 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy252 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 253 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy253 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 254 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy254 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 255 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy255 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 256 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy256 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 257 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy257 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 258 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy258 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 259 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy259 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 260 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy260 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 261 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy261 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 262 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy262 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 263 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy263 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 264 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy264 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 265 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy265 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 266 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy266 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 267 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy267 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 268 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy268 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 269 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy269 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 270 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy270 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 271 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy271 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 272 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy272 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 273 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy273 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 274 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy274 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 275 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy275 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 276 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy276 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 277 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy277 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 278 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy278 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 279 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy279 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 280 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy280 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 281 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy281 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 282 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy282 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 283 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy283 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 284 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy284 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 285 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy285 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 286 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy286 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 287 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy287 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 288 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy288 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 289 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy289 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 290 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy290 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 291 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy291 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 292 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy292 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 293 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy293 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 294 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy294 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 295 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy295 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 296 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy296 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 297 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy297 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 298 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy298 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 299 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy299 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 300 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy300 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 301 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy301 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 302 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy302 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 303 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy303 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 304 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy304 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 305 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy305 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 306 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy306 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 307 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy307 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 308 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy308 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 309 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy309 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 310 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy310 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 311 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy311 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 312 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy312 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 313 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy313 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 314 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy314 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 315 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy315 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 316 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy316 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 317 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy317 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 318 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy318 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 319 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy319 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 320 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy320 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 321 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy321 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 322 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy322 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 323 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy323 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 324 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy324 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 325 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy325 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 326 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy326 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 327 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy327 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 328 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy328 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 329 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy329 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 330 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy330 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 331 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy331 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 332 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy332 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 333 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy333 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 334 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy334 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 335 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy335 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 336 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy336 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 337 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy337 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 338 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy338 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 339 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy339 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 340 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy340 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 341 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy341 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 342 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy342 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 343 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy343 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 344 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy344 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 345 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy345 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 346 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy346 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 347 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy347 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 348 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy348 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 349 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy349 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 350 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy350 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 351 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy351 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 352 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy352 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 353 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy353 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 354 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy354 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 355 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy355 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 356 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy356 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 357 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy357 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 358 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy358 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 359 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy359 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 360 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy360 = avg((xy0, xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, 
    xy12, xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, 
    xy24, xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, 
    xy36, xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, 
    xy48, xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, 
    xy60, xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, 
    xy72, xy73, xy74, xy75, xy76, xy77, xy78, xy79, xy80, xy81, xy82, xy83, 
    xy84, xy85, xy86, xy87, xy88, xy89, xy90, xy91, xy92, xy93, xy94, xy95, 
    xy96, xy97, xy98, xy99, xy100, xy101, xy102, xy103, xy104, xy105, xy106, 
    xy107, xy108, xy109, xy110, xy111, xy112, xy113, xy114, xy115, xy116, 
    xy117, xy118, xy119, xy120, xy121, xy122, xy123, xy124, xy125, xy126, 
    xy127, xy128, xy129, xy130, xy131, xy132, xy133, xy134, xy135, xy136, 
    xy137, xy138, xy139, xy140, xy141, xy142, xy143, xy144, xy145, xy146, 
    xy147, xy148, xy149, xy150, xy151, xy152, xy153, xy154, xy155, xy156, 
    xy157, xy158, xy159, xy160, xy161, xy162, xy163, xy164, xy165, xy166, 
    xy167, xy168, xy169, xy170, xy171, xy172, xy173, xy174, xy175, xy176, 
    xy177, xy178, xy179, xy180, xy181, xy182, xy183, xy184, xy185, xy186, 
    xy187, xy188, xy189, xy190, xy191, xy192, xy193, xy194, xy195, xy196, 
    xy197, xy198, xy199, xy200, xy201, xy202, xy203, xy204, xy205, xy206, 
    xy207, xy208, xy209, xy210, xy211, xy212, xy213, xy214, xy215, xy216, 
    xy217, xy218, xy219, xy220, xy221, xy222, xy223, xy224, xy225, xy226, 
    xy227, xy228, xy229, xy230, xy231, xy232, xy233, xy234, xy235, xy236, 
    xy237, xy238, xy239, xy240, xy241, xy242, xy243, xy244, xy245, xy246, 
    xy247, xy248, xy249, xy250, xy251, xy252, xy253, xy254, xy255, xy256, 
    xy257, xy258, xy259, xy260, xy261, xy262, xy263, xy264, xy265, xy266, 
    xy267, xy268, xy269, xy270, xy271, xy272, xy273, xy274, xy275, xy276, 
    xy277, xy278, xy279, xy280, xy281, xy282, xy283, xy284, xy285, xy286, 
    xy287, xy288, xy289, xy290, xy291, xy292, xy293, xy294, xy295, xy296, 
    xy297, xy298, xy299, xy300, xy301, xy302, xy303, xy304, xy305, xy306, 
    xy307, xy308, xy309, xy310, xy311, xy312, xy313, xy314, xy315, xy316, 
    xy317, xy318, xy319, xy320, xy321, xy322, xy323, xy324, xy325, xy326, 
    xy327, xy328, xy329, xy330, xy331, xy332, xy333, xy334, xy335, xy336, 
    xy337, xy338, xy339, xy340, xy341, xy342, xy343, xy344, xy345, xy346, 
    xy347, xy348, xy349, xy350, xy351, xy352, xy353, xy354, xy355, xy356, 
    xy357, xy358, xy359, ), )
xy_result = session.XYData(name='FCC-1', objectToCopy=xy360, 
    sourceDescription='avg((Stress components: S11 at Element 1 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 2 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 3 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 4 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 5 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 6 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 7 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 8 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 9 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 10 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 11 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 12 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 13 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 14 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 15 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 16 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 17 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 18 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 19 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 20 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 21 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 22 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 23 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 24 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 25 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 26 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 27 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 28 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 29 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 30 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 31 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 32 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 33 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 34 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 35 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 36 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 37 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 38 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 39 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 40 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 41 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 42 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 43 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 44 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 45 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 46 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 47 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 48 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 49 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 50 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 51 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 52 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 53 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 54 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 55 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 56 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 57 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 58 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 59 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 60 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 61 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 62 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 63 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 64 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 65 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 66 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 67 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 68 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 69 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 70 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 71 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 72 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 73 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 74 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 75 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 76 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 77 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 78 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 79 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 80 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 81 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 82 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 83 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 84 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 85 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 86 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 87 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 88 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 89 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 90 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 91 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 92 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 93 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 94 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 95 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 96 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 97 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 98 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 99 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 100 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 101 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 102 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 103 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 104 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 105 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 106 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 107 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 108 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 109 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 110 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 111 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 112 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 113 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 114 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 115 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 116 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 117 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 118 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 119 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 120 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 121 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 122 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 123 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 124 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 125 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 126 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 127 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 128 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 129 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 130 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 131 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 132 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 133 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 134 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 135 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 136 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 137 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 138 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 139 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 140 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 141 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 142 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 143 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 144 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 145 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 146 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 147 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 148 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 149 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 150 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 151 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 152 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 153 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 154 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 155 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 156 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 157 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 158 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 159 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 160 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 161 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 162 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 163 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 164 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 165 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 166 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 167 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 168 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 169 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 170 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 171 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 172 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 173 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 174 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 175 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 176 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 177 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 178 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 179 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 180 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 181 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 182 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 183 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 184 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 185 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 186 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 187 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 188 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 189 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 190 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 191 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 192 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 193 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 194 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 195 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 196 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 197 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 198 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 199 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 200 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 201 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 202 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 203 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 204 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 205 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 206 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 207 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 208 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 209 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 210 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 211 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 212 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 213 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 214 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 215 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 216 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 217 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 218 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 219 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 220 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 221 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 222 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 223 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 224 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 225 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 226 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 227 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 228 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 229 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 230 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 231 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 232 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 233 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 234 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 235 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 236 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 237 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 238 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 239 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 240 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 241 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 242 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 243 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 244 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 245 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 246 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 247 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 248 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 249 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 250 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 251 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 252 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 253 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 254 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 255 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 256 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 257 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 258 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 259 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 260 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 261 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 262 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 263 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 264 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 265 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 266 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 267 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 268 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 269 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 270 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 271 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 272 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 273 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 274 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 275 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 276 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 277 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 278 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 279 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 280 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 281 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 282 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 283 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 284 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 285 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 286 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 287 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 288 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 289 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 290 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 291 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 292 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 293 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 294 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 295 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 296 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 297 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 298 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 299 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 300 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 301 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 302 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 303 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 304 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 305 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 306 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 307 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 308 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 309 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 310 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 311 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 312 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 313 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 314 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 315 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 316 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 317 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 318 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 319 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 320 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 321 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 322 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 323 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 324 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 325 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 326 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 327 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 328 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 329 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 330 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 331 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 332 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 333 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 334 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 335 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 336 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 337 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 338 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 339 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 340 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 341 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 342 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 343 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 344 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 345 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 346 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 347 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 348 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 349 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 350 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 351 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 352 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 353 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 354 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 355 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 356 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 357 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 358 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 359 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 360 Int Point 1 in ELSET SET-FCC, ),)')
c1 = session.Curve(xyData=xy_result)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
odb = session.odbs['/home/yzhang951/AlHEA/response/lam/Job-1.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 1 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 2 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy2 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 3 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy3 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 4 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy4 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 5 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy5 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 6 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy6 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 7 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy7 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 8 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy8 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 9 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy9 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 10 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy10 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 11 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy11 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 12 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy12 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 13 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy13 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 14 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy14 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 15 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy15 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 16 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy16 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 17 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy17 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 18 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy18 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 19 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy19 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 20 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy20 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 21 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy21 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 22 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy22 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 23 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy23 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 24 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy24 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 25 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy25 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 26 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy26 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 27 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy27 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 28 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy28 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 29 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy29 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 30 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy30 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 31 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy31 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 32 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy32 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 33 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy33 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 34 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy34 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 35 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy35 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 36 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy36 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 37 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy37 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 38 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy38 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 39 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy39 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 40 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy40 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 41 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy41 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 42 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy42 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 43 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy43 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 44 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy44 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 45 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy45 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 46 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy46 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 47 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy47 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 48 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy48 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 49 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy49 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 50 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy50 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 51 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy51 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 52 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy52 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 53 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy53 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 54 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy54 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 55 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy55 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 56 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy56 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 57 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy57 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 58 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy58 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 59 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy59 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 60 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy60 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 61 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy61 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 62 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy62 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 63 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy63 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 64 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy64 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 65 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy65 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 66 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy66 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 67 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy67 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 68 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy68 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 69 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy69 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 70 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy70 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 71 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy71 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 72 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy72 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 73 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy73 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 74 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy74 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 75 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy75 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 76 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy76 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 77 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy77 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 78 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy78 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 79 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy79 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 80 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy80 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 81 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy81 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 82 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy82 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 83 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy83 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 84 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy84 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 85 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy85 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 86 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy86 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 87 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy87 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 88 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy88 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 89 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy89 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 90 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy90 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 91 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy91 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 92 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy92 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 93 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy93 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 94 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy94 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 95 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy95 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 96 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy96 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 97 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy97 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 98 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy98 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 99 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy99 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 100 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy100 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 101 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy101 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 102 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy102 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 103 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy103 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 104 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy104 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 105 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy105 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 106 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy106 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 107 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy107 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 108 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy108 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 109 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy109 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 110 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy110 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 111 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy111 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 112 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy112 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 113 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy113 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 114 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy114 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 115 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy115 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 116 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy116 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 117 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy117 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 118 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy118 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 119 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy119 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 120 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy120 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 121 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy121 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 122 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy122 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 123 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy123 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 124 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy124 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 125 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy125 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 126 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy126 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 127 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy127 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 128 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy128 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 129 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy129 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 130 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy130 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 131 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy131 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 132 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy132 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 133 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy133 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 134 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy134 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 135 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy135 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 136 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy136 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 137 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy137 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 138 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy138 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 139 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy139 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 140 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy140 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 141 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy141 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 142 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy142 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 143 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy143 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 144 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy144 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 145 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy145 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 146 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy146 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 147 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy147 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 148 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy148 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 149 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy149 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 150 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy150 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 151 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy151 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 152 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy152 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 153 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy153 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 154 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy154 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 155 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy155 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 156 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy156 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 157 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy157 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 158 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy158 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 159 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy159 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 160 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy160 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 161 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy161 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 162 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy162 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 163 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy163 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 164 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy164 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 165 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy165 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 166 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy166 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 167 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy167 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 168 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy168 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 169 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy169 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 170 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy170 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 171 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy171 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 172 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy172 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 173 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy173 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 174 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy174 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 175 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy175 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 176 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy176 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 177 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy177 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 178 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy178 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 179 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy179 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 180 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy180 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 181 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy181 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 182 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy182 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 183 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy183 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 184 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy184 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 185 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy185 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 186 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy186 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 187 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy187 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 188 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy188 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 189 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy189 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 190 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy190 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 191 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy191 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 192 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy192 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 193 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy193 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 194 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy194 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 195 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy195 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 196 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy196 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 197 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy197 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 198 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy198 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 199 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy199 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 200 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy200 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 201 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy201 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 202 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy202 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 203 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy203 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 204 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy204 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 205 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy205 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 206 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy206 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 207 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy207 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 208 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy208 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 209 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy209 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 210 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy210 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 211 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy211 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 212 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy212 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 213 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy213 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 214 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy214 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 215 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy215 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 216 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy216 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 217 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy217 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 218 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy218 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 219 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy219 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 220 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy220 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 221 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy221 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 222 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy222 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 223 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy223 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 224 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy224 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 225 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy225 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 226 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy226 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 227 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy227 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 228 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy228 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 229 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy229 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 230 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy230 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 231 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy231 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 232 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy232 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 233 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy233 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 234 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy234 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 235 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy235 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 236 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy236 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 237 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy237 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 238 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy238 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 239 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy239 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 240 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy240 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 241 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy241 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 242 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy242 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 243 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy243 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 244 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy244 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 245 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy245 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 246 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy246 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 247 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy247 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 248 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy248 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 249 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy249 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 250 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy250 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 251 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy251 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 252 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy252 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 253 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy253 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 254 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy254 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 255 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy255 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 256 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy256 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 257 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy257 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 258 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy258 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 259 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy259 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 260 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy260 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 261 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy261 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 262 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy262 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 263 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy263 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 264 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy264 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 265 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy265 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 266 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy266 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 267 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy267 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 268 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy268 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 269 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy269 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 270 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy270 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 271 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy271 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 272 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy272 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 273 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy273 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 274 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy274 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 275 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy275 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 276 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy276 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 277 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy277 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 278 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy278 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 279 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy279 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 280 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy280 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 281 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy281 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 282 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy282 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 283 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy283 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 284 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy284 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 285 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy285 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 286 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy286 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 287 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy287 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 288 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy288 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 289 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy289 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 290 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy290 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 291 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy291 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 292 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy292 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 293 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy293 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 294 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy294 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 295 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy295 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 296 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy296 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 297 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy297 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 298 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy298 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 299 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy299 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 300 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy300 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 301 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy301 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 302 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy302 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 303 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy303 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 304 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy304 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 305 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy305 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 306 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy306 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 307 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy307 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 308 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy308 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 309 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy309 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 310 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy310 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 311 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy311 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 312 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy312 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 313 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy313 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 314 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy314 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 315 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy315 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 316 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy316 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 317 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy317 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 318 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy318 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 319 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy319 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 320 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy320 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 321 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy321 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 322 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy322 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 323 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy323 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 324 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy324 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 325 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy325 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 326 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy326 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 327 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy327 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 328 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy328 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 329 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy329 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 330 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy330 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 331 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy331 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 332 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy332 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 333 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy333 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 334 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy334 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 335 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy335 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 336 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy336 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 337 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy337 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 338 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy338 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 339 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy339 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 340 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy340 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 341 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy341 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 342 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy342 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 343 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy343 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 344 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy344 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 345 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy345 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 346 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy346 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 347 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy347 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 348 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy348 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 349 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy349 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 350 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy350 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 351 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy351 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 352 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy352 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 353 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy353 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 354 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy354 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 355 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy355 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 356 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy356 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 357 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy357 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 358 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy358 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 359 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy359 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 360 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy360 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 541 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy361 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 542 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy362 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 543 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy363 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 544 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy364 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 545 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy365 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 546 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy366 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 547 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy367 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 548 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy368 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 549 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy369 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 550 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy370 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 551 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy371 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 552 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy372 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 553 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy373 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 554 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy374 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 555 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy375 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 556 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy376 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 557 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy377 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 558 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy378 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 559 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy379 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 560 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy380 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 561 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy381 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 562 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy382 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 563 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy383 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 564 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy384 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 565 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy385 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 566 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy386 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 567 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy387 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 568 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy388 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 569 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy389 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 570 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy390 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 571 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy391 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 572 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy392 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 573 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy393 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 574 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy394 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 575 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy395 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 576 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy396 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 577 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy397 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 578 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy398 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 579 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy399 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 580 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy400 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 581 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy401 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 582 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy402 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 583 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy403 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 584 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy404 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 585 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy405 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 586 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy406 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 587 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy407 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 588 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy408 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 589 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy409 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 590 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy410 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 591 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy411 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 592 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy412 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 593 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy413 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 594 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy414 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 595 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy415 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 596 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy416 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 597 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy417 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 598 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy418 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 599 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy419 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 600 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy420 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 601 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy421 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 602 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy422 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 603 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy423 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 604 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy424 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 605 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy425 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 606 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy426 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 607 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy427 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 608 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy428 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 609 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy429 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 610 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy430 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 611 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy431 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 612 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy432 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 613 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy433 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 614 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy434 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 615 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy435 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 616 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy436 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 617 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy437 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 618 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy438 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 619 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy439 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 620 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy440 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 621 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy441 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 622 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy442 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 623 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy443 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 624 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy444 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 625 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy445 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 626 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy446 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 627 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy447 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 628 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy448 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 629 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy449 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 630 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy450 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 631 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy451 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 632 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy452 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 633 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy453 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 634 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy454 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 635 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy455 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 636 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy456 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 637 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy457 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 638 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy458 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 639 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy459 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 640 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy460 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 641 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy461 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 642 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy462 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 643 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy463 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 644 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy464 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 645 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy465 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 646 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy466 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 647 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy467 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 648 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy468 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 649 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy469 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 650 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy470 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 651 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy471 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 652 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy472 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 653 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy473 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 654 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy474 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 655 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy475 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 656 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy476 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 657 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy477 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 658 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy478 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 659 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy479 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 660 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy480 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 661 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy481 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 662 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy482 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 663 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy483 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 664 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy484 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 665 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy485 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 666 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy486 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 667 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy487 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 668 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy488 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 669 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy489 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 670 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy490 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 671 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy491 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 672 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy492 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 673 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy493 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 674 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy494 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 675 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy495 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 676 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy496 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 677 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy497 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 678 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy498 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 679 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy499 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 680 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy500 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 681 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy501 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 682 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy502 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 683 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy503 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 684 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy504 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 685 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy505 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 686 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy506 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 687 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy507 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 688 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy508 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 689 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy509 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 690 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy510 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 857 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy511 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 858 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy512 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 859 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy513 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 860 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy514 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 861 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy515 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 862 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy516 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 863 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy517 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 864 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy518 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 865 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy519 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 866 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy520 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 867 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy521 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 868 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy522 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 869 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy523 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 870 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy524 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 871 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy525 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 872 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy526 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 873 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy527 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 874 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy528 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 875 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy529 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 876 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy530 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 877 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy531 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 878 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy532 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 879 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy533 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 880 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy534 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 881 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy535 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 882 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy536 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 883 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy537 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 884 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy538 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 885 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy539 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 886 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy540 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 887 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy541 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 888 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy542 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 889 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy543 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 890 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy544 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 891 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy545 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 892 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy546 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 893 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy547 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 894 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy548 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 895 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy549 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 896 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy550 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 897 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy551 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 898 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy552 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 899 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy553 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 900 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy554 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 901 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy555 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 902 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy556 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 903 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy557 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 904 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy558 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 905 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy559 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 906 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy560 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 907 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy561 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 908 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy562 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 909 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy563 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 910 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy564 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 911 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy565 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 912 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy566 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 913 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy567 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 914 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy568 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 915 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy569 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 916 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy570 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 917 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy571 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 918 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy572 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 919 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy573 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 920 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy574 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 921 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy575 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 922 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy576 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 923 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy577 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 924 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy578 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 925 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy579 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 926 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy580 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 927 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy581 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 928 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy582 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 929 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy583 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 930 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy584 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 931 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy585 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 932 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy586 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 933 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy587 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 934 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy588 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 935 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy589 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 936 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy590 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 937 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy591 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 938 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy592 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 939 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy593 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 940 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy594 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 941 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy595 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 942 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy596 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 943 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy597 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 944 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy598 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 945 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy599 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 946 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy600 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 947 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy601 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 948 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy602 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 949 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy603 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 950 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy604 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 951 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy605 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 952 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy606 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 953 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy607 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 954 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy608 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 955 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy609 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 956 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy610 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 957 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy611 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 958 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy612 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 959 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy613 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 960 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy614 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 961 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy615 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 962 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy616 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 963 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy617 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 964 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy618 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 965 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy619 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 966 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy620 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 967 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy621 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 968 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy622 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 969 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy623 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 970 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy624 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 971 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy625 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 972 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy626 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 973 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy627 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 974 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy628 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 975 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy629 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 976 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy630 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 977 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy631 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 978 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy632 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 979 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy633 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 980 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy634 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 981 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy635 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 982 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy636 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 983 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy637 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 984 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy638 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 985 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy639 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 986 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy640 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 987 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy641 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 988 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy642 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 989 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy643 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 990 Int Point 1 in ELSET SET-FCC', 
    steps=('Step-1', ), suppressQuery=True)
xy644 = avg((xy0, xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, 
    xy12, xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, 
    xy24, xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, 
    xy36, xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, 
    xy48, xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, 
    xy60, xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, 
    xy72, xy73, xy74, xy75, xy76, xy77, xy78, xy79, xy80, xy81, xy82, xy83, 
    xy84, xy85, xy86, xy87, xy88, xy89, xy90, xy91, xy92, xy93, xy94, xy95, 
    xy96, xy97, xy98, xy99, xy100, xy101, xy102, xy103, xy104, xy105, xy106, 
    xy107, xy108, xy109, xy110, xy111, xy112, xy113, xy114, xy115, xy116, 
    xy117, xy118, xy119, xy120, xy121, xy122, xy123, xy124, xy125, xy126, 
    xy127, xy128, xy129, xy130, xy131, xy132, xy133, xy134, xy135, xy136, 
    xy137, xy138, xy139, xy140, xy141, xy142, xy143, xy144, xy145, xy146, 
    xy147, xy148, xy149, xy150, xy151, xy152, xy153, xy154, xy155, xy156, 
    xy157, xy158, xy159, xy160, xy161, xy162, xy163, xy164, xy165, xy166, 
    xy167, xy168, xy169, xy170, xy171, xy172, xy173, xy174, xy175, xy176, 
    xy177, xy178, xy179, xy180, xy181, xy182, xy183, xy184, xy185, xy186, 
    xy187, xy188, xy189, xy190, xy191, xy192, xy193, xy194, xy195, xy196, 
    xy197, xy198, xy199, xy200, xy201, xy202, xy203, xy204, xy205, xy206, 
    xy207, xy208, xy209, xy210, xy211, xy212, xy213, xy214, xy215, xy216, 
    xy217, xy218, xy219, xy220, xy221, xy222, xy223, xy224, xy225, xy226, 
    xy227, xy228, xy229, xy230, xy231, xy232, xy233, xy234, xy235, xy236, 
    xy237, xy238, xy239, xy240, xy241, xy242, xy243, xy244, xy245, xy246, 
    xy247, xy248, xy249, xy250, xy251, xy252, xy253, xy254, xy255, xy256, 
    xy257, xy258, xy259, xy260, xy261, xy262, xy263, xy264, xy265, xy266, 
    xy267, xy268, xy269, xy270, xy271, xy272, xy273, xy274, xy275, xy276, 
    xy277, xy278, xy279, xy280, xy281, xy282, xy283, xy284, xy285, xy286, 
    xy287, xy288, xy289, xy290, xy291, xy292, xy293, xy294, xy295, xy296, 
    xy297, xy298, xy299, xy300, xy301, xy302, xy303, xy304, xy305, xy306, 
    xy307, xy308, xy309, xy310, xy311, xy312, xy313, xy314, xy315, xy316, 
    xy317, xy318, xy319, xy320, xy321, xy322, xy323, xy324, xy325, xy326, 
    xy327, xy328, xy329, xy330, xy331, xy332, xy333, xy334, xy335, xy336, 
    xy337, xy338, xy339, xy340, xy341, xy342, xy343, xy344, xy345, xy346, 
    xy347, xy348, xy349, xy350, xy351, xy352, xy353, xy354, xy355, xy356, 
    xy357, xy358, xy359, xy360, xy361, xy362, xy363, xy364, xy365, xy366, 
    xy367, xy368, xy369, xy370, xy371, xy372, xy373, xy374, xy375, xy376, 
    xy377, xy378, xy379, xy380, xy381, xy382, xy383, xy384, xy385, xy386, 
    xy387, xy388, xy389, xy390, xy391, xy392, xy393, xy394, xy395, xy396, 
    xy397, xy398, xy399, xy400, xy401, xy402, xy403, xy404, xy405, xy406, 
    xy407, xy408, xy409, xy410, xy411, xy412, xy413, xy414, xy415, xy416, 
    xy417, xy418, xy419, xy420, xy421, xy422, xy423, xy424, xy425, xy426, 
    xy427, xy428, xy429, xy430, xy431, xy432, xy433, xy434, xy435, xy436, 
    xy437, xy438, xy439, xy440, xy441, xy442, xy443, xy444, xy445, xy446, 
    xy447, xy448, xy449, xy450, xy451, xy452, xy453, xy454, xy455, xy456, 
    xy457, xy458, xy459, xy460, xy461, xy462, xy463, xy464, xy465, xy466, 
    xy467, xy468, xy469, xy470, xy471, xy472, xy473, xy474, xy475, xy476, 
    xy477, xy478, xy479, xy480, xy481, xy482, xy483, xy484, xy485, xy486, 
    xy487, xy488, xy489, xy490, xy491, xy492, xy493, xy494, xy495, xy496, 
    xy497, xy498, xy499, xy500, xy501, xy502, xy503, xy504, xy505, xy506, 
    xy507, xy508, xy509, xy510, xy511, xy512, xy513, xy514, xy515, xy516, 
    xy517, xy518, xy519, xy520, xy521, xy522, xy523, xy524, xy525, xy526, 
    xy527, xy528, xy529, xy530, xy531, xy532, xy533, xy534, xy535, xy536, 
    xy537, xy538, xy539, xy540, xy541, xy542, xy543, xy544, xy545, xy546, 
    xy547, xy548, xy549, xy550, xy551, xy552, xy553, xy554, xy555, xy556, 
    xy557, xy558, xy559, xy560, xy561, xy562, xy563, xy564, xy565, xy566, 
    xy567, xy568, xy569, xy570, xy571, xy572, xy573, xy574, xy575, xy576, 
    xy577, xy578, xy579, xy580, xy581, xy582, xy583, xy584, xy585, xy586, 
    xy587, xy588, xy589, xy590, xy591, xy592, xy593, xy594, xy595, xy596, 
    xy597, xy598, xy599, xy600, xy601, xy602, xy603, xy604, xy605, xy606, 
    xy607, xy608, xy609, xy610, xy611, xy612, xy613, xy614, xy615, xy616, 
    xy617, xy618, xy619, xy620, xy621, xy622, xy623, xy624, xy625, xy626, 
    xy627, xy628, xy629, xy630, xy631, xy632, xy633, xy634, xy635, xy636, 
    xy637, xy638, xy639, xy640, xy641, xy642, xy643, ), )
xy_result = session.XYData(name='FCC-1', objectToCopy=xy644, 
    sourceDescription='avg((Stress components: S11 at Element 1 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 2 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 3 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 4 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 5 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 6 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 7 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 8 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 9 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 10 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 11 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 12 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 13 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 14 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 15 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 16 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 17 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 18 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 19 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 20 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 21 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 22 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 23 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 24 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 25 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 26 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 27 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 28 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 29 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 30 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 31 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 32 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 33 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 34 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 35 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 36 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 37 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 38 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 39 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 40 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 41 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 42 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 43 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 44 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 45 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 46 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 47 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 48 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 49 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 50 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 51 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 52 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 53 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 54 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 55 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 56 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 57 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 58 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 59 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 60 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 61 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 62 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 63 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 64 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 65 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 66 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 67 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 68 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 69 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 70 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 71 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 72 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 73 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 74 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 75 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 76 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 77 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 78 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 79 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 80 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 81 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 82 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 83 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 84 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 85 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 86 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 87 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 88 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 89 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 90 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 91 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 92 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 93 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 94 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 95 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 96 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 97 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 98 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 99 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 100 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 101 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 102 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 103 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 104 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 105 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 106 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 107 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 108 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 109 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 110 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 111 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 112 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 113 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 114 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 115 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 116 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 117 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 118 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 119 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 120 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 121 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 122 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 123 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 124 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 125 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 126 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 127 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 128 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 129 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 130 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 131 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 132 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 133 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 134 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 135 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 136 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 137 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 138 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 139 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 140 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 141 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 142 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 143 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 144 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 145 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 146 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 147 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 148 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 149 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 150 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 151 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 152 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 153 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 154 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 155 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 156 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 157 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 158 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 159 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 160 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 161 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 162 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 163 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 164 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 165 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 166 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 167 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 168 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 169 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 170 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 171 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 172 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 173 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 174 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 175 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 176 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 177 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 178 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 179 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 180 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 181 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 182 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 183 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 184 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 185 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 186 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 187 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 188 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 189 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 190 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 191 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 192 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 193 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 194 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 195 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 196 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 197 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 198 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 199 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 200 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 201 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 202 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 203 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 204 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 205 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 206 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 207 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 208 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 209 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 210 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 211 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 212 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 213 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 214 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 215 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 216 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 217 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 218 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 219 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 220 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 221 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 222 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 223 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 224 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 225 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 226 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 227 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 228 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 229 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 230 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 231 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 232 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 233 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 234 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 235 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 236 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 237 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 238 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 239 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 240 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 241 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 242 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 243 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 244 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 245 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 246 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 247 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 248 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 249 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 250 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 251 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 252 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 253 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 254 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 255 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 256 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 257 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 258 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 259 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 260 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 261 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 262 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 263 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 264 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 265 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 266 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 267 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 268 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 269 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 270 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 271 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 272 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 273 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 274 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 275 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 276 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 277 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 278 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 279 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 280 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 281 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 282 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 283 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 284 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 285 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 286 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 287 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 288 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 289 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 290 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 291 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 292 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 293 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 294 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 295 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 296 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 297 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 298 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 299 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 300 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 301 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 302 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 303 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 304 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 305 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 306 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 307 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 308 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 309 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 310 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 311 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 312 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 313 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 314 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 315 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 316 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 317 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 318 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 319 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 320 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 321 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 322 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 323 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 324 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 325 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 326 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 327 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 328 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 329 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 330 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 331 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 332 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 333 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 334 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 335 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 336 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 337 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 338 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 339 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 340 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 341 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 342 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 343 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 344 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 345 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 346 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 347 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 348 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 349 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 350 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 351 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 352 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 353 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 354 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 355 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 356 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 357 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 358 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 359 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 360 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 541 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 542 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 543 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 544 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 545 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 546 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 547 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 548 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 549 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 550 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 551 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 552 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 553 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 554 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 555 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 556 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 557 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 558 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 559 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 560 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 561 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 562 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 563 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 564 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 565 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 566 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 567 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 568 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 569 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 570 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 571 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 572 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 573 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 574 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 575 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 576 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 577 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 578 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 579 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 580 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 581 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 582 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 583 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 584 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 585 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 586 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 587 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 588 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 589 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 590 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 591 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 592 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 593 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 594 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 595 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 596 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 597 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 598 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 599 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 600 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 601 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 602 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 603 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 604 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 605 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 606 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 607 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 608 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 609 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 610 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 611 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 612 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 613 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 614 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 615 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 616 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 617 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 618 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 619 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 620 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 621 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 622 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 623 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 624 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 625 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 626 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 627 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 628 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 629 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 630 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 631 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 632 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 633 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 634 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 635 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 636 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 637 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 638 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 639 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 640 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 641 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 642 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 643 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 644 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 645 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 646 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 647 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 648 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 649 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 650 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 651 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 652 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 653 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 654 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 655 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 656 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 657 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 658 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 659 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 660 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 661 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 662 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 663 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 664 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 665 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 666 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 667 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 668 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 669 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 670 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 671 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 672 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 673 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 674 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 675 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 676 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 677 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 678 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 679 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 680 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 681 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 682 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 683 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 684 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 685 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 686 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 687 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 688 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 689 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 690 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 857 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 858 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 859 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 860 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 861 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 862 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 863 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 864 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 865 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 866 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 867 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 868 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 869 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 870 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 871 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 872 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 873 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 874 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 875 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 876 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 877 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 878 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 879 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 880 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 881 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 882 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 883 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 884 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 885 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 886 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 887 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 888 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 889 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 890 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 891 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 892 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 893 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 894 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 895 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 896 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 897 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 898 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 899 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 900 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 901 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 902 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 903 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 904 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 905 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 906 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 907 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 908 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 909 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 910 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 911 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 912 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 913 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 914 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 915 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 916 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 917 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 918 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 919 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 920 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 921 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 922 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 923 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 924 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 925 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 926 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 927 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 928 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 929 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 930 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 931 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 932 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 933 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 934 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 935 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 936 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 937 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 938 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 939 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 940 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 941 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 942 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 943 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 944 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 945 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 946 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 947 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 948 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 949 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 950 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 951 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 952 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 953 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 954 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 955 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 956 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 957 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 958 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 959 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 960 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 961 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 962 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 963 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 964 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 965 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 966 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 967 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 968 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 969 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 970 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 971 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 972 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 973 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 974 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 975 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 976 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 977 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 978 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 979 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 980 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 981 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 982 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 983 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 984 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 985 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 986 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 987 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 988 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 989 Int Point 1 in ELSET SET-FCC, Stress components: S11 at Element 990 Int Point 1 in ELSET SET-FCC, ),)')
c1 = session.Curve(xyData=xy_result)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
odb = session.odbs['/home/yzhang951/AlHEA/response/lam/Job-1.odb']
xy0 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 361 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy1 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 362 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy2 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 363 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy3 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 364 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy4 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 365 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy5 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 366 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy6 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 367 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy7 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 368 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy8 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 369 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy9 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 370 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy10 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 371 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy11 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 372 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy12 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 373 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy13 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 374 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy14 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 375 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy15 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 376 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy16 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 377 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy17 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 378 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy18 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 379 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy19 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 380 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy20 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 381 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy21 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 382 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy22 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 383 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy23 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 384 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy24 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 385 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy25 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 386 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy26 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 387 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy27 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 388 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy28 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 389 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy29 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 390 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy30 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 391 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy31 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 392 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy32 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 393 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy33 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 394 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy34 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 395 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy35 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 396 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy36 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 397 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy37 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 398 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy38 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 399 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy39 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 400 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy40 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 401 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy41 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 402 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy42 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 403 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy43 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 404 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy44 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 405 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy45 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 406 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy46 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 407 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy47 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 408 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy48 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 409 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy49 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 410 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy50 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 411 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy51 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 412 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy52 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 413 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy53 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 414 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy54 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 415 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy55 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 416 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy56 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 417 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy57 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 418 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy58 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 419 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy59 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 420 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy60 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 421 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy61 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 422 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy62 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 423 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy63 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 424 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy64 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 425 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy65 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 426 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy66 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 427 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy67 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 428 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy68 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 429 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy69 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 430 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy70 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 431 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy71 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 432 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy72 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 433 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy73 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 434 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy74 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 435 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy75 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 436 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy76 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 437 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy77 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 438 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy78 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 439 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy79 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 440 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy80 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 441 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy81 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 442 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy82 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 443 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy83 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 444 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy84 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 445 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy85 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 446 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy86 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 447 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy87 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 448 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy88 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 449 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy89 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 450 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy90 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 451 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy91 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 452 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy92 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 453 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy93 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 454 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy94 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 455 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy95 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 456 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy96 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 457 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy97 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 458 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy98 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 459 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy99 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 460 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy100 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 461 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy101 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 462 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy102 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 463 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy103 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 464 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy104 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 465 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy105 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 466 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy106 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 467 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy107 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 468 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy108 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 469 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy109 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 470 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy110 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 471 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy111 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 472 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy112 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 473 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy113 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 474 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy114 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 475 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy115 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 476 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy116 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 477 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy117 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 478 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy118 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 479 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy119 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 480 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy120 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 481 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy121 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 482 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy122 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 483 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy123 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 484 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy124 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 485 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy125 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 486 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy126 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 487 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy127 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 488 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy128 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 489 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy129 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 490 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy130 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 491 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy131 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 492 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy132 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 493 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy133 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 494 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy134 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 495 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy135 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 496 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy136 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 497 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy137 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 498 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy138 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 499 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy139 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 500 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy140 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 501 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy141 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 502 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy142 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 503 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy143 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 504 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy144 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 505 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy145 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 506 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy146 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 507 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy147 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 508 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy148 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 509 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy149 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 510 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy150 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 511 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy151 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 512 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy152 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 513 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy153 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 514 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy154 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 515 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy155 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 516 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy156 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 517 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy157 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 518 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy158 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 519 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy159 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 520 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy160 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 521 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy161 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 522 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy162 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 523 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy163 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 524 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy164 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 525 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy165 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 526 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy166 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 527 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy167 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 528 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy168 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 529 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy169 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 530 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy170 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 531 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy171 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 532 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy172 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 533 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy173 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 534 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy174 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 535 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy175 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 536 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy176 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 537 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy177 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 538 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy178 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 539 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy179 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 540 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy180 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 691 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy181 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 692 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy182 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 693 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy183 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 694 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy184 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 695 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy185 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 696 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy186 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 697 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy187 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 698 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy188 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 699 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy189 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 700 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy190 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 701 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy191 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 702 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy192 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 703 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy193 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 704 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy194 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 705 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy195 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 706 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy196 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 707 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy197 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 708 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy198 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 709 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy199 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 710 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy200 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 711 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy201 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 712 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy202 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 713 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy203 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 714 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy204 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 715 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy205 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 716 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy206 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 717 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy207 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 718 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy208 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 719 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy209 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 720 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy210 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 721 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy211 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 722 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy212 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 723 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy213 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 724 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy214 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 725 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy215 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 726 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy216 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 727 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy217 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 728 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy218 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 729 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy219 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 730 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy220 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 731 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy221 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 732 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy222 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 733 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy223 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 734 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy224 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 735 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy225 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 736 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy226 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 737 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy227 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 738 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy228 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 739 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy229 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 740 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy230 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 741 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy231 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 742 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy232 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 743 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy233 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 744 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy234 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 745 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy235 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 746 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy236 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 747 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy237 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 748 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy238 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 749 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy239 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 750 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy240 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 751 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy241 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 752 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy242 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 753 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy243 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 754 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy244 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 755 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy245 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 756 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy246 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 757 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy247 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 758 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy248 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 759 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy249 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 760 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy250 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 761 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy251 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 762 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy252 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 763 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy253 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 764 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy254 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 765 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy255 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 766 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy256 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 767 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy257 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 768 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy258 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 769 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy259 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 770 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy260 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 771 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy261 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 772 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy262 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 773 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy263 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 774 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy264 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 775 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy265 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 776 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy266 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 777 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy267 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 778 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy268 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 779 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy269 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 780 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy270 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 781 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy271 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 782 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy272 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 783 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy273 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 784 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy274 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 785 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy275 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 786 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy276 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 787 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy277 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 788 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy278 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 789 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy279 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 790 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy280 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 791 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy281 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 792 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy282 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 793 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy283 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 794 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy284 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 795 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy285 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 796 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy286 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 797 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy287 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 798 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy288 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 799 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy289 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 800 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy290 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 801 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy291 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 802 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy292 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 803 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy293 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 804 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy294 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 805 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy295 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 806 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy296 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 807 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy297 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 808 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy298 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 809 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy299 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 810 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy300 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 811 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy301 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 812 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy302 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 813 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy303 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 814 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy304 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 815 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy305 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 816 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy306 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 817 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy307 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 818 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy308 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 819 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy309 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 820 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy310 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 821 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy311 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 822 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy312 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 823 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy313 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 824 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy314 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 825 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy315 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 826 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy316 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 827 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy317 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 828 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy318 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 829 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy319 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 830 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy320 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 831 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy321 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 832 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy322 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 833 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy323 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 834 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy324 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 835 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy325 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 836 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy326 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 837 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy327 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 838 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy328 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 839 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy329 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 840 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy330 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 841 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy331 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 842 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy332 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 843 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy333 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 844 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy334 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 845 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy335 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 846 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy336 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 847 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy337 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 848 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy338 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 849 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy339 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 850 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy340 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 851 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy341 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 852 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy342 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 853 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy343 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 854 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy344 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 855 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy345 = xyPlot.XYDataFromHistory(odb=odb, 
    outputVariableName='Stress components: S11 at Element 856 Int Point 1 in ELSET SET-BCC', 
    steps=('Step-1', ), suppressQuery=True)
xy346 = avg((xy0, xy1, xy2, xy3, xy4, xy5, xy6, xy7, xy8, xy9, xy10, xy11, 
    xy12, xy13, xy14, xy15, xy16, xy17, xy18, xy19, xy20, xy21, xy22, xy23, 
    xy24, xy25, xy26, xy27, xy28, xy29, xy30, xy31, xy32, xy33, xy34, xy35, 
    xy36, xy37, xy38, xy39, xy40, xy41, xy42, xy43, xy44, xy45, xy46, xy47, 
    xy48, xy49, xy50, xy51, xy52, xy53, xy54, xy55, xy56, xy57, xy58, xy59, 
    xy60, xy61, xy62, xy63, xy64, xy65, xy66, xy67, xy68, xy69, xy70, xy71, 
    xy72, xy73, xy74, xy75, xy76, xy77, xy78, xy79, xy80, xy81, xy82, xy83, 
    xy84, xy85, xy86, xy87, xy88, xy89, xy90, xy91, xy92, xy93, xy94, xy95, 
    xy96, xy97, xy98, xy99, xy100, xy101, xy102, xy103, xy104, xy105, xy106, 
    xy107, xy108, xy109, xy110, xy111, xy112, xy113, xy114, xy115, xy116, 
    xy117, xy118, xy119, xy120, xy121, xy122, xy123, xy124, xy125, xy126, 
    xy127, xy128, xy129, xy130, xy131, xy132, xy133, xy134, xy135, xy136, 
    xy137, xy138, xy139, xy140, xy141, xy142, xy143, xy144, xy145, xy146, 
    xy147, xy148, xy149, xy150, xy151, xy152, xy153, xy154, xy155, xy156, 
    xy157, xy158, xy159, xy160, xy161, xy162, xy163, xy164, xy165, xy166, 
    xy167, xy168, xy169, xy170, xy171, xy172, xy173, xy174, xy175, xy176, 
    xy177, xy178, xy179, xy180, xy181, xy182, xy183, xy184, xy185, xy186, 
    xy187, xy188, xy189, xy190, xy191, xy192, xy193, xy194, xy195, xy196, 
    xy197, xy198, xy199, xy200, xy201, xy202, xy203, xy204, xy205, xy206, 
    xy207, xy208, xy209, xy210, xy211, xy212, xy213, xy214, xy215, xy216, 
    xy217, xy218, xy219, xy220, xy221, xy222, xy223, xy224, xy225, xy226, 
    xy227, xy228, xy229, xy230, xy231, xy232, xy233, xy234, xy235, xy236, 
    xy237, xy238, xy239, xy240, xy241, xy242, xy243, xy244, xy245, xy246, 
    xy247, xy248, xy249, xy250, xy251, xy252, xy253, xy254, xy255, xy256, 
    xy257, xy258, xy259, xy260, xy261, xy262, xy263, xy264, xy265, xy266, 
    xy267, xy268, xy269, xy270, xy271, xy272, xy273, xy274, xy275, xy276, 
    xy277, xy278, xy279, xy280, xy281, xy282, xy283, xy284, xy285, xy286, 
    xy287, xy288, xy289, xy290, xy291, xy292, xy293, xy294, xy295, xy296, 
    xy297, xy298, xy299, xy300, xy301, xy302, xy303, xy304, xy305, xy306, 
    xy307, xy308, xy309, xy310, xy311, xy312, xy313, xy314, xy315, xy316, 
    xy317, xy318, xy319, xy320, xy321, xy322, xy323, xy324, xy325, xy326, 
    xy327, xy328, xy329, xy330, xy331, xy332, xy333, xy334, xy335, xy336, 
    xy337, xy338, xy339, xy340, xy341, xy342, xy343, xy344, xy345, ), )
xy_result = session.XYData(name='BCC-1', objectToCopy=xy346, 
    sourceDescription='avg((Stress components: S11 at Element 361 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 362 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 363 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 364 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 365 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 366 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 367 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 368 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 369 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 370 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 371 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 372 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 373 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 374 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 375 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 376 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 377 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 378 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 379 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 380 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 381 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 382 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 383 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 384 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 385 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 386 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 387 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 388 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 389 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 390 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 391 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 392 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 393 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 394 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 395 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 396 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 397 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 398 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 399 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 400 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 401 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 402 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 403 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 404 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 405 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 406 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 407 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 408 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 409 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 410 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 411 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 412 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 413 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 414 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 415 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 416 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 417 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 418 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 419 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 420 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 421 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 422 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 423 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 424 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 425 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 426 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 427 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 428 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 429 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 430 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 431 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 432 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 433 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 434 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 435 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 436 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 437 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 438 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 439 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 440 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 441 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 442 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 443 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 444 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 445 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 446 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 447 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 448 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 449 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 450 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 451 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 452 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 453 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 454 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 455 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 456 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 457 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 458 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 459 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 460 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 461 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 462 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 463 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 464 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 465 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 466 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 467 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 468 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 469 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 470 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 471 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 472 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 473 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 474 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 475 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 476 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 477 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 478 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 479 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 480 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 481 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 482 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 483 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 484 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 485 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 486 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 487 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 488 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 489 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 490 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 491 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 492 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 493 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 494 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 495 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 496 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 497 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 498 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 499 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 500 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 501 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 502 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 503 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 504 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 505 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 506 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 507 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 508 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 509 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 510 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 511 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 512 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 513 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 514 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 515 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 516 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 517 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 518 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 519 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 520 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 521 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 522 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 523 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 524 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 525 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 526 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 527 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 528 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 529 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 530 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 531 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 532 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 533 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 534 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 535 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 536 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 537 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 538 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 539 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 540 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 691 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 692 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 693 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 694 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 695 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 696 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 697 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 698 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 699 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 700 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 701 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 702 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 703 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 704 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 705 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 706 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 707 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 708 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 709 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 710 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 711 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 712 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 713 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 714 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 715 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 716 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 717 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 718 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 719 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 720 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 721 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 722 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 723 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 724 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 725 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 726 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 727 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 728 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 729 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 730 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 731 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 732 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 733 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 734 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 735 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 736 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 737 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 738 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 739 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 740 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 741 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 742 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 743 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 744 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 745 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 746 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 747 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 748 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 749 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 750 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 751 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 752 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 753 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 754 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 755 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 756 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 757 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 758 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 759 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 760 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 761 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 762 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 763 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 764 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 765 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 766 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 767 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 768 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 769 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 770 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 771 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 772 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 773 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 774 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 775 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 776 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 777 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 778 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 779 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 780 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 781 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 782 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 783 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 784 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 785 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 786 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 787 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 788 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 789 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 790 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 791 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 792 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 793 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 794 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 795 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 796 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 797 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 798 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 799 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 800 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 801 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 802 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 803 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 804 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 805 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 806 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 807 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 808 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 809 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 810 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 811 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 812 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 813 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 814 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 815 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 816 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 817 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 818 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 819 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 820 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 821 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 822 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 823 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 824 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 825 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 826 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 827 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 828 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 829 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 830 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 831 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 832 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 833 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 834 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 835 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 836 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 837 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 838 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 839 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 840 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 841 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 842 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 843 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 844 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 845 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 846 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 847 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 848 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 849 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 850 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 851 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 852 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 853 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 854 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 855 Int Point 1 in ELSET SET-BCC, Stress components: S11 at Element 856 Int Point 1 in ELSET SET-BCC, ),)')
c1 = session.Curve(xyData=xy_result)
xyp = session.xyPlots['XYPlot-1']
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
x0 = session.xyDataObjects['BCC-1']
x1 = session.xyDataObjects['FCC-1']
session.writeXYReport(fileName='lam_ph.rpt', appendMode=OFF, xyData=(x0, x1))