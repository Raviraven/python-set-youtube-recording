# Set youtube recording

Script written for automating youtube recording based on app written by NirSoft - Sound Volume View. 
Runs OBS and Audacity and sets default microphone and speakers with volume set to 50%.

### Settings
Update settings with values which suits you

    SpeakersName=""
    MicroName=""
    DefaultDeviceType=
    OBSShortcutLocation=""
    AudacityLocation=""
    RavBotekLocation=r"";


Speakers and micro name are names or ids from Sound Volume View and are used to set them to default devices and volume of speakers.
Default device type - used for setting as default:
    
    0 - console
    1 - multimedia
    2 - communications
    
OBS shortcut location - path to the obs shortcut location (obs.lnk) - doesn't work with obs.exe.
Audacity location - path to the audacity location (audacity.exe)
RavBotek location - path to the chat bot (in my case - written by me, but if u have some .exe file of chat bot from other sources - paste here its location!)

### Run

    1. Donwload scripts
    2. Configure settings
    3. Choose which file you want to run set_yt_recording.bat or set_twitch_stream.bat


### URLs

https://www.nirsoft.net/utils/sound_volume_view.html
