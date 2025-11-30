import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

print("⏳ Loading audio file...")
y, sr = librosa.load('ocean_mix.wav', sr=None)

print("🧮 Computing Short-Time Fourier Transform (STFT)...")
D = librosa.stft(y, n_fft=2048, hop_length=512)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure(figsize=(12, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram: Ocean Noise = Biological Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency (Hz)')
plt.ylim(0, 2000)

output_file = 'spectrogram_output.png'
print(f"💾 Saving visualization to {output_file}...")
plt.savefig(output_file)
print("✅ Done. Open the folder to view the image.")