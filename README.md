Sadly, the python library for accessing the YouTube API `pytube` seems to be no longer working due to API changes made by YouTube. 
Therefore all scripts interacting with YouTube are no longer working too.

# SprachAnalyse

This project includes code for generating vocabulary frequency tables from recorded speech and for downloading audio from specific YouTube channels. 
Functionality is split into small scripts that can operate on each others output.

For this personal project, all documentation is contained in this README file.

# How to run
1. `pip install -r requirements.txt`
2. [download](https://alphacephei.com/vosk/models) vosk model `vosk-model-small-de-0.15` and put into project root
3 . `python3 main.py <channel_url> <num_vidoes> <audio_target_dir>`

# Scripts
Here I want to provide interface decsriptions for all scripts.

- `channel.py <channel_url> <n>`:
    - `stdout`: first `n` newline separated video urls from the given channel.
- `getAudio.py <target_path>`:
    - `stdin`: newline separated video urls
    - download audio for all given urls to the `target_path` 
- `ls.py <target> <regex>`:
    - `stdout`: all absolute paths of file in `target` matching `regex`.
- `speech2text.py`
    - For each given audio file a transcript file is created.
    - `stdin`: newline separated file paths
    - `stdout`: newly created absolute filepaths
- `statistics.py [<files>]`
    - Creates from unstructured text word frequency statistics.
    - `<files>` are space separated files.
    - `stdin`: if `<files>` is not given as argument, then newline separated files from stdin are expected.
    - `stdout`: semicolon separated word frequencies encoded as `<word>,<count>`.
- `merge_statistics.py [<files>]`:
    - Combines all word frequency statistics from the given files 
    - `<files>` is space separated.
    - `stdin`: if `<files>` is not given as argument, then newline separated files from stdin are expected.
- `main.py <channel_url> <num_videos> <target_path>`
    Collectes video urls from the given channel, downloads audio to `<target_path>` and creates a word frequency file for all downloaded audio.
- `download.cmd` like `main.py`. 

# TODO
- improve code documentation
- improve error messages
