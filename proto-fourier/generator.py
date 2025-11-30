import numpy as np
import scipy.io.wavfile as wav

SAMPLE_RATE = 44100
DURATION = 10
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

ocean_noise = 0.1 * np.random.normal(0, 1, t.shape)
freq_signal = 1000

whale_call = 0.5 * np.sin(2 * np.pi * freq_signal *t)
mask = np.where((t > 2) & (t < 4), 1.0, 0.0)
whale_call = whale_call * mask
final_mix = ocean_noise + whale_call

scaled_data = np.int16(final_mix * 32767)
wav.write('ocean_mix.wav', SAMPLE_RATE, scaled_data)
print(f"✅ Done. File 'ocean_mix.wav' generated! Duration: {DURATION}s")
print("-> Open the folder to listen to the file.")