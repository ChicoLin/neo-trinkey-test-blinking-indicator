import board
import neopixel
import supervisor
import time
import touchio


pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=0.01)
touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)
status = 0 # 0 for IDEL, 1 for SUCCESS, 2 for FAILURE

def Success():
    pixels.fill((0, 255, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)

def Failure():
    pixels.fill((255, 0, 0))
    time.sleep(0.5)
    pixels.fill((0, 0, 0))
    time.sleep(0.5)

def Idle():
    pixels.fill((0, 0, 0))

def SerialRead(curr_status):
    st = curr_status
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        if "SUCCESS" in value:
            st = 1
        elif "FAILED" in value:
            st = 2
    return st

while True:
    if status == 0:
        status = SerialRead(status)
    # Set status to IDLE when touched.
    if touch1.value or touch2.value:
        status = 0  # IDLE

    if status == 0:
        Idle()
    elif status == 1:
        Success()
    elif status == 2:
        Failure()
