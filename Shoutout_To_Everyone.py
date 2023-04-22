# win32com.client:
# This library is a part of the pywin32 package and can
# be used to access the Windows Speech API (SAPI) and convert text to speech.
#  there are other Python libraries that you can use to convert text to speech on Windows


import win32com.client as wincl

# Initialize the SAPI engine
engine = wincl.Dispatch("SAPI.SpVoice")

# Convert text to speech
text = ["Harsh","Sundaram","Ashutosh","Karuna","priyanshu","Nikhil"]
for i in text:

 engine.Speak(f'Hey,how are you {i}')

engine.Speak("BY HARSH NISHRA , HMC PROJECTS")
