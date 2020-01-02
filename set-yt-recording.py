import Settings
import subprocess
import os

def set_yt_recording():
    try:
        obs_path_converted = str("\"" + Settings.OBSShortcutLocation + "\"")
        audacity_path_converted = str("\"" + Settings.AudacityLocation + "\"")

        # subprocess.run(["SoundVolumeView.exe", "/SetDefault", str(Settings.MicroName), str(Settings.DefaultDeviceType)])
        # subprocess.run(["SoundVolumeView.exe", "/SetDefault", str(Settings.Name), str(Settings.DefaultDeviceType)])
        # subprocess.run(["SoundVolumeView.exe", "/SetVolume", str(Settings.Name), "50"])
        # subprocess.run(["SoundVolumeView.exe", "/Unmute", str(Settings.Name)])

        # to change, only one works at one time
        os.system(obs_path_converted)
        os.system(audacity_path_converted)
    except Exception as error:
        print("An error occured: {0}".format(error))


if __name__ == "__main__":
    set_yt_recording()
