#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on December 18, 2023, at 10:22
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
expName = 'Wisconsin Card Sorting Task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\Joce\\Documents\\Jocelyn\\PolyU RA\\wisconsin-card-sorting-task-master\\Wisconsin Card Sorting Task_lastrun.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
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
# MRI TR
TR = 1.6

# ISI for each trial
import pandas as pd
timings = pd.read_excel('timings_wisconsin.xlsx')
timings = timings['Timings'].tolist()

# Initialize trial
print('initialize first trial vars')
rules = [0, 1, 2]
corr_counter = 0
rule_switch_counter = 0
rule_idx = np.random.choice(rules)
trials_per_rule = np.random.randint(4,7)
useRows = np.arange(64) + int(64 * rule_idx)
iti = 0
trial_counter = 0
instructions = visual.TextStim(win=win, name='instructions',
    text='In this task you will be required to sort the presented cards based on a rule i.e. the cards will have to be sorted based on either colour, shape or number. The rule will not be presented, however you will receive feedback on each trial. After a certain amount of trials the rule will change to a different one. To select your response click on one of the four cards presented at the top of the screen. ',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=.9, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Example"
ExampleClock = core.Clock()
example_text = visual.TextStim(win=win, name='example_text',
    text='For example, you may see a screen like this:',
    font='Arial',
    pos=(0, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
example_image = visual.ImageStim(
    win=win,
    name='example_image', 
    image='example.jpg', mask=None,
    ori=0, pos=(0, 0.15), size=(0.7, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
example_text_2 = visual.TextStim(win=win, name='example_text_2',
    text='The presented card (bottom centre) can be categorised based on shape (dots), colour (yellow) or number (three). Click on the first card if you want to categorise it by the shape, second if you want categorise it by colour and third if you want to categorise it by number. After you select your response, feedback will be provided. Click on the image to start the experiment.',
    font='Arial',
    pos=(0, -0.25), height=0.04, wrapWidth=.9, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Choose_rule"
Choose_ruleClock = core.Clock()

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Trials"
TrialsClock = core.Clock()
one_red_dot = visual.ImageStim(
    win=win,
    name='one_red_dot', 
    image='images/1redDot.jpg', mask=None,
    ori=0, pos=(-0.375, 0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
two_yellow_triangles = visual.ImageStim(
    win=win,
    name='two_yellow_triangles', 
    image='images/2yellowTriangles.jpg', mask=None,
    ori=0, pos=(-0.125, 0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
three_green_crosses = visual.ImageStim(
    win=win,
    name='three_green_crosses', 
    image='images/3greenCrosses.jpg', mask=None,
    ori=0, pos=(0.125, 0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
four_blue_stars = visual.ImageStim(
    win=win,
    name='four_blue_stars', 
    image='images/4blueStars.jpg', mask=None,
    ori=0, pos=(0.375, 0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trial_card = visual.ImageStim(
    win=win,
    name='trial_card', 
    image='sin', mask=None,
    ori=0, pos=(0, -0.2), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
response = keyboard.Keyboard()

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
msg = ''
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Songti SC',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "End"
EndClock = core.Clock()
thank_you = visual.TextStim(win=win, name='thank_you',
    text='This is the end of the experiment.\nThank you for your time.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructions, key_resp]
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
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
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
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Example"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
ExampleComponents = [example_text, example_image, example_text_2, key_resp_2]
for thisComponent in ExampleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ExampleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Example"-------
while continueRoutine:
    # get current time
    t = ExampleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ExampleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *example_text* updates
    if example_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_text.frameNStart = frameN  # exact frame index
        example_text.tStart = t  # local t and not account for scr refresh
        example_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_text, 'tStartRefresh')  # time at next scr refresh
        example_text.setAutoDraw(True)
    
    # *example_image* updates
    if example_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_image.frameNStart = frameN  # exact frame index
        example_image.tStart = t  # local t and not account for scr refresh
        example_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_image, 'tStartRefresh')  # time at next scr refresh
        example_image.setAutoDraw(True)
    
    # *example_text_2* updates
    if example_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_text_2.frameNStart = frameN  # exact frame index
        example_text_2.tStart = t  # local t and not account for scr refresh
        example_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_text_2, 'tStartRefresh')  # time at next scr refresh
        example_text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ExampleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Example"-------
for thisComponent in ExampleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('example_text.started', example_text.tStartRefresh)
thisExp.addData('example_text.stopped', example_text.tStopRefresh)
thisExp.addData('example_image.started', example_image.tStartRefresh)
thisExp.addData('example_image.stopped', example_image.tStopRefresh)
thisExp.addData('example_text_2.started', example_text_2.tStartRefresh)
thisExp.addData('example_text_2.stopped', example_text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Example" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=80, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "Choose_rule"-------
    continueRoutine = True
    # update component parameters for each repeat
    rules = [0, 1, 2]
    iti = 0
    
    print('changing rule')
    thisExp.addData('TR', 1.6)
    corr_counter = 0
    rule_switch_counter += 1
    rules.remove(rule_idx)
    rule_idx = np.random.choice(rules)
    trials_per_rule = np.random.randint(4,7)
    useRows = np.arange(64) + int(64 * rule_idx)
    
    # keep track of which components have finished
    Choose_ruleComponents = []
    for thisComponent in Choose_ruleComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Choose_ruleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Choose_rule"-------
    while continueRoutine:
        # get current time
        t = Choose_ruleClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Choose_ruleClock)
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
        for thisComponent in Choose_ruleComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choose_rule"-------
    for thisComponent in Choose_ruleComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Choose_rule" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trial_by_rule = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('cards.xlsx', selection=useRows),
        seed=None, name='trial_by_rule')
    thisExp.addLoop(trial_by_rule)  # add the loop to the experiment
    thisTrial_by_rule = trial_by_rule.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_by_rule.rgb)
    if thisTrial_by_rule != None:
        for paramName in thisTrial_by_rule:
            exec('{} = thisTrial_by_rule[paramName]'.format(paramName))
    
    for thisTrial_by_rule in trial_by_rule:
        currentLoop = trial_by_rule
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_by_rule.rgb)
        if thisTrial_by_rule != None:
            for paramName in thisTrial_by_rule:
                exec('{} = thisTrial_by_rule[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "jitter"-------
        continueRoutine = True
        # update component parameters for each repeat
        if trial_by_rule.thisN == 0:
            iti = timings[trial_counter] + TR
        else:
            iti = timings[trial_counter]
        
        thisExp.addData('ITI', iti)
        
        # keep track of which components have finished
        jitterComponents = [fixation]
        for thisComponent in jitterComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        jitterClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "jitter"-------
        while continueRoutine:
            # get current time
            t = jitterClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=jitterClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + iti-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                    fixation.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in jitterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "jitter"-------
        for thisComponent in jitterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_by_rule.addData('fixation.started', fixation.tStartRefresh)
        trial_by_rule.addData('fixation.stopped', fixation.tStopRefresh)
        # the Routine "jitter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Trials"-------
        continueRoutine = True
        routineTimer.add(3.500000)
        # update component parameters for each repeat
        thisExp.addData('useRows', useRows[trials.thisN])
        
        trial_counter += 1
        thisExp.addData('trial_num', trial_counter)
        
        corr = 0
        rt = 0
        trial_card.setImage(card)
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        TrialsComponents = [one_red_dot, two_yellow_triangles, three_green_crosses, four_blue_stars, trial_card, response]
        for thisComponent in TrialsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Trials"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = TrialsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrialsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # RT more accurate in Each Frame
            rt = round(t*1000)
            
            # *one_red_dot* updates
            if one_red_dot.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                one_red_dot.frameNStart = frameN  # exact frame index
                one_red_dot.tStart = t  # local t and not account for scr refresh
                one_red_dot.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(one_red_dot, 'tStartRefresh')  # time at next scr refresh
                one_red_dot.setAutoDraw(True)
            if one_red_dot.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > one_red_dot.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    one_red_dot.tStop = t  # not accounting for scr refresh
                    one_red_dot.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(one_red_dot, 'tStopRefresh')  # time at next scr refresh
                    one_red_dot.setAutoDraw(False)
            
            # *two_yellow_triangles* updates
            if two_yellow_triangles.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                two_yellow_triangles.frameNStart = frameN  # exact frame index
                two_yellow_triangles.tStart = t  # local t and not account for scr refresh
                two_yellow_triangles.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_yellow_triangles, 'tStartRefresh')  # time at next scr refresh
                two_yellow_triangles.setAutoDraw(True)
            if two_yellow_triangles.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > two_yellow_triangles.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    two_yellow_triangles.tStop = t  # not accounting for scr refresh
                    two_yellow_triangles.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(two_yellow_triangles, 'tStopRefresh')  # time at next scr refresh
                    two_yellow_triangles.setAutoDraw(False)
            
            # *three_green_crosses* updates
            if three_green_crosses.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                three_green_crosses.frameNStart = frameN  # exact frame index
                three_green_crosses.tStart = t  # local t and not account for scr refresh
                three_green_crosses.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(three_green_crosses, 'tStartRefresh')  # time at next scr refresh
                three_green_crosses.setAutoDraw(True)
            if three_green_crosses.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > three_green_crosses.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    three_green_crosses.tStop = t  # not accounting for scr refresh
                    three_green_crosses.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(three_green_crosses, 'tStopRefresh')  # time at next scr refresh
                    three_green_crosses.setAutoDraw(False)
            
            # *four_blue_stars* updates
            if four_blue_stars.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                four_blue_stars.frameNStart = frameN  # exact frame index
                four_blue_stars.tStart = t  # local t and not account for scr refresh
                four_blue_stars.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(four_blue_stars, 'tStartRefresh')  # time at next scr refresh
                four_blue_stars.setAutoDraw(True)
            if four_blue_stars.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > four_blue_stars.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    four_blue_stars.tStop = t  # not accounting for scr refresh
                    four_blue_stars.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(four_blue_stars, 'tStopRefresh')  # time at next scr refresh
                    four_blue_stars.setAutoDraw(False)
            
            # *trial_card* updates
            if trial_card.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                trial_card.frameNStart = frameN  # exact frame index
                trial_card.tStart = t  # local t and not account for scr refresh
                trial_card.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_card, 'tStartRefresh')  # time at next scr refresh
                trial_card.setAutoDraw(True)
            if trial_card.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trial_card.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    trial_card.tStop = t  # not accounting for scr refresh
                    trial_card.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trial_card, 'tStopRefresh')  # time at next scr refresh
                    trial_card.setAutoDraw(False)
            
            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response.tStartRefresh + 3.5-frameTolerance:
                    # keep track of stop time/frame for later
                    response.tStop = t  # not accounting for scr refresh
                    response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                    response.status = FINISHED
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trials"-------
        for thisComponent in TrialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_resp = int(response.keys)
        
        if trial_resp == corrAns:
            corr = 1
        
        thisExp.addData('Score', corr)
        thisExp.addData('RT', rt)
        trial_by_rule.addData('one_red_dot.started', one_red_dot.tStartRefresh)
        trial_by_rule.addData('one_red_dot.stopped', one_red_dot.tStopRefresh)
        trial_by_rule.addData('two_yellow_triangles.started', two_yellow_triangles.tStartRefresh)
        trial_by_rule.addData('two_yellow_triangles.stopped', two_yellow_triangles.tStopRefresh)
        trial_by_rule.addData('three_green_crosses.started', three_green_crosses.tStartRefresh)
        trial_by_rule.addData('three_green_crosses.stopped', three_green_crosses.tStopRefresh)
        trial_by_rule.addData('four_blue_stars.started', four_blue_stars.tStartRefresh)
        trial_by_rule.addData('four_blue_stars.stopped', four_blue_stars.tStopRefresh)
        trial_by_rule.addData('trial_card.started', trial_card.tStartRefresh)
        trial_by_rule.addData('trial_card.stopped', trial_card.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
        trial_by_rule.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trial_by_rule.addData('response.rt', response.rt)
        trial_by_rule.addData('response.started', response.tStartRefresh)
        trial_by_rule.addData('response.stopped', response.tStopRefresh)
        
        # ------Prepare to start Routine "Feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if corr == 1:
            msg="正確"
            corr_counter += 1
        else:
            msg="錯誤"
        feedback_text.setText(msg)
        # keep track of which components have finished
        FeedbackComponents = [feedback_text]
        for thisComponent in FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(True)
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if corr_counter == trials_per_rule:
            trial_by_rule.finished = True
        
        if trial_counter == 80:
            trial_by_rule.finished = True
            trials.finished = True
        trial_by_rule.addData('feedback_text.started', feedback_text.tStartRefresh)
        trial_by_rule.addData('feedback_text.stopped', feedback_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trial_by_rule'
    
    thisExp.nextEntry()
    
# completed 80 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [thank_you]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        thank_you.setAutoDraw(True)
    if thank_you.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            thank_you.tStop = t  # not accounting for scr refresh
            thank_you.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thank_you, 'tStopRefresh')  # time at next scr refresh
            thank_you.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thank_you.started', thank_you.tStartRefresh)
thisExp.addData('thank_you.stopped', thank_you.tStopRefresh)

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
