#! python3
# twitter_service_remover.py - helps you de-auth services from your Twitter
import pyautogui

# Safety features; mouse to the upper left corner to abort
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# Make sure you set the handedness variable!
lefthanded = True
if lefthanded:
    mainbutton = 'right'
else:
    mainbutton = 'left'

width, height = pyautogui.size()
clickpoint = width,height

# test print
print (width, height)

# These are the names of the screenshot snippets used to find the
# right places to click
areaname = 'apps_area.png'
backname = 'arrow.png'
revokename = 'revoke.png'
revokeloc = None
backloc = None

limit = int(input('Please enter the number of Apps you wish to de-authorize: '))

# Try to find the top app in the authorizations
# im = pyautogui.screenshot()
pyautogui.moveTo(5,5)
firstloc = pyautogui.locateOnScreen(areaname)

# test print
#print(areaname, firstloc)

# We're finished before we begin if we never find an app in the list
done = False
if firstloc == None:
    done = True

# Loop, searching for each click and exiting if any location attempt fails
# We click every time we find that the screen is in a recognizable state
# at the correct time
count = 0
while (done == False and count<limit):
    firstclick = (firstloc.left + (firstloc.width / 2),
                  firstloc.top+firstloc.height-2)
    print (firstclick)
    pyautogui.click(firstclick, button=mainbutton)
    pyautogui.moveRel(-150,0,0.25)
    print('Start looking for revoke')
#    if (revokeloc == None):
    revokeloc = pyautogui.locateOnScreen(revokename)
    print('Done looking for revoke')
    if (revokeloc != None):
        revokeclick = pyautogui.center(revokeloc)
        pyautogui.moveTo(revokeclick,duration=0.5)
        pyautogui.click(revokeclick, button=mainbutton)
        if (backloc == None):
            backloc = pyautogui.locateOnScreen(backname)
        if (backloc != None):
            lastclick = pyautogui.center(backloc)
            print (lastclick)
            pyautogui.click(lastclick, button=mainbutton)
            pyautogui.moveRel(-150,0,0.25)
            firstloc = pyautogui.locateOnScreen(areaname)
            if (firstloc == None):
                done = True
                print('Hit a None result looking for an App')
        else:
            done = True
            print ('Hit a None result looking for the back button.')

    else:
        done = True
        print("Couldn't find revoke button.")
    count+=1;


##print('Press Ctrl-C to quit.')
##try:
##    while True:
##        # Get and print the mouse coordinates.
##        x, y = pyautogui.position()
##        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
##        print(positionStr, end='')
##        print('\b' * len(positionStr), end='', flush=True)
##except KeyboardInterrupt:
##    print('\nDone.')


