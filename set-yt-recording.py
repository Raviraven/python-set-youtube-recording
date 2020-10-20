import Settings
import os
import subprocess

def set_sound_devices():
    subprocess.run(["SoundVolumeView.exe", "/SetDefault", str(Settings.DEFAULT_MICROPHONE_ID), str(Settings.DEFAULT_DEVICE_TYPE)])
    subprocess.run(["SoundVolumeView.exe", "/SetDefault", str(Settings.DEFAULT_SPEAKER_ID), str(Settings.DEFAULT_DEVICE_TYPE)])
    subprocess.run(["SoundVolumeView.exe", "/SetVolume", str(Settings.DEFAULT_SPEAKER_ID), str(Settings.DEFAULT_VOLUME_LEVEL)])
    subprocess.run(["SoundVolumeView.exe", "/Unmute", str(Settings.DEFAULT_SPEAKER_ID)])


def run_apps():
    os.startfile(Settings.OBS_SHORTCUT)  
    os.startfile(Settings.AUDIO_SOFTWARE_LOCATION)
    os.startfile(Settings.TASK_MANAGER)


def set_yt_recording():
    try:
        set_sound_devices()
        run_apps()
    except Exception as error:
        print("An error occured: {0}".format(error))


if __name__ == "__main__":
    set_yt_recording()
