clear; close all;


%==========================================================================
% input of experiment
%==========================================================================
subjcode=input('Subject ID: ');
set_no=input('Set no: ');


if ~ismember(subjcode,[101:999])
    fprintf(2,'Incorrect subject ID\n');
    fprintf(2,'Please try again\n');
    return
elseif ~ismember(set_no,[1:4])
    fprintf(2,'Incorrect set no\n');
    fprintf(2,'Please try again\n');
    return
end



% sanity check to prevent overwriting
if exist([pwd '/data/s' int2str(subjcode) '_behav.mat'],'file')
    fprintf(2,'Data file exists\n');
    fprintf(2,'Check subject ID\n');
    return
end


ListenChar(2);

%==========================================================================
% Read schedule
%==========================================================================
new_block_trialno=[0:3].*24+1;

sche=load([pwd '/sche/exp_set' num2str(set_no) '.txt.']);

env1_rew=sche(:,1:20);
env2_rew=sche(:,21:40);
env1_prob=sche(:,41);
env2_prob=sche(:,42);
env1_mean=sche(:,43);
env2_mean=sche(:,44);
env1_var=sche(:,45);
env2_var=sche(:,46);
env1_skew=sche(:,47);
env2_skew=sche(:,48);
env1_EV=sche(:,49);
env2_EV=sche(:,50);
all_trial_code=sche(:,51);
%-------------------------------
response_timeframe=4;
total_earning=0;
resp=nan(size(sche,1),1);

%==========================================================================
% Reference number of jitter
%==========================================================================
jitter_sche=load([pwd '/sche/jitter_time.txt']);

