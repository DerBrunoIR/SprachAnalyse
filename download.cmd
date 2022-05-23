@echo off
REM %1 = channel_url
REM %2 = max videos
REM %3 = output_folder
python .\channel.py %1 %2 | python .\getAudio.py %3 | python .\speech2text.py | python ./statistics.py
