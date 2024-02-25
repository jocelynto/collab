#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), Tue Nov 18 10:18:46 2014
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
expName = 'PsychoPy_DDT1'  # from the Builder filename that created this script
expInfo = {u'P': u'', u'sess': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['P'], expInfo['sess'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT1.psyexp',
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

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionStim = visual.ImageStim(win=win, name='InstructionStim',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Initating_vars"
Initating_varsClock = core.Clock()
import random

## Setting up the variables for trial 1##
#reward values
ll = 100 #larger-later reward is $100

#double-limit algorithm values
OLL1 = 0 #outer-limit of lower band for 1-day delay
ILL1 = 0 #inner-limit of lower band for 1-day delay
IUL1 = ll #inner-limit of upper band for 1-day delay
OUL1 = ll #outer-limit of upper band for 1-day delay
OLL2 = 0 #outer-limit of lower band for 1-week delay
ILL2 = 0 #inner-limit of lower band for 1-week delay
IUL2 = ll #inner-limit of upper band for 1-week delay
OUL2 = ll #outer-limit of upper band for 1-week delay
OLL3 = 0 #outer-limit of lower band for 1-month delay
ILL3 = 0 #inner-limit of lower band for 1-month delay
IUL3 = ll #inner-limit of upper band for 1-month delay
OUL3 = ll #outer-limit of upper band for 1-month delay
OLL4 = 0 #outer-limit of lower band for 1-year delay
ILL4 = 0 #inner-limit of lower band for 1-year delay
IUL4 = ll #inner-limit of upper band for 1-year delay
OUL4 = ll #outer-limit of upper band for 1-year delay

#initial dummy variables for the status of the indifference point at trial #1 (0 = not yet reached, 1 = reached)
ip1 = 0
ip2 = 0
ip3 = 0
ip4 = 0

# setting a dummy variable to determine the side of screen to present stimuli on trial #1
a = [0,1]

# setting a dummy variable to determine which rows to select from the conditions file
row = [0,1,2,3]

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
FixationStim = visual.ImageStim(win=win, name='FixationStim',
    image='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/stimuli/start.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()

TrialStim = visual.ImageStim(win=win, name='TrialStim',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
LLStim = visual.TextStim(win=win, ori=0, name='LLStim',
    text='default text',    font='Arial',
    pos=[0,0], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
SSStim = visual.TextStim(win=win, ori=0, name='SSStim',
    text='default text',    font='Arial',
    pos=[0,0], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
EndStim = visual.ImageStim(win=win, name='EndStim',
    image='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/stimuli/end.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "RowUpdate"
RowUpdateClock = core.Clock()


# Initialize components for Routine "end_session"
end_sessionClock = core.Clock()
EndSessStim = visual.TextStim(win=win, ori=0, name='EndSessStim',
    text='You have completed this section of the experiment, \n\nthanks for participating!',    font='Arial',
    pos=[0, 0], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
DDTInst = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT1.psyexp',
    trialList=data.importConditions('conditions_DDTinst.xlsx'),
    seed=None, name='DDTInst')
thisExp.addLoop(DDTInst)  # add the loop to the experiment
thisDDTInst = DDTInst.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisDDTInst.rgb)
if thisDDTInst != None:
    for paramName in thisDDTInst.keys():
        exec(paramName + '= thisDDTInst.' + paramName)

for thisDDTInst in DDTInst:
    currentLoop = DDTInst
    # abbreviate parameter names if possible (e.g. rgb = thisDDTInst.rgb)
    if thisDDTInst != None:
        for paramName in thisDDTInst.keys():
            exec(paramName + '= thisDDTInst.' + paramName)
    
    #------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    InstructionStim.setImage(stim)
    InstructionKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
    InstructionKey.status = NOT_STARTED
    # keep track of which components have finished
    InstructionsComponents = []
    InstructionsComponents.append(InstructionStim)
    InstructionsComponents.append(InstructionKey)
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Instructions"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionStim* updates
        if t >= 0.0 and InstructionStim.status == NOT_STARTED:
            # keep track of start time/frame for later
            InstructionStim.tStart = t  # underestimates by a little under one frame
            InstructionStim.frameNStart = frameN  # exact frame index
            InstructionStim.setAutoDraw(True)
        
        # *InstructionKey* updates
        if t >= 0.0 and InstructionKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            InstructionKey.tStart = t  # underestimates by a little under one frame
            InstructionKey.frameNStart = frameN  # exact frame index
            InstructionKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if InstructionKey.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
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
    
    #-------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1 repeats of 'DDTInst'


#------Prepare to start Routine "Initating_vars"-------
t = 0
Initating_varsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

# keep track of which components have finished
Initating_varsComponents = []
for thisComponent in Initating_varsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Initating_vars"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Initating_varsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Initating_varsComponents:
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

#-------Ending Routine "Initating_vars"-------
for thisComponent in Initating_varsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc
DDTminiblocks = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT1.psyexp',
    trialList=[None],
    seed=None, name='DDTminiblocks')
thisExp.addLoop(DDTminiblocks)  # add the loop to the experiment
thisDDTminiblock = DDTminiblocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisDDTminiblock.rgb)
if thisDDTminiblock != None:
    for paramName in thisDDTminiblock.keys():
        exec(paramName + '= thisDDTminiblock.' + paramName)

for thisDDTminiblock in DDTminiblocks:
    currentLoop = DDTminiblocks
    # abbreviate parameter names if possible (e.g. rgb = thisDDTminiblock.rgb)
    if thisDDTminiblock != None:
        for paramName in thisDDTminiblock.keys():
            exec(paramName + '= thisDDTminiblock.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    DDTtrial = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT1.psyexp',
        trialList=data.importConditions('conditions_DDTtask.xlsx', selection=row),
        seed=None, name='DDTtrial')
    thisExp.addLoop(DDTtrial)  # add the loop to the experiment
    thisDDTtrial = DDTtrial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisDDTtrial.rgb)
    if thisDDTtrial != None:
        for paramName in thisDDTtrial.keys():
            exec(paramName + '= thisDDTtrial.' + paramName)
    
    for thisDDTtrial in DDTtrial:
        currentLoop = DDTtrial
        # abbreviate parameter names if possible (e.g. rgb = thisDDTtrial.rgb)
        if thisDDTtrial != None:
            for paramName in thisDDTtrial.keys():
                exec(paramName + '= thisDDTtrial.' + paramName)
        
        #------Prepare to start Routine "Fixation"-------
        t = 0
        FixationClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        # keep track of which components have finished
        FixationComponents = []
        FixationComponents.append(FixationStim)
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Fixation"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = FixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixationStim* updates
            if t >= 0.0 and FixationStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                FixationStim.tStart = t  # underestimates by a little under one frame
                FixationStim.frameNStart = frameN  # exact frame index
                FixationStim.setAutoDraw(True)
            elif FixationStim.status == STARTED and t >= (0.0 + (random.uniform(1.4,1.6)-win.monitorFramePeriod*0.75)): #most of one frame period left
                FixationStim.setAutoDraw(False)
            
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
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Fixation"-------
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        ## Updating the smaller-sooner reward value, determining side of presentation ##
        
        # Clearing the SS value because I have OCD
        ss = None
        
        # Updating the SS value
        if delay == 1 and ip1 == 0: # if 1-day indif. point has not been reached, update ss
            ss1 = random.randrange(OLL1,OUL1+0.05*ll,0.05*ll)
            DDTtrial.addData('ss1',ss1)
            ss = ss1
        elif delay == 1 and ip1 == 1: #if indif. point has been reached...
            ss1 = ss1 # keep as last 1-day smaller-sooner value
            ss = ss1
        elif delay == 2 and ip2 == 0: # if 1-week indif. point has not been reached, update ss
            ss2 = random.randrange(OLL2,OUL2+0.05*ll,0.05*ll)
            DDTtrial.addData('ss2',ss2)
            ss = ss2
        elif delay == 2 and ip2 == 1: #if indif. point has been reached...
            ss2 = ss2 # keep as last 1-day smaller-sooner value
            ss = ss2
        elif delay == 3 and ip3 == 0: # if 1-month indif. point has not been reached, update ss
            ss3 = random.randrange(OLL3,OUL3+0.05*ll,0.05*ll)
            DDTtrial.addData('ss3',ss3)
            ss = ss3
        elif delay == 3 and ip3 == 1: #if indif. point has been reached...
            ss3 = ss3 # keep as last 1-month smaller-sooner value
            ss = ss3
        elif delay == 4 and ip4 == 0: # if 1-year indif. point has not been reached, update ss
            ss4 = random.randrange(OLL4,OUL4+0.05*ll,0.05*ll)
            DDTtrial.addData('ss4',ss4)
            ss = ss4
        elif delay == 4 and ip4 == 1: #if indif. point has been reached...
            ss4 = ss4 # keep as last 1-year smaller-sooner value
            ss = ss4
        
        #determining which background image to display (i.e. left or right)
        side = random.choice(a)
        if side == 0:
            background = r_background
            llloc = [270,37]
            ssloc = [-335, 37]
        elif side == 1:
            background = l_background
            llloc = [-435, 37]
            ssloc = [320,37]
        TrialStim.setImage(background)
        LLStim.setText('$%.0f' %(ll))
        LLStim.setPos(llloc)
        SSStim.setText('$%.0f' %(ss))
        SSStim.setPos(ssloc)
        TrialResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        TrialResp.status = NOT_STARTED
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(TrialStim)
        trialComponents.append(LLStim)
        trialComponents.append(SSStim)
        trialComponents.append(TrialResp)
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
            
            
            # *TrialStim* updates
            if t >= 0.0 and TrialStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialStim.tStart = t  # underestimates by a little under one frame
                TrialStim.frameNStart = frameN  # exact frame index
                TrialStim.setAutoDraw(True)
            
            # *LLStim* updates
            if t >= 0.0 and LLStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                LLStim.tStart = t  # underestimates by a little under one frame
                LLStim.frameNStart = frameN  # exact frame index
                LLStim.setAutoDraw(True)
            
            # *SSStim* updates
            if t >= 0.0 and SSStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                SSStim.tStart = t  # underestimates by a little under one frame
                SSStim.frameNStart = frameN  # exact frame index
                SSStim.setAutoDraw(True)
            
            # *TrialResp* updates
            if t >= 0.0 and TrialResp.status == NOT_STARTED:
                # keep track of start time/frame for later
                TrialResp.tStart = t  # underestimates by a little under one frame
                TrialResp.frameNStart = frameN  # exact frame index
                TrialResp.status = STARTED
                # keyboard checking is just starting
                TrialResp.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if TrialResp.status == STARTED:
                theseKeys = event.getKeys(keyList=['v', 'b'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    TrialResp.keys = theseKeys[-1]  # just the last key pressed
                    TrialResp.rt = TrialResp.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
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
        ## Coding Responses as "immediate" or "delayed", and updating double-limit algorithm ranges accordingly
        
        # Coding response types:
        if side == 0 and TrialResp.keys == 'v':
            resp = 'immediate'
        elif side == 0 and TrialResp.keys == 'b':
            resp = 'delayed'
        elif side == 1 and TrialResp.keys == 'b':
            resp = 'immediate'
        elif side == 1 and TrialResp.keys == 'v':
            resp = 'delayed'
        
        # Updating the double-limit algorithm values according to the participants' responses
        if delay == 1 and ip1 == 0:
            #data to hold onto for each 1-day trial
            DDTtrial.addData('OLL1',OLL1)
            DDTtrial.addData('ILL1',ILL1)
            DDTtrial.addData('IUL1',IUL1)
            DDTtrial.addData('OUL1',OUL1)
            DDTtrial.addData('resp',resp)
            #Updating the algorithm for the 1-day delay
            if resp == 'immediate' and ss1 < IUL1: #Lowers the entire upper band if the participant chooses the ss reward
                OUL1 = IUL1
                IUL1 = ss1
                if ss1 < ILL1: # if the participant chooses the ss reward when it is low enough, the lower band is also decreased
                    OLL1 = 0
                    ILL1 = ss1
            elif resp == 'delayed' and ss1 > ILL1: #Raises the entire lower band if the participant chooses the ll reward
                OLL1 = ILL1
                ILL1 = ss1
                if ss1 > IUL1: # if the participant chooses the ll reward when the ss value is high enough, the upper band is also increased
                    OUL1 = ll
                    IUL1 = ss1
            elif resp == 'immediate' and ss1 >= IUL1: #If the participant chooses the ss reward and it is within the upper band, the outer upper band decreases accordingly
                OUL1 = ss1
            elif resp == 'delayed' and ss1 <= ILL1: #If the participant chooses the ll reward when the ss is within the lower band, the outer lower band increases accordingly
                OLL1 = ss1
        
        if delay == 2 and ip2 == 0:
            #data to hold onto for each 1-week trial
            DDTtrial.addData('OLL2',OLL2)
            DDTtrial.addData('ILL2',ILL2)
            DDTtrial.addData('IUL2',IUL2)
            DDTtrial.addData('OUL2',OUL2)
            DDTtrial.addData('resp',resp)
            #Updating the algorithm for the 1-week delay
            if resp == 'immediate' and ss2 < IUL2: #Lowers the entire upper band if the participant chooses the ss reward
                OUL2 = IUL2
                IUL2 = ss2
                if ss2 < ILL2: # if the participant chooses the ss reward when it is low enough, the lower band is also decreased
                    OLL2 = 0
                    ILL2 = ss2
            elif resp == 'delayed' and ss2 > ILL2: #Raises the entire lower band if the participant chooses the ll reward
                OLL2 = ILL2
                ILL2 = ss2
                if ss2 > IUL2: # if the participant chooses the ll reward when the ss value is high enough, the upper band is also increased
                    OUL2 = ll
                    IUL2 = ss2
            elif resp == 'immediate' and ss2 >= IUL2: #If the participant chooses the ss reward and it is within the upper band, the outer upper band decreases accordingly
                OUL2 = ss2
            elif resp == 'delayed' and ss2 <= ILL2: #If the participant chooses the ll reward when the ss is within the lower band, the outer lower band increases accordingly
                OLL2 = ss2
        
        if delay == 3 and ip3 == 0:
            #data to hold onto for each 1-month trial
            DDTtrial.addData('OLL3',OLL3)
            DDTtrial.addData('ILL3',ILL3)
            DDTtrial.addData('IUL3',IUL3)
            DDTtrial.addData('OUL3',OUL3)
            DDTtrial.addData('resp',resp)
            #Updating the algorithm for the 1-month delay
            if resp == 'immediate' and ss3 < IUL3: #Lowers the entire upper band if the participant chooses the ss reward
                OUL3 = IUL3
                IUL3 = ss3
                if ss3 < ILL3: # if the participant chooses the ss reward when it is low enough, the lower band is also decreased
                    OLL3 = 0
                    ILL3 = ss3
            elif resp == 'delayed' and ss3 > ILL3: #Raises the entire lower band if the participant chooses the ll reward
                OLL3 = ILL3
                ILL3 = ss3
                if ss3 > IUL3: # if the participant chooses the ll reward when the ss value is high enough, the upper band is also increased
                    OUL3 = ll
                    IUL3 = ss3
            elif resp == 'immediate' and ss3 >= IUL3: #If the participant chooses the ss reward and it is within the upper band, the outer upper band decreases accordingly
                OUL3 = ss3
            elif resp == 'delayed' and ss3 <= ILL3: #If the participant chooses the ll reward when the ss is within the lower band, the outer lower band increases accordingly
                OLL3 = ss3
        
        if delay == 4 and ip4 == 0:
            #data to hold onto for each 1-year trial
            DDTtrial.addData('OLL4',OLL4)
            DDTtrial.addData('ILL4',ILL4)
            DDTtrial.addData('IUL4',IUL4)
            DDTtrial.addData('OUL4',OUL4)
            DDTtrial.addData('resp',resp)
            #Updating the algorithm for the 1-year delay
            if resp == 'immediate' and ss4 < IUL4: #Lowers the entire upper band if the participant chooses the ss reward
                OUL4 = IUL4
                IUL4 = ss4
                if ss4 < ILL4: # if the participant chooses the ss reward when it is low enough, the lower band is also decreased
                    OLL4 = 0
                    ILL4 = ss4
            elif resp == 'delayed' and ss4 > ILL4: #Raises the entire lower band if the participant chooses the ll reward
                OLL4 = ILL4
                ILL4 = ss4
                if ss4 > IUL4: # if the participant chooses the ll reward when the ss value is high enough, the upper band is also increased
                    OUL4 = ll
                    IUL4 = ss4
            elif resp == 'immediate' and ss4 >= IUL4: #If the participant chooses the ss reward and it is within the upper band, the outer upper band decreases accordingly
                OUL4 = ss4
            elif resp == 'delayed' and ss4 <= ILL4: #If the participant chooses the ll reward when the ss is within the lower band, the outer lower band increases accordingly
                OLL4 = ss4
        
        # check responses
        if TrialResp.keys in ['', [], None]:  # No response was made
           TrialResp.keys=None
        # store data for DDTtrial (TrialHandler)
        DDTtrial.addData('TrialResp.keys',TrialResp.keys)
        if TrialResp.keys != None:  # we had a response
            DDTtrial.addData('TrialResp.rt', TrialResp.rt)
        
        #------Prepare to start Routine "ITI"-------
        t = 0
        ITIClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = []
        ITIComponents.append(EndStim)
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ITI"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EndStim* updates
            if t >= 0.0 and EndStim.status == NOT_STARTED:
                # keep track of start time/frame for later
                EndStim.tStart = t  # underestimates by a little under one frame
                EndStim.frameNStart = frameN  # exact frame index
                EndStim.setAutoDraw(True)
            elif EndStim.status == STARTED and t >= (0.0 + (random.uniform(0.4,0.6)-win.monitorFramePeriod*0.75)): #most of one frame period left
                EndStim.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
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
        
        #-------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'DDTtrial'
    
    
    #------Prepare to start Routine "RowUpdate"-------
    t = 0
    RowUpdateClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    ## Determining whether the indifference points have been reached for each delay
    OLL = [OLL1,OLL2,OLL3,OLL4]
    OUL = [OUL1,OUL2,OUL3,OUL4]
    row = [0,1,2,3]
    for i in range(len(row)):
        d = OUL[i] - OLL[i]
        if d <= 5:
            ip = 1
        elif d > 5:
            ip = 0
    #    DDTminiblocks.addData('ip%',ip) %(i)
        ## ENDING LOOP FOR INDIFFERENCE POINTS THAT HAVE BEEN REACHED
        if ip == 1: # if the ip was just reached, remove it
            row.remove(i)
    #    DDTminiblocks.addData('rows',row) # Saving rows, which is the # used to determine which stimiuli are presented in the next loop
        if not row:
            DDTminiblocks.finished = True
    # keep track of which components have finished
    RowUpdateComponents = []
    for thisComponent in RowUpdateComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "RowUpdate"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = RowUpdateClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RowUpdateComponents:
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
    
    #-------Ending Routine "RowUpdate"-------
    for thisComponent in RowUpdateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
# completed 100 repeats of 'DDTminiblocks'


#------Prepare to start Routine "end_session"-------
t = 0
end_sessionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
EndSessResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
EndSessResp.status = NOT_STARTED
# keep track of which components have finished
end_sessionComponents = []
end_sessionComponents.append(EndSessStim)
end_sessionComponents.append(EndSessResp)
for thisComponent in end_sessionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end_session"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = end_sessionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndSessStim* updates
    if t >= 0.0 and EndSessStim.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndSessStim.tStart = t  # underestimates by a little under one frame
        EndSessStim.frameNStart = frameN  # exact frame index
        EndSessStim.setAutoDraw(True)
    
    # *EndSessResp* updates
    if t >= 0.0 and EndSessResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndSessResp.tStart = t  # underestimates by a little under one frame
        EndSessResp.frameNStart = frameN  # exact frame index
        EndSessResp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if EndSessResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_sessionComponents:
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

#-------Ending Routine "end_session"-------
for thisComponent in end_sessionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



win.close()
core.quit()
