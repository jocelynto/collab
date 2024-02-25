#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on February 21, 2024, at 18:22
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
expName = 'nback-master-final'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\jocel\\Documents\\Collab project Marco Pang\\nback-master-final\\nback-master-final_lastrun.py',
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

# --- Initialize components for Routine "trigger" ---
# Run 'Begin Experiment' code from choose_trials
import numpy as np
import pandas as pd

# Choosing random runs from the 8 E-Prime runs
run_idx = np.random.choice(8,2,replace=False)
#print("run_idx", run_idx)

# Initializing indices from the .xlsx stim schedule
run_idx_1 = list(range(80*run_idx[0],80*run_idx[0]+80))
run_idx_2 = list(range(80*run_idx[1],80*run_idx[1]+80))
run_rows = run_idx_1 + run_idx_2

# Initializing target pics
dataframe = pd.read_excel("trialTypes_nback.xlsx")

rules_ls_1 = dataframe.loc[dataframe['Run'] == run_idx[0]+1, 'BlockType'].tolist() # if the code doesn't work try changing this to .to_list()
rules_ls_2 = dataframe.loc[dataframe['Run'] == run_idx[1]+1, 'BlockType'].tolist() # if the code doesn't work try changing this to .to_list()
rules_ls = rules_ls_1[0::10] + rules_ls_2[0::10]

target_ls = []
for idx, rule in enumerate(rules_ls):
    if rule == '2-Back':
        target_stim_name = dataframe['Stimulus'][run_rows[10*idx]]
    elif rule == '0-Back':
        min_range = min(run_rows[10*idx:10*idx+10])
        max_range = max(run_rows[10*idx:10*idx+10])
        # print(min_range,max_range)
        target_stim_name = dataframe[min_range:max_range].loc[dataframe['CorrectResponse'] == 'target','Stimulus'].iloc[0]        
    target_ls.append(target_stim_name)

# Initializing stim pics from the 2 runs
stim_run_1 = dataframe.loc[dataframe['Run'] == run_idx[0]+1, 'Stimulus'].tolist()
stim_run_2 = dataframe.loc[dataframe['Run'] == run_idx[1]+1, 'Stimulus'].tolist()

stim_run_1 = ['nback_stimuli/'+str(i) for i in stim_run_1]
stim_run_2 = ['nback_stimuli/'+str(i) for i in stim_run_2]

stim_block_1 = []
stim_block_2 = []

for i in range(0, 80, 20):
    stim_block_1.extend(stim_run_1[i:i+10])
    stim_block_2.extend(stim_run_1[i+10:i+20])

for i in range(0, 80, 20):
    stim_block_1.extend(stim_run_2[i:i+10])
    stim_block_2.extend(stim_run_2[i+10:i+20])
