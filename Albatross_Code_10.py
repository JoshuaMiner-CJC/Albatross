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

def subroutine01(joystick, md1, md2, md3, md4, liftfr, liftbr, liftbl, liftfl, winch, leftfourbar, rightfourbar, claw, screwgun):
    if joystick.get_button(10):

        # First Movement
        start_time = time.time()
        while time.time() - start_time < 1.5:
            md1.setTargetVelocity(-10)
            md2.setTargetVelocity(-10)
            md3.setTargetVelocity(10)
            md4.setTargetVelocity(10)
            liftfr.setTargetVelocity(0)
            liftbr.setTargetVelocity(0)
            liftbl.setTargetVelocity(0)
            liftfl.setTargetVelocity(0)
            winch.setTargetVelocity(0)
            leftfourbar.setTargetVelocity(0)
            rightfourbar.setTargetVelocity(0)
            claw.setTargetVelocity(0)
            screwgun.setTargetVelocity(0)
            time.sleep(0.02)

        # Wait
        start_time = time.time()
        while time.time() - start_time < 1:
            md1.setTargetVelocity(0)
            md2.setTargetVelocity(0)
            md3.setTargetVelocity(0)
            md4.setTargetVelocity(0)
            liftfr.setTargetVelocity(0)
            liftbr.setTargetVelocity(0)
            liftbl.setTargetVelocity(0)
            liftfl.setTargetVelocity(0)
            winch.setTargetVelocity(0)
            leftfourbar.setTargetVelocity(0)
            rightfourbar.setTargetVelocity(0)
            claw.setTargetVelocity(0)
            screwgun.setTargetVelocity(0)
            time.sleep(0.02)

        # Second Movement
        start_time = time.time()
        while time.time() - start_time < 1.5:
            md1.setTargetVelocity(10)
            md2.setTargetVelocity(10)
            md3.setTargetVelocity(-10)
            md4.setTargetVelocity(-10)
            liftfr.setTargetVelocity(0)
            liftbr.setTargetVelocity(0)
            liftbl.setTargetVelocity(0)
            liftfl.setTargetVelocity(0)
            winch.setTargetVelocity(0)            
            leftfourbar.setTargetVelocity(0)
            rightfourbar.setTargetVelocity(0)
            claw.setTargetVelocity(0)
            screwgun.setTargetVelocity(0)
            time.sleep(0.02)

        # Wait
        start_time = time.time()
        while time.time() - start_time < 1:
            md1.setTargetVelocity(0)
            md2.setTargetVelocity(0)
            md3.setTargetVelocity(0)
            md4.setTargetVelocity(0)
            liftfr.setTargetVelocity(0)
            liftbr.setTargetVelocity(0)
            liftbl.setTargetVelocity(0)
            liftfl.setTargetVelocity(0)
            winch.setTargetVelocity(0)
            leftfourbar.setTargetVelocity(0)
            rightfourbar.setTargetVelocity(0)
            claw.setTargetVelocity(0)
            screwgun.setTargetVelocity(0)
            time.sleep(0.02)

        # Third Movement
        start_time = time.time()
        while time.time() - start_time < 1.5:
            md1.setTargetVelocity(10)
            md2.setTargetVelocity(10)
            md3.setTargetVelocity(10)
            md4.setTargetVelocity(10)
            liftfr.setTargetVelocity(0)
            liftbr.setTargetVelocity(0)
            liftbl.setTargetVelocity(0)
            liftfl.setTargetVelocity(0)
            winch.setTargetVelocity(0)
            leftfourbar.setTargetVelocity(0)
            rightfourbar.setTargetVelocity(0)
            claw.setTargetVelocity(0)
            screwgun.setTargetVelocity(0)
            time.sleep(0.02)

        # Wait
        start_time = time.time()
        while time.time() - start_time < 1:
            md1.setTargetVelocity(0)
            md2.setTargetVelocity(0)
            md3.setTargetVelocity(0)
            md4.setTargetVelocity(0)
            liftfr.setTargetVelocity(0)
            liftbr.setTargetVelocity(0)
            liftbl.setTargetVelocity(0)
            liftfl.setTargetVelocity(0)
            winch.setTargetVelocity(0)
            leftfourbar.setTargetVelocity(0)
            rightfourbar.setTargetVelocity(0)
            claw.setTargetVelocity(0)
            screwgun.setTargetVelocity(0)
            time.sleep(0.02)

        # Fourth Movement
        start_time = time.time()
        while time.time() - start_time < 1.5:
            md1.setTargetVelocity(-10)
            md2.setTargetVelocity(-10)
            md3.setTargetVelocity(-10)
            md4.setTargetVelocity(-10)
            liftfr.setTargetVelocity(0)
            liftbr.setTargetVelocity(0)
            liftbl.setTargetVelocity(0)
            liftfl.setTargetVelocity(0)
            winch.setTargetVelocity(0)
            leftfourbar.setTargetVelocity(0)
            rightfourbar.setTargetVelocity(0)
            claw.setTargetVelocity(0)
            screwgun.setTargetVelocity(0)
            time.sleep(0.02)

        # Stop all movement
        md1.setTargetVelocity(0)
        md2.setTargetVelocity(0)
        md3.setTargetVelocity(0)
        md4.setTargetVelocity(0)
        liftfr.setTargetVelocity(0)
        liftbr.setTargetVelocity(0)
        liftbl.setTargetVelocity(0)
        liftfl.setTargetVelocity(0)
        winch.setTargetVelocity(0)
        leftfourbar.setTargetVelocity(0)
        rightfourbar.setTargetVelocity(0)
        claw.setTargetVelocity(0)
        screwgun.setTargetVelocity(0)
        