jit_new_block=1;
jit_iti=2;
jit_stim_onset=3;
jit_drawing=4;
jit_reward_delivery=5;
jit_after_reward_delivery=6;
jit_tooslow=7;
%-------------------------------
timelog.new_block=nan(size(sche,1),2);
timelog.iti=nan(size(sche,1),2);
timelog.stim_onset=nan(size(sche,1),2);
timelog.resp_feedback=nan(size(sche,1),2);
timelog.drawing=nan(size(sche,1),2);
timelog.reward_delivery=nan(size(sche,1),2);
timelog.tooslow=nan(size(sche,1),2);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
try
    %======================================================================
    % Default settings
    %======================================================================
    Screen('Preference','SuppressAllWarnings',1);
    Screen('Preference', 'SkipSyncTests', 2);

    screens=Screen('Screens');      %looks for how many screens are connected to the computer
    screen_in_use=max(screens);     %if there is more than one screen, it selects one of them without the menu bar and assigns an arbitrary name to it
    [myscreen,rect]=Screen('OpenWindow',screen_in_use,[118,113,113]);         %myscreen-->the name of the screen, rect-->save the coordinates of the screen
    [screenXpixels, screenYpixels] = Screen('WindowSize',myscreen);    
    [x_center,y_center]=RectCenter(rect);
    % Activate for alpha
    Screen('BlendFunction', myscreen, 'GL_SRC_ALPHA', 'GL_ONE_MINUS_SRC_ALPHA');
    
    %set response buttons
    HideCursor;
    left_key=KbName('1!');
    right_key=KbName('2@');
    exit=KbName('esc');
    
    activeKeys = [left_key, right_key, exit];
    RestrictKeysForKbCheck(activeKeys);

    %======================================================================
    % Set colour, picutures, bars, coordinates
    %======================================================================
    green=[17,173,0];
    yellow=[255,255,0];
    grey=[200,200,200];
    red=[175,0,0];
    %----------------------------------------------------------------------
    % function-local variables
    within_function_info.myscreen=myscreen;
    within_function_info.x_center=x_center;
    within_function_info.y_center=y_center;
    within_function_info.green=green;
    within_function_info.grey=grey;
    within_function_info.yellow=yellow;

    %======================================================================
    % receive trigger from the MRI scanner to begin
    %======================================================================
    Screen('TextSize',myscreen,50);
    %DrawFormattedText(myscreen,'Get ready','center','center',[255,255,255]);
    Screen('TextFont', myscreen, '-:lang=ja');
    msg1 = [23526, 39511, 21363, 23559, 38283, 22987];
    DrawFormattedText(myscreen, msg1,'center','center',[255,255,255]);
    Screen('Flip',myscreen);
    
    trigger=KbName('s');
    ListenChar(0);
    exp_start_time=KbTriggerWait(trigger);
    ListenChar(2);
    %======================================================================




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Main task
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Start page
    %======================================================================
    Screen('TextSize',myscreen,50);
    Screen('TextFont', myscreen, '-:lang=ja');
    msg2 = [28310, 20633, 22909, 35531, 25353, 32, 1];
    DrawFormattedText(myscreen,msg2,'center','center',[255,255,255]);
   
    Screen('Flip',myscreen);
    KbWait;
    Screen('Flip',myscreen);
    

    for trial_no=1:length(all_trial_code)
        %==================================================================
        % indication of new block
        %==================================================================
        if ismember(trial_no,new_block_trialno)
            Screen('Flip',myscreen);                       
            
            Screen('TextSize',myscreen,80);
            Screen('TextFont', myscreen, '-:lang=ja');
            msg3 = [38283, 22987];
            DrawFormattedText(myscreen,msg3,'center',y_center,[255,255,255]);
            %DrawFormattedText(myscreen,'begins','center',y_center+50,[255,255,255]);

            Screen('Flip',myscreen);
            timelog.new_block(trial_no,1)=GetSecs;
            WaitSecs(jitter_sche(trial_no,jit_new_block));
            timelog.new_block(trial_no,2)=GetSecs-timelog.new_block(trial_no,1);
        end

        %==================================================================
        % iti
        %==================================================================
        Screen('Flip',myscreen);    % flush the screen

        Screen('TextSize',myscreen,200);
        Screen('TextFont', myscreen, 'Arial');
        DrawFormattedText(myscreen,'+','center','center',[255,255,255]);
 
        WaitSecs(jitter_sche(trial_no,jit_iti));
        Screen('Flip',myscreen);
        timelog.iti(trial_no,1)=GetSecs;

        %================================================================== 
        % stimuli onset
        %==================================================================
        Screen('TextSize',myscreen,100);
        [current_env1_bg_coor, current_env2_bg_coor]=show_envs(env1_rew(trial_no,:),env2_rew(trial_no,:),env1_prob(trial_no),env2_prob(trial_no),within_function_info);

        WaitSecs(jitter_sche(trial_no,jit_stim_onset));

        timelog.iti(trial_no,2)=GetSecs-timelog.iti(trial_no,1);
        Screen('Flip',myscreen,[],1);
        timelog.stim_onset(trial_no,1)=GetSecs;

        %--------------------------------------        
        % start recording response
        %-------------------------------------- 
        timedout=false;
        onset_time=GetSecs;

        while ~timedout
            [keyIsDown,keysecs,keyCode]=KbCheck;
            
            if keyCode(exit)==1
                ListenChar(0);
                Screen('CloseAll');  
                return;

            elseif keyCode(left_key)==1 && isnan(resp(trial_no))  
                RT(trial_no,1)=keysecs-onset_time;
                resp(trial_no,1)=1;
                trial_code(trial_no,1)=all_trial_code(trial_no);
                
                cho_rew(trial_no,:)=env1_rew(trial_no,:);
                cho_prob(trial_no,1)=env1_prob(trial_no);
                cho_mean(trial_no,1)=env1_mean(trial_no);
                cho_var(trial_no,1)=env1_var(trial_no);
                cho_skew(trial_no,1)=env1_skew(trial_no);
                cho_EV(trial_no,1)=env1_EV(trial_no);

                uncho_rew(trial_no,:)=env2_rew(trial_no,:);
                uncho_prob(trial_no,1)=env2_prob(trial_no);
                uncho_mean(trial_no,1)=env2_mean(trial_no);
                uncho_var(trial_no,1)=env2_var(trial_no);
                uncho_skew(trial_no,1)=env2_skew(trial_no);
                uncho_EV(trial_no,1)=env2_EV(trial_no);
                %--------------------------------------------
                num_bars=length(find(~isnan(cho_rew(trial_no,:))));
                red_frame_yshift=60;
                if num_bars==1
                    red_frame_xshift=100;
                else
                    red_frame_xshift=60;                   
                end

                Screen('FrameRect',myscreen,red,[current_env1_bg_coor(1)-red_frame_xshift, current_env1_bg_coor(2)-red_frame_yshift*3, current_env1_bg_coor(3)+red_frame_xshift, current_env1_bg_coor(4)+red_frame_yshift],14);
                
                timelog.stim_onset(trial_no,2)=GetSecs-timelog.stim_onset(trial_no,1);
                Screen('Flip',myscreen,[],1);
                timelog.resp_feedback(trial_no,1)=GetSecs;
                break;

            elseif keyCode(right_key)==1 && isnan(resp(trial_no))  
                RT(trial_no,1)=keysecs-onset_time;
                resp(trial_no,1)=2;
                trial_code(trial_no,1)=all_trial_code(trial_no);
                
                cho_rew(trial_no,:)=env2_rew(trial_no,:);
                cho_prob(trial_no,1)=env2_prob(trial_no);
                cho_mean(trial_no,1)=env2_mean(trial_no);
                cho_var(trial_no,1)=env2_var(trial_no);
                cho_skew(trial_no,1)=env2_skew(trial_no);
                cho_EV(trial_no,1)=env2_EV(trial_no);

                uncho_rew(trial_no,:)=env1_rew(trial_no,:);
                uncho_prob(trial_no,1)=env1_prob(trial_no);
                uncho_mean(trial_no,1)=env1_mean(trial_no);
                uncho_var(trial_no,1)=env1_var(trial_no);
                uncho_skew(trial_no,1)=env1_skew(trial_no);
                uncho_EV(trial_no,1)=env1_EV(trial_no);
                %--------------------------------------------
                num_bars=length(find(~isnan(cho_rew(trial_no,:))));
                red_frame_yshift=60;
                if num_bars==1
                    red_frame_xshift=100;
                else
                    red_frame_xshift=60;                   
                end
                
                Screen('FrameRect',myscreen,red,[current_env2_bg_coor(1)-red_frame_xshift, current_env2_bg_coor(2)-red_frame_yshift*3, current_env2_bg_coor(3)+red_frame_xshift, current_env2_bg_coor(4)+red_frame_yshift],14);

                timelog.stim_onset(trial_no,2)=GetSecs-timelog.stim_onset(trial_no,1);
                Screen('Flip',myscreen,[],1);
                timelog.resp_feedback(trial_no,1)=GetSecs;
                break;
            end  


            % quit the while loop if the response time frame is exceeded
            if (keysecs-onset_time)>response_timeframe
                RT(trial_no,1)=response_timeframe;
                resp(trial_no,1)=0;
                trial_code(trial_no,1)=all_trial_code(trial_no);

                cho_rew(trial_no,:)=nan(1,size(env1_rew,2));
                cho_prob(trial_no,1)=nan;
                cho_mean(trial_no,1)=nan;
                cho_var(trial_no,1)=nan;
                cho_skew(trial_no,1)=nan;
                cho_EV(trial_no,1)=nan;

                uncho_rew(trial_no,:)=nan(1,size(env1_rew,2));
                uncho_prob(trial_no,1)=nan;
                uncho_mean(trial_no,1)=nan;
                uncho_var(trial_no,1)=nan;
                uncho_skew(trial_no,1)=nan;
                uncho_EV(trial_no,1)=nan;
                %--------------------------------
                timelog.stim_onset(trial_no,2)=GetSecs-timelog.stim_onset(trial_no,1);
                Screen('Flip',myscreen);

                Screen('TextSize',myscreen,90);
                Screen('TextStyle',myscreen,1);     % 1=bold
                Screen('TextFont', myscreen, '-:lang=ja');
                msg4 = [22826, 24930, 33];
                DrawFormattedText(myscreen,msg4,'center','center',[255,255,255]);
                Screen('TextFont', myscreen, 'Arial');                
                DrawFormattedText(myscreen,'-100!','center',y_center+200,red);
                total_earning=total_earning-100;

                timedout=true;

                Screen('Flip',myscreen);
                timelog.tooslow(trial_no,1)=GetSecs;
                WaitSecs(jitter_sche(trial_no,jit_tooslow));
                timelog.tooslow(trial_no,2)=GetSecs-timelog.tooslow(trial_no,1);

                Screen('TextStyle',myscreen,0);

                break
            end
        end

        %==================================================================
        % outcome phase
        %==================================================================
        if resp(trial_no,1)~=0   
            %--------------------------------------------------------------
            %                   highlight drawn items
            %--------------------------------------------------------------
            [drawn_ind(trial_no,1),drawn_val(trial_no,1)]=outcome_drawing(env1_rew(trial_no,:),env2_rew(trial_no,:),resp(trial_no),within_function_info);
    
            WaitSecs(jitter_sche(trial_no,jit_drawing));

            timelog.resp_feedback(trial_no,2)=GetSecs-timelog.resp_feedback(trial_no,1);
            Screen('Flip',myscreen,[],1);
            timelog.drawing(trial_no,1)=GetSecs;
                     
            %--------------------------------------------------------------
            %                   determine trial earning
            %--------------------------------------------------------------
            rand_prob=rand*100;
    
            if cho_prob(trial_no,1)>rand_prob
                won_reward(trial_no,1)=drawn_val(trial_no,1);
            else
                won_reward(trial_no,1)=0;
            end

            total_earning=total_earning+won_reward(trial_no,1);

            %--------------------------------------------------------------
            %                   display reward outcome
            %--------------------------------------------------------------
            display_outcome_reward(env1_rew(trial_no,:),env2_rew(trial_no,:),resp(trial_no),won_reward(trial_no),within_function_info);
            
            WaitSecs(jitter_sche(trial_no,jit_reward_delivery));

            timelog.drawing(trial_no,2)=GetSecs-timelog.drawing(trial_no,1);
            Screen('Flip',myscreen);
            timelog.reward_delivery(trial_no,1)=GetSecs;

            % clear up the screen
            WaitSecs(jitter_sche(trial_no,jit_after_reward_delivery));
            Screen('Flip',myscreen);
            timelog.reward_delivery(trial_no,2)=GetSecs-timelog.reward_delivery(trial_no,1);
        end


        %==================================================================
        % resting page
        %==================================================================
        Screen('TextSize',myscreen,50);
        
        if trial_no==length(all_trial_code)/2
            Screen('TextFont', myscreen, '-:lang=ja');
            msg5 = [20445, 25345, 38748, 27490];
            msg6 = [28310, 20633, 22909, 35531, 25353, 32, 1];
            DrawFormattedText(myscreen,msg5,'center','center',[255,255,255]);
            DrawFormattedText(myscreen,msg6,'center',y_center+100,[255,255,255]);
            Screen('Flip',myscreen);

            KbWait;
        end
        %==================================================================
    end

    
    results.RT=RT;
    results.response=resp;
    results.trial_code=trial_code;
    results.cho_rew=cho_rew;
    results.cho_prob=cho_prob;
    results.cho_mean=cho_mean;
    results.cho_var=cho_var;
    results.cho_skew=cho_skew;
    results.cho_EV=cho_EV;
    results.uncho_rew=uncho_rew;
    results.uncho_prob=uncho_prob;
    results.uncho_mean=uncho_mean;
    results.uncho_var=uncho_var;
    results.uncho_skew=uncho_skew;
    results.uncho_EV=uncho_EV;
    results.drawn_ind=drawn_ind;
    results.drawn_val=drawn_val;

    
    if ~exist([pwd '/data/s' int2str(subjcode) '_behav.mat'])
        save([pwd '/data/s' int2str(subjcode) '_behav.mat']);
    else
        fprintf(2,'Check subject ID\n');
        fprintf(2,'Data saved in temporary mat file\n');
        
        save([pwd '/data/temp_s' int2str(subjcode) '_behav.mat']);
    end
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Finish page
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Screen('Flip',myscreen);
    Screen('TextSize',myscreen,50);
    msg7 = [23526, 39511, 23436, 25104];
    DrawFormattedText(myscreen,msg7,'center','center',[255,255,255]);
    %DrawFormattedText(myscreen,'Thank you!!!','center',y_center+100,[255,255,255]);
    Screen('Flip',myscreen);
    KbWait;

    ListenChar(0);
    Screen('CloseAll');         %screen(¡¥Close¡¦, OBJECT)-->close specific object,"OBJECT" is the object name
