#!/usr/bin/python

# rgbhsv.py 
# author Mike Quentel

import sys
import math
from Tkinter import Tk, Canvas, IntVar, Label, LabelFrame, Scale, HORIZONTAL

def toDegrees(raw_value):
  return int(raw_value * 360)

def fromDegrees(degrees_value):
  return float(degrees_value/360.0)

def toRoundedPercentage(raw_value):
  return int(round(raw_value * 100))

def fromPercentage(percent_value):
  return float(percent_value * 0.01)

def from8bit(bit_value):
  return float(bit_value/256.0)

def to8bit(raw_value):
  return int(round(raw_value * 256))

def rgb2hsv(R, G, B):
  print "Start of rgb2hsv()"
  
  if R == G == B == 0.0:
    return {'h':0, 's':0, 'v':0}
  
  # DETERMINES MAXIMUM RGB VALUE "V" WHICH IS A MEASURE OF THE DEPARTURE 
  # FROM BLACK.
  V = max(R, G, B)
  
  # DETERMINES MININUM RGB VALUE "X".
  X = min(R, G, B)
  
  # DETERMINES SATURATION "S".
  S = (V - X)/V
  
  # DETERMINES ADJUSTED RED, GREEN, BLUE VALUES "r", "g", "b".
  r = (V - R)/(V - X)
  g = (V - G)/(V - X)
  b = (V - B)/(V - X)
  
  # DETERMINES HUE "H"
  H = 0
  if R == V:
    H = G == X and 5 + b or 1 - g
  if G == V:
    H = B == X and 1 + r or 3 -b
  else:
    H = R == X and 3 + g or 5 - r
  H /= 6.0
  
  hue = toDegrees(H)
  saturation = toRoundedPercentage(S)
  value = toRoundedPercentage(V)

  return {'h':hue, 's':saturation, 'v':value}

def hsv2rgb(H, S, V):
  print "Start of hsv2rgb()"
  
  if H == S == V == 0.0:
    return {'r':0, 'g':0, 'b':0}
  
  H *= 6
  I = math.floor(H)
  F = H - I
  M = V * (1 - S)
  N = V * (1 - S * F)
  K = V * (1 - S * (1 - F))
  
  R = G = B = 0.0
  if I == 0:
    R = V
    G = K
    B = M
  elif I == 1:
    R = N
    G = V
    B = M
  elif I == 2:
    R = M
    G = V
    B = K
  elif I == 3:
    R = M
    G = N
    B = V
  elif I == 4:
    R = K
    G = M
    B = V
  else:
    R = V
    G = M
    B = N

  red = to8bit(R)
  green = to8bit(G)
  blue = to8bit(B)
  
  return {'r':red, 'g':green, 'b':blue}

#################### START GUI COMPONENTS ######################################
def init(r, g, b):
  print "init(r, g, b)"
  r_var.set(r)
  r_sel(r_var)
  g_var.set(g)
  g_sel(g_var)
  b_var.set(b)
  b_sel(b_var)
  canvas.config(bg="#%02x%02x%02x" % (r, g, b))

def updateHSV():
  print "updateHSV()"
  red = r_var.get()
  green = g_var.get()
  blue = b_var.get()
  R = from8bit(red)
  G = from8bit(green)
  B = from8bit(blue)
  hsv = rgb2hsv(R, G, B)
  hue = hsv.get('h')
  saturation = hsv.get('s')
  value = hsv.get('v')
  h_scale.set(hue)
  s_scale.set(saturation)
  v_scale.set(value)
  
def updateRGB():
  print "updateRGB()"
  hue = h_var.get()
  saturation = s_var.get()
  value = v_var.get()
  H = fromDegrees(hue)
  S = fromPercentage(saturation)
  V = fromPercentage(value)
  rgb = hsv2rgb(H, S, V)
  red = rgb.get('r')
  green = rgb.get('g')
  blue = rgb.get('b')
  r_scale.set(red)
  g_scale.set(green)
  b_scale.set(blue)
  canvas.config(bg="#%02x%02x%02x" % (red, green, blue))
  
def r_sel(val):
  print "r_sel(" + str(val) + ")"
  selection = "R = " + str(r_var.get())
  r_label.config(text = selection)
  updateHSV()
  
  
