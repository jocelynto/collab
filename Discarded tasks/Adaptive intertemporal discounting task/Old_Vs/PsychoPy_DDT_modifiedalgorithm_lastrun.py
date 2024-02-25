#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), Tue Nov 11 15:45:16 2014
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'PsychoPy_DDT_modifiedalgorithm'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT/PsychoPy_DDT_modifiedalgorithm.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(2560, 1440), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
fixation = visual.ImageStim(win=win, name='fixation',
    image='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT/stimuli/start.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
bg_stim = visual.ImageStim(win=win, name='bg_stim',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ll_stim = visual.TextStim(win=win, ori=0, name='ll_stim',
    text='default text',    font='Arial',
    pos=[270,37], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
ss_stim = visual.TextStim(win=win, ori=0, name='ss_stim',
    text='default text',    font='Arial',
    pos=[-335, 37], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
import random
#Setting up the variables
ss = random.randrange(0,100,5)
ll = 100

OLL1 = 0
ILL1 = 0
IUL1 = 100
OUL1 = 100

OLL2 = 0
ILL2 = 0
IUL2 = 100
OUL2 = 100

OLL3 = 0
ILL3 = 0
IUL3 = 100
OUL3 = 100

OLL4 = 0
ILL4 = 0
IUL4 = 100
OUL4 = 100



# Initialize components for Routine "End"
EndClock = core.Clock()
end_image = visual.ImageStim(win=win, name='end_image',
    image='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT/stimuli/end.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ip1 = 0
ip2 = 0
ip3 = 0
ip4 = 0

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
loop = data.TrialHandler(nReps=25, method='random', 
    extraInfo=expInfo, originPath=u'/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT/PsychoPy_DDT_modifiedalgorithm.psyexp',
    trialList=data.importConditions('conditions_DDT.xlsx'),
    seed=None, name='loop')
thisExp.addLoop(loop)  # add the loop to the experiment
thisLoop = loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisLoop.rgb)
if thisLoop != None:
    for paramName in thisLoop.keys():
        exec(paramName + '= thisLoop.' + paramName)

for thisLoop in loop:
    currentLoop = loop
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop.keys():
            exec(paramName + '= thisLoop.' + paramName)
    
    #------Prepare to start Routine "Fixation"-------
    t = 0
    FixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationComponents = []
    FixationComponents.append(fixation)
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Fixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t  # underestimates by a little under one frame
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        elif fixation.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Fixation"-------
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    bg_stim.setImage(background)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    ll_stim.setText('$%.0f' %(ll))
    ss_stim.setText('$%.0f' %(ss))
    #Computing updated Sooner/Smaller (SS) values for trial
    if delay == 1:
        ss = random.randrange(OLL1,OUL1,5)
    elif delay == 2:
        ss = random.randrange(OLL2,OUL2,5)
    elif delay == 3:
        ss = random.randrange(OLL3,OUL3,5)
    elif delay == 4:
        ss = random.randrange(OLL4,OUL4,5)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(bg_stim)
    trialComponents.append(response)
    trialComponents.append(ll_stim)
    trialComponents.append(ss_stim)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bg_stim* updates
        if t >= 0.0 and bg_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            bg_stim.tStart = t  # underestimates by a little under one frame
            bg_stim.frameNStart = frameN  # exact frame index
            bg_stim.setAutoDraw(True)
        
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *ll_stim* updates
        if t >= 0.0 and ll_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            ll_stim.tStart = t  # underestimates by a little under one frame
            ll_stim.frameNStart = frameN  # exact frame index
            ll_stim.setAutoDraw(True)
        
        # *ss_stim* updates
        if t >= 0.0 and ss_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss_stim.tStart = t  # underestimates by a little under one frame
            ss_stim.frameNStart = frameN  # exact frame index
            ss_stim.setAutoDraw(True)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
       response.keys=None
    # store data for loop (TrialHandler)
    loop.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        loop.addData('response.rt', response.rt)
    #Updating the 1-day delay
    if delay == 1:
        #Data to keep
        loop.addData('response.keys1',response.keys) 
        loop.addData('OLL1',OLL1)
        loop.addData('ILL1',ILL1)
        loop.addData('IUL1',IUL1)
        loop.addData('OUL1',OUL1)
        loop.addData('ss1',ss)
        loop.addData('ip1',ip1)
        #RULE 1
        if response.keys == 'v' and ss < IUL1: 
            OLL1 = OLL1
            ILL1 = ILL1
            IUL1 = ss
            OUL1 = IUL1
            if ss < ILL1:
                OLL1 = 0
                ILL1 = ss
                IUL1 = IUL1
                OUL1 = OUL1
            elif ss >= ILL1:
                pass
        #RULE 2
        elif response.keys == 'v' and ss >= IUL1: 
            OLL1 = OLL1
            ILL1 = ILL1
            IUL1 = IUL1
            OUL1 = ss
        #RULE 3
        elif response.keys == 'b' and ss <= ILL1: 
            OLL1 = ss
            ILL1 = ILL1
            IUL1 = IUL1
            OUL1 = OUL1
        #RULE 4
        elif response.keys == 'b' and ss > ILL1: 
            OLL1 = ILL1
            ILL1 = ss
            IUL1 = IUL1
            OUL1 = OUL1
            if ss > IUL1:
                OLL1 = OLL1
                ILL1 = ILL1
                IUL1 = ss
                OUL1 = 100
            elif ss <= IUL1:
                pass
    
    #Updating the 1-week delay
    if delay == 2:
        #Data to keep
        loop.addData('response.keys2',response.keys) 
        loop.addData('OLL2',OLL2)
        loop.addData('ILL2',ILL2)
        loop.addData('IUL2',IUL2)
        loop.addData('OUL2',OUL2)
        loop.addData('ss2',ss)
        loop.addData('ip2',ip2)
        #RULE 1
        if response.keys == 'v' and ss < IUL2: 
            OLL2 = OLL2
            ILL2 = ILL2
            IUL2 = ss
            OUL2 = IUL2
            if ss < ILL2:
                OLL2 = 0
                ILL2 = ss
                IUL2 = IUL2
                OUL2 = OUL2
            elif ss >= ILL2:
                pass
        #RULE 2
        elif response.keys == 'v' and ss >= IUL2: 
            OLL2 = OLL2
            ILL2 = ILL2
            IUL2 = IUL2
            OUL2 = ss
        #RULE 3
        elif response.keys == 'b' and ss <= ILL2: 
            OLL2 = ss
            ILL2 = ILL2
            IUL2 = IUL2
            OUL2 = OUL2
        #RULE 4
        elif response.keys == 'b' and ss > ILL2: 
            OLL2 = ILL2
            ILL2 = ss
            IUL2 = IUL2
            OUL2 = OUL2
            if ss > IUL2:
                OLL2 = OLL2
                ILL2 = ILL2
                IUL2 = ss
                OUL2 = 100
            elif ss <= IUL2:
                pass
    
    #Updating the 1-month delay
    if delay == 3:
        #Data to keep
        loop.addData('response.keys3',response.keys) 
        loop.addData('OLL3',OLL3)
        loop.addData('ILL3',ILL3)
        loop.addData('IUL3',IUL3)
        loop.addData('OUL3',OUL3)
        loop.addData('ss3',ss)
        loop.addData('ip3',ip3)
        #RULE 1
        if response.keys == 'v' and ss < IUL3: 
            OLL3 = OLL3
            ILL3 = ILL3
            IUL3 = ss
            OUL3 = IUL3
            if ss < ILL3:
                OLL3 = 0
                ILL3 = ss
                IUL3 = IUL3
                OUL3 = OUL3
            elif ss >= ILL3:
                pass
        #RULE 2
        elif response.keys == 'v' and ss >= IUL3: 
            OLL3 = OLL3
            ILL3 = ILL3
            IUL3 = IUL3
            OUL3 = ss
        #RULE 3
        elif response.keys == 'b' and ss <= ILL3: 
            OLL3 = ss
            ILL3 = ILL3
            IUL3 = IUL3
            OUL3 = OUL3
        #RULE 4
        elif response.keys == 'b' and ss > ILL3: 
            OLL3 = ILL3
            ILL3 = ss
            IUL3 = IUL3
            OUL3 = OUL3
            if ss > IUL3:
                OLL3 = OLL3
                ILL3 = ILL3
                IUL3 = ss
                OUL3 = 100
            elif ss <= IUL3:
                pass
    
    #Updating the 1-year delay
    if delay == 4:
        #Data to keep
        loop.addData('response.keys4',response.keys) 
        loop.addData('OLL4',OLL4)
        loop.addData('ILL4',ILL4)
        loop.addData('IUL4',IUL4)
        loop.addData('OUL4',OUL4)
        loop.addData('ss4',ss)
        loop.addData('ip4',ip4)
        #RULE 1
        if response.keys == 'v' and ss < IUL4: 
            OLL4 = OLL4
            ILL4 = ILL4
            IUL4 = ss
            OUL4 = IUL4
            if ss < ILL4:
                OLL4 = 0
                ILL4 = ss
                IUL4 = IUL4
                OUL4 = OUL4
            elif ss >= ILL4:
                pass
        #RULE 2
        elif response.keys == 'v' and ss >= IUL4: 
            OLL4 = OLL4
            ILL4 = ILL4
            IUL4 = IUL4
            OUL4 = ss
        #RULE 3
        elif response.keys == 'b' and ss <= ILL4: 
            OLL4 = ss
            ILL4 = ILL4
            IUL4 = IUL4
            OUL4 = OUL4
        #RULE 4
        elif response.keys == 'b' and ss > ILL4: 
            OLL4 = ILL4
            ILL4 = ss
            IUL4 = IUL4
            OUL4 = OUL4
            if ss > IUL4:
                OLL4 = OLL4
                ILL4 = ILL4
                IUL4 = ss
                OUL4 = 100
            elif ss <= IUL4:
                pass
    
    #------Prepare to start Routine "End"-------
    t = 0
    EndClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    ip1 = ip1
    ip2 = ip2
    ip3 = ip3
    ip4 = ip4
    # keep track of which components have finished
    EndComponents = []
    EndComponents.append(end_image)
    for thisComponent in EndComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "End"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EndClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_image* updates
        if t >= 0.0 and end_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            end_image.tStart = t  # underestimates by a little under one frame
            end_image.frameNStart = frameN  # exact frame index
            end_image.setAutoDraw(True)
        elif end_image.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            end_image.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "End"-------
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if delay == 1:
        day = OUL1 - OLL1
        if day <= 5:
            ip1 = 1
        elif day > 5:
            pass
    
    if delay == 2:
        week = OUL2 - OLL2
        if week <= 5:
            ip2 = 1
        elif week > 5:
            pass
    
    if delay == 3:
        month = OUL3 - OLL3
        if month <= 5:
            ip3 = 1
        elif month > 5:
            pass
    
    if delay == 4:
        year = OUL4 - OLL4
        if year <= 5:
            ip4 = 1
        elif year > 5:
            pass
    thisExp.nextEntry()
    
# completed 25 repeats of 'loop'



win.close()
core.quit()
