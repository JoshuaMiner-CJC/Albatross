import pyCandle as pc
import time
import pygame

# Initialize pygame and controller
pygame.init()
pygame.joystick.init()

# Wait for controller to be found
if pygame.joystick.get_count() == 0:
    print("No controller found - plug in your remote and try again")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Controller connected: {joystick.get_name()}")

# Subroutine Section

def subroutine01(joystick, md1, md2, md3, md4):
    if joystick.get_button(0):

        # First Movement
        start_time = time.time()
        while time.time() - start_time < 1.5:
            md1.setTargetVelocity(-3)
            md2.setTargetVelocity(-3)
            md3.setTargetVelocity(3)
            md4.setTargetVelocity(3)
            time.sleep(0.02)

        # Second Movement
        start_time = time.time()
        while time.time() - start_time < 1.5:
            md1.setTargetVelocity(1)
            md2.setTargetVelocity(1)
            md3.setTargetVelocity(-1)
            md4.setTargetVelocity(1)
            time.sleep(0.02)

        # Stop all movement
        md1.setTargetVelocity(0)
        md2.setTargetVelocity(0)
        md3.setTargetVelocity(0)
        md4.setTargetVelocity(0)

# Uncomment this for debugging the CANdlelib stack
# pc.logVerbosity(pc.Verbosity_E.VERBOSITY_3)

# Initialize CANdle on the USB bus (SPI bus not supported yet)
candle = pc.attachCandle(pc.CANdleDatarate_E.CAN_DATARATE_1M, pc.busTypes_t.USB)

md1 = pc.MD(354, candle)
md2 = pc.MD(355, candle)
md3 = pc.MD(356, candle)
md4 = pc.MD(357, candle)

err1 = md1.init()
err2 = md2.init()
err3 = md3.init()
err4 = md4.init()
print(f"Motor 354 initialized with status: {err1}")
print(f"Motor 355 initialized with status: {err2}")
print(f"Motor 356 initialized with status: {err3}")
print(f"Motor 357 initialized with status: {err4}")

# Main Code Loop

if err1 == pc.MD_Error_t.OK:

    # Set motion mode of the MD
    md1.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    md2.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    md3.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    md4.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)

    # Enable motor power
    md1.enable()
    md2.enable()
    md3.enable()
    md4.enable()

    MAX_SPEED = 17.0

    # This loop is crucial as MD requires constant polling by any of its functions
    # in order to keep the motor alive.
    # The frequency of required polling can be adjusted via watchdog register in the MD.

    while True:

        # Read pygame events - this is requried to get fresh joystick data
        pygame.event.pump()

        # Read left joystick vertical axis
        left = -joystick.get_axis(1)

        # Read right joystick vertical axis
        right = -joystick.get_axis(3)

        # Calculate motor speeds
        md1.setTargetVelocity(-left * MAX_SPEED)
        md2.setTargetVelocity(-left * MAX_SPEED)
        md3.setTargetVelocity(right * MAX_SPEED)
        md4.setTargetVelocity(right * MAX_SPEED)

        #Subroutine Grab

        subroutine01(joystick, md1, md2, md3, md4)

        # Sleep less than wdg timer
        time.sleep(0.02)

    # Disable motor power
    md1.disable()
    md2.disable()
    md3.disable()
    md4.disable()