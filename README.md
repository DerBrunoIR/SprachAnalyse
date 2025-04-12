Sadly, the python library for accessing the YouTube API `pytube` seems to be no longer working due to API changes made by YouTube.

This project includes code for generating vocabulary frequency tables from recorded speech and for downloading audio from specific YouTube channels. 
Functionality is split into small scripts that can operate on each others output.

For this personal project, all documentation is contained in this README file.

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
- `statistics.py <files>`
    - `stdin`: if `<files>` is empty, then newline separated file paths are expected.
    - `stdout`: semicolon separated word frequencies encoded as `<word>,<count>`.
- `merge_statistics.py`: like `statitistics.py` but single threaded.
- `main.py`


