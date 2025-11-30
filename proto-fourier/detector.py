import numpy as np
import librosa

FILENAME = 'ocean_mix.wav'
THRESHOLD = 0.3
print(f"🎧 Chargement de {FILENAME}...")
y, sr = librosa.load(FILENAME, sr=None)
rms_curve = librosa.feature.rms(y=y)[0]
max_intensity = np.max(rms_curve)
print(f"📊 Max Intensity measured: {max_intensity:.5f}")
max_index = np.argmax(rms_curve)
max_intensity = rms_curve[max_index]
timestamp = librosa.frames_to_time(max_index, sr=sr)
print(f"📊 Analysis Result:")
print(f"   - Max Intensity: {max_intensity:.5f}")
print(f"   - Time Location: {timestamp:.2f} seconds")
if max_intensity > THRESHOLD:
    print(f"🚨 ALERT! Signal detected (Level > {THRESHOLD})")
else:
    print(f"✅ CLEAR. Ocean is calm (Max < {THRESHOLD})")