# Uncomment this for debugging the CANdlelib stack
# pc.logVerbosity(pc.Verbosity_E.VERBOSITY_3)

# Initialize CANdle on the USB bus (SPI bus not supported yet)
candle = pc.attachCandle(pc.CANdleDatarate_E.CAN_DATARATE_1M, pc.busTypes_t.USB)

# ---- PDS SETUP - must come before motor init ----
pds_ids = pc.Pds.discoverPDS(candle)
if not pds_ids:
    print("No PDS found - check connection")
    exit()

pds = pc.Pds(pds_ids[0], candle)
pds.init()

power_stages = []
for socket_num in range(1, 7):
    socket = getattr(pc.socketIndex_E, f'SOCKET_{socket_num}')
    if pds.verifyModuleSocket(pc.moduleType_E.POWER_STAGE, socket):
        ps = pds.attachPowerStage(socket)
        if ps:
            ps.enable()
            power_stages.append(ps)
            print(f"Power stage enabled at socket {socket_num}")

# ---- END PDS SETUP ----

md1 = pc.MD(354, candle)
md2 = pc.MD(355, candle)
md3 = pc.MD(356, candle)
md4 = pc.MD(357, candle)
liftfr = pc.MD(764, candle)
liftbr = pc.MD(765, candle)
liftbl = pc.MD(766, candle)
liftfl = pc.MD(863, candle)
winch = pc.MD(876, candle)
leftfourbar = pc.MD(871, candle)
rightfourbar = pc.MD(873, candle)
claw = pc.MD(874, candle)
screwgun = pc.MD(875, candle)
print([m for m in dir(md1) if not m.startswith('_')])
print(dir(pc.MotionMode_t))

err1 = md1.init()
err2 = md2.init()
err3 = md3.init()
err4 = md4.init()
err5 = liftfr.init()
err6 = liftbr.init()
err7 = liftbl.init()
err8 = liftfl.init()
err9 = winch.init()
err10 = leftfourbar.init()
err11 = rightfourbar.init()
err12 = claw.init()
err13 = screwgun.init()
print(f"Motor 354 initialized with status: {err1}")
print(f"Motor 355 initialized with status: {err2}")
print(f"Motor 356 initialized with status: {err3}")
print(f"Motor 357 initialized with status: {err4}")
print(f"Motor 764 initialized with status: {err5}")
print(f"Motor 765 initialized with status: {err6}")
print(f"Motor 766 initialized with status: {err7}")
print(f"Motor 863 initialized with status: {err8}")
print(f"Motor 876 initialized with status: {err9}")
print(f"Motor 871 initialized with status: {err10}")
print(f"Motor 873 initialized with status: {err11}")
print(f"Motor 874 initialized with status: {err12}")
print(f"Motor 875 initialized with status: {err13}")
print("fourbar status:", err10, err11)

