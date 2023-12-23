import time
from gd5800_mp3_serial import Gd5800Mp3Serial

print('setup')
mp3 = Gd5800Mp3Serial(tx_pin=12, rx_pin=13)
mp3.reset()
mp3.stop()

mp3.equalizer = Gd5800Mp3Serial.EQUALIZER_NORMAL
mp3.volume = 48

print('loop')
while True:
    print('status:', mp3.status)
    mp3.play_by_index(3)
    print('status:', mp3.status)
    time.sleep(2)
    mp3.stop()
