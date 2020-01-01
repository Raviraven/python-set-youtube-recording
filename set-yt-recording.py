import Settings
import subprocess

def set_yt_recording():
    try:
        # subprocess.run(["SoundVolumeView.exe", "/SetDefault", str(Settings.Name), str(Settings.DefaultDeviceType)])
        # subprocess.run(["SoundVolumeView.exe", "/SetVolume", str(Settings.Name), "50"])
        # subprocess.run(["SoundVolumeView.exe", "/Unmute", str(Settings.Name)])

        subprocess.run([Settings.OBSShortcutLocation, ""])
    except Exception as error:
        print("An error occured: {0}".format(error))
    
if __name__ == "__main__":
    set_yt_recording()