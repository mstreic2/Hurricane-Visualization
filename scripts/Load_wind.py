# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Image Reader'
wf01raw = ImageReader(registrationName='Wf01.raw*', FileNames=['C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf01.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf02.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf03.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf04.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf05.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf06.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf07.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf08.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf09.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf10.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf11.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf12.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf13.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf14.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf15.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf16.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf17.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf18.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf19.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf20.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf21.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf22.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf23.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf24.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf25.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf26.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf27.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf28.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf29.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf30.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf31.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf32.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf33.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf34.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf35.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf36.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf37.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf38.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf39.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf40.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf41.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf42.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf43.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf44.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf45.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf46.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf47.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Wf48.raw'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'Image Reader'
vf01raw = ImageReader(registrationName='Vf01.raw*', FileNames=['C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf01.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf02.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf03.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf04.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf05.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf06.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf07.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf08.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf09.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf10.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf11.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf12.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf13.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf14.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf15.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf16.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf17.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf18.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf19.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf20.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf21.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf22.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf23.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf24.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf25.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf26.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf27.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf28.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf29.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf30.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf31.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf32.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf33.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf34.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf35.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf36.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf37.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf38.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf39.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf40.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf41.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf42.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf43.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf44.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf45.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf46.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf47.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Vf48.raw'])

# create a new 'Image Reader'
uf01raw = ImageReader(registrationName='Uf01.raw*', FileNames=['C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf01.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf02.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf03.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf04.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf05.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf06.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf07.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf08.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf09.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf10.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf11.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf12.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf13.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf14.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf15.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf16.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf17.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf18.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf19.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf20.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf21.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf22.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf23.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf24.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf25.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf26.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf27.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf28.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf29.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf30.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf31.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf32.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf33.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf34.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf35.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf36.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf37.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf38.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf39.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf40.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf41.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf42.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf43.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf44.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf45.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf46.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf47.raw', 'C:\\Users\\Matth\\Documents\\Spring2023\\CS5635\\Final-Project\\hurricane_data_sets\\Isabel_data\\raw\\Uf48.raw'])

# set active source
SetActiveSource(vf01raw)

# set active source
SetActiveSource(uf01raw)

# set active source
SetActiveSource(vf01raw)

# set active source
SetActiveSource(wf01raw)

# Properties modified on wf01raw
wf01raw.DataScalarType = 'float'
wf01raw.DataExtent = [0, 499, 0, 499, 0, 99]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
wf01rawDisplay = Show(wf01raw, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
wf01rawDisplay.Representation = 'Outline'
wf01rawDisplay.ColorArrayName = ['POINTS', '']
wf01rawDisplay.SelectTCoordArray = 'None'
wf01rawDisplay.SelectNormalArray = 'None'
wf01rawDisplay.SelectTangentArray = 'None'
wf01rawDisplay.OSPRayScaleArray = 'ImageFile'
wf01rawDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
wf01rawDisplay.SelectOrientationVectors = 'None'
wf01rawDisplay.ScaleFactor = 49.900000000000006
wf01rawDisplay.SelectScaleArray = 'ImageFile'
wf01rawDisplay.GlyphType = 'Arrow'
wf01rawDisplay.GlyphTableIndexArray = 'ImageFile'
wf01rawDisplay.GaussianRadius = 2.495
wf01rawDisplay.SetScaleArray = ['POINTS', 'ImageFile']
wf01rawDisplay.ScaleTransferFunction = 'PiecewiseFunction'
wf01rawDisplay.OpacityArray = ['POINTS', 'ImageFile']
wf01rawDisplay.OpacityTransferFunction = 'PiecewiseFunction'
wf01rawDisplay.DataAxesGrid = 'GridAxesRepresentation'
wf01rawDisplay.PolarAxes = 'PolarAxesRepresentation'
wf01rawDisplay.ScalarOpacityUnitDistance = 2.4485118066882516
wf01rawDisplay.OpacityArrayName = ['POINTS', 'ImageFile']
wf01rawDisplay.ColorArray2Name = ['POINTS', 'ImageFile']
wf01rawDisplay.IsosurfaceValues = [5.000000204592394e+34]
wf01rawDisplay.SliceFunction = 'Plane'
wf01rawDisplay.Slice = 49
wf01rawDisplay.SelectInputVectors = [None, '']
wf01rawDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
wf01rawDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2884.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
wf01rawDisplay.ScaleTransferFunction.Points = [-0.9479222297668457, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
wf01rawDisplay.OpacityTransferFunction.Points = [-0.9479222297668457, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
wf01rawDisplay.SliceFunction.Origin = [249.5, 249.5, 49.5]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Properties modified on vf01raw
vf01raw.DataScalarType = 'float'
vf01raw.DataExtent = [0, 499, 0, 499, 0, 99]

# show data in view
vf01rawDisplay = Show(vf01raw, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
vf01rawDisplay.Representation = 'Outline'
vf01rawDisplay.ColorArrayName = ['POINTS', '']
vf01rawDisplay.SelectTCoordArray = 'None'
vf01rawDisplay.SelectNormalArray = 'None'
vf01rawDisplay.SelectTangentArray = 'None'
vf01rawDisplay.OSPRayScaleArray = 'ImageFile'
vf01rawDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
vf01rawDisplay.SelectOrientationVectors = 'None'
vf01rawDisplay.ScaleFactor = 49.900000000000006
vf01rawDisplay.SelectScaleArray = 'ImageFile'
vf01rawDisplay.GlyphType = 'Arrow'
vf01rawDisplay.GlyphTableIndexArray = 'ImageFile'
vf01rawDisplay.GaussianRadius = 2.495
vf01rawDisplay.SetScaleArray = ['POINTS', 'ImageFile']
vf01rawDisplay.ScaleTransferFunction = 'PiecewiseFunction'
vf01rawDisplay.OpacityArray = ['POINTS', 'ImageFile']
vf01rawDisplay.OpacityTransferFunction = 'PiecewiseFunction'
vf01rawDisplay.DataAxesGrid = 'GridAxesRepresentation'
vf01rawDisplay.PolarAxes = 'PolarAxesRepresentation'
vf01rawDisplay.ScalarOpacityUnitDistance = 2.4485118066882516
vf01rawDisplay.OpacityArrayName = ['POINTS', 'ImageFile']
vf01rawDisplay.ColorArray2Name = ['POINTS', 'ImageFile']
vf01rawDisplay.IsosurfaceValues = [5.000000204592394e+34]
vf01rawDisplay.SliceFunction = 'Plane'
vf01rawDisplay.Slice = 49
vf01rawDisplay.SelectInputVectors = [None, '']
vf01rawDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
vf01rawDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2884.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
vf01rawDisplay.ScaleTransferFunction.Points = [-52.00224304199219, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
vf01rawDisplay.OpacityTransferFunction.Points = [-52.00224304199219, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
vf01rawDisplay.SliceFunction.Origin = [249.5, 249.5, 49.5]

# Properties modified on uf01raw
uf01raw.DataScalarType = 'float'
uf01raw.DataExtent = [0, 499, 0, 499, 0, 99]

# show data in view
uf01rawDisplay = Show(uf01raw, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
uf01rawDisplay.Representation = 'Outline'
uf01rawDisplay.ColorArrayName = ['POINTS', '']
uf01rawDisplay.SelectTCoordArray = 'None'
uf01rawDisplay.SelectNormalArray = 'None'
uf01rawDisplay.SelectTangentArray = 'None'
uf01rawDisplay.OSPRayScaleArray = 'ImageFile'
uf01rawDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
uf01rawDisplay.SelectOrientationVectors = 'None'
uf01rawDisplay.ScaleFactor = 49.900000000000006
uf01rawDisplay.SelectScaleArray = 'ImageFile'
uf01rawDisplay.GlyphType = 'Arrow'
uf01rawDisplay.GlyphTableIndexArray = 'ImageFile'
uf01rawDisplay.GaussianRadius = 2.495
uf01rawDisplay.SetScaleArray = ['POINTS', 'ImageFile']
uf01rawDisplay.ScaleTransferFunction = 'PiecewiseFunction'
uf01rawDisplay.OpacityArray = ['POINTS', 'ImageFile']
uf01rawDisplay.OpacityTransferFunction = 'PiecewiseFunction'
uf01rawDisplay.DataAxesGrid = 'GridAxesRepresentation'
uf01rawDisplay.PolarAxes = 'PolarAxesRepresentation'
uf01rawDisplay.ScalarOpacityUnitDistance = 2.4485118066882516
uf01rawDisplay.OpacityArrayName = ['POINTS', 'ImageFile']
uf01rawDisplay.ColorArray2Name = ['POINTS', 'ImageFile']
uf01rawDisplay.IsosurfaceValues = [5.000000204592394e+34]
uf01rawDisplay.SliceFunction = 'Plane'
uf01rawDisplay.Slice = 49
uf01rawDisplay.SelectInputVectors = [None, '']
uf01rawDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
uf01rawDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2884.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
uf01rawDisplay.ScaleTransferFunction.Points = [-56.66746520996094, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
uf01rawDisplay.OpacityTransferFunction.Points = [-56.66746520996094, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
uf01rawDisplay.SliceFunction.Origin = [249.5, 249.5, 49.5]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(vf01raw)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=vf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=vf01rawDisplay)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=vf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=vf01rawDisplay)

# set active source
SetActiveSource(uf01raw)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=uf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=uf01rawDisplay)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=uf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=uf01rawDisplay)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[wf01raw, vf01raw, uf01raw])

# show data in view
appendAttributes1Display = Show(appendAttributes1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
appendAttributes1Display.Representation = 'Outline'
appendAttributes1Display.ColorArrayName = ['POINTS', '']
appendAttributes1Display.SelectTCoordArray = 'None'
appendAttributes1Display.SelectNormalArray = 'None'
appendAttributes1Display.SelectTangentArray = 'None'
appendAttributes1Display.OSPRayScaleArray = 'ImageFile'
appendAttributes1Display.OSPRayScaleFunction = 'PiecewiseFunction'
appendAttributes1Display.SelectOrientationVectors = 'None'
appendAttributes1Display.ScaleFactor = 49.900000000000006
appendAttributes1Display.SelectScaleArray = 'ImageFile'
appendAttributes1Display.GlyphType = 'Arrow'
appendAttributes1Display.GlyphTableIndexArray = 'ImageFile'
appendAttributes1Display.GaussianRadius = 2.495
appendAttributes1Display.SetScaleArray = ['POINTS', 'ImageFile']
appendAttributes1Display.ScaleTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.OpacityArray = ['POINTS', 'ImageFile']
appendAttributes1Display.OpacityTransferFunction = 'PiecewiseFunction'
appendAttributes1Display.DataAxesGrid = 'GridAxesRepresentation'
appendAttributes1Display.PolarAxes = 'PolarAxesRepresentation'
appendAttributes1Display.ScalarOpacityUnitDistance = 2.4485118066882516
appendAttributes1Display.OpacityArrayName = ['POINTS', 'ImageFile']
appendAttributes1Display.ColorArray2Name = ['POINTS', 'ImageFile']
appendAttributes1Display.IsosurfaceValues = [5.000000204592394e+34]
appendAttributes1Display.SliceFunction = 'Plane'
appendAttributes1Display.Slice = 49
appendAttributes1Display.SelectInputVectors = [None, '']
appendAttributes1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
appendAttributes1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2884.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
appendAttributes1Display.ScaleTransferFunction.Points = [-0.9479222297668457, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
appendAttributes1Display.OpacityTransferFunction.Points = [-0.9479222297668457, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
appendAttributes1Display.SliceFunction.Origin = [249.5, 249.5, 49.5]

# hide data in view
Hide(uf01raw, renderView1)

# hide data in view
Hide(vf01raw, renderView1)

# hide data in view
Hide(wf01raw, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(wf01raw)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=wf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=wf01rawDisplay)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=wf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=wf01rawDisplay)

# Properties modified on wf01raw
wf01raw.ScalarArrayName = 'z'

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(vf01raw)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=vf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=vf01rawDisplay)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=vf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=vf01rawDisplay)

# Properties modified on vf01raw
vf01raw.ScalarArrayName = 'y'

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(uf01raw)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=uf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=uf01rawDisplay)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=uf01rawDisplay.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=uf01rawDisplay)

# Properties modified on uf01raw
uf01raw.ScalarArrayName = 'x'

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(appendAttributes1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=appendAttributes1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=appendAttributes1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=appendAttributes1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=appendAttributes1Display)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=appendAttributes1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'wind'
calculator1.Function = 'x*iHat+y*jHat+z*kHat'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Outline'
calculator1Display.ColorArrayName = ['POINTS', '']
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'z'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'wind'
calculator1Display.ScaleFactor = 49.900000000000006
calculator1Display.SelectScaleArray = 'z'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'z'
calculator1Display.GaussianRadius = 2.495
calculator1Display.SetScaleArray = ['POINTS', 'z']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'z']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 2.4485118066882516
calculator1Display.OpacityArrayName = ['POINTS', 'z']
calculator1Display.ColorArray2Name = ['POINTS', 'z']
calculator1Display.IsosurfaceValues = [5.000000204592394e+34]
calculator1Display.SliceFunction = 'Plane'
calculator1Display.Slice = 49
calculator1Display.SelectInputVectors = ['POINTS', 'wind']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2884.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [-0.9479222297668457, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [-0.9479222297668457, 0.0, 0.5, 0.0, 1.0000000409184788e+35, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
calculator1Display.SliceFunction.Origin = [249.5, 249.5, 49.5]

# hide data in view
Hide(appendAttributes1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1574, 902)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [249.5, 249.5, 1426.1432349145146]
renderView1.CameraFocalPoint = [249.5, 249.5, 49.5]
renderView1.CameraParallelScale = 356.3014875074198

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).