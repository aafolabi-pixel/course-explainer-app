import subprocess
import os

sound_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds', 'notification.mp3')

try:
    # macOS
    subprocess.run(['afplay', sound_path], check=True)
except FileNotFoundError:
    try:
        # Windows fallback
        import ctypes
        ctypes.windll.winmm.PlaySoundW(sound_path, None, 0x00020001)
    except Exception:
        pass
except Exception:
    pass
