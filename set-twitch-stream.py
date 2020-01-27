import Settings
import os
import subprocess


def set_twitch_stream():
    try:
        subprocess.run(["SoundVolumeView.exe", "/SetDefault", str(Settings.MicroName), str(Settings.DefaultDeviceType)])
        subprocess.run(["SoundVolumeView.exe", "/SetDefault", str(Settings.SpeakersName), str(Settings.DefaultDeviceType)])
        subprocess.run(["SoundVolumeView.exe", "/SetVolume", str(Settings.SpeakersName), str(Settings.VolumeLevel)])
        subprocess.run(["SoundVolumeView.exe", "/Unmute", str(Settings.SpeakersName)])
        os.startfile(Settings.OBSShortcutLocation)
        os.startfile(Settings.TaskManagerLocation)
        os.startfile(Settings.RavBotekLocation)
    except Exception as error:
        print("An error occured {0}".format(error))


if __name__ == "__main__":
    set_twitch_stream()