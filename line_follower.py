import pi2go, time

pi2go.init()

speed = 60

try:
  while True:
    left = pi2go.irLeftLine()
    right = pi2go.irRightLine()
    if left == right:
      pi2go.forward(speed)
      print 'forward'
    elif left == True:
      pi2go.spinRight(speed)
      print 'right'
    elif right == True:
        print 'left'
      pi2go.spinLeft(speed)
finally:
  pi2go.cleanup()
