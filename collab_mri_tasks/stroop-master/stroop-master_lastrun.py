#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on March 06, 2024, at 11:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'stroop-master'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jocel\\Documents\\collab_mri_tasks\\stroop-master\\stroop-master_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "instructions" ---
# Run 'Begin Experiment' code from choose_trials
# Choosing trials for each condition

# congruent, match
rows1 = np.arange(4)
cond1 = np.random.choice(rows1,18,replace=True)

# incongruent, match
rows2 = np.arange(12)+4
cond2 = np.random.choice(rows2,18,replace=True)

# congruent, no match
rows3 = np.arange(12)+16
cond3 = np.random.choice(rows3,18,replace=True)

# incongruent, no match
rows4 = np.arange(36)+28
cond4 = np.random.choice(rows4,18,replace=False)

# neutral, match
rows5 = np.arange(16)+64
cond5 = np.random.choice(rows5,18,replace=True)

# neutral, no match
rows6 = np.arange(48)+80
cond6 = np.random.choice(rows6,18,replace=False)

order_idx = [0,1,2,0,1,2,0,1,2]
np.random.shuffle(order_idx)

neutral_done = 0
congruent_done = 0
incongruent_done = 0
instr_txt = visual.TextStim(win=win, name='instr_txt',
    text='你將會在熒幕上看到兩個字。\n\n如果上方的字的顔色與下方的字的意思吻合，\n請按 左鍵\n如果上方的字的顔色與下方的字的意思不吻合，\n請按 右鍵',
    font='Songti SC',
    units='height', pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prepared_resp = keyboard.Keyboard()

# --- Initialize components for Routine "trigger" ---
trigger_txt = visual.TextStim(win=win, name='trigger_txt',
    text='+',
    font='Songti SC',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trigger_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prepare" ---
prep_instr = visual.TextStim(win=win, name='prep_instr',
    text='請判斷上方的字的顔色與下方的字的意思是否吻合',
    font='Songti SC',
    pos=(-0.1, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
start_indicator = visual.TextStim(win=win, name='start_indicator',
    text='開始',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "stim" ---
top_txt = visual.TextStim(win=win, name='top_txt',
    text='',
    font='Arial',
    units='height', pos=(0, 0.2), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
bottom_txt = visual.TextStim(win=win, name='bottom_txt',
    text='',
    font='Arial',
    pos=(0, -0.2), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "iti" ---
trial_fixation = visual.TextStim(win=win, name='trial_fixation',
    text='+',
    font='Songti SC',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "rest" ---
rest_txt = visual.TextStim(win=win, name='rest_txt',
    text='保持靜止',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "complete" ---
end_txt = visual.TextStim(win=win, name='end_txt',
    text='實驗完成',
    font='Songti SC',
    units='height', pos=[0, 0], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
prepared_resp.keys = []
prepared_resp.rt = []
_prepared_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [instr_txt, prepared_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_txt* updates
    
    # if instr_txt is starting this frame...
    if instr_txt.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instr_txt.frameNStart = frameN  # exact frame index
        instr_txt.tStart = t  # local t and not account for scr refresh
        instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_txt.started')
        # update status
        instr_txt.status = STARTED
        instr_txt.setAutoDraw(True)
    
    # if instr_txt is active this frame...
    if instr_txt.status == STARTED:
        # update params
        pass
    
    # *prepared_resp* updates
    waitOnFlip = False
    
    # if prepared_resp is starting this frame...
    if prepared_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        prepared_resp.frameNStart = frameN  # exact frame index
        prepared_resp.tStart = t  # local t and not account for scr refresh
        prepared_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prepared_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prepared_resp.started')
        # update status
        prepared_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(prepared_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(prepared_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if prepared_resp.status == STARTED and not waitOnFlip:
        theseKeys = prepared_resp.getKeys(keyList=['space'], waitRelease=False)
        _prepared_resp_allKeys.extend(theseKeys)
        if len(_prepared_resp_allKeys):
            prepared_resp.keys = _prepared_resp_allKeys[-1].name  # just the last key pressed
            prepared_resp.rt = _prepared_resp_allKeys[-1].rt
            prepared_resp.duration = _prepared_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trigger" ---
continueRoutine = True
# update component parameters for each repeat
trigger_resp.keys = []
trigger_resp.rt = []
_trigger_resp_allKeys = []
# keep track of which components have finished
triggerComponents = [trigger_txt, trigger_resp]
for thisComponent in triggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "trigger" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_txt* updates
    
    # if trigger_txt is starting this frame...
    if trigger_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_txt.frameNStart = frameN  # exact frame index
        trigger_txt.tStart = t  # local t and not account for scr refresh
        trigger_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger_txt.started')
        # update status
        trigger_txt.status = STARTED
        trigger_txt.setAutoDraw(True)
    
    # if trigger_txt is active this frame...
    if trigger_txt.status == STARTED:
        # update params
        pass
    
    # *trigger_resp* updates
    waitOnFlip = False
    
    # if trigger_resp is starting this frame...
    if trigger_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_resp.frameNStart = frameN  # exact frame index
        trigger_resp.tStart = t  # local t and not account for scr refresh
        trigger_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger_resp.started')
        # update status
        trigger_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_resp.status == STARTED and not waitOnFlip:
        theseKeys = trigger_resp.getKeys(keyList=['s'], waitRelease=False)
        _trigger_resp_allKeys.extend(theseKeys)
        if len(_trigger_resp_allKeys):
            trigger_resp.keys = _trigger_resp_allKeys[-1].name  # just the last key pressed
            trigger_resp.rt = _trigger_resp_allKeys[-1].rt
            trigger_resp.duration = _trigger_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trigger" ---
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_resp.keys in ['', [], None]:  # No response was made
    trigger_resp.keys = None
thisExp.addData('trigger_resp.keys',trigger_resp.keys)
if trigger_resp.keys != None:  # we had a response
    thisExp.addData('trigger_resp.rt', trigger_resp.rt)
    thisExp.addData('trigger_resp.duration', trigger_resp.duration)
thisExp.nextEntry()
# the Routine "trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=9.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "prepare" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prep_trials
    n = block.thisN
    
    if order_idx[n] == 0:
        use_rows = cond5[neutral_done*6:neutral_done*6+6],cond6[neutral_done*6:neutral_done*6+6]
        neutral_done += 1
    elif order_idx[n] == 1:
        use_rows = cond1[congruent_done*6:congruent_done*6+6],cond3[congruent_done*6:congruent_done*6+6]
        congruent_done += 1
    elif order_idx[n] == 2:
        use_rows = cond2[incongruent_done*6:incongruent_done*6+6],cond4[incongruent_done*6:incongruent_done*6+6]
        incongruent_done += 1
    
    use_rows = np.concatenate(use_rows)
    np.random.shuffle(use_rows)
    
    # keep track of which components have finished
    prepareComponents = [prep_instr, start_indicator]
    for thisComponent in prepareComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prepare" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prep_instr* updates
        
        # if prep_instr is starting this frame...
        if prep_instr.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            prep_instr.frameNStart = frameN  # exact frame index
            prep_instr.tStart = t  # local t and not account for scr refresh
            prep_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prep_instr, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prep_instr.started')
            # update status
            prep_instr.status = STARTED
            prep_instr.setAutoDraw(True)
        
        # if prep_instr is active this frame...
        if prep_instr.status == STARTED:
            # update params
            pass
        
        # if prep_instr is stopping this frame...
        if prep_instr.status == STARTED:
            if frameN >= 120:
                # keep track of stop time/frame for later
                prep_instr.tStop = t  # not accounting for scr refresh
                prep_instr.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prep_instr.stopped')
                # update status
                prep_instr.status = FINISHED
                prep_instr.setAutoDraw(False)
        
        # *start_indicator* updates
        
        # if start_indicator is starting this frame...
        if start_indicator.status == NOT_STARTED and frameN >= 120.0:
            # keep track of start time/frame for later
            start_indicator.frameNStart = frameN  # exact frame index
            start_indicator.tStart = t  # local t and not account for scr refresh
            start_indicator.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_indicator, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_indicator.started')
            # update status
            start_indicator.status = STARTED
            start_indicator.setAutoDraw(True)
        
        # if start_indicator is active this frame...
        if start_indicator.status == STARTED:
            # update params
            pass
        
        # if start_indicator is stopping this frame...
        if start_indicator.status == STARTED:
            if frameN >= 150.0:
                # keep track of stop time/frame for later
                start_indicator.tStop = t  # not accounting for scr refresh
                start_indicator.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'start_indicator.stopped')
                # update status
                start_indicator.status = FINISHED
                start_indicator.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepareComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prepare" ---
    for thisComponent in prepareComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prepare" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialTypes.xlsx', selection=use_rows),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from this_trial
        thisExp.addData('use_rows', use_rows[trials.thisN])
        top_txt.setColor(topColour, colorSpace='rgb')
        top_txt.setText(topText)
        bottom_txt.setText(bottomText)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        stimComponents = [top_txt, bottom_txt, key_resp]
        for thisComponent in stimComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *top_txt* updates
            
            # if top_txt is starting this frame...
            if top_txt.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                top_txt.frameNStart = frameN  # exact frame index
                top_txt.tStart = t  # local t and not account for scr refresh
                top_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(top_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'top_txt.started')
                # update status
                top_txt.status = STARTED
                top_txt.setAutoDraw(True)
            
            # if top_txt is active this frame...
            if top_txt.status == STARTED:
                # update params
                pass
            
            # if top_txt is stopping this frame...
            if top_txt.status == STARTED:
                if frameN >= 120:
                    # keep track of stop time/frame for later
                    top_txt.tStop = t  # not accounting for scr refresh
                    top_txt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'top_txt.stopped')
                    # update status
                    top_txt.status = FINISHED
                    top_txt.setAutoDraw(False)
            
            # *bottom_txt* updates
            
            # if bottom_txt is starting this frame...
            if bottom_txt.status == NOT_STARTED and frameN >= 6.0:
                # keep track of start time/frame for later
                bottom_txt.frameNStart = frameN  # exact frame index
                bottom_txt.tStart = t  # local t and not account for scr refresh
                bottom_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(bottom_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'bottom_txt.started')
                # update status
                bottom_txt.status = STARTED
                bottom_txt.setAutoDraw(True)
            
            # if bottom_txt is active this frame...
            if bottom_txt.status == STARTED:
                # update params
                pass
            
            # if bottom_txt is stopping this frame...
            if bottom_txt.status == STARTED:
                if frameN >= 120.0:
                    # keep track of stop time/frame for later
                    bottom_txt.tStop = t  # not accounting for scr refresh
                    bottom_txt.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'bottom_txt.stopped')
                    # update status
                    bottom_txt.status = FINISHED
                    bottom_txt.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and frameN >= 6:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp is stopping this frame...
            if key_resp.status == STARTED:
                if frameN >= 120:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['1','2'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    key_resp.duration = _key_resp_allKeys[0].duration
                    # was this correct?
                    if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stim" ---
        for thisComponent in stimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "iti" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from trial_fix_show
        if trials.thisN == 11:
            continueRoutine = False
        # keep track of which components have finished
        itiComponents = [trial_fixation]
        for thisComponent in itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "iti" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_fixation* updates
            
            # if trial_fixation is starting this frame...
            if trial_fixation.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                trial_fixation.frameNStart = frameN  # exact frame index
                trial_fixation.tStart = t  # local t and not account for scr refresh
                trial_fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation.started')
                # update status
                trial_fixation.status = STARTED
                trial_fixation.setAutoDraw(True)
            
            # if trial_fixation is active this frame...
            if trial_fixation.status == STARTED:
                # update params
                pass
            
            # if trial_fixation is stopping this frame...
            if trial_fixation.status == STARTED:
                if frameN >= 30:
                    # keep track of stop time/frame for later
                    trial_fixation.tStop = t  # not accounting for scr refresh
                    trial_fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'trial_fixation.stopped')
                    # update status
                    trial_fixation.status = FINISHED
                    trial_fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "iti" ---
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "rest" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    restComponents = [rest_txt]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "rest" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_txt* updates
        
        # if rest_txt is starting this frame...
        if rest_txt.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            rest_txt.frameNStart = frameN  # exact frame index
            rest_txt.tStart = t  # local t and not account for scr refresh
            rest_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_txt.started')
            # update status
            rest_txt.status = STARTED
            rest_txt.setAutoDraw(True)
        
        # if rest_txt is active this frame...
        if rest_txt.status == STARTED:
            # update params
            pass
        
        # if rest_txt is stopping this frame...
        if rest_txt.status == STARTED:
            if frameN >= 1802:
                # keep track of stop time/frame for later
                rest_txt.tStop = t  # not accounting for scr refresh
                rest_txt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_txt.stopped')
                # update status
                rest_txt.status = FINISHED
                rest_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "rest" ---
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 9.0 repeats of 'block'


# --- Prepare to start Routine "complete" ---
continueRoutine = True
# update component parameters for each repeat
end_key_resp.keys = []
end_key_resp.rt = []
_end_key_resp_allKeys = []
# keep track of which components have finished
completeComponents = [end_txt, end_key_resp]
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
frameN = -1

# --- Run Routine "complete" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_txt* updates
    
    # if end_txt is starting this frame...
    if end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_txt.frameNStart = frameN  # exact frame index
        end_txt.tStart = t  # local t and not account for scr refresh
        end_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_txt.started')
        # update status
        end_txt.status = STARTED
        end_txt.setAutoDraw(True)
    
    # if end_txt is active this frame...
    if end_txt.status == STARTED:
        # update params
        pass
    
    # *end_key_resp* updates
    waitOnFlip = False
    
    # if end_key_resp is starting this frame...
    if end_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_key_resp.frameNStart = frameN  # exact frame index
        end_key_resp.tStart = t  # local t and not account for scr refresh
        end_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_key_resp.started')
        # update status
        end_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_key_resp.getKeys(keyList=['q'], waitRelease=False)
        _end_key_resp_allKeys.extend(theseKeys)
        if len(_end_key_resp_allKeys):
            end_key_resp.keys = _end_key_resp_allKeys[-1].name  # just the last key pressed
            end_key_resp.rt = _end_key_resp_allKeys[-1].rt
            end_key_resp.duration = _end_key_resp_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in completeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "complete" ---
for thisComponent in completeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_key_resp.keys in ['', [], None]:  # No response was made
    end_key_resp.keys = None
thisExp.addData('end_key_resp.keys',end_key_resp.keys)
if end_key_resp.keys != None:  # we had a response
    thisExp.addData('end_key_resp.rt', end_key_resp.rt)
    thisExp.addData('end_key_resp.duration', end_key_resp.duration)
thisExp.nextEntry()
# the Routine "complete" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
