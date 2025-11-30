import numpy as np
import librosa

class ActiveSonar:
    def __init__(self, threshold=0.3):
        self.threshold = threshold
        self.y = None
        self.sr = None
        print(f"🤖 ActiveSonar System initialized (Threshold: {self.threshold})")

    def load_file(self, filename):
        print(f"📂 Loading file: {filename}...")
        try:
            self.y, self.sr = librosa.load(filename, sr=None)
            print("✅ File loaded successfully.")
        except Exception as e:
            print(f"❌ Error loading file: {e}")

    def scan(self):
        if self.y is None:
            print("⚠️ No data loaded. Please load a file first.")
            return False
        print("🔍 Scanning for biological signatures...")
        rms_curve = librosa.feature.rms(y=self.y)[0]
        max_intensity = np.max(rms_curve)
        max_index = np.argmax(rms_curve)
        timestamp = librosa.frames_to_time(max_index, sr=self.sr)
        print(f"   >>> Peak Energy: {max_intensity:.4f}")
        print(f"   >>> Location: {timestamp:.2f}s")

        if max_intensity > self.threshold:
            print(f"🚨 CONTACT CONFIRMED at {timestamp:.2f}s!")
            return True
        else:
            print("💤 No threats detected.")
            return False
        
if __name__ == "__main__":
    my_sonar = ActiveSonar(threshold=0.3)
    my_sonar.load_file('ocean_mix.wav')
    result = my_sonar.scan()