def g_sel(val):
  print "g_sel(" + str(val) + ")"
  selection = "G = " + str(g_var.get())
  g_label.config(text = selection)
  updateHSV()
  
def b_sel(val):
  print "b_sel(" + str(val) + ")"
  selection = "B = " + str(b_var.get())
  b_label.config(text = selection)
  updateHSV()
  
def h_sel(val):
  print "h_sel(" + str(val) + ")"
  selection = "H = " + str(h_var.get())
  h_label.config(text = selection)
  updateRGB()

def s_sel(val):
  print "s_sel(" + str(val) + ")"
  selection = "S = " + str(s_var.get())
  s_label.config(text = selection)
  updateRGB()
  
def v_sel(val):
  print "v_sel(" + str(val) + ")"
  selection = "V = " + str(v_var.get())
  v_label.config(text = selection)
  updateRGB()
  
tk = Tk()
tk.wm_title("Colour Demo")

canvas = Canvas(width=400, height=300, bg="#%02x%02x%02x" % (0, 0, 0))
canvas.pack()

rgbFrame = LabelFrame(tk, text="RGB")
rgbFrame.pack(fill="both", expand="yes")

r_var = IntVar()
r_scale = Scale(rgbFrame, variable = r_var, from_=0, to=255, showvalue=0, orient=HORIZONTAL, command=r_sel)
r_scale.pack()
r_label = Label(rgbFrame)
r_label.pack()

g_var = IntVar()
g_scale = Scale(rgbFrame, variable = g_var, from_=0, to=255, showvalue=0, orient=HORIZONTAL, command=g_sel)
g_scale.pack()
g_label = Label(rgbFrame)
g_label.pack()

b_var = IntVar()
b_scale = Scale(rgbFrame, variable = b_var, from_=0, to=255, showvalue=0, orient=HORIZONTAL, command=b_sel)
b_scale.pack()
b_label = Label(rgbFrame)
b_label.pack()

hsvFrame = LabelFrame(tk, text="HSV")
hsvFrame.pack(fill="both", expand="yes")

h_var = IntVar()
h_scale = Scale(hsvFrame, variable = h_var, from_=0, to=360, showvalue=0, orient=HORIZONTAL, command=h_sel)
h_scale.pack()
h_label = Label(hsvFrame)
h_label.pack()

s_var = IntVar()
s_scale = Scale(hsvFrame, variable = s_var, from_=0, to=100, showvalue=0, orient=HORIZONTAL, command=s_sel)
s_scale.pack()
s_label = Label(hsvFrame)
s_label.pack()

v_var = IntVar()
v_scale = Scale(hsvFrame, variable = v_var, from_=0, to=100, showvalue=0, orient=HORIZONTAL, command=v_sel)
v_scale.pack()
v_label = Label(hsvFrame)
v_label.pack()

#################### END GUI COMPONENTS ########################################

def main():
  # TEST VALUE: mint-green:
  # red, green, blue: 36, 174, 133
  # HSL: 108, 158, 99
  # HSV: 162, 79, 68
  print "Start of main()" 
  
  red = 36
  green = 174
  blue = 133
  hue = 162
  saturation = 79
  value = 68
  
  R = from8bit(red)
  G = from8bit(green)
  B = from8bit(blue)
  
  print "INPUT red, green, blue: " + str(red) + ", " + str(green) + ", " + str(blue)
  print "INPUT hue, saturation, value: " + str(hue) + ", " + str(saturation) + ", " + str(value)
  
  hsv = rgb2hsv(R, G, B)
  h = hsv.get('h')
  s = hsv.get('s')
  v = hsv.get('v')
  
  print "hsv: " + str(h) + ", " + str(s) + ", " + str(v)

  H = fromDegrees(hue)
  S = fromPercentage(saturation)
  V = fromPercentage(value)
  
  rgb = hsv2rgb(H, S, V)
  r = rgb.get('r')
  g = rgb.get('g')
  b = rgb.get('b')
  
  print "rgb: " + str(r) + ", " + str(g) + ", " + str(b)
  
  init(red, green, blue)  
  tk.mainloop()
  
# Specifies name of main function.
if __name__ == "__main__":
    sys.exit(main())
    