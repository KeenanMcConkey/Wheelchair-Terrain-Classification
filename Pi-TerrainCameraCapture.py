'''
    Simple RasperryPi application to periodically capture images of terrain as 
    a wheelchair moves across it using the Pi Camera
    
    Use SSH to run this application from a remote laptop:

	$ssh -X pi@196.168.0.101
	$python ~/TerrainCamera/TerrainCameraCapture.py

    To download images from the Pi

	scp -r pi@192.168.0.101:~/TerrainCamera/images <location/on/laptop>
    
    Created by Keenan McConkey on 2019.08.27
'''

from os import path, mkdir
from time import time, sleep
from picamera import PiCamera
from multiprocessing import Process

# Current directory of this file
CURR_PATH = path.dirname(path.realpath(__file__))

# Path to image folder
IMG_PATH = path.join(CURR_PATH, 'images')

'''
Camera that periodically captures a terrain image using the PiCamera
'''
class TerrainCamera:
    '''
    Init parameters and PiCamera
    '''
    def __init__(self, terrain, res = (1024, 768)):
        self.terrain = terrain
        self.terrain_path = path.join(IMG_PATH, self.terrain)
        
        # Create folder for current terrain
        if not path.exists(self.terrain_path):
            mkdir(self.terrain_path)
        
        # Init PiCamera object
        self.camera = PiCamera(resolution = res, framerate = 25)
        self.camera.start_preview(fullscreen = False,
                                  window = (75, 75, 512, 360))
        
    '''
    Periodically capture images at given frequency
    '''
    def periodic_capture(self, samp_period = 0.1):
        # Track number of captures
        self.capture_count = 0
        
        while True:
            # Save to terrain img folder
            self.curr_capture_file = path.join(self.terrain_path,
                                               '%04d.jpg' % self.capture_count)
            self.camera.capture(self.curr_capture_file)
            self.capture_count += 1
            
            # Sleep for sampling period (so not 100% accurate period)
            sleep(samp_period)
            
    '''
    Stop the PiCamera
    '''
    def stop_periodic_capture(self):
        self.camera.stop_preview()
    
if __name__ == '__main__':
    # Get terrain type
    input_terrain = raw_input('Input terrain type: ')
    
    while not input_terrain:
        input_terrain = raw_input('Please input terrain type: ')
    
    # Get sampling period
    input_samp_period = raw_input('Input sampling period (in s, default = 0.1): ')
    
    if not input_samp_period:
        input_samp_period = 0.1
    else:
        input_samp_period = float(input_samp_period)
        
    # Create image folder if it does not already exist
    if not path.exists(IMG_PATH):
        mkdir(IMG_PATH)
    
    # Start camera, stop at KeyboardInterrupt
    # TODO: Use multithreading
    try:
        terrainCam = TerrainCamera(input_terrain)
        terrainCam.periodic_capture(input_samp_period)
    except KeyboardInterrupt:
        terrainCam.stop_periodic_capture()
