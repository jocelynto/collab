#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on March 06, 2024, at 11:13
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
prefs.hardware['audioLatencyMode'] = '3'
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
expName = 'nback-practise'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
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
    originPath='C:\\Users\\jocel\\Documents\\collab_mri_tasks\\nback-practise\\nback-practise_lastrun.py',
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
    monitor='testMonitor', color='black', colorSpace='rgb',
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

rows1 = np.arange(48)
match_idx = np.random.choice(rows1,40,replace=False)

rows2 = np.arange(48)+48
no_match_idx = np.random.choice(rows2,40,replace=False)
instr_txt = visual.TextStim(win=win, name='instr_txt',
    text='請根據熒幕上的指示判斷\n照片是否與兩項之前的照片相符\n或\n照片是否與目標相符\n\n如果相符請按左鍵, 不相符請按右鍵\n\n準備好請按左鍵',
    font='Songti SC',
    pos=(0,0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
prepared_resp = keyboard.Keyboard()

# --- Initialize components for Routine "prepare" ---
target = visual.ImageStim(
    win=win,
    name='target', 
    image='nback_stimuli/TO_103_TOOL120_BA.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
prep_instr = visual.TextStim(win=win, name='prep_instr',
    text='',
    font='Songti SC',
    pos=[0,0], height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "iti" ---
trial_fixation = visual.TextStim(win=win, name='trial_fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "stim" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from corr_counting
corr_counter = 0

# --- Initialize components for Routine "complete" ---
end_txt = visual.TextStim(win=win, name='end_txt',
    text='實驗完成',
    font='Songti SC',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
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
    if instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    if prepared_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        theseKeys = prepared_resp.getKeys(keyList=['left'], waitRelease=False)
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
# check responses
if prepared_resp.keys in ['', [], None]:  # No response was made
    prepared_resp.keys = None
thisExp.addData('prepared_resp.keys',prepared_resp.keys)
if prepared_resp.keys != None:  # we had a response
    thisExp.addData('prepared_resp.rt', prepared_resp.rt)
    thisExp.addData('prepared_resp.duration', prepared_resp.duration)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=2.0, method='sequential', 
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
    
    use_rows = list(range(n*10,n*10+10))
    block_rules = ['2-Back','0-Back']
    block_rule = block_rules[n]
    
    if block_rule == '0-Back':
        rule_txt = '目標'
        txt_loc = (0,0.2)
        im_loc = (0,-0.1)
    elif block_rule == '2-Back':
        rule_txt = '兩項之前'
        txt_loc = (0,0)
        im_loc = (1,1)
    
    target.setPos(im_loc)
    prep_instr.setPos(txt_loc)
    prep_instr.setText(rule_txt)
    # keep track of which components have finished
    prepareComponents = [target, prep_instr]
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
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *target* updates
        
        # if target is starting this frame...
        if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target.started')
            # update status
            target.status = STARTED
            target.setAutoDraw(True)
        
        # if target is active this frame...
        if target.status == STARTED:
            # update params
            pass
        
        # if target is stopping this frame...
        if target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > target.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target.stopped')
                # update status
                target.status = FINISHED
                target.setAutoDraw(False)
        
        # *prep_instr* updates
        
        # if prep_instr is starting this frame...
        if prep_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prep_instr.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                prep_instr.tStop = t  # not accounting for scr refresh
                prep_instr.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prep_instr.stopped')
                # update status
                prep_instr.status = FINISHED
                prep_instr.setAutoDraw(False)
        
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
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trialTypes_practise.xlsx', selection=use_rows),
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
        
        # --- Prepare to start Routine "iti" ---
        continueRoutine = True
        # update component parameters for each repeat
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
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trial_fixation* updates
            
            # if trial_fixation is starting this frame...
            if trial_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_fixation.tStartRefresh + 0.5-frameTolerance:
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from this_trial
        trial_im = 'nback_stimuli/'+Stimulus
        image.setImage(trial_im)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        stimComponents = [image, key_resp]
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
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.stopped')
                    # update status
                    key_resp.status = FINISHED
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    key_resp.duration = _key_resp_allKeys[0].duration
            
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
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from corr_counting
        try:
            if key_resp.keys == 'left':
                if CorrectResponse == 'target':
                    thisExp.addData('corr_var', 1)
                    corr_counter += 1
                elif CorrectResponse == 'nontarget':
                    thisExp.addData('corr_var', 0)
            elif key_resp.keys == 'right':
                if CorrectResponse == 'target':
                    thisExp.addData('corr_var', 0)
                elif CorrectResponse == 'nontarget':
                    thisExp.addData('corr_var', 1)
                    corr_counter += 1
        except TypeError:
            thisExp.addData('corr_var', 0)
        
        if int(trials.thisN) == 9:
            print('counter', BlockType, '=', corr_counter)
            corr_counter = 0
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'block'


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
# Run 'End Experiment' code from corr_counting
print("counter = ", corr_counter, "/20")

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