# Main Code Loop

if err1 == pc.MD_Error_t.OK:

    for md in (md1, md2, md3, md4, liftfr, liftbr, liftbl, liftfl, winch):
        md.setProfileAcceleration(30.0)
        md.setProfileDeceleration(30.0)
        md.setMaxTorque(19.0)

    for md in (leftfourbar, rightfourbar, claw, screwgun):
        md.setProfileAcceleration(10.0)
        md.setProfileDeceleration(10.0)
        md.setMaxTorque(48.0)



    # Set motion mode of the MD
    md1.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    md2.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    md3.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    md4.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    liftfr.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    liftbr.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    liftbl.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    liftfl.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    winch.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    leftfourbar.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    rightfourbar.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    claw.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)
    screwgun.setMotionMode(pc.MotionMode_t.PROFILE_VELOCITY)


    # Enable motor power
    md1.enable()
    md2.enable()
    md3.enable()
    md4.enable()
    liftfr.enable()
    liftbr.enable()
    liftbl.enable()
    liftfl.enable()
    winch.enable()
    leftfourbar.enable()
    rightfourbar.enable()
    claw.enable()
    screwgun.enable()


    MAX_SPEED = 19.5
    TORQUE_SPEED = 5.0

    A_BUTTON = 0
    B_BUTTON = 1
    X_BUTTON = 3
    Y_BUTTON = 4

    LEFT_TRIGGER = 5
    LEFT_UPPER_TRIGGER = 6
    RIGHT_TRIGGER = 4
    RIGHT_UPPER_TRIGGER = 7


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



        #Scissor Lift Protocol
        lift = 0
        if joystick.get_axis(RIGHT_TRIGGER) > 0.5:
            lift = MAX_SPEED
        elif joystick.get_button(RIGHT_UPPER_TRIGGER):
            lift = -MAX_SPEED
        liftfr.setTargetVelocity(-lift)
        liftbr.setTargetVelocity(-lift)
        liftbl.setTargetVelocity(lift)
        liftfl.setTargetVelocity(lift)
        



        #Button Test Protocol
        winch_speed = 0
        if joystick.get_button(B_BUTTON):
            winch_speed = -MAX_SPEED
        winch.setTargetVelocity(winch_speed)


        # Four Bar Protocol
        fourbar_speed = 0
        if joystick.get_axis(LEFT_TRIGGER) > 0.5:
            fourbar_speed = -TORQUE_SPEED
        elif joystick.get_button(LEFT_UPPER_TRIGGER):
            fourbar_speed = TORQUE_SPEED
        leftfourbar.setTargetVelocity(fourbar_speed)
        rightfourbar.setTargetVelocity(-fourbar_speed)

        if fourbar_speed !=0:
            print("Torque Output:", leftfourbar.getTorque())

        # Claw Protocol
        claw_speed = 0
        if joystick.get_button(A_BUTTON):
            claw_speed = -TORQUE_SPEED
        elif joystick.get_button(B_BUTTON):
            claw_speed = TORQUE_SPEED
        claw.setTargetVelocity(claw_speed)

        # ScrewGun Protocol
        screwgun_speed = 0
        if joystick.get_button(X_BUTTON):
            screwgun_speed = -TORQUE_SPEED
        elif joystick.get_button(Y_BUTTON):
            screwgun_speed = TORQUE_SPEED
        screwgun.setTargetVelocity(screwgun_speed)












            
        #Subroutine Grab

        subroutine01(joystick, md1, md2, md3, md4, liftfr, liftbr, liftbl, liftfl, winch, leftfourbar, rightfourbar, claw, screwgun)

        # Sleep less than wdg timer
        time.sleep(0.02)

    # Disable motor power
    md1.disable()
    md2.disable()
    md3.disable()
    md4.disable()
    liftfr.disable()
    liftbr.disable()
    liftbl.disable()
    liftfl.disable()
    winch.disable()
    leftfourbar.disable()
    rightfourbar.disable()
    claw.disable()
    screwgun.disable()


    for ps in power_stages:
        ps.disable()