import pyfiglet
from pytube import YouTube
import os

ascci_banner = pyfiglet.figlet_format("YOUTUBE TO MP3")
print(ascci_banner)

URL = input("YT VIDEO URL: ")
yt = YouTube(URL)

try:
  print("\nPROCESSING...")
  video = yt.streams.filter(only_audio=True).first()
  out_file = video.download()

  base, ext = os.path.splitext(out_file)
  new_file = base + ".mp3"
  os.rename(out_file, new_file)
  print("\nDOWNLOAD DONE!")

except:
  print("\nERROR! CONTACT DEVELOPER")