catch
    ListenChar(0);
    Screen('CloseAll');    % close Screen window, for main experiment
    rethrow(lasterror);     % reissue the error, for debugging 
end
















function [env1_bg_coor, env2_bg_coor]=show_envs(env1_rew,env2_rew,env1_prob,env2_prob,within_function_info)
    % read the variables for local use
    var_names=fieldnames(within_function_info);
    for n=1:length(var_names)
        eval([var_names{n} '=within_function_info.' var_names{n} ';']);
    end

    %======================================================================
    % coordinates of the environment background
    %======================================================================
    num_bars=length(find(~isnan(env1_rew)));
    env_bg_xshift=100;
    env_bg_yshift=20;
    barheight_per_unit=8;   % i.e. when x=1, height=5
    barheight_max=20;
    
    if num_bars==20
        barwidth=12;
        interval_btw_bars=4;
    elseif num_bars==10
        barwidth=22;
        interval_btw_bars=8;
    elseif num_bars==4
        barwidth=40;
        interval_btw_bars=18;
    elseif num_bars==2
        barwidth=80;
        interval_btw_bars=24;
    elseif num_bars==1
        env_bg_xshift=140;
        barwidth=120;
        interval_btw_bars=26;
    end

    env1_bg_right=x_center - env_bg_xshift;
    env1_bg_left=env1_bg_right - barwidth*num_bars - (num_bars-1)*interval_btw_bars;
    env1_bg_top=y_center + env_bg_yshift;
    env1_bg_bottom=env1_bg_top + barheight_per_unit*barheight_max;
    env1_bg_coor=[env1_bg_left, env1_bg_top, env1_bg_right, env1_bg_bottom];

    env2_bg_left=x_center + env_bg_xshift;
    env2_bg_right=env2_bg_left + barwidth*num_bars + (num_bars-1)*interval_btw_bars;
    env2_bg_top=y_center + env_bg_yshift;
    env2_bg_bottom=env2_bg_top + barheight_per_unit*barheight_max;
    env2_bg_coor=[env2_bg_left, env2_bg_top, env2_bg_right, env2_bg_bottom];
    
    %======================================================================
    % coordinates of the environment probability texts
    %======================================================================
    prob_text_y_coor=y_center-100;

    env1_text_xcoor_digit1=env1_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 60;
    env2_text_xcoor_digit1=env2_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 60;

    if num_bars==20
        env1_text_xcoor_digit2=env1_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 92;  
        env2_text_xcoor_digit2=env2_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 92;
    else
        env1_text_xcoor_digit2=env1_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 97;  
        env2_text_xcoor_digit2=env2_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 97;
    end
    
    %======================================================================
    % display env background
    %======================================================================
    Screen('FillRect',myscreen,grey,env1_bg_coor);
    Screen('FillRect',myscreen,grey,env2_bg_coor);
    
    %======================================================================
    % display the bars
    %======================================================================
    env1_rew=env1_rew./10;
    env2_rew=env2_rew./10;

    for x=1:size(env1_rew,2)
        % set left env bars
        temp_bar_left=env1_bg_coor(1) + (x-1)*barwidth + (x-1)*interval_btw_bars;
        temp_bar_right=temp_bar_left + barwidth;
        temp_bar_bottom=env1_bg_coor(4);
        temp_bar_top=temp_bar_bottom - barheight_per_unit*env1_rew(x);

        temp_bar_coor_left=[temp_bar_left,temp_bar_top,temp_bar_right,temp_bar_bottom];
        %--------------------------
        % set right env bars
        temp_bar_left=env2_bg_coor(1) + (x-1)*barwidth + (x-1)*interval_btw_bars;
        temp_bar_right=temp_bar_left + barwidth;
        temp_bar_bottom=env2_bg_coor(4);
        temp_bar_top=temp_bar_bottom - barheight_per_unit*env2_rew(x);

        temp_bar_coor_right=[temp_bar_left,temp_bar_top,temp_bar_right,temp_bar_bottom];
        %------------------------------------------------------------------
        Screen('FillRect',myscreen, green, temp_bar_coor_left);
        Screen('FillRect',myscreen, green, temp_bar_coor_right);
    end

    %======================================================================
    % display the probability text
    %======================================================================
    env1_reward_text=[num2str(env1_prob) '%'];
    env2_reward_text=[num2str(env2_prob) '%'];
    env1_reward_text_digit=numel(num2str(env1_prob));  % check no. of digits
    env2_reward_text_digit=numel(num2str(env2_prob));  % check no. of digits

    Screen('DrawText',myscreen, env1_reward_text, eval(['env1_text_xcoor_digit' int2str(env1_reward_text_digit)]), prob_text_y_coor, green);
    Screen('DrawText',myscreen, env2_reward_text, eval(['env2_text_xcoor_digit' int2str(env2_reward_text_digit)]), prob_text_y_coor, green);
