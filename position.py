from pymouse import PyMouse

m = PyMouse()

print m.screen_size()
#m.move(500,200)
#m.click(28,348,1) #cliquer
while True:
  #m.click(261,365,1)
  print m.position()
