# https://stackoverflow.com/questions/46789053/python3-tkinter-analog-gauge
import tkinter as tk
from math import pi, cos, sin


class Meter(tk.Frame):
    def __init__(self, master=None, **kw):
        tk.Frame.__init__(self, master, **kw)

        self.meter = []
        self.angle = []
        self.var = tk.IntVar(self, 0)

        self.canvas = tk.Canvas(self, width=200, height=110,
                                borderwidth=2, relief='sunken',
                                bg='white')
        self.scale = tk.Scale(self, orient='horizontal', from_=0, to=100, variable=self.var)

        for j, i in enumerate(range(0, 100, 5)):
            self.meter.append(self.canvas.create_line(100, 100, 10, 100,
                                                      fill='grey%i' % i,
                                                      width=3,
                                                      arrow='last'))
            self.angle.append(0)
            self.canvas.lower(self.meter[j])
            self.updateMeterLine(0.2, j)

        self.canvas.create_arc(10, 10, 190, 190, extent=108, start=36,
                               style='arc', outline='red')

        self.canvas.pack(fill='both')
        self.scale.pack()

        self.var.trace_add('write', self.updateMeter)  # if this line raises an error, change it to the old way of adding a trace: self.var.trace('w', self.updateMeter)
        self.updateMeterTimer()

    def updateMeterLine(self, a, l=0):
        """Draw a meter line (and recurse for lighter ones...)"""
        oldangle = self.angle[l]
        self.angle[l] = a
        x = 100 - 90 * cos(a * pi)
        y = 100 - 90 * sin(a * pi)
        self.canvas.coords(self.meter[l], 100, 100, x, y)
        l += 1
        if l < len(self.meter):
            self.updateMeterLine(oldangle, l)

    def updateMeter(self, name1, name2, op):
        """Convert variable to angle on trace"""
        mini = self.scale.cget('from')
        maxi = self.scale.cget('to')
        pos = (self.var.get() - mini) / (maxi - mini)
        self.updateMeterLine(pos * 0.6 + 0.2)

    def updateMeterTimer(self):
        """Fade over time"""
        self.var.set(self.var.get())
        self.after(20, self.updateMeterTimer)


if __name__ == '__main__':
    root = tk.Tk()
    meter = Meter(root)
    meter.pack()
    root.mainloop()