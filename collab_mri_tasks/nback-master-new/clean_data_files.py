import pandas as pd
import numpy as np
import csv
from os import listdir
from os.path import isfile, join

messypath = 'data/' # change folder name when necessary
cleanpath = 'cleaned_logs/'
in_folder = [f for f in listdir(messypath) if isfile(join(messypath, f)) and f.endswith('.csv')]
# in_folder = ['testing_nback-master-new_2024_Feb_29_1609']
# messy_in_folder = ['2s_ZB216_nback-master-new_2024-03-04_15h29.25.634.csv']
# clean_in_folder = ['2s_ZB216_nback-master-new_2024-03-04_15h29.25.634_cleaned.csv']

trial_types = pd.read_excel("trialTypes_nback.xlsx")

col_names = ['run', 'block', 'block_type', 'stim_type', 'stimulus', 'target', 'corr_ans', \
             'iti_onset', 'iti_offset', 'iti_duration', 'stim_onset', 'stim_offset', 'stim_duration', \
             'key_resp', 'key_resp_rt', 'corr_var', \
             'instr_onset', 'instr_offset', 'instr_duration', 'rest_onset', 'rest_offset', 'rest_duration']

for file_no in range(len(in_folder)):
    with open(messypath + in_folder[file_no], "r") as file:
        df = pd.read_csv(file)
        total_runs = df['run_no'].dropna().unique().astype(int)
    with open(cleanpath + in_folder[file_no], 'w', newline='') as nf:
        writer = csv.writer(nf, delimiter=',')
        writer.writerow(col_names)

        for run in range(2):
            for block in range(8):
                for trial in range(10):
                    run_no = total_runs[run] + 1
                    trial_info = trial_types.loc[[(run_no - 1) * 80 + block * 10 + trial]]
                    block_no = trial_info['Block'].item()
                    block_type = trial_info['BlockType'].item()
                    stim_type = trial_info['StimType'].item()
                    stimulus = trial_info['Stimulus'].item()
                    target_type = trial_info['CorrectResponse'].item()
                    corr_ans = trial_info['corrAns'].item()

                    trial_stim = f'image_{block % 2 + 1}_{(trial + 1)}'
                    stim_onset = df[trial_stim + '.started'].tolist()[run*4 + block//2 + 2]
                    stim_offset = df[trial_stim + '.stopped'].tolist()[run*4 + block//2 + 2]
                    stim_duration = np.subtract(stim_offset, stim_onset)
                    if np.isnan(stim_duration):
                        if block % 2 == 0 and trial == 9:
                            stim_offset = df['prep_instr_2.started'].tolist()[run*4 + block//2 + 2]
                        elif block % 2 == 1 and trial == 9:
                            stim_offset = df['rest_txt.started'].tolist()[run*4 + block//2 + 2]
                        stim_duration = np.subtract(stim_offset, stim_onset)

                    trial_iti = f'trial_fixation_{block % 2 + 1}_{(trial + 1)}'
                    iti_onset = df[trial_iti + '.started'].tolist()[run*4 + block//2 + 2]
                    iti_offset = df[trial_iti + '.stopped'].tolist()[run*4 + block//2 + 2]
                    iti_duration = np.subtract(iti_offset, iti_onset)

                    trial_resp = f'key_resp_{block % 2 + 1}_{(trial + 1)}'
                    resp_key = df[trial_resp + '.keys'].tolist()[run*4 + block//2 + 2]
                    try:
                        resp_rt = df[trial_resp + '.rt'].tolist()[run*4 + block//2 + 2]
                    except:
                        resp_rt = None
                    corr_var = 1 if resp_key == corr_ans else 0

                    if block%2 == 0 and trial == 0:
                        block_instr = f'prep_instr_1'
                        block_instr_onset = df[block_instr+'.started'].tolist()[run*4 + block//2 + 2]
                        block_instr_offset = df[block_instr+'.stopped'].tolist()[run*4 + block//2 + 2]
                        block_instr_duration = np.subtract(block_instr_offset, block_instr_onset)
                    elif block%2 == 1 and trial == 0:
                        block_instr = f'prep_instr_2'
                        block_instr_onset = df[block_instr+'.started'].tolist()[run*4 + block//2 + 2]
                        block_instr_offset = df[block_instr+'.stopped'].tolist()[run*4 + block//2 + 2]
                        block_instr_duration = np.subtract(block_instr_offset, block_instr_onset)
                    else:
                        block_instr_onset = None
                        block_instr_offset = None
                        block_instr_duration = None

                    if block%2 == 1 and trial == 9:
                        block_rest = 'rest_txt'
                        block_rest_onset = df[block_rest+'.started'].tolist()[run*4 + block//2 + 2]
                        block_rest_offset = df[block_rest+'.stopped'].tolist()[run*4 + block//2 + 2]
                        block_rest_duration = np.subtract(block_rest_offset, block_rest_onset)
                    else:
                        block_rest_onset = None
                        block_rest_offset = None
                        block_rest_duration = None

                    line = [run_no, block_no, block_type, stim_type, stimulus, target_type, corr_ans, \
                            iti_onset, iti_offset, iti_duration, stim_onset, stim_offset, stim_duration, \
                            resp_key, resp_rt, corr_var, \
                            block_instr_onset, block_instr_offset, block_instr_duration, \
                            block_rest_onset, block_rest_offset, block_rest_duration]
                    line = [str(i) for i in line]
                    line = ','.join(line)
                    nf.write(line + '\n')