end




function [drawn_bar_ind,drawn_val]=outcome_drawing(env1_rew,env2_rew,resp,within_function_info)
    % read the variables for local use
    var_names=fieldnames(within_function_info);
    for n=1:length(var_names)
        eval([var_names{n} '=within_function_info.' var_names{n} ';']);
    end

    %======================================================================
    % random drawing
    %======================================================================
    eval(['env' int2str(resp) '_rew(isnan(env' int2str(resp) '_rew))=[];']);
    drawn_bar_ind=randi([1 size(eval(['env' int2str(resp) '_rew']),2)]);
    drawn_val=eval(['env' int2str(resp) '_rew(drawn_bar_ind)']);

    % rescale for displaying the bars
    env1_rew=env1_rew./10;
    env2_rew=env2_rew./10;
    
    %======================================================================
    % coordinates of the environment background
    %======================================================================
    num_bars=length(find(~isnan(env1_rew)));
    env_bg_xshift=100;
    env_bg_yshift=20;
    barheight_per_unit=8;   % i.e. when x=1, height=5
    barheight_max=20;
    
    if num_bars==20
        barwidth=12;
        interval_btw_bars=4;
    elseif num_bars==10
        barwidth=22;
        interval_btw_bars=8;
    elseif num_bars==4
        barwidth=40;
        interval_btw_bars=18;
    elseif num_bars==2
        barwidth=80;
        interval_btw_bars=24;
    elseif num_bars==1
        env_bg_xshift=140;
        barwidth=120;
        interval_btw_bars=26;
    end

    env1_bg_right=x_center - env_bg_xshift;
    env1_bg_left=env1_bg_right - barwidth*num_bars - (num_bars-1)*interval_btw_bars;
    env1_bg_top=y_center + env_bg_yshift;
    env1_bg_bottom=env1_bg_top + barheight_per_unit*barheight_max;
    env1_bg_coor=[env1_bg_left, env1_bg_top, env1_bg_right, env1_bg_bottom];

    env2_bg_left=x_center + env_bg_xshift;
    env2_bg_right=env2_bg_left + barwidth*num_bars + (num_bars-1)*interval_btw_bars;
    env2_bg_top=y_center + env_bg_yshift;
    env2_bg_bottom=env2_bg_top + barheight_per_unit*barheight_max;
    env2_bg_coor=[env2_bg_left, env2_bg_top, env2_bg_right, env2_bg_bottom];
    %----------------------------------------------------------------------
    temp_bar_left=eval(['env' int2str(resp) '_bg_coor(1)']) + (drawn_bar_ind-1)*barwidth + (drawn_bar_ind-1)*interval_btw_bars;
    temp_bar_right=temp_bar_left + barwidth;
    temp_bar_bottom=eval(['env' int2str(resp) '_bg_coor(4)']);
    temp_bar_top=temp_bar_bottom - eval(['barheight_per_unit*env' int2str(resp) '_rew(drawn_bar_ind)']);  

    temp_bar_coor=[temp_bar_left,temp_bar_top,temp_bar_right,temp_bar_bottom];
    %----------------------------------------------------------------------
    Screen('FillRect',myscreen, yellow, temp_bar_coor);