trigger_txt = visual.TextStim(win=win, name='trigger_txt',
    text='實驗即將開始',
    font='Songti SC',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trigger_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instructions" ---
instr_txt = visual.TextStim(win=win, name='instr_txt',
    text="請根據熒幕上的指示判斷\n照片是否與兩項之前的照片相符\n或\n照片是否與目標相符\n\n如果相符請按'1', 不相符請按 '2' \n\n準備好請按 '1' ",
    font='Songti SC',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
prepared_resp = keyboard.Keyboard()
prep_instr_0_1 = visual.TextStim(win=win, name='prep_instr_0_1',
    text='',
    font='Songti SC',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
target_0_1 = visual.ImageStim(
    win=win,
    name='target_0_1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
trial_fixation_0_1 = visual.TextStim(win=win, name='trial_fixation_0_1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
image_0_1 = visual.ImageStim(
    win=win,
    name='image_0_1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
key_resp_0_1 = keyboard.Keyboard()
trial_fixation_0_2 = visual.TextStim(win=win, name='trial_fixation_0_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
image_0_2 = visual.ImageStim(
    win=win,
    name='image_0_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
key_resp_0_2 = keyboard.Keyboard()
trial_fixation_0_3 = visual.TextStim(win=win, name='trial_fixation_0_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
image_0_3 = visual.ImageStim(
    win=win,
    name='image_0_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
key_resp_0_3 = keyboard.Keyboard()
trial_fixation_0_4 = visual.TextStim(win=win, name='trial_fixation_0_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
image_0_4 = visual.ImageStim(
    win=win,
    name='image_0_4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
key_resp_0_4 = keyboard.Keyboard()
trial_fixation_0_5 = visual.TextStim(win=win, name='trial_fixation_0_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-19.0);
image_0_5 = visual.ImageStim(
    win=win,
    name='image_0_5', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
key_resp_0_5 = keyboard.Keyboard()
trial_fixation_0_6 = visual.TextStim(win=win, name='trial_fixation_0_6',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-22.0);
image_0_6 = visual.ImageStim(
    win=win,
    name='image_0_6', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
key_resp_0_6 = keyboard.Keyboard()
trial_fixation_0_7 = visual.TextStim(win=win, name='trial_fixation_0_7',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-25.0);
image_0_7 = visual.ImageStim(
    win=win,
    name='image_0_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-26.0)
key_resp_0_7 = keyboard.Keyboard()
trial_fixation_0_8 = visual.TextStim(win=win, name='trial_fixation_0_8',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-28.0);
image_0_8 = visual.ImageStim(
    win=win,
    name='image_0_8', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-29.0)
key_resp_0_8 = keyboard.Keyboard()
trial_fixation_0_9 = visual.TextStim(win=win, name='trial_fixation_0_9',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-31.0);
image_0_9 = visual.ImageStim(
    win=win,
    name='image_0_9', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-32.0)
key_resp_0_9 = keyboard.Keyboard()
trial_fixation_0_10 = visual.TextStim(win=win, name='trial_fixation_0_10',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-34.0);
image_0_10 = visual.ImageStim(
    win=win,
    name='image_0_10', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-35.0)
key_resp_0_10 = keyboard.Keyboard()
prep_instr_0_2 = visual.TextStim(win=win, name='prep_instr_0_2',
    text='',
    font='Songti SC',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-37.0);
target_0_2 = visual.ImageStim(
    win=win,
    name='target_0_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-38.0)
trial_fixation_3_1 = visual.TextStim(win=win, name='trial_fixation_3_1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-39.0);
image_3_1 = visual.ImageStim(
    win=win,
    name='image_3_1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-40.0)
key_resp_3_1 = keyboard.Keyboard()
trial_fixation_3_2 = visual.TextStim(win=win, name='trial_fixation_3_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-42.0);
image_3_2 = visual.ImageStim(
    win=win,
    name='image_3_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-43.0)
key_resp_3_2 = keyboard.Keyboard()
trial_fixation_3_3 = visual.TextStim(win=win, name='trial_fixation_3_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-45.0);
image_3_3 = visual.ImageStim(
    win=win,
    name='image_3_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-46.0)
key_resp_3_3 = keyboard.Keyboard()
trial_fixation_3_4 = visual.TextStim(win=win, name='trial_fixation_3_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-48.0);
image_3_4 = visual.ImageStim(
    win=win,
    name='image_3_4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-49.0)
key_resp_3_4 = keyboard.Keyboard()
trial_fixation_3_5 = visual.TextStim(win=win, name='trial_fixation_3_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-51.0);
image_3_5 = visual.ImageStim(
    win=win,
    name='image_3_5', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-52.0)
key_resp_3_5 = keyboard.Keyboard()
trial_fixation_3_6 = visual.TextStim(win=win, name='trial_fixation_3_6',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-54.0);
image_3_6 = visual.ImageStim(
    win=win,
    name='image_3_6', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-55.0)
key_resp_3_6 = keyboard.Keyboard()
trial_fixation_3_7 = visual.TextStim(win=win, name='trial_fixation_3_7',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-57.0);
image_3_7 = visual.ImageStim(
    win=win,
    name='image_3_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-58.0)
key_resp_3_7 = keyboard.Keyboard()
trial_fixation_3_8 = visual.TextStim(win=win, name='trial_fixation_3_8',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-60.0);
image_3_8 = visual.ImageStim(
    win=win,
    name='image_3_8', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-61.0)
key_resp_3_8 = keyboard.Keyboard()
trial_fixation_3_9 = visual.TextStim(win=win, name='trial_fixation_3_9',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-63.0);
image_3_9 = visual.ImageStim(
    win=win,
    name='image_3_9', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-64.0)
key_resp_3_9 = keyboard.Keyboard()
trial_fixation_3_10 = visual.TextStim(win=win, name='trial_fixation_3_10',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-66.0);
image_3_10 = visual.ImageStim(
    win=win,
    name='image_3_10', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-67.0)
key_resp_3_10 = keyboard.Keyboard()

# --- Initialize components for Routine "stim_block" ---
rest_txt_1 = visual.TextStim(win=win, name='rest_txt_1',
    text='休息',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
prep_instr_1 = visual.TextStim(win=win, name='prep_instr_1',
    text='',
    font='Songti SC',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
target_1 = visual.ImageStim(
    win=win,
    name='target_1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
trial_fixation_1_1 = visual.TextStim(win=win, name='trial_fixation_1_1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
image_1_1 = visual.ImageStim(
    win=win,
    name='image_1_1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
key_resp_1_1 = keyboard.Keyboard()
trial_fixation_1_2 = visual.TextStim(win=win, name='trial_fixation_1_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
image_1_2 = visual.ImageStim(
    win=win,
    name='image_1_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
key_resp_1_2 = keyboard.Keyboard()
trial_fixation_1_3 = visual.TextStim(win=win, name='trial_fixation_1_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
image_1_3 = visual.ImageStim(
    win=win,
    name='image_1_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
key_resp_1_3 = keyboard.Keyboard()
trial_fixation_1_4 = visual.TextStim(win=win, name='trial_fixation_1_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
image_1_4 = visual.ImageStim(
    win=win,
    name='image_1_4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
key_resp_1_4 = keyboard.Keyboard()
trial_fixation_1_5 = visual.TextStim(win=win, name='trial_fixation_1_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
image_1_5 = visual.ImageStim(
    win=win,
    name='image_1_5', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
key_resp_1_5 = keyboard.Keyboard()
trial_fixation_1_6 = visual.TextStim(win=win, name='trial_fixation_1_6',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-20.0);
image_1_6 = visual.ImageStim(
    win=win,
    name='image_1_6', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
key_resp_1_6 = keyboard.Keyboard()
trial_fixation_1_7 = visual.TextStim(win=win, name='trial_fixation_1_7',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-23.0);
image_1_7 = visual.ImageStim(
    win=win,
    name='image_1_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
key_resp_1_7 = keyboard.Keyboard()
trial_fixation_1_8 = visual.TextStim(win=win, name='trial_fixation_1_8',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-26.0);
image_1_8 = visual.ImageStim(
    win=win,
    name='image_1_8', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-27.0)
key_resp_1_8 = keyboard.Keyboard()
trial_fixation_1_9 = visual.TextStim(win=win, name='trial_fixation_1_9',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-29.0);
image_1_9 = visual.ImageStim(
    win=win,
    name='image_1_9', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-30.0)
key_resp_1_9 = keyboard.Keyboard()
trial_fixation_1_10 = visual.TextStim(win=win, name='trial_fixation_1_10',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-32.0);
image_1_10 = visual.ImageStim(
    win=win,
    name='image_1_10', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-33.0)
key_resp_1_10 = keyboard.Keyboard()
prep_instr_2 = visual.TextStim(win=win, name='prep_instr_2',
    text='',
    font='Songti SC',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-35.0);
target_2 = visual.ImageStim(
    win=win,
    name='target_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-36.0)
trial_fixation_2_1 = visual.TextStim(win=win, name='trial_fixation_2_1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-37.0);
image_2_1 = visual.ImageStim(
    win=win,
    name='image_2_1', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-38.0)
key_resp_2_1 = keyboard.Keyboard()
trial_fixation_2_2 = visual.TextStim(win=win, name='trial_fixation_2_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-40.0);
image_2_2 = visual.ImageStim(
    win=win,
    name='image_2_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-41.0)
key_resp_2_2 = keyboard.Keyboard()
trial_fixation_2_3 = visual.TextStim(win=win, name='trial_fixation_2_3',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-43.0);
image_2_3 = visual.ImageStim(
    win=win,
    name='image_2_3', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-44.0)
key_resp_2_3 = keyboard.Keyboard()
trial_fixation_2_4 = visual.TextStim(win=win, name='trial_fixation_2_4',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-46.0);
image_2_4 = visual.ImageStim(
    win=win,
    name='image_2_4', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-47.0)
key_resp_2_4 = keyboard.Keyboard()
trial_fixation_2_5 = visual.TextStim(win=win, name='trial_fixation_2_5',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-49.0);
image_2_5 = visual.ImageStim(
    win=win,
    name='image_2_5', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-50.0)
key_resp_2_5 = keyboard.Keyboard()
trial_fixation_2_6 = visual.TextStim(win=win, name='trial_fixation_2_6',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-52.0);
image_2_6 = visual.ImageStim(
    win=win,
    name='image_2_6', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-53.0)
key_resp_2_6 = keyboard.Keyboard()
trial_fixation_2_7 = visual.TextStim(win=win, name='trial_fixation_2_7',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-55.0);
image_2_7 = visual.ImageStim(
    win=win,
    name='image_2_7', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-56.0)
key_resp_2_7 = keyboard.Keyboard()
trial_fixation_2_8 = visual.TextStim(win=win, name='trial_fixation_2_8',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-58.0);
image_2_8 = visual.ImageStim(
    win=win,
    name='image_2_8', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-59.0)
key_resp_2_8 = keyboard.Keyboard()
trial_fixation_2_9 = visual.TextStim(win=win, name='trial_fixation_2_9',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-61.0);
image_2_9 = visual.ImageStim(
    win=win,
    name='image_2_9', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-62.0)
key_resp_2_9 = keyboard.Keyboard()
trial_fixation_2_10 = visual.TextStim(win=win, name='trial_fixation_2_10',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-64.0);
image_2_10 = visual.ImageStim(
    win=win,
    name='image_2_10', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-65.0)
key_resp_2_10 = keyboard.Keyboard()

# --- Initialize components for Routine "rest" ---
rest_txt_2 = visual.TextStim(win=win, name='rest_txt_2',
    text='休息',
    font='Songti SC',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

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

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from prep_trials_0_1
n = 0

im_file_1 = stim_block_1[n*10]
im_file_2 = stim_block_1[n*10+1]
im_file_3 = stim_block_1[n*10+2]
im_file_4 = stim_block_1[n*10+3]
im_file_5 = stim_block_1[n*10+4]
im_file_6 = stim_block_1[n*10+5]
im_file_7 = stim_block_1[n*10+6]
im_file_8 = stim_block_1[n*10+7]
im_file_9 = stim_block_1[n*10+8]
im_file_10 = stim_block_1[n*10+9]

target_im_1 = 'nback_stimuli/'+target_ls[n*2]
block_rule_1 = rules_ls[n*2]

if block_rule_1 == '0-Back':
    rule_txt_1 = '目標'
    txt_loc_1 = (0,0.2)
    im_loc_1 = (0,-0.1)
elif block_rule_1 == '2-Back':
    rule_txt_1 = '兩項之前'
    txt_loc_1 = (0,0)
    im_loc_1 = (1,1)

thisExp.addData('run_no', run_idx[n//4])
# Run 'Begin Routine' code from prep_trials_0_2
n = 0
im_file_2_1 = stim_block_2[n*10]
im_file_2_2 = stim_block_2[n*10+1]
im_file_2_3 = stim_block_2[n*10+2]
im_file_2_4 = stim_block_2[n*10+3]
im_file_2_5 = stim_block_2[n*10+4]
im_file_2_6 = stim_block_2[n*10+5]
im_file_2_7 = stim_block_2[n*10+6]
im_file_2_8 = stim_block_2[n*10+7]
im_file_2_9 = stim_block_2[n*10+8]
im_file_2_10 = stim_block_2[n*10+9]

target_im_2 = 'nback_stimuli/'+target_ls[n*2+1]
block_rule_2 = rules_ls[n*2+1]

if block_rule_2 == '0-Back':
    rule_txt_2 = '目標'
    txt_loc_2 = (0,0.2)
    im_loc_2 = (0,-0.1)
elif block_rule_2 == '2-Back':
    rule_txt_2 = '兩項之前'
    txt_loc_2 = (0,0)
    im_loc_2 = (1,1)
prepared_resp.keys = []
prepared_resp.rt = []
_prepared_resp_allKeys = []
prep_instr_0_1.setPos(txt_loc_1)
prep_instr_0_1.setText(rule_txt_1)
target_0_1.setPos(im_loc_1)
target_0_1.setImage(target_im_1)
image_0_1.setImage(im_file_1)
key_resp_0_1.keys = []
key_resp_0_1.rt = []
_key_resp_0_1_allKeys = []
image_0_2.setImage(im_file_2)
key_resp_0_2.keys = []
key_resp_0_2.rt = []
_key_resp_0_2_allKeys = []
image_0_3.setImage(im_file_3)
key_resp_0_3.keys = []
key_resp_0_3.rt = []
_key_resp_0_3_allKeys = []
image_0_4.setImage(im_file_4)
key_resp_0_4.keys = []
key_resp_0_4.rt = []
_key_resp_0_4_allKeys = []
image_0_5.setImage(im_file_5)
key_resp_0_5.keys = []
key_resp_0_5.rt = []
_key_resp_0_5_allKeys = []
image_0_6.setImage(im_file_6)
key_resp_0_6.keys = []
key_resp_0_6.rt = []
_key_resp_0_6_allKeys = []
image_0_7.setImage(im_file_7)
key_resp_0_7.keys = []
key_resp_0_7.rt = []
_key_resp_0_7_allKeys = []
image_0_8.setImage(im_file_8)
key_resp_0_8.keys = []
key_resp_0_8.rt = []
_key_resp_0_8_allKeys = []
image_0_9.setImage(im_file_9)
key_resp_0_9.keys = []
key_resp_0_9.rt = []
_key_resp_0_9_allKeys = []
image_0_10.setImage(im_file_10)
key_resp_0_10.keys = []
key_resp_0_10.rt = []
_key_resp_0_10_allKeys = []
prep_instr_0_2.setPos(txt_loc_2)
prep_instr_0_2.setText(rule_txt_2)
target_0_2.setPos(im_loc_2)
target_0_2.setImage(target_im_2)
image_3_1.setImage(im_file_2_1)
key_resp_3_1.keys = []
key_resp_3_1.rt = []
_key_resp_3_1_allKeys = []
image_3_2.setImage(im_file_2_2)
key_resp_3_2.keys = []
key_resp_3_2.rt = []
_key_resp_3_2_allKeys = []
image_3_3.setImage(im_file_2_3)
key_resp_3_3.keys = []
key_resp_3_3.rt = []
_key_resp_3_3_allKeys = []
image_3_4.setImage(im_file_2_4)
key_resp_3_4.keys = []
key_resp_3_4.rt = []
_key_resp_3_4_allKeys = []
image_3_5.setImage(im_file_2_5)
key_resp_3_5.keys = []
key_resp_3_5.rt = []
_key_resp_3_5_allKeys = []
image_3_6.setImage(im_file_2_6)
key_resp_3_6.keys = []
key_resp_3_6.rt = []
_key_resp_3_6_allKeys = []
image_3_7.setImage(im_file_2_7)
key_resp_3_7.keys = []
key_resp_3_7.rt = []
_key_resp_3_7_allKeys = []
image_3_8.setImage(im_file_2_8)
key_resp_3_8.keys = []
key_resp_3_8.rt = []
_key_resp_3_8_allKeys = []
image_3_9.setImage(im_file_2_9)
key_resp_3_9.keys = []
key_resp_3_9.rt = []
_key_resp_3_9_allKeys = []
image_3_10.setImage(im_file_2_10)
key_resp_3_10.keys = []
key_resp_3_10.rt = []
_key_resp_3_10_allKeys = []
# keep track of which components have finished
instructionsComponents = [instr_txt, prepared_resp, prep_instr_0_1, target_0_1, trial_fixation_0_1, image_0_1, key_resp_0_1, trial_fixation_0_2, image_0_2, key_resp_0_2, trial_fixation_0_3, image_0_3, key_resp_0_3, trial_fixation_0_4, image_0_4, key_resp_0_4, trial_fixation_0_5, image_0_5, key_resp_0_5, trial_fixation_0_6, image_0_6, key_resp_0_6, trial_fixation_0_7, image_0_7, key_resp_0_7, trial_fixation_0_8, image_0_8, key_resp_0_8, trial_fixation_0_9, image_0_9, key_resp_0_9, trial_fixation_0_10, image_0_10, key_resp_0_10, prep_instr_0_2, target_0_2, trial_fixation_3_1, image_3_1, key_resp_3_1, trial_fixation_3_2, image_3_2, key_resp_3_2, trial_fixation_3_3, image_3_3, key_resp_3_3, trial_fixation_3_4, image_3_4, key_resp_3_4, trial_fixation_3_5, image_3_5, key_resp_3_5, trial_fixation_3_6, image_3_6, key_resp_3_6, trial_fixation_3_7, image_3_7, key_resp_3_7, trial_fixation_3_8, image_3_8, key_resp_3_8, trial_fixation_3_9, image_3_9, key_resp_3_9, trial_fixation_3_10, image_3_10, key_resp_3_10]
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
    # Run 'Each Frame' code from prepared
    prepared_continue = False
    if prepared_resp.getKeys(keyList=['1']):
        prepared_continue = True
    
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
    
    # if instr_txt is stopping this frame...
    if instr_txt.status == STARTED:
        if bool(prepared_continue):
            # keep track of stop time/frame for later
            instr_txt.tStop = t  # not accounting for scr refresh
            instr_txt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instr_txt.stopped')
            # update status
            instr_txt.status = FINISHED
            instr_txt.setAutoDraw(False)
    
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
    
    # if prepared_resp is stopping this frame...
    if prepared_resp.status == STARTED:
        if bool(prepared_continue):
            # keep track of stop time/frame for later
            prepared_resp.tStop = t  # not accounting for scr refresh
            prepared_resp.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prepared_resp.stopped')
            # update status
            prepared_resp.status = FINISHED
            prepared_resp.status = FINISHED
    if prepared_resp.status == STARTED and not waitOnFlip:
        theseKeys = prepared_resp.getKeys(keyList=['1'], waitRelease=False)
        _prepared_resp_allKeys.extend(theseKeys)
        if len(_prepared_resp_allKeys):
            prepared_resp.keys = _prepared_resp_allKeys[0].name  # just the first key pressed
            prepared_resp.rt = _prepared_resp_allKeys[0].rt
            prepared_resp.duration = _prepared_resp_allKeys[0].duration
    
    # *prep_instr_0_1* updates
    
    # if prep_instr_0_1 is starting this frame...
    if prep_instr_0_1.status == NOT_STARTED and prepared_continue:
        # keep track of start time/frame for later
        prep_instr_0_1.frameNStart = frameN  # exact frame index
        prep_instr_0_1.tStart = t  # local t and not account for scr refresh
        prep_instr_0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prep_instr_0_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prep_instr_0_1.started')
        # update status
        prep_instr_0_1.status = STARTED
        prep_instr_0_1.setAutoDraw(True)
    
    # if prep_instr_0_1 is active this frame...
    if prep_instr_0_1.status == STARTED:
        # update params
        pass
    
    # if prep_instr_0_1 is stopping this frame...
    if prep_instr_0_1.status == STARTED:
        if frameN >= (prep_instr_0_1.frameNStart + 150):
            # keep track of stop time/frame for later
            prep_instr_0_1.tStop = t  # not accounting for scr refresh
            prep_instr_0_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prep_instr_0_1.stopped')
            # update status
            prep_instr_0_1.status = FINISHED
            prep_instr_0_1.setAutoDraw(False)
    
    # *target_0_1* updates
    
    # if target_0_1 is starting this frame...
    if target_0_1.status == NOT_STARTED and prepared_continue:
        # keep track of start time/frame for later
        target_0_1.frameNStart = frameN  # exact frame index
        target_0_1.tStart = t  # local t and not account for scr refresh
        target_0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(target_0_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'target_0_1.started')
        # update status
        target_0_1.status = STARTED
        target_0_1.setAutoDraw(True)
    
    # if target_0_1 is active this frame...
    if target_0_1.status == STARTED:
        # update params
        pass
    
    # if target_0_1 is stopping this frame...
    if target_0_1.status == STARTED:
        if frameN >= (target_0_1.frameNStart + 150):
            # keep track of stop time/frame for later
            target_0_1.tStop = t  # not accounting for scr refresh
            target_0_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_0_1.stopped')
            # update status
            target_0_1.status = FINISHED
            target_0_1.setAutoDraw(False)
    
    # *trial_fixation_0_1* updates
    
    # if trial_fixation_0_1 is starting this frame...
    if trial_fixation_0_1.status == NOT_STARTED and prep_instr_0_1.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_1.frameNStart = frameN  # exact frame index
        trial_fixation_0_1.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_1.started')
        # update status
        trial_fixation_0_1.status = STARTED
        trial_fixation_0_1.setAutoDraw(True)
    
    # if trial_fixation_0_1 is active this frame...
    if trial_fixation_0_1.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_1 is stopping this frame...
    if trial_fixation_0_1.status == STARTED:
        if frameN >= (trial_fixation_0_1.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_1.tStop = t  # not accounting for scr refresh
            trial_fixation_0_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_1.stopped')
            # update status
            trial_fixation_0_1.status = FINISHED
            trial_fixation_0_1.setAutoDraw(False)
    
    # *image_0_1* updates
    
    # if image_0_1 is starting this frame...
    if image_0_1.status == NOT_STARTED and trial_fixation_0_1.status==FINISHED:
        # keep track of start time/frame for later
        image_0_1.frameNStart = frameN  # exact frame index
        image_0_1.tStart = t  # local t and not account for scr refresh
        image_0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_1.started')
        # update status
        image_0_1.status = STARTED
        image_0_1.setAutoDraw(True)
    
    # if image_0_1 is active this frame...
    if image_0_1.status == STARTED:
        # update params
        pass
    
    # if image_0_1 is stopping this frame...
    if image_0_1.status == STARTED:
        if frameN >= (image_0_1.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_1.tStop = t  # not accounting for scr refresh
            image_0_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_1.stopped')
            # update status
            image_0_1.status = FINISHED
            image_0_1.setAutoDraw(False)
    
    # *key_resp_0_1* updates
    waitOnFlip = False
    
    # if key_resp_0_1 is starting this frame...
    if key_resp_0_1.status == NOT_STARTED and trial_fixation_0_1.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_1.frameNStart = frameN  # exact frame index
        key_resp_0_1.tStart = t  # local t and not account for scr refresh
        key_resp_0_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_1.started')
        # update status
        key_resp_0_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_1 is stopping this frame...
    if key_resp_0_1.status == STARTED:
        if frameN >= 150:
            # keep track of stop time/frame for later
            key_resp_0_1.tStop = t  # not accounting for scr refresh
            key_resp_0_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_1.stopped')
            # update status
            key_resp_0_1.status = FINISHED
            key_resp_0_1.status = FINISHED
    if key_resp_0_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_1.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_1_allKeys.extend(theseKeys)
        if len(_key_resp_0_1_allKeys):
            key_resp_0_1.keys = _key_resp_0_1_allKeys[0].name  # just the first key pressed
            key_resp_0_1.rt = _key_resp_0_1_allKeys[0].rt
            key_resp_0_1.duration = _key_resp_0_1_allKeys[0].duration
    
    # *trial_fixation_0_2* updates
    
    # if trial_fixation_0_2 is starting this frame...
    if trial_fixation_0_2.status == NOT_STARTED and key_resp_0_1.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_2.frameNStart = frameN  # exact frame index
        trial_fixation_0_2.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_2.started')
        # update status
        trial_fixation_0_2.status = STARTED
        trial_fixation_0_2.setAutoDraw(True)
    
    # if trial_fixation_0_2 is active this frame...
    if trial_fixation_0_2.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_2 is stopping this frame...
    if trial_fixation_0_2.status == STARTED:
        if frameN >= (trial_fixation_0_2.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_2.tStop = t  # not accounting for scr refresh
            trial_fixation_0_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_2.stopped')
            # update status
            trial_fixation_0_2.status = FINISHED
            trial_fixation_0_2.setAutoDraw(False)
    
    # *image_0_2* updates
    
    # if image_0_2 is starting this frame...
    if image_0_2.status == NOT_STARTED and trial_fixation_0_2.status==FINISHED:
        # keep track of start time/frame for later
        image_0_2.frameNStart = frameN  # exact frame index
        image_0_2.tStart = t  # local t and not account for scr refresh
        image_0_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_2.started')
        # update status
        image_0_2.status = STARTED
        image_0_2.setAutoDraw(True)
    
    # if image_0_2 is active this frame...
    if image_0_2.status == STARTED:
        # update params
        pass
    
    # if image_0_2 is stopping this frame...
    if image_0_2.status == STARTED:
        if frameN >= (image_0_2.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_2.tStop = t  # not accounting for scr refresh
            image_0_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_2.stopped')
            # update status
            image_0_2.status = FINISHED
            image_0_2.setAutoDraw(False)
    
    # *key_resp_0_2* updates
    waitOnFlip = False
    
    # if key_resp_0_2 is starting this frame...
    if key_resp_0_2.status == NOT_STARTED and trial_fixation_0_2.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_2.frameNStart = frameN  # exact frame index
        key_resp_0_2.tStart = t  # local t and not account for scr refresh
        key_resp_0_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_2.started')
        # update status
        key_resp_0_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_2 is stopping this frame...
    if key_resp_0_2.status == STARTED:
        if frameN >= (key_resp_0_2.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_2.tStop = t  # not accounting for scr refresh
            key_resp_0_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_2.stopped')
            # update status
            key_resp_0_2.status = FINISHED
            key_resp_0_2.status = FINISHED
    if key_resp_0_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_2.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_2_allKeys.extend(theseKeys)
        if len(_key_resp_0_2_allKeys):
            key_resp_0_2.keys = _key_resp_0_2_allKeys[0].name  # just the first key pressed
            key_resp_0_2.rt = _key_resp_0_2_allKeys[0].rt
            key_resp_0_2.duration = _key_resp_0_2_allKeys[0].duration
    
    # *trial_fixation_0_3* updates
    
    # if trial_fixation_0_3 is starting this frame...
    if trial_fixation_0_3.status == NOT_STARTED and key_resp_0_2.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_3.frameNStart = frameN  # exact frame index
        trial_fixation_0_3.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_3.started')
        # update status
        trial_fixation_0_3.status = STARTED
        trial_fixation_0_3.setAutoDraw(True)
    
    # if trial_fixation_0_3 is active this frame...
    if trial_fixation_0_3.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_3 is stopping this frame...
    if trial_fixation_0_3.status == STARTED:
        if frameN >= (trial_fixation_0_3.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_3.tStop = t  # not accounting for scr refresh
            trial_fixation_0_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_3.stopped')
            # update status
            trial_fixation_0_3.status = FINISHED
            trial_fixation_0_3.setAutoDraw(False)
    
    # *image_0_3* updates
    
    # if image_0_3 is starting this frame...
    if image_0_3.status == NOT_STARTED and trial_fixation_0_3.status==FINISHED:
        # keep track of start time/frame for later
        image_0_3.frameNStart = frameN  # exact frame index
        image_0_3.tStart = t  # local t and not account for scr refresh
        image_0_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_3.started')
        # update status
        image_0_3.status = STARTED
        image_0_3.setAutoDraw(True)
    
    # if image_0_3 is active this frame...
    if image_0_3.status == STARTED:
        # update params
        pass
    
    # if image_0_3 is stopping this frame...
    if image_0_3.status == STARTED:
        if frameN >= (image_0_3.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_3.tStop = t  # not accounting for scr refresh
            image_0_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_3.stopped')
            # update status
            image_0_3.status = FINISHED
            image_0_3.setAutoDraw(False)
    
    # *key_resp_0_3* updates
    waitOnFlip = False
    
    # if key_resp_0_3 is starting this frame...
    if key_resp_0_3.status == NOT_STARTED and trial_fixation_0_3.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_3.frameNStart = frameN  # exact frame index
        key_resp_0_3.tStart = t  # local t and not account for scr refresh
        key_resp_0_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_3.started')
        # update status
        key_resp_0_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_3 is stopping this frame...
    if key_resp_0_3.status == STARTED:
        if frameN >= (key_resp_0_3.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_3.tStop = t  # not accounting for scr refresh
            key_resp_0_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_3.stopped')
            # update status
            key_resp_0_3.status = FINISHED
            key_resp_0_3.status = FINISHED
    if key_resp_0_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_3.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_3_allKeys.extend(theseKeys)
        if len(_key_resp_0_3_allKeys):
            key_resp_0_3.keys = _key_resp_0_3_allKeys[0].name  # just the first key pressed
            key_resp_0_3.rt = _key_resp_0_3_allKeys[0].rt
            key_resp_0_3.duration = _key_resp_0_3_allKeys[0].duration
    
    # *trial_fixation_0_4* updates
    
    # if trial_fixation_0_4 is starting this frame...
    if trial_fixation_0_4.status == NOT_STARTED and key_resp_0_3.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_4.frameNStart = frameN  # exact frame index
        trial_fixation_0_4.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_4.started')
        # update status
        trial_fixation_0_4.status = STARTED
        trial_fixation_0_4.setAutoDraw(True)
    
    # if trial_fixation_0_4 is active this frame...
    if trial_fixation_0_4.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_4 is stopping this frame...
    if trial_fixation_0_4.status == STARTED:
        if frameN >= (trial_fixation_0_4.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_4.tStop = t  # not accounting for scr refresh
            trial_fixation_0_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_4.stopped')
            # update status
            trial_fixation_0_4.status = FINISHED
            trial_fixation_0_4.setAutoDraw(False)
    
    # *image_0_4* updates
    
    # if image_0_4 is starting this frame...
    if image_0_4.status == NOT_STARTED and trial_fixation_0_4.status==FINISHED:
        # keep track of start time/frame for later
        image_0_4.frameNStart = frameN  # exact frame index
        image_0_4.tStart = t  # local t and not account for scr refresh
        image_0_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_4.started')
        # update status
        image_0_4.status = STARTED
        image_0_4.setAutoDraw(True)
    
    # if image_0_4 is active this frame...
    if image_0_4.status == STARTED:
        # update params
        pass
    
    # if image_0_4 is stopping this frame...
    if image_0_4.status == STARTED:
        if frameN >= (image_0_4.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_4.tStop = t  # not accounting for scr refresh
            image_0_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_4.stopped')
            # update status
            image_0_4.status = FINISHED
            image_0_4.setAutoDraw(False)
    
    # *key_resp_0_4* updates
    waitOnFlip = False
    
    # if key_resp_0_4 is starting this frame...
    if key_resp_0_4.status == NOT_STARTED and trial_fixation_0_4.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_4.frameNStart = frameN  # exact frame index
        key_resp_0_4.tStart = t  # local t and not account for scr refresh
        key_resp_0_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_4.started')
        # update status
        key_resp_0_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_4 is stopping this frame...
    if key_resp_0_4.status == STARTED:
        if frameN >= (key_resp_0_4.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_4.tStop = t  # not accounting for scr refresh
            key_resp_0_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_4.stopped')
            # update status
            key_resp_0_4.status = FINISHED
            key_resp_0_4.status = FINISHED
    if key_resp_0_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_4.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_4_allKeys.extend(theseKeys)
        if len(_key_resp_0_4_allKeys):
            key_resp_0_4.keys = _key_resp_0_4_allKeys[0].name  # just the first key pressed
            key_resp_0_4.rt = _key_resp_0_4_allKeys[0].rt
            key_resp_0_4.duration = _key_resp_0_4_allKeys[0].duration
    
    # *trial_fixation_0_5* updates
    
    # if trial_fixation_0_5 is starting this frame...
    if trial_fixation_0_5.status == NOT_STARTED and key_resp_0_4.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_5.frameNStart = frameN  # exact frame index
        trial_fixation_0_5.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_5.started')
        # update status
        trial_fixation_0_5.status = STARTED
        trial_fixation_0_5.setAutoDraw(True)
    
    # if trial_fixation_0_5 is active this frame...
    if trial_fixation_0_5.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_5 is stopping this frame...
    if trial_fixation_0_5.status == STARTED:
        if frameN >= (trial_fixation_0_5.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_5.tStop = t  # not accounting for scr refresh
            trial_fixation_0_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_5.stopped')
            # update status
            trial_fixation_0_5.status = FINISHED
            trial_fixation_0_5.setAutoDraw(False)
    
    # *image_0_5* updates
    
    # if image_0_5 is starting this frame...
    if image_0_5.status == NOT_STARTED and trial_fixation_0_5.status==FINISHED:
        # keep track of start time/frame for later
        image_0_5.frameNStart = frameN  # exact frame index
        image_0_5.tStart = t  # local t and not account for scr refresh
        image_0_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_5.started')
        # update status
        image_0_5.status = STARTED
        image_0_5.setAutoDraw(True)
    
    # if image_0_5 is active this frame...
    if image_0_5.status == STARTED:
        # update params
        pass
    
    # if image_0_5 is stopping this frame...
    if image_0_5.status == STARTED:
        if frameN >= (image_0_5.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_5.tStop = t  # not accounting for scr refresh
            image_0_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_5.stopped')
            # update status
            image_0_5.status = FINISHED
            image_0_5.setAutoDraw(False)
    
    # *key_resp_0_5* updates
    waitOnFlip = False
    
    # if key_resp_0_5 is starting this frame...
    if key_resp_0_5.status == NOT_STARTED and trial_fixation_0_5.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_5.frameNStart = frameN  # exact frame index
        key_resp_0_5.tStart = t  # local t and not account for scr refresh
        key_resp_0_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_5.started')
        # update status
        key_resp_0_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_5 is stopping this frame...
    if key_resp_0_5.status == STARTED:
        if frameN >= (key_resp_0_5.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_5.tStop = t  # not accounting for scr refresh
            key_resp_0_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_5.stopped')
            # update status
            key_resp_0_5.status = FINISHED
            key_resp_0_5.status = FINISHED
    if key_resp_0_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_5.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_5_allKeys.extend(theseKeys)
        if len(_key_resp_0_5_allKeys):
            key_resp_0_5.keys = _key_resp_0_5_allKeys[0].name  # just the first key pressed
            key_resp_0_5.rt = _key_resp_0_5_allKeys[0].rt
            key_resp_0_5.duration = _key_resp_0_5_allKeys[0].duration
    
    # *trial_fixation_0_6* updates
    
    # if trial_fixation_0_6 is starting this frame...
    if trial_fixation_0_6.status == NOT_STARTED and key_resp_0_5.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_6.frameNStart = frameN  # exact frame index
        trial_fixation_0_6.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_6.started')
        # update status
        trial_fixation_0_6.status = STARTED
        trial_fixation_0_6.setAutoDraw(True)
    
    # if trial_fixation_0_6 is active this frame...
    if trial_fixation_0_6.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_6 is stopping this frame...
    if trial_fixation_0_6.status == STARTED:
        if frameN >= (trial_fixation_0_6.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_6.tStop = t  # not accounting for scr refresh
            trial_fixation_0_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_6.stopped')
            # update status
            trial_fixation_0_6.status = FINISHED
            trial_fixation_0_6.setAutoDraw(False)
    
    # *image_0_6* updates
    
    # if image_0_6 is starting this frame...
    if image_0_6.status == NOT_STARTED and trial_fixation_0_6.status==FINISHED:
        # keep track of start time/frame for later
        image_0_6.frameNStart = frameN  # exact frame index
        image_0_6.tStart = t  # local t and not account for scr refresh
        image_0_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_6.started')
        # update status
        image_0_6.status = STARTED
        image_0_6.setAutoDraw(True)
    
    # if image_0_6 is active this frame...
    if image_0_6.status == STARTED:
        # update params
        pass
    
    # if image_0_6 is stopping this frame...
    if image_0_6.status == STARTED:
        if frameN >= (image_0_6.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_6.tStop = t  # not accounting for scr refresh
            image_0_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_6.stopped')
            # update status
            image_0_6.status = FINISHED
            image_0_6.setAutoDraw(False)
    
    # *key_resp_0_6* updates
    waitOnFlip = False
    
    # if key_resp_0_6 is starting this frame...
    if key_resp_0_6.status == NOT_STARTED and trial_fixation_0_6.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_6.frameNStart = frameN  # exact frame index
        key_resp_0_6.tStart = t  # local t and not account for scr refresh
        key_resp_0_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_6.started')
        # update status
        key_resp_0_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_6 is stopping this frame...
    if key_resp_0_6.status == STARTED:
        if frameN >= (key_resp_0_6.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_6.tStop = t  # not accounting for scr refresh
            key_resp_0_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_6.stopped')
            # update status
            key_resp_0_6.status = FINISHED
            key_resp_0_6.status = FINISHED
    if key_resp_0_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_6.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_6_allKeys.extend(theseKeys)
        if len(_key_resp_0_6_allKeys):
            key_resp_0_6.keys = _key_resp_0_6_allKeys[0].name  # just the first key pressed
            key_resp_0_6.rt = _key_resp_0_6_allKeys[0].rt
            key_resp_0_6.duration = _key_resp_0_6_allKeys[0].duration
    
    # *trial_fixation_0_7* updates
    
    # if trial_fixation_0_7 is starting this frame...
    if trial_fixation_0_7.status == NOT_STARTED and key_resp_0_6.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_7.frameNStart = frameN  # exact frame index
        trial_fixation_0_7.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_7.started')
        # update status
        trial_fixation_0_7.status = STARTED
        trial_fixation_0_7.setAutoDraw(True)
    
    # if trial_fixation_0_7 is active this frame...
    if trial_fixation_0_7.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_7 is stopping this frame...
    if trial_fixation_0_7.status == STARTED:
        if frameN >= (trial_fixation_0_7.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_7.tStop = t  # not accounting for scr refresh
            trial_fixation_0_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_7.stopped')
            # update status
            trial_fixation_0_7.status = FINISHED
            trial_fixation_0_7.setAutoDraw(False)
    
    # *image_0_7* updates
    
    # if image_0_7 is starting this frame...
    if image_0_7.status == NOT_STARTED and trial_fixation_0_7.status==FINISHED:
        # keep track of start time/frame for later
        image_0_7.frameNStart = frameN  # exact frame index
        image_0_7.tStart = t  # local t and not account for scr refresh
        image_0_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_7.started')
        # update status
        image_0_7.status = STARTED
        image_0_7.setAutoDraw(True)
    
    # if image_0_7 is active this frame...
    if image_0_7.status == STARTED:
        # update params
        pass
    
    # if image_0_7 is stopping this frame...
    if image_0_7.status == STARTED:
        if frameN >= (image_0_7.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_7.tStop = t  # not accounting for scr refresh
            image_0_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_7.stopped')
            # update status
            image_0_7.status = FINISHED
            image_0_7.setAutoDraw(False)
    
    # *key_resp_0_7* updates
    waitOnFlip = False
    
    # if key_resp_0_7 is starting this frame...
    if key_resp_0_7.status == NOT_STARTED and trial_fixation_0_7.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_7.frameNStart = frameN  # exact frame index
        key_resp_0_7.tStart = t  # local t and not account for scr refresh
        key_resp_0_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_7.started')
        # update status
        key_resp_0_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_7 is stopping this frame...
    if key_resp_0_7.status == STARTED:
        if frameN >= (key_resp_0_7.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_7.tStop = t  # not accounting for scr refresh
            key_resp_0_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_7.stopped')
            # update status
            key_resp_0_7.status = FINISHED
            key_resp_0_7.status = FINISHED
    if key_resp_0_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_7.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_7_allKeys.extend(theseKeys)
        if len(_key_resp_0_7_allKeys):
            key_resp_0_7.keys = _key_resp_0_7_allKeys[0].name  # just the first key pressed
            key_resp_0_7.rt = _key_resp_0_7_allKeys[0].rt
            key_resp_0_7.duration = _key_resp_0_7_allKeys[0].duration
    
    # *trial_fixation_0_8* updates
    
    # if trial_fixation_0_8 is starting this frame...
    if trial_fixation_0_8.status == NOT_STARTED and key_resp_0_7.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_8.frameNStart = frameN  # exact frame index
        trial_fixation_0_8.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_8.started')
        # update status
        trial_fixation_0_8.status = STARTED
        trial_fixation_0_8.setAutoDraw(True)
    
    # if trial_fixation_0_8 is active this frame...
    if trial_fixation_0_8.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_8 is stopping this frame...
    if trial_fixation_0_8.status == STARTED:
        if frameN >= (trial_fixation_0_8.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_8.tStop = t  # not accounting for scr refresh
            trial_fixation_0_8.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_8.stopped')
            # update status
            trial_fixation_0_8.status = FINISHED
            trial_fixation_0_8.setAutoDraw(False)
    
    # *image_0_8* updates
    
    # if image_0_8 is starting this frame...
    if image_0_8.status == NOT_STARTED and trial_fixation_0_8.status==FINISHED:
        # keep track of start time/frame for later
        image_0_8.frameNStart = frameN  # exact frame index
        image_0_8.tStart = t  # local t and not account for scr refresh
        image_0_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_8.started')
        # update status
        image_0_8.status = STARTED
        image_0_8.setAutoDraw(True)
    
    # if image_0_8 is active this frame...
    if image_0_8.status == STARTED:
        # update params
        pass
    
    # if image_0_8 is stopping this frame...
    if image_0_8.status == STARTED:
        if frameN >= (image_0_8.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_8.tStop = t  # not accounting for scr refresh
            image_0_8.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_8.stopped')
            # update status
            image_0_8.status = FINISHED
            image_0_8.setAutoDraw(False)
    
    # *key_resp_0_8* updates
    waitOnFlip = False
    
    # if key_resp_0_8 is starting this frame...
    if key_resp_0_8.status == NOT_STARTED and trial_fixation_0_8.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_8.frameNStart = frameN  # exact frame index
        key_resp_0_8.tStart = t  # local t and not account for scr refresh
        key_resp_0_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_8.started')
        # update status
        key_resp_0_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_8 is stopping this frame...
    if key_resp_0_8.status == STARTED:
        if frameN >= (key_resp_0_8.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_8.tStop = t  # not accounting for scr refresh
            key_resp_0_8.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_8.stopped')
            # update status
            key_resp_0_8.status = FINISHED
            key_resp_0_8.status = FINISHED
    if key_resp_0_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_8.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_8_allKeys.extend(theseKeys)
        if len(_key_resp_0_8_allKeys):
            key_resp_0_8.keys = _key_resp_0_8_allKeys[0].name  # just the first key pressed
            key_resp_0_8.rt = _key_resp_0_8_allKeys[0].rt
            key_resp_0_8.duration = _key_resp_0_8_allKeys[0].duration
    
    # *trial_fixation_0_9* updates
    
    # if trial_fixation_0_9 is starting this frame...
    if trial_fixation_0_9.status == NOT_STARTED and key_resp_0_8.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_9.frameNStart = frameN  # exact frame index
        trial_fixation_0_9.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_9.started')
        # update status
        trial_fixation_0_9.status = STARTED
        trial_fixation_0_9.setAutoDraw(True)
    
    # if trial_fixation_0_9 is active this frame...
    if trial_fixation_0_9.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_9 is stopping this frame...
    if trial_fixation_0_9.status == STARTED:
        if frameN >= (trial_fixation_0_9.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_9.tStop = t  # not accounting for scr refresh
            trial_fixation_0_9.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_9.stopped')
            # update status
            trial_fixation_0_9.status = FINISHED
            trial_fixation_0_9.setAutoDraw(False)
    
    # *image_0_9* updates
    
    # if image_0_9 is starting this frame...
    if image_0_9.status == NOT_STARTED and trial_fixation_0_9.status==FINISHED:
        # keep track of start time/frame for later
        image_0_9.frameNStart = frameN  # exact frame index
        image_0_9.tStart = t  # local t and not account for scr refresh
        image_0_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_9.started')
        # update status
        image_0_9.status = STARTED
        image_0_9.setAutoDraw(True)
    
    # if image_0_9 is active this frame...
    if image_0_9.status == STARTED:
        # update params
        pass
    
    # if image_0_9 is stopping this frame...
    if image_0_9.status == STARTED:
        if frameN >= (image_0_9.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_9.tStop = t  # not accounting for scr refresh
            image_0_9.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_9.stopped')
            # update status
            image_0_9.status = FINISHED
            image_0_9.setAutoDraw(False)
    
    # *key_resp_0_9* updates
    waitOnFlip = False
    
    # if key_resp_0_9 is starting this frame...
    if key_resp_0_9.status == NOT_STARTED and trial_fixation_0_9.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_9.frameNStart = frameN  # exact frame index
        key_resp_0_9.tStart = t  # local t and not account for scr refresh
        key_resp_0_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_9.started')
        # update status
        key_resp_0_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_9 is stopping this frame...
    if key_resp_0_9.status == STARTED:
        if frameN >= (key_resp_0_9.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_9.tStop = t  # not accounting for scr refresh
            key_resp_0_9.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_9.stopped')
            # update status
            key_resp_0_9.status = FINISHED
            key_resp_0_9.status = FINISHED
    if key_resp_0_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_9.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_9_allKeys.extend(theseKeys)
        if len(_key_resp_0_9_allKeys):
            key_resp_0_9.keys = _key_resp_0_9_allKeys[0].name  # just the first key pressed
            key_resp_0_9.rt = _key_resp_0_9_allKeys[0].rt
            key_resp_0_9.duration = _key_resp_0_9_allKeys[0].duration
    
    # *trial_fixation_0_10* updates
    
    # if trial_fixation_0_10 is starting this frame...
    if trial_fixation_0_10.status == NOT_STARTED and key_resp_0_9.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_0_10.frameNStart = frameN  # exact frame index
        trial_fixation_0_10.tStart = t  # local t and not account for scr refresh
        trial_fixation_0_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_0_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_0_10.started')
        # update status
        trial_fixation_0_10.status = STARTED
        trial_fixation_0_10.setAutoDraw(True)
    
    # if trial_fixation_0_10 is active this frame...
    if trial_fixation_0_10.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_0_10 is stopping this frame...
    if trial_fixation_0_10.status == STARTED:
        if frameN >= (trial_fixation_0_10.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_0_10.tStop = t  # not accounting for scr refresh
            trial_fixation_0_10.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_0_10.stopped')
            # update status
            trial_fixation_0_10.status = FINISHED
            trial_fixation_0_10.setAutoDraw(False)
    
    # *image_0_10* updates
    
    # if image_0_10 is starting this frame...
    if image_0_10.status == NOT_STARTED and trial_fixation_0_10.status==FINISHED:
        # keep track of start time/frame for later
        image_0_10.frameNStart = frameN  # exact frame index
        image_0_10.tStart = t  # local t and not account for scr refresh
        image_0_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_0_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_0_10.started')
        # update status
        image_0_10.status = STARTED
        image_0_10.setAutoDraw(True)
    
    # if image_0_10 is active this frame...
    if image_0_10.status == STARTED:
        # update params
        pass
    
    # if image_0_10 is stopping this frame...
    if image_0_10.status == STARTED:
        if frameN >= (image_0_10.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_0_10.tStop = t  # not accounting for scr refresh
            image_0_10.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_0_10.stopped')
            # update status
            image_0_10.status = FINISHED
            image_0_10.setAutoDraw(False)
    
    # *key_resp_0_10* updates
    waitOnFlip = False
    
    # if key_resp_0_10 is starting this frame...
    if key_resp_0_10.status == NOT_STARTED and trial_fixation_0_10.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_0_10.frameNStart = frameN  # exact frame index
        key_resp_0_10.tStart = t  # local t and not account for scr refresh
        key_resp_0_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_0_10.started')
        # update status
        key_resp_0_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_0_10 is stopping this frame...
    if key_resp_0_10.status == STARTED:
        if frameN >= (key_resp_0_10.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_0_10.tStop = t  # not accounting for scr refresh
            key_resp_0_10.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_0_10.stopped')
            # update status
            key_resp_0_10.status = FINISHED
            key_resp_0_10.status = FINISHED
    if key_resp_0_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0_10.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_0_10_allKeys.extend(theseKeys)
        if len(_key_resp_0_10_allKeys):
            key_resp_0_10.keys = _key_resp_0_10_allKeys[0].name  # just the first key pressed
            key_resp_0_10.rt = _key_resp_0_10_allKeys[0].rt
            key_resp_0_10.duration = _key_resp_0_10_allKeys[0].duration
    
    # *prep_instr_0_2* updates
    
    # if prep_instr_0_2 is starting this frame...
    if prep_instr_0_2.status == NOT_STARTED and key_resp_0_10.status==FINISHED:
        # keep track of start time/frame for later
        prep_instr_0_2.frameNStart = frameN  # exact frame index
        prep_instr_0_2.tStart = t  # local t and not account for scr refresh
        prep_instr_0_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prep_instr_0_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'prep_instr_0_2.started')
        # update status
        prep_instr_0_2.status = STARTED
        prep_instr_0_2.setAutoDraw(True)
    
    # if prep_instr_0_2 is active this frame...
    if prep_instr_0_2.status == STARTED:
        # update params
        pass
    
    # if prep_instr_0_2 is stopping this frame...
    if prep_instr_0_2.status == STARTED:
        if frameN >= (prep_instr_0_2.frameNStart + 150):
            # keep track of stop time/frame for later
            prep_instr_0_2.tStop = t  # not accounting for scr refresh
            prep_instr_0_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prep_instr_0_2.stopped')
            # update status
            prep_instr_0_2.status = FINISHED
            prep_instr_0_2.setAutoDraw(False)
    
    # *target_0_2* updates
    
    # if target_0_2 is starting this frame...
    if target_0_2.status == NOT_STARTED and key_resp_0_10.status==FINISHED:
        # keep track of start time/frame for later
        target_0_2.frameNStart = frameN  # exact frame index
        target_0_2.tStart = t  # local t and not account for scr refresh
        target_0_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(target_0_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'target_0_2.started')
        # update status
        target_0_2.status = STARTED
        target_0_2.setAutoDraw(True)
    
    # if target_0_2 is active this frame...
    if target_0_2.status == STARTED:
        # update params
        pass
    
    # if target_0_2 is stopping this frame...
    if target_0_2.status == STARTED:
        if frameN >= (target_0_2.frameNStart + 150):
            # keep track of stop time/frame for later
            target_0_2.tStop = t  # not accounting for scr refresh
            target_0_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_0_2.stopped')
            # update status
            target_0_2.status = FINISHED
            target_0_2.setAutoDraw(False)
    
    # *trial_fixation_3_1* updates
    
    # if trial_fixation_3_1 is starting this frame...
    if trial_fixation_3_1.status == NOT_STARTED and target_0_2.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_1.frameNStart = frameN  # exact frame index
        trial_fixation_3_1.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_1.started')
        # update status
        trial_fixation_3_1.status = STARTED
        trial_fixation_3_1.setAutoDraw(True)
    
    # if trial_fixation_3_1 is active this frame...
    if trial_fixation_3_1.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_1 is stopping this frame...
    if trial_fixation_3_1.status == STARTED:
        if frameN >= (trial_fixation_3_1.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_1.tStop = t  # not accounting for scr refresh
            trial_fixation_3_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_1.stopped')
            # update status
            trial_fixation_3_1.status = FINISHED
            trial_fixation_3_1.setAutoDraw(False)
    
    # *image_3_1* updates
    
    # if image_3_1 is starting this frame...
    if image_3_1.status == NOT_STARTED and trial_fixation_3_1.status==FINISHED:
        # keep track of start time/frame for later
        image_3_1.frameNStart = frameN  # exact frame index
        image_3_1.tStart = t  # local t and not account for scr refresh
        image_3_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_1.started')
        # update status
        image_3_1.status = STARTED
        image_3_1.setAutoDraw(True)
    
    # if image_3_1 is active this frame...
    if image_3_1.status == STARTED:
        # update params
        pass
    
    # if image_3_1 is stopping this frame...
    if image_3_1.status == STARTED:
        if frameN >= (image_3_1.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_1.tStop = t  # not accounting for scr refresh
            image_3_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_1.stopped')
            # update status
            image_3_1.status = FINISHED
            image_3_1.setAutoDraw(False)
    
    # *key_resp_3_1* updates
    waitOnFlip = False
    
    # if key_resp_3_1 is starting this frame...
    if key_resp_3_1.status == NOT_STARTED and trial_fixation_3_1.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_1.frameNStart = frameN  # exact frame index
        key_resp_3_1.tStart = t  # local t and not account for scr refresh
        key_resp_3_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_1.started')
        # update status
        key_resp_3_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_1 is stopping this frame...
    if key_resp_3_1.status == STARTED:
        if frameN >= (key_resp_3_1.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_1.tStop = t  # not accounting for scr refresh
            key_resp_3_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_1.stopped')
            # update status
            key_resp_3_1.status = FINISHED
            key_resp_3_1.status = FINISHED
    if key_resp_3_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_1.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_1_allKeys.extend(theseKeys)
        if len(_key_resp_3_1_allKeys):
            key_resp_3_1.keys = _key_resp_3_1_allKeys[0].name  # just the first key pressed
            key_resp_3_1.rt = _key_resp_3_1_allKeys[0].rt
            key_resp_3_1.duration = _key_resp_3_1_allKeys[0].duration
    
    # *trial_fixation_3_2* updates
    
    # if trial_fixation_3_2 is starting this frame...
    if trial_fixation_3_2.status == NOT_STARTED and key_resp_3_1.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_2.frameNStart = frameN  # exact frame index
        trial_fixation_3_2.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_2.started')
        # update status
        trial_fixation_3_2.status = STARTED
        trial_fixation_3_2.setAutoDraw(True)
    
    # if trial_fixation_3_2 is active this frame...
    if trial_fixation_3_2.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_2 is stopping this frame...
    if trial_fixation_3_2.status == STARTED:
        if frameN >= (trial_fixation_3_2.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_2.tStop = t  # not accounting for scr refresh
            trial_fixation_3_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_2.stopped')
            # update status
            trial_fixation_3_2.status = FINISHED
            trial_fixation_3_2.setAutoDraw(False)
    
    # *image_3_2* updates
    
    # if image_3_2 is starting this frame...
    if image_3_2.status == NOT_STARTED and trial_fixation_3_2.status==FINISHED:
        # keep track of start time/frame for later
        image_3_2.frameNStart = frameN  # exact frame index
        image_3_2.tStart = t  # local t and not account for scr refresh
        image_3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_2.started')
        # update status
        image_3_2.status = STARTED
        image_3_2.setAutoDraw(True)
    
    # if image_3_2 is active this frame...
    if image_3_2.status == STARTED:
        # update params
        pass
    
    # if image_3_2 is stopping this frame...
    if image_3_2.status == STARTED:
        if frameN >= (image_3_2.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_2.tStop = t  # not accounting for scr refresh
            image_3_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_2.stopped')
            # update status
            image_3_2.status = FINISHED
            image_3_2.setAutoDraw(False)
    
    # *key_resp_3_2* updates
    waitOnFlip = False
    
    # if key_resp_3_2 is starting this frame...
    if key_resp_3_2.status == NOT_STARTED and trial_fixation_3_2.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_2.frameNStart = frameN  # exact frame index
        key_resp_3_2.tStart = t  # local t and not account for scr refresh
        key_resp_3_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_2.started')
        # update status
        key_resp_3_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_2 is stopping this frame...
    if key_resp_3_2.status == STARTED:
        if frameN >= (key_resp_3_2.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_2.tStop = t  # not accounting for scr refresh
            key_resp_3_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_2.stopped')
            # update status
            key_resp_3_2.status = FINISHED
            key_resp_3_2.status = FINISHED
    if key_resp_3_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_2.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_2_allKeys.extend(theseKeys)
        if len(_key_resp_3_2_allKeys):
            key_resp_3_2.keys = _key_resp_3_2_allKeys[0].name  # just the first key pressed
            key_resp_3_2.rt = _key_resp_3_2_allKeys[0].rt
            key_resp_3_2.duration = _key_resp_3_2_allKeys[0].duration
    
    # *trial_fixation_3_3* updates
    
    # if trial_fixation_3_3 is starting this frame...
    if trial_fixation_3_3.status == NOT_STARTED and key_resp_3_2.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_3.frameNStart = frameN  # exact frame index
        trial_fixation_3_3.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_3.started')
        # update status
        trial_fixation_3_3.status = STARTED
        trial_fixation_3_3.setAutoDraw(True)
    
    # if trial_fixation_3_3 is active this frame...
    if trial_fixation_3_3.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_3 is stopping this frame...
    if trial_fixation_3_3.status == STARTED:
        if frameN >= (trial_fixation_3_3.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_3.tStop = t  # not accounting for scr refresh
            trial_fixation_3_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_3.stopped')
            # update status
            trial_fixation_3_3.status = FINISHED
            trial_fixation_3_3.setAutoDraw(False)
    
    # *image_3_3* updates
    
    # if image_3_3 is starting this frame...
    if image_3_3.status == NOT_STARTED and trial_fixation_3_3.status==FINISHED:
        # keep track of start time/frame for later
        image_3_3.frameNStart = frameN  # exact frame index
        image_3_3.tStart = t  # local t and not account for scr refresh
        image_3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_3.started')
        # update status
        image_3_3.status = STARTED
        image_3_3.setAutoDraw(True)
    
    # if image_3_3 is active this frame...
    if image_3_3.status == STARTED:
        # update params
        pass
    
    # if image_3_3 is stopping this frame...
    if image_3_3.status == STARTED:
        if frameN >= (image_3_3.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_3.tStop = t  # not accounting for scr refresh
            image_3_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_3.stopped')
            # update status
            image_3_3.status = FINISHED
            image_3_3.setAutoDraw(False)
    
    # *key_resp_3_3* updates
    waitOnFlip = False
    
    # if key_resp_3_3 is starting this frame...
    if key_resp_3_3.status == NOT_STARTED and trial_fixation_3_3.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_3.frameNStart = frameN  # exact frame index
        key_resp_3_3.tStart = t  # local t and not account for scr refresh
        key_resp_3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_3.started')
        # update status
        key_resp_3_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_3 is stopping this frame...
    if key_resp_3_3.status == STARTED:
        if frameN >= (key_resp_3_3.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_3.tStop = t  # not accounting for scr refresh
            key_resp_3_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_3.stopped')
            # update status
            key_resp_3_3.status = FINISHED
            key_resp_3_3.status = FINISHED
    if key_resp_3_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_3.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_3_allKeys):
            key_resp_3_3.keys = _key_resp_3_3_allKeys[0].name  # just the first key pressed
            key_resp_3_3.rt = _key_resp_3_3_allKeys[0].rt
            key_resp_3_3.duration = _key_resp_3_3_allKeys[0].duration
    
    # *trial_fixation_3_4* updates
    
    # if trial_fixation_3_4 is starting this frame...
    if trial_fixation_3_4.status == NOT_STARTED and key_resp_3_3.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_4.frameNStart = frameN  # exact frame index
        trial_fixation_3_4.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_4.started')
        # update status
        trial_fixation_3_4.status = STARTED
        trial_fixation_3_4.setAutoDraw(True)
    
    # if trial_fixation_3_4 is active this frame...
    if trial_fixation_3_4.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_4 is stopping this frame...
    if trial_fixation_3_4.status == STARTED:
        if frameN >= (trial_fixation_3_4.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_4.tStop = t  # not accounting for scr refresh
            trial_fixation_3_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_4.stopped')
            # update status
            trial_fixation_3_4.status = FINISHED
            trial_fixation_3_4.setAutoDraw(False)
    
    # *image_3_4* updates
    
    # if image_3_4 is starting this frame...
    if image_3_4.status == NOT_STARTED and trial_fixation_3_4.status==FINISHED:
        # keep track of start time/frame for later
        image_3_4.frameNStart = frameN  # exact frame index
        image_3_4.tStart = t  # local t and not account for scr refresh
        image_3_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_4.started')
        # update status
        image_3_4.status = STARTED
        image_3_4.setAutoDraw(True)
    
    # if image_3_4 is active this frame...
    if image_3_4.status == STARTED:
        # update params
        pass
    
    # if image_3_4 is stopping this frame...
    if image_3_4.status == STARTED:
        if frameN >= (image_3_4.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_4.tStop = t  # not accounting for scr refresh
            image_3_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_4.stopped')
            # update status
            image_3_4.status = FINISHED
            image_3_4.setAutoDraw(False)
    
    # *key_resp_3_4* updates
    waitOnFlip = False
    
    # if key_resp_3_4 is starting this frame...
    if key_resp_3_4.status == NOT_STARTED and trial_fixation_3_4.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_4.frameNStart = frameN  # exact frame index
        key_resp_3_4.tStart = t  # local t and not account for scr refresh
        key_resp_3_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_4.started')
        # update status
        key_resp_3_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_4 is stopping this frame...
    if key_resp_3_4.status == STARTED:
        if frameN >= (key_resp_3_4.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_4.tStop = t  # not accounting for scr refresh
            key_resp_3_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_4.stopped')
            # update status
            key_resp_3_4.status = FINISHED
            key_resp_3_4.status = FINISHED
    if key_resp_3_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_4.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_4_allKeys.extend(theseKeys)
        if len(_key_resp_3_4_allKeys):
            key_resp_3_4.keys = _key_resp_3_4_allKeys[0].name  # just the first key pressed
            key_resp_3_4.rt = _key_resp_3_4_allKeys[0].rt
            key_resp_3_4.duration = _key_resp_3_4_allKeys[0].duration
    
    # *trial_fixation_3_5* updates
    
    # if trial_fixation_3_5 is starting this frame...
    if trial_fixation_3_5.status == NOT_STARTED and key_resp_3_4.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_5.frameNStart = frameN  # exact frame index
        trial_fixation_3_5.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_5.started')
        # update status
        trial_fixation_3_5.status = STARTED
        trial_fixation_3_5.setAutoDraw(True)
    
    # if trial_fixation_3_5 is active this frame...
    if trial_fixation_3_5.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_5 is stopping this frame...
    if trial_fixation_3_5.status == STARTED:
        if frameN >= (trial_fixation_3_5.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_5.tStop = t  # not accounting for scr refresh
            trial_fixation_3_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_5.stopped')
            # update status
            trial_fixation_3_5.status = FINISHED
            trial_fixation_3_5.setAutoDraw(False)
    
    # *image_3_5* updates
    
    # if image_3_5 is starting this frame...
    if image_3_5.status == NOT_STARTED and trial_fixation_3_5.status==FINISHED:
        # keep track of start time/frame for later
        image_3_5.frameNStart = frameN  # exact frame index
        image_3_5.tStart = t  # local t and not account for scr refresh
        image_3_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_5.started')
        # update status
        image_3_5.status = STARTED
        image_3_5.setAutoDraw(True)
    
    # if image_3_5 is active this frame...
    if image_3_5.status == STARTED:
        # update params
        pass
    
    # if image_3_5 is stopping this frame...
    if image_3_5.status == STARTED:
        if frameN >= (image_3_5.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_5.tStop = t  # not accounting for scr refresh
            image_3_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_5.stopped')
            # update status
            image_3_5.status = FINISHED
            image_3_5.setAutoDraw(False)
    
    # *key_resp_3_5* updates
    waitOnFlip = False
    
    # if key_resp_3_5 is starting this frame...
    if key_resp_3_5.status == NOT_STARTED and trial_fixation_3_5.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_5.frameNStart = frameN  # exact frame index
        key_resp_3_5.tStart = t  # local t and not account for scr refresh
        key_resp_3_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_5.started')
        # update status
        key_resp_3_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_5 is stopping this frame...
    if key_resp_3_5.status == STARTED:
        if frameN >= (key_resp_3_5.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_5.tStop = t  # not accounting for scr refresh
            key_resp_3_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_5.stopped')
            # update status
            key_resp_3_5.status = FINISHED
            key_resp_3_5.status = FINISHED
    if key_resp_3_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_5.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_5_allKeys.extend(theseKeys)
        if len(_key_resp_3_5_allKeys):
            key_resp_3_5.keys = _key_resp_3_5_allKeys[0].name  # just the first key pressed
            key_resp_3_5.rt = _key_resp_3_5_allKeys[0].rt
            key_resp_3_5.duration = _key_resp_3_5_allKeys[0].duration
    
    # *trial_fixation_3_6* updates
    
    # if trial_fixation_3_6 is starting this frame...
    if trial_fixation_3_6.status == NOT_STARTED and key_resp_3_5.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_6.frameNStart = frameN  # exact frame index
        trial_fixation_3_6.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_6.started')
        # update status
        trial_fixation_3_6.status = STARTED
        trial_fixation_3_6.setAutoDraw(True)
    
    # if trial_fixation_3_6 is active this frame...
    if trial_fixation_3_6.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_6 is stopping this frame...
    if trial_fixation_3_6.status == STARTED:
        if frameN >= (trial_fixation_3_6.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_6.tStop = t  # not accounting for scr refresh
            trial_fixation_3_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_6.stopped')
            # update status
            trial_fixation_3_6.status = FINISHED
            trial_fixation_3_6.setAutoDraw(False)
    
    # *image_3_6* updates
    
    # if image_3_6 is starting this frame...
    if image_3_6.status == NOT_STARTED and trial_fixation_3_6.status==FINISHED:
        # keep track of start time/frame for later
        image_3_6.frameNStart = frameN  # exact frame index
        image_3_6.tStart = t  # local t and not account for scr refresh
        image_3_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_6.started')
        # update status
        image_3_6.status = STARTED
        image_3_6.setAutoDraw(True)
    
    # if image_3_6 is active this frame...
    if image_3_6.status == STARTED:
        # update params
        pass
    
    # if image_3_6 is stopping this frame...
    if image_3_6.status == STARTED:
        if frameN >= (image_3_6.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_6.tStop = t  # not accounting for scr refresh
            image_3_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_6.stopped')
            # update status
            image_3_6.status = FINISHED
            image_3_6.setAutoDraw(False)
    
    # *key_resp_3_6* updates
    waitOnFlip = False
    
    # if key_resp_3_6 is starting this frame...
    if key_resp_3_6.status == NOT_STARTED and trial_fixation_3_6.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_6.frameNStart = frameN  # exact frame index
        key_resp_3_6.tStart = t  # local t and not account for scr refresh
        key_resp_3_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_6.started')
        # update status
        key_resp_3_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_6 is stopping this frame...
    if key_resp_3_6.status == STARTED:
        if frameN >= (key_resp_3_6.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_6.tStop = t  # not accounting for scr refresh
            key_resp_3_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_6.stopped')
            # update status
            key_resp_3_6.status = FINISHED
            key_resp_3_6.status = FINISHED
    if key_resp_3_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_6.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_6_allKeys.extend(theseKeys)
        if len(_key_resp_3_6_allKeys):
            key_resp_3_6.keys = _key_resp_3_6_allKeys[0].name  # just the first key pressed
            key_resp_3_6.rt = _key_resp_3_6_allKeys[0].rt
            key_resp_3_6.duration = _key_resp_3_6_allKeys[0].duration
    
    # *trial_fixation_3_7* updates
    
    # if trial_fixation_3_7 is starting this frame...
    if trial_fixation_3_7.status == NOT_STARTED and key_resp_3_6.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_7.frameNStart = frameN  # exact frame index
        trial_fixation_3_7.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_7.started')
        # update status
        trial_fixation_3_7.status = STARTED
        trial_fixation_3_7.setAutoDraw(True)
    
    # if trial_fixation_3_7 is active this frame...
    if trial_fixation_3_7.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_7 is stopping this frame...
    if trial_fixation_3_7.status == STARTED:
        if frameN >= (trial_fixation_3_7.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_7.tStop = t  # not accounting for scr refresh
            trial_fixation_3_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_7.stopped')
            # update status
            trial_fixation_3_7.status = FINISHED
            trial_fixation_3_7.setAutoDraw(False)
    
    # *image_3_7* updates
    
    # if image_3_7 is starting this frame...
    if image_3_7.status == NOT_STARTED and trial_fixation_3_7.status==FINISHED:
        # keep track of start time/frame for later
        image_3_7.frameNStart = frameN  # exact frame index
        image_3_7.tStart = t  # local t and not account for scr refresh
        image_3_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_7.started')
        # update status
        image_3_7.status = STARTED
        image_3_7.setAutoDraw(True)
    
    # if image_3_7 is active this frame...
    if image_3_7.status == STARTED:
        # update params
        pass
    
    # if image_3_7 is stopping this frame...
    if image_3_7.status == STARTED:
        if frameN >= (image_3_7.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_7.tStop = t  # not accounting for scr refresh
            image_3_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_7.stopped')
            # update status
            image_3_7.status = FINISHED
            image_3_7.setAutoDraw(False)
    
    # *key_resp_3_7* updates
    waitOnFlip = False
    
    # if key_resp_3_7 is starting this frame...
    if key_resp_3_7.status == NOT_STARTED and trial_fixation_3_7.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_7.frameNStart = frameN  # exact frame index
        key_resp_3_7.tStart = t  # local t and not account for scr refresh
        key_resp_3_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_7.started')
        # update status
        key_resp_3_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_7 is stopping this frame...
    if key_resp_3_7.status == STARTED:
        if frameN >= (key_resp_3_7.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_7.tStop = t  # not accounting for scr refresh
            key_resp_3_7.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_7.stopped')
            # update status
            key_resp_3_7.status = FINISHED
            key_resp_3_7.status = FINISHED
    if key_resp_3_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_7.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_7_allKeys.extend(theseKeys)
        if len(_key_resp_3_7_allKeys):
            key_resp_3_7.keys = _key_resp_3_7_allKeys[0].name  # just the first key pressed
            key_resp_3_7.rt = _key_resp_3_7_allKeys[0].rt
            key_resp_3_7.duration = _key_resp_3_7_allKeys[0].duration
    
    # *trial_fixation_3_8* updates
    
    # if trial_fixation_3_8 is starting this frame...
    if trial_fixation_3_8.status == NOT_STARTED and key_resp_3_7.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_8.frameNStart = frameN  # exact frame index
        trial_fixation_3_8.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_8.started')
        # update status
        trial_fixation_3_8.status = STARTED
        trial_fixation_3_8.setAutoDraw(True)
    
    # if trial_fixation_3_8 is active this frame...
    if trial_fixation_3_8.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_8 is stopping this frame...
    if trial_fixation_3_8.status == STARTED:
        if frameN >= (trial_fixation_3_8.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_8.tStop = t  # not accounting for scr refresh
            trial_fixation_3_8.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_8.stopped')
            # update status
            trial_fixation_3_8.status = FINISHED
            trial_fixation_3_8.setAutoDraw(False)
    
    # *image_3_8* updates
    
    # if image_3_8 is starting this frame...
    if image_3_8.status == NOT_STARTED and trial_fixation_3_8.status==FINISHED:
        # keep track of start time/frame for later
        image_3_8.frameNStart = frameN  # exact frame index
        image_3_8.tStart = t  # local t and not account for scr refresh
        image_3_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_8.started')
        # update status
        image_3_8.status = STARTED
        image_3_8.setAutoDraw(True)
    
    # if image_3_8 is active this frame...
    if image_3_8.status == STARTED:
        # update params
        pass
    
    # if image_3_8 is stopping this frame...
    if image_3_8.status == STARTED:
        if frameN >= (image_3_8.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_8.tStop = t  # not accounting for scr refresh
            image_3_8.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_8.stopped')
            # update status
            image_3_8.status = FINISHED
            image_3_8.setAutoDraw(False)
    
    # *key_resp_3_8* updates
    waitOnFlip = False
    
    # if key_resp_3_8 is starting this frame...
    if key_resp_3_8.status == NOT_STARTED and trial_fixation_3_8.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_8.frameNStart = frameN  # exact frame index
        key_resp_3_8.tStart = t  # local t and not account for scr refresh
        key_resp_3_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_8.started')
        # update status
        key_resp_3_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_8 is stopping this frame...
    if key_resp_3_8.status == STARTED:
        if frameN >= (key_resp_3_8.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_8.tStop = t  # not accounting for scr refresh
            key_resp_3_8.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_8.stopped')
            # update status
            key_resp_3_8.status = FINISHED
            key_resp_3_8.status = FINISHED
    if key_resp_3_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_8.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_8_allKeys.extend(theseKeys)
        if len(_key_resp_3_8_allKeys):
            key_resp_3_8.keys = _key_resp_3_8_allKeys[0].name  # just the first key pressed
            key_resp_3_8.rt = _key_resp_3_8_allKeys[0].rt
            key_resp_3_8.duration = _key_resp_3_8_allKeys[0].duration
    
    # *trial_fixation_3_9* updates
    
    # if trial_fixation_3_9 is starting this frame...
    if trial_fixation_3_9.status == NOT_STARTED and key_resp_3_8.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_9.frameNStart = frameN  # exact frame index
        trial_fixation_3_9.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_9.started')
        # update status
        trial_fixation_3_9.status = STARTED
        trial_fixation_3_9.setAutoDraw(True)
    
    # if trial_fixation_3_9 is active this frame...
    if trial_fixation_3_9.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_9 is stopping this frame...
    if trial_fixation_3_9.status == STARTED:
        if frameN >= (trial_fixation_3_9.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_9.tStop = t  # not accounting for scr refresh
            trial_fixation_3_9.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_9.stopped')
            # update status
            trial_fixation_3_9.status = FINISHED
            trial_fixation_3_9.setAutoDraw(False)
    
    # *image_3_9* updates
    
    # if image_3_9 is starting this frame...
    if image_3_9.status == NOT_STARTED and trial_fixation_3_9.status==FINISHED:
        # keep track of start time/frame for later
        image_3_9.frameNStart = frameN  # exact frame index
        image_3_9.tStart = t  # local t and not account for scr refresh
        image_3_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_9.started')
        # update status
        image_3_9.status = STARTED
        image_3_9.setAutoDraw(True)
    
    # if image_3_9 is active this frame...
    if image_3_9.status == STARTED:
        # update params
        pass
    
    # if image_3_9 is stopping this frame...
    if image_3_9.status == STARTED:
        if frameN >= (image_3_9.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_9.tStop = t  # not accounting for scr refresh
            image_3_9.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_9.stopped')
            # update status
            image_3_9.status = FINISHED
            image_3_9.setAutoDraw(False)
    
    # *key_resp_3_9* updates
    waitOnFlip = False
    
    # if key_resp_3_9 is starting this frame...
    if key_resp_3_9.status == NOT_STARTED and trial_fixation_3_9.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_9.frameNStart = frameN  # exact frame index
        key_resp_3_9.tStart = t  # local t and not account for scr refresh
        key_resp_3_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_9.started')
        # update status
        key_resp_3_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_9 is stopping this frame...
    if key_resp_3_9.status == STARTED:
        if frameN >= (key_resp_3_9.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_9.tStop = t  # not accounting for scr refresh
            key_resp_3_9.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_9.stopped')
            # update status
            key_resp_3_9.status = FINISHED
            key_resp_3_9.status = FINISHED
    if key_resp_3_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_9.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_9_allKeys.extend(theseKeys)
        if len(_key_resp_3_9_allKeys):
            key_resp_3_9.keys = _key_resp_3_9_allKeys[0].name  # just the first key pressed
            key_resp_3_9.rt = _key_resp_3_9_allKeys[0].rt
            key_resp_3_9.duration = _key_resp_3_9_allKeys[0].duration
    
    # *trial_fixation_3_10* updates
    
    # if trial_fixation_3_10 is starting this frame...
    if trial_fixation_3_10.status == NOT_STARTED and key_resp_3_9.status==FINISHED:
        # keep track of start time/frame for later
        trial_fixation_3_10.frameNStart = frameN  # exact frame index
        trial_fixation_3_10.tStart = t  # local t and not account for scr refresh
        trial_fixation_3_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trial_fixation_3_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trial_fixation_3_10.started')
        # update status
        trial_fixation_3_10.status = STARTED
        trial_fixation_3_10.setAutoDraw(True)
    
    # if trial_fixation_3_10 is active this frame...
    if trial_fixation_3_10.status == STARTED:
        # update params
        pass
    
    # if trial_fixation_3_10 is stopping this frame...
    if trial_fixation_3_10.status == STARTED:
        if frameN >= (trial_fixation_3_10.frameNStart + 30.0):
            # keep track of stop time/frame for later
            trial_fixation_3_10.tStop = t  # not accounting for scr refresh
            trial_fixation_3_10.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_3_10.stopped')
            # update status
            trial_fixation_3_10.status = FINISHED
            trial_fixation_3_10.setAutoDraw(False)
    
    # *image_3_10* updates
    
    # if image_3_10 is starting this frame...
    if image_3_10.status == NOT_STARTED and trial_fixation_3_10.status==FINISHED:
        # keep track of start time/frame for later
        image_3_10.frameNStart = frameN  # exact frame index
        image_3_10.tStart = t  # local t and not account for scr refresh
        image_3_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_3_10.started')
        # update status
        image_3_10.status = STARTED
        image_3_10.setAutoDraw(True)
    
    # if image_3_10 is active this frame...
    if image_3_10.status == STARTED:
        # update params
        pass
    
    # if image_3_10 is stopping this frame...
    if image_3_10.status == STARTED:
        if frameN >= (image_3_10.frameNStart + 150.0):
            # keep track of stop time/frame for later
            image_3_10.tStop = t  # not accounting for scr refresh
            image_3_10.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_3_10.stopped')
            # update status
            image_3_10.status = FINISHED
            image_3_10.setAutoDraw(False)
    
    # *key_resp_3_10* updates
    waitOnFlip = False
    
    # if key_resp_3_10 is starting this frame...
    if key_resp_3_10.status == NOT_STARTED and trial_fixation_3_10.status==FINISHED:
        # keep track of start time/frame for later
        key_resp_3_10.frameNStart = frameN  # exact frame index
        key_resp_3_10.tStart = t  # local t and not account for scr refresh
        key_resp_3_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3_10, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3_10.started')
        # update status
        key_resp_3_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    
    # if key_resp_3_10 is stopping this frame...
    if key_resp_3_10.status == STARTED:
        if frameN >= (key_resp_3_10.frameNStart + 150):
            # keep track of stop time/frame for later
            key_resp_3_10.tStop = t  # not accounting for scr refresh
            key_resp_3_10.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3_10.stopped')
            # update status
            key_resp_3_10.status = FINISHED
            key_resp_3_10.status = FINISHED
    if key_resp_3_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3_10.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_10_allKeys.extend(theseKeys)
        if len(_key_resp_3_10_allKeys):
            key_resp_3_10.keys = _key_resp_3_10_allKeys[0].name  # just the first key pressed
            key_resp_3_10.rt = _key_resp_3_10_allKeys[0].rt
            key_resp_3_10.duration = _key_resp_3_10_allKeys[0].duration
    
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
# check responses
if key_resp_0_1.keys in ['', [], None]:  # No response was made
    key_resp_0_1.keys = None
thisExp.addData('key_resp_0_1.keys',key_resp_0_1.keys)
if key_resp_0_1.keys != None:  # we had a response
    thisExp.addData('key_resp_0_1.rt', key_resp_0_1.rt)
    thisExp.addData('key_resp_0_1.duration', key_resp_0_1.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_2.keys in ['', [], None]:  # No response was made
    key_resp_0_2.keys = None
thisExp.addData('key_resp_0_2.keys',key_resp_0_2.keys)
if key_resp_0_2.keys != None:  # we had a response
    thisExp.addData('key_resp_0_2.rt', key_resp_0_2.rt)
    thisExp.addData('key_resp_0_2.duration', key_resp_0_2.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_3.keys in ['', [], None]:  # No response was made
    key_resp_0_3.keys = None
thisExp.addData('key_resp_0_3.keys',key_resp_0_3.keys)
if key_resp_0_3.keys != None:  # we had a response
    thisExp.addData('key_resp_0_3.rt', key_resp_0_3.rt)
    thisExp.addData('key_resp_0_3.duration', key_resp_0_3.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_4.keys in ['', [], None]:  # No response was made
    key_resp_0_4.keys = None
thisExp.addData('key_resp_0_4.keys',key_resp_0_4.keys)
if key_resp_0_4.keys != None:  # we had a response
    thisExp.addData('key_resp_0_4.rt', key_resp_0_4.rt)
    thisExp.addData('key_resp_0_4.duration', key_resp_0_4.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_5.keys in ['', [], None]:  # No response was made
    key_resp_0_5.keys = None
thisExp.addData('key_resp_0_5.keys',key_resp_0_5.keys)
if key_resp_0_5.keys != None:  # we had a response
    thisExp.addData('key_resp_0_5.rt', key_resp_0_5.rt)
    thisExp.addData('key_resp_0_5.duration', key_resp_0_5.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_6.keys in ['', [], None]:  # No response was made
    key_resp_0_6.keys = None
thisExp.addData('key_resp_0_6.keys',key_resp_0_6.keys)
if key_resp_0_6.keys != None:  # we had a response
    thisExp.addData('key_resp_0_6.rt', key_resp_0_6.rt)
    thisExp.addData('key_resp_0_6.duration', key_resp_0_6.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_7.keys in ['', [], None]:  # No response was made
    key_resp_0_7.keys = None
thisExp.addData('key_resp_0_7.keys',key_resp_0_7.keys)
if key_resp_0_7.keys != None:  # we had a response
    thisExp.addData('key_resp_0_7.rt', key_resp_0_7.rt)
    thisExp.addData('key_resp_0_7.duration', key_resp_0_7.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_8.keys in ['', [], None]:  # No response was made
    key_resp_0_8.keys = None
thisExp.addData('key_resp_0_8.keys',key_resp_0_8.keys)
if key_resp_0_8.keys != None:  # we had a response
    thisExp.addData('key_resp_0_8.rt', key_resp_0_8.rt)
    thisExp.addData('key_resp_0_8.duration', key_resp_0_8.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_9.keys in ['', [], None]:  # No response was made
    key_resp_0_9.keys = None
thisExp.addData('key_resp_0_9.keys',key_resp_0_9.keys)
if key_resp_0_9.keys != None:  # we had a response
    thisExp.addData('key_resp_0_9.rt', key_resp_0_9.rt)
    thisExp.addData('key_resp_0_9.duration', key_resp_0_9.duration)
thisExp.nextEntry()
# check responses
if key_resp_0_10.keys in ['', [], None]:  # No response was made
    key_resp_0_10.keys = None
thisExp.addData('key_resp_0_10.keys',key_resp_0_10.keys)
if key_resp_0_10.keys != None:  # we had a response
    thisExp.addData('key_resp_0_10.rt', key_resp_0_10.rt)
    thisExp.addData('key_resp_0_10.duration', key_resp_0_10.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_1.keys in ['', [], None]:  # No response was made
    key_resp_3_1.keys = None
thisExp.addData('key_resp_3_1.keys',key_resp_3_1.keys)
if key_resp_3_1.keys != None:  # we had a response
    thisExp.addData('key_resp_3_1.rt', key_resp_3_1.rt)
    thisExp.addData('key_resp_3_1.duration', key_resp_3_1.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_2.keys in ['', [], None]:  # No response was made
    key_resp_3_2.keys = None
thisExp.addData('key_resp_3_2.keys',key_resp_3_2.keys)
if key_resp_3_2.keys != None:  # we had a response
    thisExp.addData('key_resp_3_2.rt', key_resp_3_2.rt)
    thisExp.addData('key_resp_3_2.duration', key_resp_3_2.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_3.keys in ['', [], None]:  # No response was made
    key_resp_3_3.keys = None
thisExp.addData('key_resp_3_3.keys',key_resp_3_3.keys)
if key_resp_3_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3_3.rt', key_resp_3_3.rt)
    thisExp.addData('key_resp_3_3.duration', key_resp_3_3.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_4.keys in ['', [], None]:  # No response was made
    key_resp_3_4.keys = None
thisExp.addData('key_resp_3_4.keys',key_resp_3_4.keys)
if key_resp_3_4.keys != None:  # we had a response
    thisExp.addData('key_resp_3_4.rt', key_resp_3_4.rt)
    thisExp.addData('key_resp_3_4.duration', key_resp_3_4.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_5.keys in ['', [], None]:  # No response was made
    key_resp_3_5.keys = None
thisExp.addData('key_resp_3_5.keys',key_resp_3_5.keys)
if key_resp_3_5.keys != None:  # we had a response
    thisExp.addData('key_resp_3_5.rt', key_resp_3_5.rt)
    thisExp.addData('key_resp_3_5.duration', key_resp_3_5.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_6.keys in ['', [], None]:  # No response was made
    key_resp_3_6.keys = None
thisExp.addData('key_resp_3_6.keys',key_resp_3_6.keys)
if key_resp_3_6.keys != None:  # we had a response
    thisExp.addData('key_resp_3_6.rt', key_resp_3_6.rt)
    thisExp.addData('key_resp_3_6.duration', key_resp_3_6.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_7.keys in ['', [], None]:  # No response was made
    key_resp_3_7.keys = None
thisExp.addData('key_resp_3_7.keys',key_resp_3_7.keys)
if key_resp_3_7.keys != None:  # we had a response
    thisExp.addData('key_resp_3_7.rt', key_resp_3_7.rt)
    thisExp.addData('key_resp_3_7.duration', key_resp_3_7.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_8.keys in ['', [], None]:  # No response was made
    key_resp_3_8.keys = None
thisExp.addData('key_resp_3_8.keys',key_resp_3_8.keys)
if key_resp_3_8.keys != None:  # we had a response
    thisExp.addData('key_resp_3_8.rt', key_resp_3_8.rt)
    thisExp.addData('key_resp_3_8.duration', key_resp_3_8.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_9.keys in ['', [], None]:  # No response was made
    key_resp_3_9.keys = None
thisExp.addData('key_resp_3_9.keys',key_resp_3_9.keys)
if key_resp_3_9.keys != None:  # we had a response
    thisExp.addData('key_resp_3_9.rt', key_resp_3_9.rt)
    thisExp.addData('key_resp_3_9.duration', key_resp_3_9.duration)
thisExp.nextEntry()
# check responses
if key_resp_3_10.keys in ['', [], None]:  # No response was made
    key_resp_3_10.keys = None
thisExp.addData('key_resp_3_10.keys',key_resp_3_10.keys)
if key_resp_3_10.keys != None:  # we had a response
    thisExp.addData('key_resp_3_10.rt', key_resp_3_10.rt)
    thisExp.addData('key_resp_3_10.duration', key_resp_3_10.duration)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
run = data.TrialHandler(nReps=7.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='run')
thisExp.addLoop(run)  # add the loop to the experiment
thisRun = run.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in run:
    currentLoop = run
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "stim_block" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from prep_trials_1
    n = run.thisN
    
    im_file_1 = stim_block_1[n*10]
    im_file_2 = stim_block_1[n*10+1]
    im_file_3 = stim_block_1[n*10+2]
    im_file_4 = stim_block_1[n*10+3]
    im_file_5 = stim_block_1[n*10+4]
    im_file_6 = stim_block_1[n*10+5]
    im_file_7 = stim_block_1[n*10+6]
    im_file_8 = stim_block_1[n*10+7]
    im_file_9 = stim_block_1[n*10+8]
    im_file_10 = stim_block_1[n*10+9]
    
    target_im_1 = 'nback_stimuli/'+target_ls[n*2]
    block_rule_1 = rules_ls[n*2]
    
    if block_rule_1 == '0-Back':
        rule_txt_1 = '目標'
        txt_loc_1 = (0,0.2)
        im_loc_1 = (0,-0.1)
    elif block_rule_1 == '2-Back':
        rule_txt_1 = '兩項之前'
        txt_loc_1 = (0,0)
        im_loc_1 = (1,1)
    
    thisExp.addData('run_no', run_idx[n//4])
    # Run 'Begin Routine' code from prep_trials_2
    n = run.thisN + 1
    im_file_2_1 = stim_block_2[n*10]
    im_file_2_2 = stim_block_2[n*10+1]
    im_file_2_3 = stim_block_2[n*10+2]
    im_file_2_4 = stim_block_2[n*10+3]
    im_file_2_5 = stim_block_2[n*10+4]
    im_file_2_6 = stim_block_2[n*10+5]
    im_file_2_7 = stim_block_2[n*10+6]
    im_file_2_8 = stim_block_2[n*10+7]
    im_file_2_9 = stim_block_2[n*10+8]
    im_file_2_10 = stim_block_2[n*10+9]
    
    target_im_2 = 'nback_stimuli/'+target_ls[n*2+1]
    block_rule_2 = rules_ls[n*2+1]
    
    if block_rule_2 == '0-Back':
        rule_txt_2 = '目標'
        txt_loc_2 = (0,0.2)
        im_loc_2 = (0,-0.1)
    elif block_rule_2 == '2-Back':
        rule_txt_2 = '兩項之前'
        txt_loc_2 = (0,0)
        im_loc_2 = (1,1)
    prep_instr_1.setPos(txt_loc_1)
    prep_instr_1.setText(rule_txt_1)
    target_1.setPos(im_loc_1)
    target_1.setImage(target_im_1)
    image_1_1.setImage(im_file_1)
    key_resp_1_1.keys = []
    key_resp_1_1.rt = []
    _key_resp_1_1_allKeys = []
    image_1_2.setImage(im_file_2)
    key_resp_1_2.keys = []
    key_resp_1_2.rt = []
    _key_resp_1_2_allKeys = []
    image_1_3.setImage(im_file_3)
    key_resp_1_3.keys = []
    key_resp_1_3.rt = []
    _key_resp_1_3_allKeys = []
    image_1_4.setImage(im_file_4)
    key_resp_1_4.keys = []
    key_resp_1_4.rt = []
    _key_resp_1_4_allKeys = []
    image_1_5.setImage(im_file_5)
    key_resp_1_5.keys = []
    key_resp_1_5.rt = []
    _key_resp_1_5_allKeys = []
    image_1_6.setImage(im_file_6)
    key_resp_1_6.keys = []
    key_resp_1_6.rt = []
    _key_resp_1_6_allKeys = []
    image_1_7.setImage(im_file_7)
    key_resp_1_7.keys = []
    key_resp_1_7.rt = []
    _key_resp_1_7_allKeys = []
    image_1_8.setImage(im_file_8)
    key_resp_1_8.keys = []
    key_resp_1_8.rt = []
    _key_resp_1_8_allKeys = []
    image_1_9.setImage(im_file_9)
    key_resp_1_9.keys = []
    key_resp_1_9.rt = []
    _key_resp_1_9_allKeys = []
    image_1_10.setImage(im_file_10)
    key_resp_1_10.keys = []
    key_resp_1_10.rt = []
    _key_resp_1_10_allKeys = []
    prep_instr_2.setPos(txt_loc_2)
    prep_instr_2.setText(rule_txt_2)
    target_2.setPos(im_loc_2)
    target_2.setImage(target_im_2)
    image_2_1.setImage(im_file_2_1)
    key_resp_2_1.keys = []
    key_resp_2_1.rt = []
    _key_resp_2_1_allKeys = []
    image_2_2.setImage(im_file_2_2)
    key_resp_2_2.keys = []
    key_resp_2_2.rt = []
    _key_resp_2_2_allKeys = []
    image_2_3.setImage(im_file_2_3)
    key_resp_2_3.keys = []
    key_resp_2_3.rt = []
    _key_resp_2_3_allKeys = []
    image_2_4.setImage(im_file_2_4)
    key_resp_2_4.keys = []
    key_resp_2_4.rt = []
    _key_resp_2_4_allKeys = []
    image_2_5.setImage(im_file_2_5)
    key_resp_2_5.keys = []
    key_resp_2_5.rt = []
    _key_resp_2_5_allKeys = []
    image_2_6.setImage(im_file_2_6)
    key_resp_2_6.keys = []
    key_resp_2_6.rt = []
    _key_resp_2_6_allKeys = []
    image_2_7.setImage(im_file_2_7)
    key_resp_2_7.keys = []
    key_resp_2_7.rt = []
    _key_resp_2_7_allKeys = []
    image_2_8.setImage(im_file_2_8)
    key_resp_2_8.keys = []
    key_resp_2_8.rt = []
    _key_resp_2_8_allKeys = []
    image_2_9.setImage(im_file_2_9)
    key_resp_2_9.keys = []
    key_resp_2_9.rt = []
    _key_resp_2_9_allKeys = []
    image_2_10.setImage(im_file_2_10)
    key_resp_2_10.keys = []
    key_resp_2_10.rt = []
    _key_resp_2_10_allKeys = []
    # keep track of which components have finished
    stim_blockComponents = [rest_txt_1, prep_instr_1, target_1, trial_fixation_1_1, image_1_1, key_resp_1_1, trial_fixation_1_2, image_1_2, key_resp_1_2, trial_fixation_1_3, image_1_3, key_resp_1_3, trial_fixation_1_4, image_1_4, key_resp_1_4, trial_fixation_1_5, image_1_5, key_resp_1_5, trial_fixation_1_6, image_1_6, key_resp_1_6, trial_fixation_1_7, image_1_7, key_resp_1_7, trial_fixation_1_8, image_1_8, key_resp_1_8, trial_fixation_1_9, image_1_9, key_resp_1_9, trial_fixation_1_10, image_1_10, key_resp_1_10, prep_instr_2, target_2, trial_fixation_2_1, image_2_1, key_resp_2_1, trial_fixation_2_2, image_2_2, key_resp_2_2, trial_fixation_2_3, image_2_3, key_resp_2_3, trial_fixation_2_4, image_2_4, key_resp_2_4, trial_fixation_2_5, image_2_5, key_resp_2_5, trial_fixation_2_6, image_2_6, key_resp_2_6, trial_fixation_2_7, image_2_7, key_resp_2_7, trial_fixation_2_8, image_2_8, key_resp_2_8, trial_fixation_2_9, image_2_9, key_resp_2_9, trial_fixation_2_10, image_2_10, key_resp_2_10]
    for thisComponent in stim_blockComponents:
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
    
    # --- Run Routine "stim_block" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_txt_1* updates
        
        # if rest_txt_1 is starting this frame...
        if rest_txt_1.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            rest_txt_1.frameNStart = frameN  # exact frame index
            rest_txt_1.tStart = t  # local t and not account for scr refresh
            rest_txt_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_txt_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_txt_1.started')
            # update status
            rest_txt_1.status = STARTED
            rest_txt_1.setAutoDraw(True)
        
        # if rest_txt_1 is active this frame...
        if rest_txt_1.status == STARTED:
            # update params
            pass
        
        # if rest_txt_1 is stopping this frame...
        if rest_txt_1.status == STARTED:
            if frameN >= 901:
                # keep track of stop time/frame for later
                rest_txt_1.tStop = t  # not accounting for scr refresh
                rest_txt_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_txt_1.stopped')
                # update status
                rest_txt_1.status = FINISHED
                rest_txt_1.setAutoDraw(False)
        
        # *prep_instr_1* updates
        
        # if prep_instr_1 is starting this frame...
        if prep_instr_1.status == NOT_STARTED and rest_txt_1.status==FINISHED:
            # keep track of start time/frame for later
            prep_instr_1.frameNStart = frameN  # exact frame index
            prep_instr_1.tStart = t  # local t and not account for scr refresh
            prep_instr_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prep_instr_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prep_instr_1.started')
            # update status
            prep_instr_1.status = STARTED
            prep_instr_1.setAutoDraw(True)
        
        # if prep_instr_1 is active this frame...
        if prep_instr_1.status == STARTED:
            # update params
            pass
        
        # if prep_instr_1 is stopping this frame...
        if prep_instr_1.status == STARTED:
            if frameN >= (prep_instr_1.frameNStart + 150):
                # keep track of stop time/frame for later
                prep_instr_1.tStop = t  # not accounting for scr refresh
                prep_instr_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prep_instr_1.stopped')
                # update status
                prep_instr_1.status = FINISHED
                prep_instr_1.setAutoDraw(False)
        
        # *target_1* updates
        
        # if target_1 is starting this frame...
        if target_1.status == NOT_STARTED and rest_txt_1.status==FINISHED:
            # keep track of start time/frame for later
            target_1.frameNStart = frameN  # exact frame index
            target_1.tStart = t  # local t and not account for scr refresh
            target_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_1.started')
            # update status
            target_1.status = STARTED
            target_1.setAutoDraw(True)
        
        # if target_1 is active this frame...
        if target_1.status == STARTED:
            # update params
            pass
        
        # if target_1 is stopping this frame...
        if target_1.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                target_1.tStop = t  # not accounting for scr refresh
                target_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_1.stopped')
                # update status
                target_1.status = FINISHED
                target_1.setAutoDraw(False)
        
        # *trial_fixation_1_1* updates
        
        # if trial_fixation_1_1 is starting this frame...
        if trial_fixation_1_1.status == NOT_STARTED and target_1.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_1.frameNStart = frameN  # exact frame index
            trial_fixation_1_1.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_1.started')
            # update status
            trial_fixation_1_1.status = STARTED
            trial_fixation_1_1.setAutoDraw(True)
        
        # if trial_fixation_1_1 is active this frame...
        if trial_fixation_1_1.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_1 is stopping this frame...
        if trial_fixation_1_1.status == STARTED:
            if frameN >= (trial_fixation_1_1.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_1.tStop = t  # not accounting for scr refresh
                trial_fixation_1_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_1.stopped')
                # update status
                trial_fixation_1_1.status = FINISHED
                trial_fixation_1_1.setAutoDraw(False)
        
        # *image_1_1* updates
        
        # if image_1_1 is starting this frame...
        if image_1_1.status == NOT_STARTED and trial_fixation_1_1.status==FINISHED:
            # keep track of start time/frame for later
            image_1_1.frameNStart = frameN  # exact frame index
            image_1_1.tStart = t  # local t and not account for scr refresh
            image_1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_1.started')
            # update status
            image_1_1.status = STARTED
            image_1_1.setAutoDraw(True)
        
        # if image_1_1 is active this frame...
        if image_1_1.status == STARTED:
            # update params
            pass
        
        # if image_1_1 is stopping this frame...
        if image_1_1.status == STARTED:
            if frameN >= (image_1_1.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_1.tStop = t  # not accounting for scr refresh
                image_1_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_1.stopped')
                # update status
                image_1_1.status = FINISHED
                image_1_1.setAutoDraw(False)
        
        # *key_resp_1_1* updates
        waitOnFlip = False
        
        # if key_resp_1_1 is starting this frame...
        if key_resp_1_1.status == NOT_STARTED and trial_fixation_1_1.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_1.frameNStart = frameN  # exact frame index
            key_resp_1_1.tStart = t  # local t and not account for scr refresh
            key_resp_1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_1.started')
            # update status
            key_resp_1_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_1 is stopping this frame...
        if key_resp_1_1.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_1.tStop = t  # not accounting for scr refresh
                key_resp_1_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_1.stopped')
                # update status
                key_resp_1_1.status = FINISHED
                key_resp_1_1.status = FINISHED
        if key_resp_1_1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_1.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_1_allKeys.extend(theseKeys)
            if len(_key_resp_1_1_allKeys):
                key_resp_1_1.keys = _key_resp_1_1_allKeys[0].name  # just the first key pressed
                key_resp_1_1.rt = _key_resp_1_1_allKeys[0].rt
                key_resp_1_1.duration = _key_resp_1_1_allKeys[0].duration
        
        # *trial_fixation_1_2* updates
        
        # if trial_fixation_1_2 is starting this frame...
        if trial_fixation_1_2.status == NOT_STARTED and key_resp_1_1.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_2.frameNStart = frameN  # exact frame index
            trial_fixation_1_2.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_2.started')
            # update status
            trial_fixation_1_2.status = STARTED
            trial_fixation_1_2.setAutoDraw(True)
        
        # if trial_fixation_1_2 is active this frame...
        if trial_fixation_1_2.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_2 is stopping this frame...
        if trial_fixation_1_2.status == STARTED:
            if frameN >= (trial_fixation_1_2.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_2.tStop = t  # not accounting for scr refresh
                trial_fixation_1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_2.stopped')
                # update status
                trial_fixation_1_2.status = FINISHED
                trial_fixation_1_2.setAutoDraw(False)
        
        # *image_1_2* updates
        
        # if image_1_2 is starting this frame...
        if image_1_2.status == NOT_STARTED and trial_fixation_1_2.status==FINISHED:
            # keep track of start time/frame for later
            image_1_2.frameNStart = frameN  # exact frame index
            image_1_2.tStart = t  # local t and not account for scr refresh
            image_1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_2.started')
            # update status
            image_1_2.status = STARTED
            image_1_2.setAutoDraw(True)
        
        # if image_1_2 is active this frame...
        if image_1_2.status == STARTED:
            # update params
            pass
        
        # if image_1_2 is stopping this frame...
        if image_1_2.status == STARTED:
            if frameN >= (image_1_2.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_2.tStop = t  # not accounting for scr refresh
                image_1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_2.stopped')
                # update status
                image_1_2.status = FINISHED
                image_1_2.setAutoDraw(False)
        
        # *key_resp_1_2* updates
        waitOnFlip = False
        
        # if key_resp_1_2 is starting this frame...
        if key_resp_1_2.status == NOT_STARTED and trial_fixation_1_2.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_2.frameNStart = frameN  # exact frame index
            key_resp_1_2.tStart = t  # local t and not account for scr refresh
            key_resp_1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_2.started')
            # update status
            key_resp_1_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_2 is stopping this frame...
        if key_resp_1_2.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_2.tStop = t  # not accounting for scr refresh
                key_resp_1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_2.stopped')
                # update status
                key_resp_1_2.status = FINISHED
                key_resp_1_2.status = FINISHED
        if key_resp_1_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_2.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_2_allKeys.extend(theseKeys)
            if len(_key_resp_1_2_allKeys):
                key_resp_1_2.keys = _key_resp_1_2_allKeys[0].name  # just the first key pressed
                key_resp_1_2.rt = _key_resp_1_2_allKeys[0].rt
                key_resp_1_2.duration = _key_resp_1_2_allKeys[0].duration
        
        # *trial_fixation_1_3* updates
        
        # if trial_fixation_1_3 is starting this frame...
        if trial_fixation_1_3.status == NOT_STARTED and key_resp_1_2.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_3.frameNStart = frameN  # exact frame index
            trial_fixation_1_3.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_3.started')
            # update status
            trial_fixation_1_3.status = STARTED
            trial_fixation_1_3.setAutoDraw(True)
        
        # if trial_fixation_1_3 is active this frame...
        if trial_fixation_1_3.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_3 is stopping this frame...
        if trial_fixation_1_3.status == STARTED:
            if frameN >= (trial_fixation_1_3.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_3.tStop = t  # not accounting for scr refresh
                trial_fixation_1_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_3.stopped')
                # update status
                trial_fixation_1_3.status = FINISHED
                trial_fixation_1_3.setAutoDraw(False)
        
        # *image_1_3* updates
        
        # if image_1_3 is starting this frame...
        if image_1_3.status == NOT_STARTED and trial_fixation_1_3.status==FINISHED:
            # keep track of start time/frame for later
            image_1_3.frameNStart = frameN  # exact frame index
            image_1_3.tStart = t  # local t and not account for scr refresh
            image_1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_3.started')
            # update status
            image_1_3.status = STARTED
            image_1_3.setAutoDraw(True)
        
        # if image_1_3 is active this frame...
        if image_1_3.status == STARTED:
            # update params
            pass
        
        # if image_1_3 is stopping this frame...
        if image_1_3.status == STARTED:
            if frameN >= (image_1_3.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_3.tStop = t  # not accounting for scr refresh
                image_1_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_3.stopped')
                # update status
                image_1_3.status = FINISHED
                image_1_3.setAutoDraw(False)
        
        # *key_resp_1_3* updates
        waitOnFlip = False
        
        # if key_resp_1_3 is starting this frame...
        if key_resp_1_3.status == NOT_STARTED and trial_fixation_1_3.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_3.frameNStart = frameN  # exact frame index
            key_resp_1_3.tStart = t  # local t and not account for scr refresh
            key_resp_1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_3.started')
            # update status
            key_resp_1_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_3 is stopping this frame...
        if key_resp_1_3.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_3.tStop = t  # not accounting for scr refresh
                key_resp_1_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_3.stopped')
                # update status
                key_resp_1_3.status = FINISHED
                key_resp_1_3.status = FINISHED
        if key_resp_1_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_3.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_3_allKeys.extend(theseKeys)
            if len(_key_resp_1_3_allKeys):
                key_resp_1_3.keys = _key_resp_1_3_allKeys[0].name  # just the first key pressed
                key_resp_1_3.rt = _key_resp_1_3_allKeys[0].rt
                key_resp_1_3.duration = _key_resp_1_3_allKeys[0].duration
        
        # *trial_fixation_1_4* updates
        
        # if trial_fixation_1_4 is starting this frame...
        if trial_fixation_1_4.status == NOT_STARTED and key_resp_1_3.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_4.frameNStart = frameN  # exact frame index
            trial_fixation_1_4.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_4.started')
            # update status
            trial_fixation_1_4.status = STARTED
            trial_fixation_1_4.setAutoDraw(True)
        
        # if trial_fixation_1_4 is active this frame...
        if trial_fixation_1_4.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_4 is stopping this frame...
        if trial_fixation_1_4.status == STARTED:
            if frameN >= (trial_fixation_1_4.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_4.tStop = t  # not accounting for scr refresh
                trial_fixation_1_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_4.stopped')
                # update status
                trial_fixation_1_4.status = FINISHED
                trial_fixation_1_4.setAutoDraw(False)
        
        # *image_1_4* updates
        
        # if image_1_4 is starting this frame...
        if image_1_4.status == NOT_STARTED and trial_fixation_1_4.status==FINISHED:
            # keep track of start time/frame for later
            image_1_4.frameNStart = frameN  # exact frame index
            image_1_4.tStart = t  # local t and not account for scr refresh
            image_1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_4.started')
            # update status
            image_1_4.status = STARTED
            image_1_4.setAutoDraw(True)
        
        # if image_1_4 is active this frame...
        if image_1_4.status == STARTED:
            # update params
            pass
        
        # if image_1_4 is stopping this frame...
        if image_1_4.status == STARTED:
            if frameN >= (image_1_4.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_4.tStop = t  # not accounting for scr refresh
                image_1_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_4.stopped')
                # update status
                image_1_4.status = FINISHED
                image_1_4.setAutoDraw(False)
        
        # *key_resp_1_4* updates
        waitOnFlip = False
        
        # if key_resp_1_4 is starting this frame...
        if key_resp_1_4.status == NOT_STARTED and trial_fixation_1_4.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_4.frameNStart = frameN  # exact frame index
            key_resp_1_4.tStart = t  # local t and not account for scr refresh
            key_resp_1_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_4.started')
            # update status
            key_resp_1_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_4 is stopping this frame...
        if key_resp_1_4.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_4.tStop = t  # not accounting for scr refresh
                key_resp_1_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_4.stopped')
                # update status
                key_resp_1_4.status = FINISHED
                key_resp_1_4.status = FINISHED
        if key_resp_1_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_4.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_4_allKeys.extend(theseKeys)
            if len(_key_resp_1_4_allKeys):
                key_resp_1_4.keys = _key_resp_1_4_allKeys[0].name  # just the first key pressed
                key_resp_1_4.rt = _key_resp_1_4_allKeys[0].rt
                key_resp_1_4.duration = _key_resp_1_4_allKeys[0].duration
        
        # *trial_fixation_1_5* updates
        
        # if trial_fixation_1_5 is starting this frame...
        if trial_fixation_1_5.status == NOT_STARTED and key_resp_1_4.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_5.frameNStart = frameN  # exact frame index
            trial_fixation_1_5.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_5.started')
            # update status
            trial_fixation_1_5.status = STARTED
            trial_fixation_1_5.setAutoDraw(True)
        
        # if trial_fixation_1_5 is active this frame...
        if trial_fixation_1_5.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_5 is stopping this frame...
        if trial_fixation_1_5.status == STARTED:
            if frameN >= (trial_fixation_1_5.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_5.tStop = t  # not accounting for scr refresh
                trial_fixation_1_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_5.stopped')
                # update status
                trial_fixation_1_5.status = FINISHED
                trial_fixation_1_5.setAutoDraw(False)
        
        # *image_1_5* updates
        
        # if image_1_5 is starting this frame...
        if image_1_5.status == NOT_STARTED and trial_fixation_1_5.status==FINISHED:
            # keep track of start time/frame for later
            image_1_5.frameNStart = frameN  # exact frame index
            image_1_5.tStart = t  # local t and not account for scr refresh
            image_1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_5.started')
            # update status
            image_1_5.status = STARTED
            image_1_5.setAutoDraw(True)
        
        # if image_1_5 is active this frame...
        if image_1_5.status == STARTED:
            # update params
            pass
        
        # if image_1_5 is stopping this frame...
        if image_1_5.status == STARTED:
            if frameN >= (image_1_5.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_5.tStop = t  # not accounting for scr refresh
                image_1_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_5.stopped')
                # update status
                image_1_5.status = FINISHED
                image_1_5.setAutoDraw(False)
        
        # *key_resp_1_5* updates
        waitOnFlip = False
        
        # if key_resp_1_5 is starting this frame...
        if key_resp_1_5.status == NOT_STARTED and trial_fixation_1_5.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_5.frameNStart = frameN  # exact frame index
            key_resp_1_5.tStart = t  # local t and not account for scr refresh
            key_resp_1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_5.started')
            # update status
            key_resp_1_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_5 is stopping this frame...
        if key_resp_1_5.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_5.tStop = t  # not accounting for scr refresh
                key_resp_1_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_5.stopped')
                # update status
                key_resp_1_5.status = FINISHED
                key_resp_1_5.status = FINISHED
        if key_resp_1_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_5.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_5_allKeys.extend(theseKeys)
            if len(_key_resp_1_5_allKeys):
                key_resp_1_5.keys = _key_resp_1_5_allKeys[0].name  # just the first key pressed
                key_resp_1_5.rt = _key_resp_1_5_allKeys[0].rt
                key_resp_1_5.duration = _key_resp_1_5_allKeys[0].duration
        
        # *trial_fixation_1_6* updates
        
        # if trial_fixation_1_6 is starting this frame...
        if trial_fixation_1_6.status == NOT_STARTED and key_resp_1_5.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_6.frameNStart = frameN  # exact frame index
            trial_fixation_1_6.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_6.started')
            # update status
            trial_fixation_1_6.status = STARTED
            trial_fixation_1_6.setAutoDraw(True)
        
        # if trial_fixation_1_6 is active this frame...
        if trial_fixation_1_6.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_6 is stopping this frame...
        if trial_fixation_1_6.status == STARTED:
            if frameN >= (trial_fixation_1_6.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_6.tStop = t  # not accounting for scr refresh
                trial_fixation_1_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_6.stopped')
                # update status
                trial_fixation_1_6.status = FINISHED
                trial_fixation_1_6.setAutoDraw(False)
        
        # *image_1_6* updates
        
        # if image_1_6 is starting this frame...
        if image_1_6.status == NOT_STARTED and trial_fixation_1_6.status==FINISHED:
            # keep track of start time/frame for later
            image_1_6.frameNStart = frameN  # exact frame index
            image_1_6.tStart = t  # local t and not account for scr refresh
            image_1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_6.started')
            # update status
            image_1_6.status = STARTED
            image_1_6.setAutoDraw(True)
        
        # if image_1_6 is active this frame...
        if image_1_6.status == STARTED:
            # update params
            pass
        
        # if image_1_6 is stopping this frame...
        if image_1_6.status == STARTED:
            if frameN >= (image_1_6.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_6.tStop = t  # not accounting for scr refresh
                image_1_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_6.stopped')
                # update status
                image_1_6.status = FINISHED
                image_1_6.setAutoDraw(False)
        
        # *key_resp_1_6* updates
        waitOnFlip = False
        
        # if key_resp_1_6 is starting this frame...
        if key_resp_1_6.status == NOT_STARTED and trial_fixation_1_6.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_6.frameNStart = frameN  # exact frame index
            key_resp_1_6.tStart = t  # local t and not account for scr refresh
            key_resp_1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_6.started')
            # update status
            key_resp_1_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_6 is stopping this frame...
        if key_resp_1_6.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_6.tStop = t  # not accounting for scr refresh
                key_resp_1_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_6.stopped')
                # update status
                key_resp_1_6.status = FINISHED
                key_resp_1_6.status = FINISHED
        if key_resp_1_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_6.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_6_allKeys.extend(theseKeys)
            if len(_key_resp_1_6_allKeys):
                key_resp_1_6.keys = _key_resp_1_6_allKeys[0].name  # just the first key pressed
                key_resp_1_6.rt = _key_resp_1_6_allKeys[0].rt
                key_resp_1_6.duration = _key_resp_1_6_allKeys[0].duration
        
        # *trial_fixation_1_7* updates
        
        # if trial_fixation_1_7 is starting this frame...
        if trial_fixation_1_7.status == NOT_STARTED and key_resp_1_6.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_7.frameNStart = frameN  # exact frame index
            trial_fixation_1_7.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_7.started')
            # update status
            trial_fixation_1_7.status = STARTED
            trial_fixation_1_7.setAutoDraw(True)
        
        # if trial_fixation_1_7 is active this frame...
        if trial_fixation_1_7.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_7 is stopping this frame...
        if trial_fixation_1_7.status == STARTED:
            if frameN >= (trial_fixation_1_7.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_7.tStop = t  # not accounting for scr refresh
                trial_fixation_1_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_7.stopped')
                # update status
                trial_fixation_1_7.status = FINISHED
                trial_fixation_1_7.setAutoDraw(False)
        
        # *image_1_7* updates
        
        # if image_1_7 is starting this frame...
        if image_1_7.status == NOT_STARTED and trial_fixation_1_7.status==FINISHED:
            # keep track of start time/frame for later
            image_1_7.frameNStart = frameN  # exact frame index
            image_1_7.tStart = t  # local t and not account for scr refresh
            image_1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_7.started')
            # update status
            image_1_7.status = STARTED
            image_1_7.setAutoDraw(True)
        
        # if image_1_7 is active this frame...
        if image_1_7.status == STARTED:
            # update params
            pass
        
        # if image_1_7 is stopping this frame...
        if image_1_7.status == STARTED:
            if frameN >= (image_1_7.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_7.tStop = t  # not accounting for scr refresh
                image_1_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_7.stopped')
                # update status
                image_1_7.status = FINISHED
                image_1_7.setAutoDraw(False)
        
        # *key_resp_1_7* updates
        waitOnFlip = False
        
        # if key_resp_1_7 is starting this frame...
        if key_resp_1_7.status == NOT_STARTED and trial_fixation_1_7.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_7.frameNStart = frameN  # exact frame index
            key_resp_1_7.tStart = t  # local t and not account for scr refresh
            key_resp_1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_7.started')
            # update status
            key_resp_1_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_7 is stopping this frame...
        if key_resp_1_7.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_7.tStop = t  # not accounting for scr refresh
                key_resp_1_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_7.stopped')
                # update status
                key_resp_1_7.status = FINISHED
                key_resp_1_7.status = FINISHED
        if key_resp_1_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_7.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_7_allKeys.extend(theseKeys)
            if len(_key_resp_1_7_allKeys):
                key_resp_1_7.keys = _key_resp_1_7_allKeys[0].name  # just the first key pressed
                key_resp_1_7.rt = _key_resp_1_7_allKeys[0].rt
                key_resp_1_7.duration = _key_resp_1_7_allKeys[0].duration
        
        # *trial_fixation_1_8* updates
        
        # if trial_fixation_1_8 is starting this frame...
        if trial_fixation_1_8.status == NOT_STARTED and key_resp_1_7.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_8.frameNStart = frameN  # exact frame index
            trial_fixation_1_8.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_8.started')
            # update status
            trial_fixation_1_8.status = STARTED
            trial_fixation_1_8.setAutoDraw(True)
        
        # if trial_fixation_1_8 is active this frame...
        if trial_fixation_1_8.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_8 is stopping this frame...
        if trial_fixation_1_8.status == STARTED:
            if frameN >= (trial_fixation_1_8.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_8.tStop = t  # not accounting for scr refresh
                trial_fixation_1_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_8.stopped')
                # update status
                trial_fixation_1_8.status = FINISHED
                trial_fixation_1_8.setAutoDraw(False)
        
        # *image_1_8* updates
        
        # if image_1_8 is starting this frame...
        if image_1_8.status == NOT_STARTED and trial_fixation_1_8.status==FINISHED:
            # keep track of start time/frame for later
            image_1_8.frameNStart = frameN  # exact frame index
            image_1_8.tStart = t  # local t and not account for scr refresh
            image_1_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_8.started')
            # update status
            image_1_8.status = STARTED
            image_1_8.setAutoDraw(True)
        
        # if image_1_8 is active this frame...
        if image_1_8.status == STARTED:
            # update params
            pass
        
        # if image_1_8 is stopping this frame...
        if image_1_8.status == STARTED:
            if frameN >= (image_1_8.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_8.tStop = t  # not accounting for scr refresh
                image_1_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_8.stopped')
                # update status
                image_1_8.status = FINISHED
                image_1_8.setAutoDraw(False)
        
        # *key_resp_1_8* updates
        waitOnFlip = False
        
        # if key_resp_1_8 is starting this frame...
        if key_resp_1_8.status == NOT_STARTED and trial_fixation_1_8.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_8.frameNStart = frameN  # exact frame index
            key_resp_1_8.tStart = t  # local t and not account for scr refresh
            key_resp_1_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_8.started')
            # update status
            key_resp_1_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_8 is stopping this frame...
        if key_resp_1_8.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_8.tStop = t  # not accounting for scr refresh
                key_resp_1_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_8.stopped')
                # update status
                key_resp_1_8.status = FINISHED
                key_resp_1_8.status = FINISHED
        if key_resp_1_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_8.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_8_allKeys.extend(theseKeys)
            if len(_key_resp_1_8_allKeys):
                key_resp_1_8.keys = _key_resp_1_8_allKeys[0].name  # just the first key pressed
                key_resp_1_8.rt = _key_resp_1_8_allKeys[0].rt
                key_resp_1_8.duration = _key_resp_1_8_allKeys[0].duration
        
        # *trial_fixation_1_9* updates
        
        # if trial_fixation_1_9 is starting this frame...
        if trial_fixation_1_9.status == NOT_STARTED and key_resp_1_8.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_9.frameNStart = frameN  # exact frame index
            trial_fixation_1_9.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_9.started')
            # update status
            trial_fixation_1_9.status = STARTED
            trial_fixation_1_9.setAutoDraw(True)
        
        # if trial_fixation_1_9 is active this frame...
        if trial_fixation_1_9.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_9 is stopping this frame...
        if trial_fixation_1_9.status == STARTED:
            if frameN >= (trial_fixation_1_9.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_9.tStop = t  # not accounting for scr refresh
                trial_fixation_1_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_9.stopped')
                # update status
                trial_fixation_1_9.status = FINISHED
                trial_fixation_1_9.setAutoDraw(False)
        
        # *image_1_9* updates
        
        # if image_1_9 is starting this frame...
        if image_1_9.status == NOT_STARTED and trial_fixation_1_9.status==FINISHED:
            # keep track of start time/frame for later
            image_1_9.frameNStart = frameN  # exact frame index
            image_1_9.tStart = t  # local t and not account for scr refresh
            image_1_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_9.started')
            # update status
            image_1_9.status = STARTED
            image_1_9.setAutoDraw(True)
        
        # if image_1_9 is active this frame...
        if image_1_9.status == STARTED:
            # update params
            pass
        
        # if image_1_9 is stopping this frame...
        if image_1_9.status == STARTED:
            if frameN >= (image_1_9.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_9.tStop = t  # not accounting for scr refresh
                image_1_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_9.stopped')
                # update status
                image_1_9.status = FINISHED
                image_1_9.setAutoDraw(False)
        
        # *key_resp_1_9* updates
        waitOnFlip = False
        
        # if key_resp_1_9 is starting this frame...
        if key_resp_1_9.status == NOT_STARTED and trial_fixation_1_9.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_9.frameNStart = frameN  # exact frame index
            key_resp_1_9.tStart = t  # local t and not account for scr refresh
            key_resp_1_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_9.started')
            # update status
            key_resp_1_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_9 is stopping this frame...
        if key_resp_1_9.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_9.tStop = t  # not accounting for scr refresh
                key_resp_1_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_9.stopped')
                # update status
                key_resp_1_9.status = FINISHED
                key_resp_1_9.status = FINISHED
        if key_resp_1_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_9.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_9_allKeys.extend(theseKeys)
            if len(_key_resp_1_9_allKeys):
                key_resp_1_9.keys = _key_resp_1_9_allKeys[0].name  # just the first key pressed
                key_resp_1_9.rt = _key_resp_1_9_allKeys[0].rt
                key_resp_1_9.duration = _key_resp_1_9_allKeys[0].duration
        
        # *trial_fixation_1_10* updates
        
        # if trial_fixation_1_10 is starting this frame...
        if trial_fixation_1_10.status == NOT_STARTED and key_resp_1_9.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_1_10.frameNStart = frameN  # exact frame index
            trial_fixation_1_10.tStart = t  # local t and not account for scr refresh
            trial_fixation_1_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_1_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_1_10.started')
            # update status
            trial_fixation_1_10.status = STARTED
            trial_fixation_1_10.setAutoDraw(True)
        
        # if trial_fixation_1_10 is active this frame...
        if trial_fixation_1_10.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_1_10 is stopping this frame...
        if trial_fixation_1_10.status == STARTED:
            if frameN >= (trial_fixation_1_10.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_1_10.tStop = t  # not accounting for scr refresh
                trial_fixation_1_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_1_10.stopped')
                # update status
                trial_fixation_1_10.status = FINISHED
                trial_fixation_1_10.setAutoDraw(False)
        
        # *image_1_10* updates
        
        # if image_1_10 is starting this frame...
        if image_1_10.status == NOT_STARTED and trial_fixation_1_10.status==FINISHED:
            # keep track of start time/frame for later
            image_1_10.frameNStart = frameN  # exact frame index
            image_1_10.tStart = t  # local t and not account for scr refresh
            image_1_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_1_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_1_10.started')
            # update status
            image_1_10.status = STARTED
            image_1_10.setAutoDraw(True)
        
        # if image_1_10 is active this frame...
        if image_1_10.status == STARTED:
            # update params
            pass
        
        # if image_1_10 is stopping this frame...
        if image_1_10.status == STARTED:
            if frameN >= (image_1_10.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_1_10.tStop = t  # not accounting for scr refresh
                image_1_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_1_10.stopped')
                # update status
                image_1_10.status = FINISHED
                image_1_10.setAutoDraw(False)
        
        # *key_resp_1_10* updates
        waitOnFlip = False
        
        # if key_resp_1_10 is starting this frame...
        if key_resp_1_10.status == NOT_STARTED and trial_fixation_1_10.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_1_10.frameNStart = frameN  # exact frame index
            key_resp_1_10.tStart = t  # local t and not account for scr refresh
            key_resp_1_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_1_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1_10.started')
            # update status
            key_resp_1_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_1_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_1_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_1_10 is stopping this frame...
        if key_resp_1_10.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                key_resp_1_10.tStop = t  # not accounting for scr refresh
                key_resp_1_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1_10.stopped')
                # update status
                key_resp_1_10.status = FINISHED
                key_resp_1_10.status = FINISHED
        if key_resp_1_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1_10.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_1_10_allKeys.extend(theseKeys)
            if len(_key_resp_1_10_allKeys):
                key_resp_1_10.keys = _key_resp_1_10_allKeys[0].name  # just the first key pressed
                key_resp_1_10.rt = _key_resp_1_10_allKeys[0].rt
                key_resp_1_10.duration = _key_resp_1_10_allKeys[0].duration
        
        # *prep_instr_2* updates
        
        # if prep_instr_2 is starting this frame...
        if prep_instr_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            prep_instr_2.frameNStart = frameN  # exact frame index
            prep_instr_2.tStart = t  # local t and not account for scr refresh
            prep_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prep_instr_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'prep_instr_2.started')
            # update status
            prep_instr_2.status = STARTED
            prep_instr_2.setAutoDraw(True)
        
        # if prep_instr_2 is active this frame...
        if prep_instr_2.status == STARTED:
            # update params
            pass
        
        # if prep_instr_2 is stopping this frame...
        if prep_instr_2.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                prep_instr_2.tStop = t  # not accounting for scr refresh
                prep_instr_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prep_instr_2.stopped')
                # update status
                prep_instr_2.status = FINISHED
                prep_instr_2.setAutoDraw(False)
        
        # *target_2* updates
        
        # if target_2 is starting this frame...
        if target_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            target_2.frameNStart = frameN  # exact frame index
            target_2.tStart = t  # local t and not account for scr refresh
            target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_2.started')
            # update status
            target_2.status = STARTED
            target_2.setAutoDraw(True)
        
        # if target_2 is active this frame...
        if target_2.status == STARTED:
            # update params
            pass
        
        # if target_2 is stopping this frame...
        if target_2.status == STARTED:
            if frameN >= 150:
                # keep track of stop time/frame for later
                target_2.tStop = t  # not accounting for scr refresh
                target_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_2.stopped')
                # update status
                target_2.status = FINISHED
                target_2.setAutoDraw(False)
        
        # *trial_fixation_2_1* updates
        
        # if trial_fixation_2_1 is starting this frame...
        if trial_fixation_2_1.status == NOT_STARTED and target_2.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_1.frameNStart = frameN  # exact frame index
            trial_fixation_2_1.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_1.started')
            # update status
            trial_fixation_2_1.status = STARTED
            trial_fixation_2_1.setAutoDraw(True)
        
        # if trial_fixation_2_1 is active this frame...
        if trial_fixation_2_1.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_1 is stopping this frame...
        if trial_fixation_2_1.status == STARTED:
            if frameN >= (trial_fixation_2_1.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_1.tStop = t  # not accounting for scr refresh
                trial_fixation_2_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_1.stopped')
                # update status
                trial_fixation_2_1.status = FINISHED
                trial_fixation_2_1.setAutoDraw(False)
        
        # *image_2_1* updates
        
        # if image_2_1 is starting this frame...
        if image_2_1.status == NOT_STARTED and trial_fixation_2_1.status==FINISHED:
            # keep track of start time/frame for later
            image_2_1.frameNStart = frameN  # exact frame index
            image_2_1.tStart = t  # local t and not account for scr refresh
            image_2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_1.started')
            # update status
            image_2_1.status = STARTED
            image_2_1.setAutoDraw(True)
        
        # if image_2_1 is active this frame...
        if image_2_1.status == STARTED:
            # update params
            pass
        
        # if image_2_1 is stopping this frame...
        if image_2_1.status == STARTED:
            if frameN >= (image_2_1.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_1.tStop = t  # not accounting for scr refresh
                image_2_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_1.stopped')
                # update status
                image_2_1.status = FINISHED
                image_2_1.setAutoDraw(False)
        
        # *key_resp_2_1* updates
        waitOnFlip = False
        
        # if key_resp_2_1 is starting this frame...
        if key_resp_2_1.status == NOT_STARTED and trial_fixation_2_1.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_1.frameNStart = frameN  # exact frame index
            key_resp_2_1.tStart = t  # local t and not account for scr refresh
            key_resp_2_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_1.started')
            # update status
            key_resp_2_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_1 is stopping this frame...
        if key_resp_2_1.status == STARTED:
            if frameN >= (key_resp_2_1.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_1.tStop = t  # not accounting for scr refresh
                key_resp_2_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_1.stopped')
                # update status
                key_resp_2_1.status = FINISHED
                key_resp_2_1.status = FINISHED
        if key_resp_2_1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_1.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_1_allKeys.extend(theseKeys)
            if len(_key_resp_2_1_allKeys):
                key_resp_2_1.keys = _key_resp_2_1_allKeys[0].name  # just the first key pressed
                key_resp_2_1.rt = _key_resp_2_1_allKeys[0].rt
                key_resp_2_1.duration = _key_resp_2_1_allKeys[0].duration
        
        # *trial_fixation_2_2* updates
        
        # if trial_fixation_2_2 is starting this frame...
        if trial_fixation_2_2.status == NOT_STARTED and key_resp_2_1.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_2.frameNStart = frameN  # exact frame index
            trial_fixation_2_2.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_2.started')
            # update status
            trial_fixation_2_2.status = STARTED
            trial_fixation_2_2.setAutoDraw(True)
        
        # if trial_fixation_2_2 is active this frame...
        if trial_fixation_2_2.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_2 is stopping this frame...
        if trial_fixation_2_2.status == STARTED:
            if frameN >= (trial_fixation_2_2.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_2.tStop = t  # not accounting for scr refresh
                trial_fixation_2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_2.stopped')
                # update status
                trial_fixation_2_2.status = FINISHED
                trial_fixation_2_2.setAutoDraw(False)
        
        # *image_2_2* updates
        
        # if image_2_2 is starting this frame...
        if image_2_2.status == NOT_STARTED and trial_fixation_2_2.status==FINISHED:
            # keep track of start time/frame for later
            image_2_2.frameNStart = frameN  # exact frame index
            image_2_2.tStart = t  # local t and not account for scr refresh
            image_2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_2.started')
            # update status
            image_2_2.status = STARTED
            image_2_2.setAutoDraw(True)
        
        # if image_2_2 is active this frame...
        if image_2_2.status == STARTED:
            # update params
            pass
        
        # if image_2_2 is stopping this frame...
        if image_2_2.status == STARTED:
            if frameN >= (image_2_2.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_2.tStop = t  # not accounting for scr refresh
                image_2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_2.stopped')
                # update status
                image_2_2.status = FINISHED
                image_2_2.setAutoDraw(False)
        
        # *key_resp_2_2* updates
        waitOnFlip = False
        
        # if key_resp_2_2 is starting this frame...
        if key_resp_2_2.status == NOT_STARTED and trial_fixation_2_2.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_2.frameNStart = frameN  # exact frame index
            key_resp_2_2.tStart = t  # local t and not account for scr refresh
            key_resp_2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_2.started')
            # update status
            key_resp_2_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_2 is stopping this frame...
        if key_resp_2_2.status == STARTED:
            if frameN >= (key_resp_2_2.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_2.tStop = t  # not accounting for scr refresh
                key_resp_2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_2.stopped')
                # update status
                key_resp_2_2.status = FINISHED
                key_resp_2_2.status = FINISHED
        if key_resp_2_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_2.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_2_allKeys):
                key_resp_2_2.keys = _key_resp_2_2_allKeys[0].name  # just the first key pressed
                key_resp_2_2.rt = _key_resp_2_2_allKeys[0].rt
                key_resp_2_2.duration = _key_resp_2_2_allKeys[0].duration
        
        # *trial_fixation_2_3* updates
        
        # if trial_fixation_2_3 is starting this frame...
        if trial_fixation_2_3.status == NOT_STARTED and key_resp_2_2.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_3.frameNStart = frameN  # exact frame index
            trial_fixation_2_3.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_3.started')
            # update status
            trial_fixation_2_3.status = STARTED
            trial_fixation_2_3.setAutoDraw(True)
        
        # if trial_fixation_2_3 is active this frame...
        if trial_fixation_2_3.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_3 is stopping this frame...
        if trial_fixation_2_3.status == STARTED:
            if frameN >= (trial_fixation_2_3.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_3.tStop = t  # not accounting for scr refresh
                trial_fixation_2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_3.stopped')
                # update status
                trial_fixation_2_3.status = FINISHED
                trial_fixation_2_3.setAutoDraw(False)
        
        # *image_2_3* updates
        
        # if image_2_3 is starting this frame...
        if image_2_3.status == NOT_STARTED and trial_fixation_2_3.status==FINISHED:
            # keep track of start time/frame for later
            image_2_3.frameNStart = frameN  # exact frame index
            image_2_3.tStart = t  # local t and not account for scr refresh
            image_2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_3.started')
            # update status
            image_2_3.status = STARTED
            image_2_3.setAutoDraw(True)
        
        # if image_2_3 is active this frame...
        if image_2_3.status == STARTED:
            # update params
            pass
        
        # if image_2_3 is stopping this frame...
        if image_2_3.status == STARTED:
            if frameN >= (image_2_3.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_3.tStop = t  # not accounting for scr refresh
                image_2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_3.stopped')
                # update status
                image_2_3.status = FINISHED
                image_2_3.setAutoDraw(False)
        
        # *key_resp_2_3* updates
        waitOnFlip = False
        
        # if key_resp_2_3 is starting this frame...
        if key_resp_2_3.status == NOT_STARTED and trial_fixation_2_3.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_3.frameNStart = frameN  # exact frame index
            key_resp_2_3.tStart = t  # local t and not account for scr refresh
            key_resp_2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_3.started')
            # update status
            key_resp_2_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_3 is stopping this frame...
        if key_resp_2_3.status == STARTED:
            if frameN >= (key_resp_2_3.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_3.tStop = t  # not accounting for scr refresh
                key_resp_2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_3.stopped')
                # update status
                key_resp_2_3.status = FINISHED
                key_resp_2_3.status = FINISHED
        if key_resp_2_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_3.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_3_allKeys.extend(theseKeys)
            if len(_key_resp_2_3_allKeys):
                key_resp_2_3.keys = _key_resp_2_3_allKeys[0].name  # just the first key pressed
                key_resp_2_3.rt = _key_resp_2_3_allKeys[0].rt
                key_resp_2_3.duration = _key_resp_2_3_allKeys[0].duration
        
        # *trial_fixation_2_4* updates
        
        # if trial_fixation_2_4 is starting this frame...
        if trial_fixation_2_4.status == NOT_STARTED and key_resp_2_3.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_4.frameNStart = frameN  # exact frame index
            trial_fixation_2_4.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_4.started')
            # update status
            trial_fixation_2_4.status = STARTED
            trial_fixation_2_4.setAutoDraw(True)
        
        # if trial_fixation_2_4 is active this frame...
        if trial_fixation_2_4.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_4 is stopping this frame...
        if trial_fixation_2_4.status == STARTED:
            if frameN >= (trial_fixation_2_4.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_4.tStop = t  # not accounting for scr refresh
                trial_fixation_2_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_4.stopped')
                # update status
                trial_fixation_2_4.status = FINISHED
                trial_fixation_2_4.setAutoDraw(False)
        
        # *image_2_4* updates
        
        # if image_2_4 is starting this frame...
        if image_2_4.status == NOT_STARTED and trial_fixation_2_4.status==FINISHED:
            # keep track of start time/frame for later
            image_2_4.frameNStart = frameN  # exact frame index
            image_2_4.tStart = t  # local t and not account for scr refresh
            image_2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_4.started')
            # update status
            image_2_4.status = STARTED
            image_2_4.setAutoDraw(True)
        
        # if image_2_4 is active this frame...
        if image_2_4.status == STARTED:
            # update params
            pass
        
        # if image_2_4 is stopping this frame...
        if image_2_4.status == STARTED:
            if frameN >= (image_2_4.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_4.tStop = t  # not accounting for scr refresh
                image_2_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_4.stopped')
                # update status
                image_2_4.status = FINISHED
                image_2_4.setAutoDraw(False)
        
        # *key_resp_2_4* updates
        waitOnFlip = False
        
        # if key_resp_2_4 is starting this frame...
        if key_resp_2_4.status == NOT_STARTED and trial_fixation_2_4.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_4.frameNStart = frameN  # exact frame index
            key_resp_2_4.tStart = t  # local t and not account for scr refresh
            key_resp_2_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_4.started')
            # update status
            key_resp_2_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_4 is stopping this frame...
        if key_resp_2_4.status == STARTED:
            if frameN >= (key_resp_2_4.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_4.tStop = t  # not accounting for scr refresh
                key_resp_2_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_4.stopped')
                # update status
                key_resp_2_4.status = FINISHED
                key_resp_2_4.status = FINISHED
        if key_resp_2_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_4.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_4_allKeys.extend(theseKeys)
            if len(_key_resp_2_4_allKeys):
                key_resp_2_4.keys = _key_resp_2_4_allKeys[0].name  # just the first key pressed
                key_resp_2_4.rt = _key_resp_2_4_allKeys[0].rt
                key_resp_2_4.duration = _key_resp_2_4_allKeys[0].duration
        
        # *trial_fixation_2_5* updates
        
        # if trial_fixation_2_5 is starting this frame...
        if trial_fixation_2_5.status == NOT_STARTED and key_resp_2_4.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_5.frameNStart = frameN  # exact frame index
            trial_fixation_2_5.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_5.started')
            # update status
            trial_fixation_2_5.status = STARTED
            trial_fixation_2_5.setAutoDraw(True)
        
        # if trial_fixation_2_5 is active this frame...
        if trial_fixation_2_5.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_5 is stopping this frame...
        if trial_fixation_2_5.status == STARTED:
            if frameN >= (trial_fixation_2_5.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_5.tStop = t  # not accounting for scr refresh
                trial_fixation_2_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_5.stopped')
                # update status
                trial_fixation_2_5.status = FINISHED
                trial_fixation_2_5.setAutoDraw(False)
        
        # *image_2_5* updates
        
        # if image_2_5 is starting this frame...
        if image_2_5.status == NOT_STARTED and trial_fixation_2_5.status==FINISHED:
            # keep track of start time/frame for later
            image_2_5.frameNStart = frameN  # exact frame index
            image_2_5.tStart = t  # local t and not account for scr refresh
            image_2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_5.started')
            # update status
            image_2_5.status = STARTED
            image_2_5.setAutoDraw(True)
        
        # if image_2_5 is active this frame...
        if image_2_5.status == STARTED:
            # update params
            pass
        
        # if image_2_5 is stopping this frame...
        if image_2_5.status == STARTED:
            if frameN >= (image_2_5.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_5.tStop = t  # not accounting for scr refresh
                image_2_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_5.stopped')
                # update status
                image_2_5.status = FINISHED
                image_2_5.setAutoDraw(False)
        
        # *key_resp_2_5* updates
        waitOnFlip = False
        
        # if key_resp_2_5 is starting this frame...
        if key_resp_2_5.status == NOT_STARTED and trial_fixation_2_5.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_5.frameNStart = frameN  # exact frame index
            key_resp_2_5.tStart = t  # local t and not account for scr refresh
            key_resp_2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_5.started')
            # update status
            key_resp_2_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_5 is stopping this frame...
        if key_resp_2_5.status == STARTED:
            if frameN >= (key_resp_2_5.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_5.tStop = t  # not accounting for scr refresh
                key_resp_2_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_5.stopped')
                # update status
                key_resp_2_5.status = FINISHED
                key_resp_2_5.status = FINISHED
        if key_resp_2_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_5.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_5_allKeys.extend(theseKeys)
            if len(_key_resp_2_5_allKeys):
                key_resp_2_5.keys = _key_resp_2_5_allKeys[0].name  # just the first key pressed
                key_resp_2_5.rt = _key_resp_2_5_allKeys[0].rt
                key_resp_2_5.duration = _key_resp_2_5_allKeys[0].duration
        
        # *trial_fixation_2_6* updates
        
        # if trial_fixation_2_6 is starting this frame...
        if trial_fixation_2_6.status == NOT_STARTED and key_resp_2_5.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_6.frameNStart = frameN  # exact frame index
            trial_fixation_2_6.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_6.started')
            # update status
            trial_fixation_2_6.status = STARTED
            trial_fixation_2_6.setAutoDraw(True)
        
        # if trial_fixation_2_6 is active this frame...
        if trial_fixation_2_6.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_6 is stopping this frame...
        if trial_fixation_2_6.status == STARTED:
            if frameN >= (trial_fixation_2_6.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_6.tStop = t  # not accounting for scr refresh
                trial_fixation_2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_6.stopped')
                # update status
                trial_fixation_2_6.status = FINISHED
                trial_fixation_2_6.setAutoDraw(False)
        
        # *image_2_6* updates
        
        # if image_2_6 is starting this frame...
        if image_2_6.status == NOT_STARTED and trial_fixation_2_6.status==FINISHED:
            # keep track of start time/frame for later
            image_2_6.frameNStart = frameN  # exact frame index
            image_2_6.tStart = t  # local t and not account for scr refresh
            image_2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_6.started')
            # update status
            image_2_6.status = STARTED
            image_2_6.setAutoDraw(True)
        
        # if image_2_6 is active this frame...
        if image_2_6.status == STARTED:
            # update params
            pass
        
        # if image_2_6 is stopping this frame...
        if image_2_6.status == STARTED:
            if frameN >= (image_2_6.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_6.tStop = t  # not accounting for scr refresh
                image_2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_6.stopped')
                # update status
                image_2_6.status = FINISHED
                image_2_6.setAutoDraw(False)
        
        # *key_resp_2_6* updates
        waitOnFlip = False
        
        # if key_resp_2_6 is starting this frame...
        if key_resp_2_6.status == NOT_STARTED and trial_fixation_2_6.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_6.frameNStart = frameN  # exact frame index
            key_resp_2_6.tStart = t  # local t and not account for scr refresh
            key_resp_2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_6.started')
            # update status
            key_resp_2_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_6 is stopping this frame...
        if key_resp_2_6.status == STARTED:
            if frameN >= (key_resp_2_6.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_6.tStop = t  # not accounting for scr refresh
                key_resp_2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_6.stopped')
                # update status
                key_resp_2_6.status = FINISHED
                key_resp_2_6.status = FINISHED
        if key_resp_2_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_6.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_6_allKeys.extend(theseKeys)
            if len(_key_resp_2_6_allKeys):
                key_resp_2_6.keys = _key_resp_2_6_allKeys[0].name  # just the first key pressed
                key_resp_2_6.rt = _key_resp_2_6_allKeys[0].rt
                key_resp_2_6.duration = _key_resp_2_6_allKeys[0].duration
        
        # *trial_fixation_2_7* updates
        
        # if trial_fixation_2_7 is starting this frame...
        if trial_fixation_2_7.status == NOT_STARTED and key_resp_2_6.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_7.frameNStart = frameN  # exact frame index
            trial_fixation_2_7.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_7.started')
            # update status
            trial_fixation_2_7.status = STARTED
            trial_fixation_2_7.setAutoDraw(True)
        
        # if trial_fixation_2_7 is active this frame...
        if trial_fixation_2_7.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_7 is stopping this frame...
        if trial_fixation_2_7.status == STARTED:
            if frameN >= (trial_fixation_2_7.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_7.tStop = t  # not accounting for scr refresh
                trial_fixation_2_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_7.stopped')
                # update status
                trial_fixation_2_7.status = FINISHED
                trial_fixation_2_7.setAutoDraw(False)
        
        # *image_2_7* updates
        
        # if image_2_7 is starting this frame...
        if image_2_7.status == NOT_STARTED and trial_fixation_2_7.status==FINISHED:
            # keep track of start time/frame for later
            image_2_7.frameNStart = frameN  # exact frame index
            image_2_7.tStart = t  # local t and not account for scr refresh
            image_2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_7.started')
            # update status
            image_2_7.status = STARTED
            image_2_7.setAutoDraw(True)
        
        # if image_2_7 is active this frame...
        if image_2_7.status == STARTED:
            # update params
            pass
        
        # if image_2_7 is stopping this frame...
        if image_2_7.status == STARTED:
            if frameN >= (image_2_7.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_7.tStop = t  # not accounting for scr refresh
                image_2_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_7.stopped')
                # update status
                image_2_7.status = FINISHED
                image_2_7.setAutoDraw(False)
        
        # *key_resp_2_7* updates
        waitOnFlip = False
        
        # if key_resp_2_7 is starting this frame...
        if key_resp_2_7.status == NOT_STARTED and trial_fixation_2_7.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_7.frameNStart = frameN  # exact frame index
            key_resp_2_7.tStart = t  # local t and not account for scr refresh
            key_resp_2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_7.started')
            # update status
            key_resp_2_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_7 is stopping this frame...
        if key_resp_2_7.status == STARTED:
            if frameN >= (key_resp_2_7.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_7.tStop = t  # not accounting for scr refresh
                key_resp_2_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_7.stopped')
                # update status
                key_resp_2_7.status = FINISHED
                key_resp_2_7.status = FINISHED
        if key_resp_2_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_7.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_7_allKeys.extend(theseKeys)
            if len(_key_resp_2_7_allKeys):
                key_resp_2_7.keys = _key_resp_2_7_allKeys[0].name  # just the first key pressed
                key_resp_2_7.rt = _key_resp_2_7_allKeys[0].rt
                key_resp_2_7.duration = _key_resp_2_7_allKeys[0].duration
        
        # *trial_fixation_2_8* updates
        
        # if trial_fixation_2_8 is starting this frame...
        if trial_fixation_2_8.status == NOT_STARTED and key_resp_2_7.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_8.frameNStart = frameN  # exact frame index
            trial_fixation_2_8.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_8.started')
            # update status
            trial_fixation_2_8.status = STARTED
            trial_fixation_2_8.setAutoDraw(True)
        
        # if trial_fixation_2_8 is active this frame...
        if trial_fixation_2_8.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_8 is stopping this frame...
        if trial_fixation_2_8.status == STARTED:
            if frameN >= (trial_fixation_2_8.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_8.tStop = t  # not accounting for scr refresh
                trial_fixation_2_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_8.stopped')
                # update status
                trial_fixation_2_8.status = FINISHED
                trial_fixation_2_8.setAutoDraw(False)
        
        # *image_2_8* updates
        
        # if image_2_8 is starting this frame...
        if image_2_8.status == NOT_STARTED and trial_fixation_2_8.status==FINISHED:
            # keep track of start time/frame for later
            image_2_8.frameNStart = frameN  # exact frame index
            image_2_8.tStart = t  # local t and not account for scr refresh
            image_2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_8.started')
            # update status
            image_2_8.status = STARTED
            image_2_8.setAutoDraw(True)
        
        # if image_2_8 is active this frame...
        if image_2_8.status == STARTED:
            # update params
            pass
        
        # if image_2_8 is stopping this frame...
        if image_2_8.status == STARTED:
            if frameN >= (image_2_8.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_8.tStop = t  # not accounting for scr refresh
                image_2_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_8.stopped')
                # update status
                image_2_8.status = FINISHED
                image_2_8.setAutoDraw(False)
        
        # *key_resp_2_8* updates
        waitOnFlip = False
        
        # if key_resp_2_8 is starting this frame...
        if key_resp_2_8.status == NOT_STARTED and trial_fixation_2_8.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_8.frameNStart = frameN  # exact frame index
            key_resp_2_8.tStart = t  # local t and not account for scr refresh
            key_resp_2_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_8.started')
            # update status
            key_resp_2_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_8 is stopping this frame...
        if key_resp_2_8.status == STARTED:
            if frameN >= (key_resp_2_8.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_8.tStop = t  # not accounting for scr refresh
                key_resp_2_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_8.stopped')
                # update status
                key_resp_2_8.status = FINISHED
                key_resp_2_8.status = FINISHED
        if key_resp_2_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_8.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_8_allKeys.extend(theseKeys)
            if len(_key_resp_2_8_allKeys):
                key_resp_2_8.keys = _key_resp_2_8_allKeys[0].name  # just the first key pressed
                key_resp_2_8.rt = _key_resp_2_8_allKeys[0].rt
                key_resp_2_8.duration = _key_resp_2_8_allKeys[0].duration
        
        # *trial_fixation_2_9* updates
        
        # if trial_fixation_2_9 is starting this frame...
        if trial_fixation_2_9.status == NOT_STARTED and key_resp_2_8.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_9.frameNStart = frameN  # exact frame index
            trial_fixation_2_9.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_9.started')
            # update status
            trial_fixation_2_9.status = STARTED
            trial_fixation_2_9.setAutoDraw(True)
        
        # if trial_fixation_2_9 is active this frame...
        if trial_fixation_2_9.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_9 is stopping this frame...
        if trial_fixation_2_9.status == STARTED:
            if frameN >= (trial_fixation_2_9.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_9.tStop = t  # not accounting for scr refresh
                trial_fixation_2_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_9.stopped')
                # update status
                trial_fixation_2_9.status = FINISHED
                trial_fixation_2_9.setAutoDraw(False)
        
        # *image_2_9* updates
        
        # if image_2_9 is starting this frame...
        if image_2_9.status == NOT_STARTED and trial_fixation_2_9.status==FINISHED:
            # keep track of start time/frame for later
            image_2_9.frameNStart = frameN  # exact frame index
            image_2_9.tStart = t  # local t and not account for scr refresh
            image_2_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_9.started')
            # update status
            image_2_9.status = STARTED
            image_2_9.setAutoDraw(True)
        
        # if image_2_9 is active this frame...
        if image_2_9.status == STARTED:
            # update params
            pass
        
        # if image_2_9 is stopping this frame...
        if image_2_9.status == STARTED:
            if frameN >= (image_2_9.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_9.tStop = t  # not accounting for scr refresh
                image_2_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_9.stopped')
                # update status
                image_2_9.status = FINISHED
                image_2_9.setAutoDraw(False)
        
        # *key_resp_2_9* updates
        waitOnFlip = False
        
        # if key_resp_2_9 is starting this frame...
        if key_resp_2_9.status == NOT_STARTED and trial_fixation_2_9.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_9.frameNStart = frameN  # exact frame index
            key_resp_2_9.tStart = t  # local t and not account for scr refresh
            key_resp_2_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_9.started')
            # update status
            key_resp_2_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_9 is stopping this frame...
        if key_resp_2_9.status == STARTED:
            if frameN >= (key_resp_2_9.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_9.tStop = t  # not accounting for scr refresh
                key_resp_2_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_9.stopped')
                # update status
                key_resp_2_9.status = FINISHED
                key_resp_2_9.status = FINISHED
        if key_resp_2_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_9.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_9_allKeys.extend(theseKeys)
            if len(_key_resp_2_9_allKeys):
                key_resp_2_9.keys = _key_resp_2_9_allKeys[0].name  # just the first key pressed
                key_resp_2_9.rt = _key_resp_2_9_allKeys[0].rt
                key_resp_2_9.duration = _key_resp_2_9_allKeys[0].duration
        
        # *trial_fixation_2_10* updates
        
        # if trial_fixation_2_10 is starting this frame...
        if trial_fixation_2_10.status == NOT_STARTED and key_resp_2_9.status==FINISHED:
            # keep track of start time/frame for later
            trial_fixation_2_10.frameNStart = frameN  # exact frame index
            trial_fixation_2_10.tStart = t  # local t and not account for scr refresh
            trial_fixation_2_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_fixation_2_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trial_fixation_2_10.started')
            # update status
            trial_fixation_2_10.status = STARTED
            trial_fixation_2_10.setAutoDraw(True)
        
        # if trial_fixation_2_10 is active this frame...
        if trial_fixation_2_10.status == STARTED:
            # update params
            pass
        
        # if trial_fixation_2_10 is stopping this frame...
        if trial_fixation_2_10.status == STARTED:
            if frameN >= (trial_fixation_2_10.frameNStart + 30.0):
                # keep track of stop time/frame for later
                trial_fixation_2_10.tStop = t  # not accounting for scr refresh
                trial_fixation_2_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trial_fixation_2_10.stopped')
                # update status
                trial_fixation_2_10.status = FINISHED
                trial_fixation_2_10.setAutoDraw(False)
        
        # *image_2_10* updates
        
        # if image_2_10 is starting this frame...
        if image_2_10.status == NOT_STARTED and trial_fixation_2_10.status==FINISHED:
            # keep track of start time/frame for later
            image_2_10.frameNStart = frameN  # exact frame index
            image_2_10.tStart = t  # local t and not account for scr refresh
            image_2_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_2_10.started')
            # update status
            image_2_10.status = STARTED
            image_2_10.setAutoDraw(True)
        
        # if image_2_10 is active this frame...
        if image_2_10.status == STARTED:
            # update params
            pass
        
        # if image_2_10 is stopping this frame...
        if image_2_10.status == STARTED:
            if frameN >= (image_2_10.frameNStart + 150.0):
                # keep track of stop time/frame for later
                image_2_10.tStop = t  # not accounting for scr refresh
                image_2_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2_10.stopped')
                # update status
                image_2_10.status = FINISHED
                image_2_10.setAutoDraw(False)
        
        # *key_resp_2_10* updates
        waitOnFlip = False
        
        # if key_resp_2_10 is starting this frame...
        if key_resp_2_10.status == NOT_STARTED and trial_fixation_2_10.status==FINISHED:
            # keep track of start time/frame for later
            key_resp_2_10.frameNStart = frameN  # exact frame index
            key_resp_2_10.tStart = t  # local t and not account for scr refresh
            key_resp_2_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2_10.started')
            # update status
            key_resp_2_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_2_10 is stopping this frame...
        if key_resp_2_10.status == STARTED:
            if frameN >= (key_resp_2_10.frameNStart + 150):
                # keep track of stop time/frame for later
                key_resp_2_10.tStop = t  # not accounting for scr refresh
                key_resp_2_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2_10.stopped')
                # update status
                key_resp_2_10.status = FINISHED
                key_resp_2_10.status = FINISHED
        if key_resp_2_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2_10.getKeys(keyList=['1','2'], waitRelease=False)
            _key_resp_2_10_allKeys.extend(theseKeys)
            if len(_key_resp_2_10_allKeys):
                key_resp_2_10.keys = _key_resp_2_10_allKeys[0].name  # just the first key pressed
                key_resp_2_10.rt = _key_resp_2_10_allKeys[0].rt
                key_resp_2_10.duration = _key_resp_2_10_allKeys[0].duration
        
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
        for thisComponent in stim_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stim_block" ---
    for thisComponent in stim_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_1_1.keys in ['', [], None]:  # No response was made
        key_resp_1_1.keys = None
    run.addData('key_resp_1_1.keys',key_resp_1_1.keys)
    if key_resp_1_1.keys != None:  # we had a response
        run.addData('key_resp_1_1.rt', key_resp_1_1.rt)
        run.addData('key_resp_1_1.duration', key_resp_1_1.duration)
    # check responses
    if key_resp_1_2.keys in ['', [], None]:  # No response was made
        key_resp_1_2.keys = None
    run.addData('key_resp_1_2.keys',key_resp_1_2.keys)
    if key_resp_1_2.keys != None:  # we had a response
        run.addData('key_resp_1_2.rt', key_resp_1_2.rt)
        run.addData('key_resp_1_2.duration', key_resp_1_2.duration)
    # check responses
    if key_resp_1_3.keys in ['', [], None]:  # No response was made
        key_resp_1_3.keys = None
    run.addData('key_resp_1_3.keys',key_resp_1_3.keys)
    if key_resp_1_3.keys != None:  # we had a response
        run.addData('key_resp_1_3.rt', key_resp_1_3.rt)
        run.addData('key_resp_1_3.duration', key_resp_1_3.duration)
    # check responses
    if key_resp_1_4.keys in ['', [], None]:  # No response was made
        key_resp_1_4.keys = None
    run.addData('key_resp_1_4.keys',key_resp_1_4.keys)
    if key_resp_1_4.keys != None:  # we had a response
        run.addData('key_resp_1_4.rt', key_resp_1_4.rt)
        run.addData('key_resp_1_4.duration', key_resp_1_4.duration)
    # check responses
    if key_resp_1_5.keys in ['', [], None]:  # No response was made
        key_resp_1_5.keys = None
    run.addData('key_resp_1_5.keys',key_resp_1_5.keys)
    if key_resp_1_5.keys != None:  # we had a response
        run.addData('key_resp_1_5.rt', key_resp_1_5.rt)
        run.addData('key_resp_1_5.duration', key_resp_1_5.duration)
    # check responses
    if key_resp_1_6.keys in ['', [], None]:  # No response was made
        key_resp_1_6.keys = None
    run.addData('key_resp_1_6.keys',key_resp_1_6.keys)
    if key_resp_1_6.keys != None:  # we had a response
        run.addData('key_resp_1_6.rt', key_resp_1_6.rt)
        run.addData('key_resp_1_6.duration', key_resp_1_6.duration)
    # check responses
    if key_resp_1_7.keys in ['', [], None]:  # No response was made
        key_resp_1_7.keys = None
    run.addData('key_resp_1_7.keys',key_resp_1_7.keys)
    if key_resp_1_7.keys != None:  # we had a response
        run.addData('key_resp_1_7.rt', key_resp_1_7.rt)
        run.addData('key_resp_1_7.duration', key_resp_1_7.duration)
    # check responses
    if key_resp_1_8.keys in ['', [], None]:  # No response was made
        key_resp_1_8.keys = None
    run.addData('key_resp_1_8.keys',key_resp_1_8.keys)
    if key_resp_1_8.keys != None:  # we had a response
        run.addData('key_resp_1_8.rt', key_resp_1_8.rt)
        run.addData('key_resp_1_8.duration', key_resp_1_8.duration)
    # check responses
    if key_resp_1_9.keys in ['', [], None]:  # No response was made
        key_resp_1_9.keys = None
    run.addData('key_resp_1_9.keys',key_resp_1_9.keys)
    if key_resp_1_9.keys != None:  # we had a response
        run.addData('key_resp_1_9.rt', key_resp_1_9.rt)
        run.addData('key_resp_1_9.duration', key_resp_1_9.duration)
    # check responses
    if key_resp_1_10.keys in ['', [], None]:  # No response was made
        key_resp_1_10.keys = None
    run.addData('key_resp_1_10.keys',key_resp_1_10.keys)
    if key_resp_1_10.keys != None:  # we had a response
        run.addData('key_resp_1_10.rt', key_resp_1_10.rt)
        run.addData('key_resp_1_10.duration', key_resp_1_10.duration)
    # check responses
    if key_resp_2_1.keys in ['', [], None]:  # No response was made
        key_resp_2_1.keys = None
    run.addData('key_resp_2_1.keys',key_resp_2_1.keys)
    if key_resp_2_1.keys != None:  # we had a response
        run.addData('key_resp_2_1.rt', key_resp_2_1.rt)
        run.addData('key_resp_2_1.duration', key_resp_2_1.duration)
    # check responses
    if key_resp_2_2.keys in ['', [], None]:  # No response was made
        key_resp_2_2.keys = None
    run.addData('key_resp_2_2.keys',key_resp_2_2.keys)
    if key_resp_2_2.keys != None:  # we had a response
        run.addData('key_resp_2_2.rt', key_resp_2_2.rt)
        run.addData('key_resp_2_2.duration', key_resp_2_2.duration)
    # check responses
    if key_resp_2_3.keys in ['', [], None]:  # No response was made
        key_resp_2_3.keys = None
    run.addData('key_resp_2_3.keys',key_resp_2_3.keys)
    if key_resp_2_3.keys != None:  # we had a response
        run.addData('key_resp_2_3.rt', key_resp_2_3.rt)
        run.addData('key_resp_2_3.duration', key_resp_2_3.duration)
    # check responses
    if key_resp_2_4.keys in ['', [], None]:  # No response was made
        key_resp_2_4.keys = None
    run.addData('key_resp_2_4.keys',key_resp_2_4.keys)
    if key_resp_2_4.keys != None:  # we had a response
        run.addData('key_resp_2_4.rt', key_resp_2_4.rt)
        run.addData('key_resp_2_4.duration', key_resp_2_4.duration)
    # check responses
    if key_resp_2_5.keys in ['', [], None]:  # No response was made
        key_resp_2_5.keys = None
    run.addData('key_resp_2_5.keys',key_resp_2_5.keys)
    if key_resp_2_5.keys != None:  # we had a response
        run.addData('key_resp_2_5.rt', key_resp_2_5.rt)
        run.addData('key_resp_2_5.duration', key_resp_2_5.duration)
    # check responses
    if key_resp_2_6.keys in ['', [], None]:  # No response was made
        key_resp_2_6.keys = None
    run.addData('key_resp_2_6.keys',key_resp_2_6.keys)
    if key_resp_2_6.keys != None:  # we had a response
        run.addData('key_resp_2_6.rt', key_resp_2_6.rt)
        run.addData('key_resp_2_6.duration', key_resp_2_6.duration)
    # check responses
    if key_resp_2_7.keys in ['', [], None]:  # No response was made
        key_resp_2_7.keys = None
    run.addData('key_resp_2_7.keys',key_resp_2_7.keys)
    if key_resp_2_7.keys != None:  # we had a response
        run.addData('key_resp_2_7.rt', key_resp_2_7.rt)
        run.addData('key_resp_2_7.duration', key_resp_2_7.duration)
    # check responses
    if key_resp_2_8.keys in ['', [], None]:  # No response was made
        key_resp_2_8.keys = None
    run.addData('key_resp_2_8.keys',key_resp_2_8.keys)
    if key_resp_2_8.keys != None:  # we had a response
        run.addData('key_resp_2_8.rt', key_resp_2_8.rt)
        run.addData('key_resp_2_8.duration', key_resp_2_8.duration)
    # check responses
    if key_resp_2_9.keys in ['', [], None]:  # No response was made
        key_resp_2_9.keys = None
    run.addData('key_resp_2_9.keys',key_resp_2_9.keys)
    if key_resp_2_9.keys != None:  # we had a response
        run.addData('key_resp_2_9.rt', key_resp_2_9.rt)
        run.addData('key_resp_2_9.duration', key_resp_2_9.duration)
    # check responses
    if key_resp_2_10.keys in ['', [], None]:  # No response was made
        key_resp_2_10.keys = None
    run.addData('key_resp_2_10.keys',key_resp_2_10.keys)
    if key_resp_2_10.keys != None:  # we had a response
        run.addData('key_resp_2_10.rt', key_resp_2_10.rt)
        run.addData('key_resp_2_10.duration', key_resp_2_10.duration)
    # the Routine "stim_block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 7.0 repeats of 'run'


# --- Prepare to start Routine "rest" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
restComponents = [rest_txt_2]
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
    
    # *rest_txt_2* updates
    
    # if rest_txt_2 is starting this frame...
    if rest_txt_2.status == NOT_STARTED and frameN >= 0:
        # keep track of start time/frame for later
        rest_txt_2.frameNStart = frameN  # exact frame index
        rest_txt_2.tStart = t  # local t and not account for scr refresh
        rest_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_txt_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_txt_2.started')
        # update status
        rest_txt_2.status = STARTED
        rest_txt_2.setAutoDraw(True)
    
    # if rest_txt_2 is active this frame...
    if rest_txt_2.status == STARTED:
        # update params
        pass
    
    # if rest_txt_2 is stopping this frame...
    if rest_txt_2.status == STARTED:
        if frameN >= 901:
            # keep track of stop time/frame for later
            rest_txt_2.tStop = t  # not accounting for scr refresh
            rest_txt_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'rest_txt_2.stopped')
            # update status
            rest_txt_2.status = FINISHED
            rest_txt_2.setAutoDraw(False)
    
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
