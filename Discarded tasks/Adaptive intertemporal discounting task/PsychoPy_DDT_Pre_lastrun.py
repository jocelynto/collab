#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on November 30, 2023, at 10:49
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'PsychoPy_DDT_Pre'  # from the Builder filename that created this script
expInfo = {'P': '', 'sess': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['P'], expInfo['sess'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Joce\\Documents\\Jocelyn\\PolyU RA\\Adaptive intertemporal discounting task\\PsychoPy_DDT_Pre_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionStim = visual.ImageStim(
    win=win,
    name='InstructionStim', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
InstructionKey = keyboard.Keyboard()

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
FixationStim = visual.ImageStim(
    win=win,
    name='FixationStim', 
    image='stimuli\\start.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
TrialStim = visual.ImageStim(
    win=win,
    name='TrialStim', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
LLStim = visual.TextStim(win=win, name='LLStim',
    text='',
    font='Arial',
    pos=[0,0], height=60, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
SSStim = visual.TextStim(win=win, name='SSStim',
    text='',
    font='Arial',
    pos=[0,0], height=60, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TrialResp = keyboard.Keyboard()

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
EndStim = visual.ImageStim(
    win=win,
    name='EndStim', 
    image='stimuli\\end.png', mask=None,
    ori=0, pos=[0, 0], size=[1500, 1125],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "testing"
testingClock = core.Clock()
testingtxt = visual.TextStim(win=win, name='testingtxt',
    text='testing before row update',
    font='Open Sans',
    pos=(0, 0), height=60.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RowUpdate"
RowUpdateClock = core.Clock()

# Initialize components for Routine "testing2"
testing2Clock = core.Clock()
testingtxt2 = visual.TextStim(win=win, name='testingtxt2',
    text='testing after row update',
    font='Open Sans',
    pos=(0, 0), height=60.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "complete"
completeClock = core.Clock()
CompleteMsg = visual.TextStim(win=win, name='CompleteMsg',
    text='This concludes the experiment. Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=60.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
DDTInst = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_DDTinst.xlsx'),
    seed=None, name='DDTInst')
thisExp.addLoop(DDTInst)  # add the loop to the experiment
thisDDTInst = DDTInst.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDDTInst.rgb)
if thisDDTInst != None:
    for paramName in thisDDTInst:
        exec('{} = thisDDTInst[paramName]'.format(paramName))

for thisDDTInst in DDTInst:
    currentLoop = DDTInst
    # abbreviate parameter names if possible (e.g. rgb = thisDDTInst.rgb)
    if thisDDTInst != None:
        for paramName in thisDDTInst:
            exec('{} = thisDDTInst[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    InstructionStim.setImage(stim)
    InstructionKey.keys = []
    InstructionKey.rt = []
    _InstructionKey_allKeys = []
    # keep track of which components have finished
    InstructionsComponents = [InstructionStim, InstructionKey]
    for thisComponent in InstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionStim* updates
        if InstructionStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionStim.frameNStart = frameN  # exact frame index
            InstructionStim.tStart = t  # local t and not account for scr refresh
            InstructionStim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionStim, 'tStartRefresh')  # time at next scr refresh
            InstructionStim.setAutoDraw(True)
        
        # *InstructionKey* updates
        waitOnFlip = False
        if InstructionKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionKey.frameNStart = frameN  # exact frame index
            InstructionKey.tStart = t  # local t and not account for scr refresh
            InstructionKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionKey, 'tStartRefresh')  # time at next scr refresh
            InstructionKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(InstructionKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(InstructionKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if InstructionKey.status == STARTED and not waitOnFlip:
            theseKeys = InstructionKey.getKeys(keyList=['space'], waitRelease=False)
            _InstructionKey_allKeys.extend(theseKeys)
            if len(_InstructionKey_allKeys):
                InstructionKey.keys = _InstructionKey_allKeys[-1].name  # just the last key pressed
                InstructionKey.rt = _InstructionKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    DDTInst.addData('InstructionStim.started', InstructionStim.tStartRefresh)
    DDTInst.addData('InstructionStim.stopped', InstructionStim.tStopRefresh)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'DDTInst'


# ------Prepare to start Routine "Initating_vars"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Initating_varsComponents = []
for thisComponent in Initating_varsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Initating_varsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Initating_vars"-------
while continueRoutine:
    # get current time
    t = Initating_varsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Initating_varsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Initating_varsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Initating_vars"-------
for thisComponent in Initating_varsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Initating_vars" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
DDTminiblocks = data.TrialHandler(nReps=100, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='DDTminiblocks')
thisExp.addLoop(DDTminiblocks)  # add the loop to the experiment
thisDDTminiblock = DDTminiblocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDDTminiblock.rgb)
if thisDDTminiblock != None:
    for paramName in thisDDTminiblock:
        exec('{} = thisDDTminiblock[paramName]'.format(paramName))

for thisDDTminiblock in DDTminiblocks:
    currentLoop = DDTminiblocks
    # abbreviate parameter names if possible (e.g. rgb = thisDDTminiblock.rgb)
    if thisDDTminiblock != None:
        for paramName in thisDDTminiblock:
            exec('{} = thisDDTminiblock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    DDTtrial = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions_DDTtask.xlsx', selection=row),
        seed=None, name='DDTtrial')
    thisExp.addLoop(DDTtrial)  # add the loop to the experiment
    thisDDTtrial = DDTtrial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisDDTtrial.rgb)
    if thisDDTtrial != None:
        for paramName in thisDDTtrial:
            exec('{} = thisDDTtrial[paramName]'.format(paramName))
    
    for thisDDTtrial in DDTtrial:
        currentLoop = DDTtrial
        # abbreviate parameter names if possible (e.g. rgb = thisDDTtrial.rgb)
        if thisDDTtrial != None:
            for paramName in thisDDTtrial:
                exec('{} = thisDDTtrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        FixationComponents = [FixationStim]
        for thisComponent in FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Fixation"-------
        while continueRoutine:
            # get current time
            t = FixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixationStim* updates
            if FixationStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixationStim.frameNStart = frameN  # exact frame index
                FixationStim.tStart = t  # local t and not account for scr refresh
                FixationStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixationStim, 'tStartRefresh')  # time at next scr refresh
                FixationStim.setAutoDraw(True)
            if FixationStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixationStim.tStartRefresh + random.uniform(1.4,1.6)-frameTolerance:
                    # keep track of stop time/frame for later
                    FixationStim.tStop = t  # not accounting for scr refresh
                    FixationStim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixationStim, 'tStopRefresh')  # time at next scr refresh
                    FixationStim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Fixation"-------
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DDTtrial.addData('FixationStim.started', FixationStim.tStartRefresh)
        DDTtrial.addData('FixationStim.stopped', FixationStim.tStopRefresh)
        # the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
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
        LLStim.setPos(llloc)
        LLStim.setText(ll)
        SSStim.setPos(ssloc)
        SSStim.setText(ss)
        TrialResp.keys = []
        TrialResp.rt = []
        _TrialResp_allKeys = []
        # keep track of which components have finished
        trialComponents = [TrialStim, LLStim, SSStim, TrialResp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrialStim* updates
            if TrialStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialStim.frameNStart = frameN  # exact frame index
                TrialStim.tStart = t  # local t and not account for scr refresh
                TrialStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialStim, 'tStartRefresh')  # time at next scr refresh
                TrialStim.setAutoDraw(True)
            
            # *LLStim* updates
            if LLStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LLStim.frameNStart = frameN  # exact frame index
                LLStim.tStart = t  # local t and not account for scr refresh
                LLStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LLStim, 'tStartRefresh')  # time at next scr refresh
                LLStim.setAutoDraw(True)
            
            # *SSStim* updates
            if SSStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SSStim.frameNStart = frameN  # exact frame index
                SSStim.tStart = t  # local t and not account for scr refresh
                SSStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SSStim, 'tStartRefresh')  # time at next scr refresh
                SSStim.setAutoDraw(True)
            
            # *TrialResp* updates
            waitOnFlip = False
            if TrialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialResp.frameNStart = frameN  # exact frame index
                TrialResp.tStart = t  # local t and not account for scr refresh
                TrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialResp, 'tStartRefresh')  # time at next scr refresh
                TrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if TrialResp.status == STARTED and not waitOnFlip:
                theseKeys = TrialResp.getKeys(keyList=['v', 'b'], waitRelease=False)
                _TrialResp_allKeys.extend(theseKeys)
                if len(_TrialResp_allKeys):
                    TrialResp.keys = _TrialResp_allKeys[-1].name  # just the last key pressed
                    TrialResp.rt = _TrialResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
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
        
        ll = ll
        DDTtrial.addData('TrialStim.started', TrialStim.tStartRefresh)
        DDTtrial.addData('TrialStim.stopped', TrialStim.tStopRefresh)
        DDTtrial.addData('LLStim.started', LLStim.tStartRefresh)
        DDTtrial.addData('LLStim.stopped', LLStim.tStopRefresh)
        DDTtrial.addData('SSStim.started', SSStim.tStartRefresh)
        DDTtrial.addData('SSStim.stopped', SSStim.tStopRefresh)
        # check responses
        if TrialResp.keys in ['', [], None]:  # No response was made
            TrialResp.keys = None
        DDTtrial.addData('TrialResp.keys',TrialResp.keys)
        if TrialResp.keys != None:  # we had a response
            DDTtrial.addData('TrialResp.rt', TrialResp.rt)
        DDTtrial.addData('TrialResp.started', TrialResp.tStartRefresh)
        DDTtrial.addData('TrialResp.stopped', TrialResp.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ITI"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [EndStim]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ITIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EndStim* updates
            if EndStim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EndStim.frameNStart = frameN  # exact frame index
                EndStim.tStart = t  # local t and not account for scr refresh
                EndStim.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EndStim, 'tStartRefresh')  # time at next scr refresh
                EndStim.setAutoDraw(True)
            if EndStim.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > EndStim.tStartRefresh + random.uniform(0.4,0.6)-frameTolerance:
                    # keep track of stop time/frame for later
                    EndStim.tStop = t  # not accounting for scr refresh
                    EndStim.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(EndStim, 'tStopRefresh')  # time at next scr refresh
                    EndStim.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        DDTtrial.addData('EndStim.started', EndStim.tStartRefresh)
        DDTtrial.addData('EndStim.stopped', EndStim.tStopRefresh)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'DDTtrial'
    
    
    # ------Prepare to start Routine "testing"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    testingComponents = [testingtxt]
    for thisComponent in testingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testingtxt* updates
        if testingtxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testingtxt.frameNStart = frameN  # exact frame index
            testingtxt.tStart = t  # local t and not account for scr refresh
            testingtxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testingtxt, 'tStartRefresh')  # time at next scr refresh
            testingtxt.setAutoDraw(True)
        if testingtxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testingtxt.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                testingtxt.tStop = t  # not accounting for scr refresh
                testingtxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testingtxt, 'tStopRefresh')  # time at next scr refresh
                testingtxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testing"-------
    for thisComponent in testingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    DDTminiblocks.addData('testingtxt.started', testingtxt.tStartRefresh)
    DDTminiblocks.addData('testingtxt.stopped', testingtxt.tStopRefresh)
    
    # ------Prepare to start Routine "RowUpdate"-------
    continueRoutine = True
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
        ## ENDING LOOP FOR INDIFFERENCE POINTS THAT HAVE BEEN REACHED
        if ip == 1: # if the ip was just reached, remove it
            row.remove(i)
        if not row:
            DDTminiblocks.finished = True
    # keep track of which components have finished
    RowUpdateComponents = []
    for thisComponent in RowUpdateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RowUpdateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RowUpdate"-------
    while continueRoutine:
        # get current time
        t = RowUpdateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RowUpdateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RowUpdateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RowUpdate"-------
    for thisComponent in RowUpdateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "RowUpdate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "testing2"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    testing2Components = [testingtxt2]
    for thisComponent in testing2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testing2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testing2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testing2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testing2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testingtxt2* updates
        if testingtxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testingtxt2.frameNStart = frameN  # exact frame index
            testingtxt2.tStart = t  # local t and not account for scr refresh
            testingtxt2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testingtxt2, 'tStartRefresh')  # time at next scr refresh
            testingtxt2.setAutoDraw(True)
        if testingtxt2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testingtxt2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                testingtxt2.tStop = t  # not accounting for scr refresh
                testingtxt2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testingtxt2, 'tStopRefresh')  # time at next scr refresh
                testingtxt2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testing2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testing2"-------
    for thisComponent in testing2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    DDTminiblocks.addData('testingtxt2.started', testingtxt2.tStartRefresh)
    DDTminiblocks.addData('testingtxt2.stopped', testingtxt2.tStopRefresh)
# completed 100 repeats of 'DDTminiblocks'


# ------Prepare to start Routine "complete"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
completeComponents = [CompleteMsg]
for thisComponent in completeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
completeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "complete"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = completeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=completeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CompleteMsg* updates
    if CompleteMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CompleteMsg.frameNStart = frameN  # exact frame index
        CompleteMsg.tStart = t  # local t and not account for scr refresh
        CompleteMsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CompleteMsg, 'tStartRefresh')  # time at next scr refresh
        CompleteMsg.setAutoDraw(True)
    if CompleteMsg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > CompleteMsg.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            CompleteMsg.tStop = t  # not accounting for scr refresh
            CompleteMsg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(CompleteMsg, 'tStopRefresh')  # time at next scr refresh
            CompleteMsg.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in completeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "complete"-------
for thisComponent in completeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('CompleteMsg.started', CompleteMsg.tStartRefresh)
thisExp.addData('CompleteMsg.stopped', CompleteMsg.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
