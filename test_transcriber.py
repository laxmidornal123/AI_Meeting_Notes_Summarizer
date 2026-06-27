from utils.transcribe import transcribe_audio

text = transcribe_audio("audio/OSR_us_000_0039_8k.wav")

print("\n====================")
print("TRANSCRIPT")
print("====================")
print(text)