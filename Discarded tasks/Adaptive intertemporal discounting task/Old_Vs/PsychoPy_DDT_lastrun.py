#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), Mon Nov 17 12:35:02 2014
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
expName = 'PsychoPy_DDT'  # from the Builder filename that created this script
expInfo = {u'P': u'', u'sess': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['P'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT.psyexp',
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
Instructions1 = visual.ImageStim(win=win, name='Instructions1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
fixation = visual.ImageStim(win=win, name='fixation',
    image=u'/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/stimuli/start.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
import random
###Setting up the variables for Trial #1####

#setting initial experiment parameters (longer later and sooner smaller values)
ll = 100
ss = random.randrange(0,100,5)

#setting initial double-limit choice algorithm values for each delay 
#(1 = 1-day, 2 = 1-week, 3 = 1-month, 4 = 1-year)
OLL1 = 0
ILL1 = 0
IUL1 = ll
OUL1 = ll

OLL2 = 0
ILL2 = 0
IUL2 = ll
OUL2 = ll

OLL3 = 0
ILL3 = 0
IUL3 = ll
OUL3 = 100

OLL4 = 0
ILL4 = 0
IUL4 = ll
OUL4 = ll

#setting initial dummy variable to indicate the status of the indifference point
ip1 = 0
ip2 = 0
ip3 = 0
ip4 = 0

#setting a dummy variable to determine side of screen presentation on each trial
a = [1,2]

#starting by selecting randomly from all possible delays
rows = range(4)

bg_stim = visual.ImageStim(win=win, name='bg_stim',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
ll_stim = visual.TextStim(win=win, ori=0, name='ll_stim',
    text='default text',    font='Arial',
    pos=[0,0], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
ss_stim = visual.TextStim(win=win, ori=0, name='ss_stim',
    text='default text',    font='Arial',
    pos=[0,0], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
end_image = visual.ImageStim(win=win, name='end_image',
    image=u'/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/stimuli/end.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "next_loop_rows"
next_loop_rowsClock = core.Clock()


# Initialize components for Routine "end_session"
end_sessionClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text="'You have completed this section of the experiment, thank you for participating!'",    font='Arial',
    pos=[0, 0], height=60, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
DDTinst = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT.psyexp',
    trialList=data.importConditions(u'conditions_DDTinst.xlsx'),
    seed=None, name='DDTinst')
thisExp.addLoop(DDTinst)  # add the loop to the experiment
thisDDTinst = DDTinst.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisDDTinst.rgb)
if thisDDTinst != None:
    for paramName in thisDDTinst.keys():
        exec(paramName + '= thisDDTinst.' + paramName)

for thisDDTinst in DDTinst:
    currentLoop = DDTinst
    # abbreviate parameter names if possible (e.g. rgb = thisDDTinst.rgb)
    if thisDDTinst != None:
        for paramName in thisDDTinst.keys():
            exec(paramName + '= thisDDTinst.' + paramName)
    
    #------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    Instructions1.setImage(stim)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    # keep track of which components have finished
    InstructionsComponents = []
    InstructionsComponents.append(Instructions1)
    InstructionsComponents.append(key_resp_2)
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
        
        # *Instructions1* updates
        if t >= 0.0 and Instructions1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Instructions1.tStart = t  # underestimates by a little under one frame
            Instructions1.frameNStart = frameN  # exact frame index
            Instructions1.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t  # underestimates by a little under one frame
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            key_resp_2.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
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
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
       key_resp_2.keys=None
    # store data for DDTinst (TrialHandler)
    DDTinst.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        DDTinst.addData('key_resp_2.rt', key_resp_2.rt)
# completed 1 repeats of 'DDTinst'


# set up handler to look after randomisation of conditions etc
Miniblocks = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT.psyexp',
    trialList=[None],
    seed=None, name='Miniblocks')
thisExp.addLoop(Miniblocks)  # add the loop to the experiment
thisMiniblock = Miniblocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMiniblock.rgb)
if thisMiniblock != None:
    for paramName in thisMiniblock.keys():
        exec(paramName + '= thisMiniblock.' + paramName)

for thisMiniblock in Miniblocks:
    currentLoop = Miniblocks
    # abbreviate parameter names if possible (e.g. rgb = thisMiniblock.rgb)
    if thisMiniblock != None:
        for paramName in thisMiniblock.keys():
            exec(paramName + '= thisMiniblock.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    DDTtask = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath='/Users/jhogeveen/Documents/Dropbox/Fall_2014/tDCS/tDCS_Study_1/PsychoPy_DDT_Pre/PsychoPy_DDT.psyexp',
        trialList=data.importConditions(u'conditions_DDTtask.xlsx', selection=rows),
        seed=None, name='DDTtask')
    thisExp.addLoop(DDTtask)  # add the loop to the experiment
    thisDDTtask = DDTtask.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisDDTtask.rgb)
    if thisDDTtask != None:
        for paramName in thisDDTtask.keys():
            exec(paramName + '= thisDDTtask.' + paramName)
    
    for thisDDTtask in DDTtask:
        currentLoop = DDTtask
        # abbreviate parameter names if possible (e.g. rgb = thisDDTtask.rgb)
        if thisDDTtask != None:
            for paramName in thisDDTtask.keys():
                exec(paramName + '= thisDDTtask.' + paramName)
        
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
        ###Updating the SS value, determining side of screen
        
        
        #Computing updated Sooner/Smaller (SS) values for trial
        if delay == 1 and ip1 == 0: #if 1-day indifference point has not been reached, update ss
            ss1 = random.randrange(OLL1,OUL1,5)
            DDTtask.addData('ss1',ss1)
            ss = ss1
        elif delay == 2 and ip2 == 0: #if 1-week indifference point has not been reached, update ss
            ss2 = random.randrange(OLL2,OUL2,5)
            DDTtask.addData('ss2',ss2)
            ss = ss2
        elif delay == 3 and ip3 == 0: #if 1-month indifference point has not been reached, update ss
            ss3 = random.randrange(OLL3,OUL3,5)
            DDTtask.addData('ss3',ss3)
            ss = ss3
        elif delay == 4 and ip3 == 0: #if 1-year indifference point has not been reached, update ss
            ss4 = random.randrange(OLL4,OUL4,5)
            DDTtask.addData('ss4',ss4)
            ss = ss4
        
        #determining which background image to display (i.e. left or right)
        side = random.choice(a)
        if side == 1:
            background = r_background
            llloc = [270,37]
            ssloc = [-335, 37]
        elif side == 2:
            background = l_background
            llloc = [-435, 37]
            ssloc = [320,37]
        
        
        
        bg_stim.setImage(background)
        response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        response.status = NOT_STARTED
        ll_stim.setText('$%.0f' %(ll))
        ll_stim.setPos(llloc)
        ss_stim.setText('$%.0f' %(ss))
        ss_stim.setPos(ssloc)
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
        # if $100 was on the right and participant hit v, the choice was the immediate reward (resp type 1)
        if side == 1 and response.keys == 'v':
            resp = 1 
        # if $100 was on the left and participant hit v, the choice was the immediate reward (resp type 1)
        elif side == 2 and response.keys == 'b':
            resp = 1
        elif side == 1 and response.keys == 'b':
            resp = 2
        elif side == 2 and response.keys == 'v':
            resp = 2
        
        ###Updating and saving 1-day specific variables####
        if delay == 1 and ip1 == 0: #if 1-day
            #Data to keep for 1-day delay
            DDTtask.addData('OLL1',OLL1)
            DDTtask.addData('ILL1',ILL1)
            DDTtask.addData('IUL1',IUL1)
            DDTtask.addData('OUL1',OUL1)
            DDTtask.addData('resptype1',resp)
        #    DDTtask.addData('ip1',ip1)
            #RULE 1
            if resp == 1 and ss < IUL1: #if 1-day and participant selects smaller-sooner value < IUL
                if ss >= ILL1: # If ss is between inside bands, lower the upper band
                    OLL1 = OLL1
                    ILL1 = ILL1
                    IUL1 = ss
                    OUL1 = IUL1
                elif ss < ILL1: #If ss is lower than the inside lower band, decrease both bands
                    OLL1 = 0
                    ILL1 = ss
                    IUL1 = ss
                    OUL1 = IUL1
            #RULE 2
            elif resp == 1 and ss >= IUL1: #if 1-day and participant selects smaller-sooner value >= IUL
                OLL1 = OLL1
                ILL1 = ILL1
                IUL1 = IUL1
                OUL1 = ss # Decrease the outer limit of the upper band
            #RULE 3
            elif resp == 2 and ss <= ILL1: #if 1-day and participant selects larger-later value when ss <= ILL
                OLL1 = ss # Increase the outer limit of the lower band
                ILL1 = ILL1
                IUL1 = IUL1
                OUL1 = OUL1
            #RULE 4
            elif resp == 2 and ss > ILL1: #if 1-day and participant selects larger-later value when ss > ILL1
                if ss <= IUL1: # If ss is between inside bands, raise the lower band
                    OLL1 = ILL1
                    ILL1 = ss
                    IUL1 = IUL1
                    OUL1 = OUL1
                elif ss > IUL1: #If ss is greater than the inside upper band, increase both bands
                    OLL1 = ILL1
                    ILL1 = ss
                    IUL1 = ss
                    OUL1 = 100     
            else: #if participant does anything other than respond 'v' or 'b', keep the bands as they are
                OLL1 = OLL1
                ILL1 = ILL1
                IUL1 = IUL1
                OUL1 = OUL1
        
        ###Updating and saving 1-week specific variables####
        if delay == 2 and ip2 == 0: #if 1-week
            #Data to keep for 1-week delay
            DDTtask.addData('OLL2',OLL2)
            DDTtask.addData('ILL2',ILL2)
            DDTtask.addData('IUL2',IUL2)
            DDTtask.addData('OUL2',OUL2)
            DDTtask.addData('resptype2',resp)
        #    DDTtask.addData('ip2',ip2)
            #RULE 1
            if resp == 1 and ss < IUL2: #if 1-week and participant selects smaller-sooner value < IUL
                if ss >= ILL2: # If ss is between inside bands, lower the upper band
                    OLL2 = OLL2
                    ILL2 = ILL2
                    IUL2 = ss
                    OUL2 = IUL2
                elif ss < ILL2: #If ss is lower than the inside lower band, decrease both bands
                    OLL2 = 0
                    ILL2 = ss
                    IUL2 = ss
                    OUL2 = IUL2
            #RULE 2
            elif resp == 1 and ss >= IUL2: #if 1-week and participant selects smaller-sooner value >= IUL
                OLL2 = OLL2
                ILL2 = ILL2
                IUL2 = IUL2
                OUL2 = ss # Decrease the outer limit of the upper band
            #RULE 3
            elif resp == 2 and ss <= ILL2: #if 1-week and participant selects larger-later value when ss <= ILL
                OLL2 = ss # Increase the outer limit of the lower band
                ILL2 = ILL2
                IUL2 = IUL2
                OUL2 = OUL2
            #RULE 4
            elif resp == 2 and ss > ILL2: #if 1-week and participant selects larger-later value when ss > ILL2
                if ss <= IUL2: # If ss is between inside bands, raise the lower band
                    OLL2 = ILL2
                    ILL2 = ss
                    IUL2 = IUL2
                    OUL2 = OUL2
                elif ss > IUL2: #If ss is greater than the inside upper band, increase both bands
                    OLL2 = ILL2
                    ILL2 = ss
                    IUL2 = ss
                    OUL2 = 100     
            else: #if participant does anything other than respond 'v' or 'b', keep the bands as they are
                OLL2 = OLL2
                ILL2 = ILL2
                IUL2 = IUL2
                OUL2 = OUL2
        
        ###Updating and saving 1-month specific variables####
        if delay == 3 and ip3 == 0: #if 1-month
            #Data to keep for 1-month delay
            DDTtask.addData('OLL3',OLL3)
            DDTtask.addData('ILL3',ILL3)
            DDTtask.addData('IUL3',IUL3)
            DDTtask.addData('OUL3',OUL3)
            DDTtask.addData('resptype3',resp)
        #    DDTtask.addData('ip3',ip3)
            #RULE 1
            if resp == 1 and ss < IUL3: #if 1-month and participant selects smaller-sooner value < IUL
                if ss >= ILL3: # If ss is between inside bands, lower the upper band
                    OLL3 = OLL3
                    ILL3 = ILL3
                    IUL3 = ss
                    OUL3 = IUL3
                elif ss < ILL3: #If ss is lower than the inside lower band, decrease both bands
                    OLL3 = 0
                    ILL3 = ss
                    IUL3 = ss
                    OUL3 = IUL3
            #RULE 2
            elif resp == 1 and ss >= IUL3: #if 1-month and participant selects smaller-sooner value >= IUL
                OLL3 = OLL3
                ILL3 = ILL3
                IUL3 = IUL3
                OUL3 = ss # Decrease the outer limit of the upper band
            #RULE 3
            elif resp == 2 and ss <= ILL3: #if 1-month and participant selects larger-later value when ss <= ILL
                OLL3 = ss # Increase the outer limit of the lower band
                ILL3 = ILL3
                IUL3 = IUL3
                OUL3 = OUL3
            #RULE 4
            elif resp == 2 and ss > ILL3: #if 1-month and participant selects larger-later value when ss > ILL3
                if ss <= IUL3: # If ss is between inside bands, raise the lower band
                    OLL3 = ILL3
                    ILL3 = ss
                    IUL3 = IUL3
                    OUL3 = OUL3
                elif ss > IUL3: #If ss is greater than the inside upper band, increase both bands
                    OLL3 = ILL3
                    ILL3 = ss
                    IUL3 = ss
                    OUL3 = 100     
            else: #if participant does anything other than respond 'v' or 'b', keep the bands as they are
                OLL3 = OLL3
                ILL3 = ILL3
                IUL3 = IUL3
                OUL3 = OUL3
        
        ###Updating and saving 1-year specific variables####
        if delay == 4 and ip4 == 0: #if 1-year
            #Data to keep for 1-year delay
            DDTtask.addData('OLL4',OLL4)
            DDTtask.addData('ILL4',ILL4)
            DDTtask.addData('IUL4',IUL4)
            DDTtask.addData('OUL4',OUL4)
            DDTtask.addData('resptype4',resp)
        #    DDTtask.addData('ip4',ip4)
            #RULE 1
            if resp == 1 and ss < IUL4: #if 1-year and participant selects smaller-sooner value < IUL
                if ss >= ILL4: # If ss is between inside bands, lower the upper band
                    OLL4 = OLL4
                    ILL4 = ILL4
                    IUL4 = ss
                    OUL4 = IUL4
                elif ss < ILL4: #If ss is lower than the inside lower band, decrease both bands
                    OLL4 = 0
                    ILL4 = ss
                    IUL4 = ss
                    OUL4 = IUL4
            #RULE 2
            elif resp == 1 and ss >= IUL4: #if 1-year and participant selects smaller-sooner value >= IUL
                OLL4 = OLL4
                ILL4 = ILL4
                IUL4 = IUL4
                OUL4 = ss # Decrease the outer limit of the upper band
            #RULE 3
            elif resp == 2 and ss <= ILL4: #if 1-year and participant selects larger-later value when ss <= ILL
                OLL4 = ss # Increase the outer limit of the lower band
                ILL4 = ILL4
                IUL4 = IUL4
                OUL4 = OUL4
            #RULE 4
            elif resp == 2 and ss > ILL4: #if 1-year and participant selects larger-later value when ss > ILL4
                if ss <= IUL4: # If ss is between inside bands, raise the lower band
                    OLL4 = ILL4
                    ILL4 = ss
                    IUL4 = IUL4
                    OUL4 = OUL4
                elif ss > IUL4: #If ss is greater than the inside upper band, increase both bands
                    OLL4 = ILL4
                    ILL4 = ss
                    IUL4 = ss
                    OUL4 = 100     
            else: #if participant does anything other than respond 'v' or 'b', keep the bands as they are
                OLL4 = OLL4
                ILL4 = ILL4
                IUL4 = IUL4
                OUL4 = OUL4
        
        ###Updating the indifference point dummy variables for each delay####
        #1-DAY INDIFFERENCE POINT
        d1 = OUL1 - OLL1
        if d1 <= 5:
            ip1 = 1
        elif d1 > 5:
            ip1 = 0
        #1-WEEK INDIFFERENCE POINT
        d2 = OUL2 - OLL2
        if d2 <= 5:
            ip2 = 1
        elif d2 > 5:
            ip2 = 0
        #1-MONTH INDIFFERENCE POINT
        d3 = OUL3 - OLL3
        if d3 <= 5:
            ip3 = 1
        elif d3 > 5:
            ip3 = 0
        #1-YEAR INDIFFERENCE POINT
        d4 = OUL4 - OLL4
        if d4 <= 5:
            ip4 = 1
        elif d4 > 5:
            ip4 = 0
        DDTtask.addData('ip1',ip1)
        DDTtask.addData('ip2',ip2)
        DDTtask.addData('ip3',ip3)
        DDTtask.addData('ip4',ip4)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
           response.keys=None
        # store data for DDTtask (TrialHandler)
        DDTtask.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            DDTtask.addData('response.rt', response.rt)
        
        #------Prepare to start Routine "End"-------
        t = 0
        EndClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.500000)
        # update component parameters for each repeat
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
        thisExp.nextEntry()
        
    # completed 1 repeats of 'DDTtask'
    
    
    #------Prepare to start Routine "next_loop_rows"-------
    t = 0
    next_loop_rowsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    ## ENDING LOOP FOR INDIFFERENCE POINTS THAT HAVE BEEN REACHED
    if ip1 == 0 and ip2 == 0 and ip3 == 0 and ip4 == 0: # no indifference points have been reached, keep all rows
        rows = range(4)
    elif ip1 == 1 and rows.index(0) >= 0:
        rows.remove(0)
    elif ip2 == 1 and rows.index(1) >= 0:
        rows.remove(1)
    elif ip3 == 1 and rows.index(2) >= 0:
        rows.remove(2)
    elif ip4 == 1 and rows.index(3) >= 0:
        rows.remove(3)
    elif ip1 == 1 and ip2 == 1 and ip3 == 1 and ip4 == 1:
        DDTtask.finished = True 
    DDTtask.addData('rows',rows) # Saving rows, which is the # used to determine which stimiuli are presented in the next loop
    # keep track of which components have finished
    next_loop_rowsComponents = []
    for thisComponent in next_loop_rowsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "next_loop_rows"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = next_loop_rowsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in next_loop_rowsComponents:
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
    
    #-------Ending Routine "next_loop_rows"-------
    for thisComponent in next_loop_rowsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
# completed 100 repeats of 'Miniblocks'


#------Prepare to start Routine "end_session"-------
t = 0
end_sessionClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
end_sessionComponents = []
end_sessionComponents.append(text)
end_sessionComponents.append(key_resp_3)
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
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
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
