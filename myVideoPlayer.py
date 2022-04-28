#!/usr/bin/env python3

from ExtractAndDisplay import *
from ConvertToGrayscale import *
import threading
import queue

# filename of clip to load
filename = 'clip.mp4'

# shared queue  
extractionQueue = queue.Queue()

extractThread = threading.Thread(target=extractFrames, args=[filename, extractionQueue, 72])
extractThread.start()

#convertThread = threading.Thread(target=)

displayThread = threading.Thread(target=displayFrames, args=[extractionQueue])
displayThread.start()
