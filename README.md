# Set youtube recording

Script written for automating youtube recording based on app written by NirSoft - Sound Volume View.  
Runs OBS and Audacity and sets default microphone and speakers with volume set to 50%.

### Settings
Update settings with values which suits you

    DEFAULT_SPEAKER_ID=""
    DEFAULT_MICROPHONE_ID=""
    DEFAULT_DEVICE_TYPE=
    OBS_SHORTCUT=""
    AUDIO_SOFTWARE_LOCATION=""
    RAVBOTEK_LOCATION=r"";


Speakers and micro name are names or ids from Sound Volume View and are used to set them to default devices and volume of speakers.
Default device type - used for setting as default:
    
    0 - console
    1 - multimedia
    2 - communications
    
OBS shortcut location - path to the obs shortcut location (obs.lnk)  
Audacity location - path to the audacity location (audacity.exe)  
RavBotek location - path to the chat bot (in my case - written by me, but if u have some .exe file of chat bot from other sources - paste here its location!)  

### Run

1. Donwload files from repository  
2. Configure settings.py file  
3. Run chosen python script  
    - using terminal  
        - Go into scripts directory  
        - Run 
        ```
        python set-yt-recording.py
        ```  
    - using .bat scripts
        - open scripts directory 
        - run chosen .bat script (from terminal or by double clicking it)

### Known bugs

- Cant run obs from obs.exe file. Solution - create shortcut and set its location in settings file

### URLs

https://www.nirsoft.net/utils/sound_volume_view.html
