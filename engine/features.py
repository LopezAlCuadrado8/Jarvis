from playsound import playsound
import eel

# Play assistant sound function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\Audio\\start_sound.mp3"
    playsound(music_dir)