end




function display_outcome_reward(env1_rew,env2_rew,resp,won_reward,within_function_info)
    % read the variables for local use
    var_names=fieldnames(within_function_info);
    for n=1:length(var_names)
        eval([var_names{n} '=within_function_info.' var_names{n} ';']);
    end

    %======================================================================
    % coordinates of the environment background
    %======================================================================
    num_bars=length(find(~isnan(env1_rew)));
    env_bg_xshift=100;
    env_bg_yshift=20;
    barheight_per_unit=8;   % i.e. when x=1, height=5
    barheight_max=20;
    
    if num_bars==20
        barwidth=12;
        interval_btw_bars=4;
    elseif num_bars==10
        barwidth=22;
        interval_btw_bars=8;
    elseif num_bars==4
        barwidth=40;
        interval_btw_bars=18;
    elseif num_bars==2
        barwidth=80;
        interval_btw_bars=24;
    elseif num_bars==1
        env_bg_xshift=140;
        barwidth=120;
        interval_btw_bars=26;
    end

    env1_bg_right=x_center - env_bg_xshift;
    env1_bg_left=env1_bg_right - barwidth*num_bars - (num_bars-1)*interval_btw_bars;
    env1_bg_top=y_center + env_bg_yshift;
    env1_bg_bottom=env1_bg_top + barheight_per_unit*barheight_max;
    env1_bg_coor=[env1_bg_left, env1_bg_top, env1_bg_right, env1_bg_bottom];

    env2_bg_left=x_center + env_bg_xshift;
    env2_bg_right=env2_bg_left + barwidth*num_bars + (num_bars-1)*interval_btw_bars;
    env2_bg_top=y_center + env_bg_yshift;
    env2_bg_bottom=env2_bg_top + barheight_per_unit*barheight_max;
    env2_bg_coor=[env2_bg_left, env2_bg_top, env2_bg_right, env2_bg_bottom];

    %======================================================================
    % coordinates of reward outcomes
    %======================================================================
    rew_outcome_y_coor=env1_bg_bottom+100;

    rew_outcome1_xcoor_digit1=env1_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 65;     % chosen opt=left
    rew_outcome1_xcoor_digit2=env1_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 85;     % chosen opt=left
    rew_outcome1_xcoor_digit3=env1_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 110;     % chosen opt=left
    rew_outcome2_xcoor_digit1=env2_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 65;     % chosen opt=right
    rew_outcome2_xcoor_digit2=env2_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 85;     % chosen opt=right
    rew_outcome2_xcoor_digit3=env2_bg_left + barwidth*(num_bars/2) + (num_bars/2-1+0.5)*interval_btw_bars - 110;     % chosen opt=right

    %======================================================================
    % display the reward outcome
    %======================================================================
    outcome_text=['+$' num2str(won_reward)];

    reward_text_digit=numel(num2str(won_reward));  % check no. of digits
    outcome_text_coor=eval(['rew_outcome' int2str(resp) '_xcoor_digit' int2str(reward_text_digit)]);

    Screen('TextSize',myscreen,75);
    Screen('DrawText',myscreen, outcome_text, outcome_text_coor, rew_outcome_y_coor, yellow);
end