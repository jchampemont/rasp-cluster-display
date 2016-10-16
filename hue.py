#!/usr/bin/env python

import fn
import ConfigParser
import colorsys
import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as touch
import math
import time

# Initializing...
i = 0
update_display = True
lcd.clear()
backlight.set_graph(0)
fns = [fn.ip_address, fn.load_average, fn.uptime]
fn_n = 0;
backlight_state = True

Config = ConfigParser.ConfigParser()
Config.read("nodes.ini")
nodes = Config.sections()
node = 0

@touch.on(touch.LEFT)
def left(channel, event):
    global fn_n, update_display
    fn_n = (fn_n - 1) % len(fns)
    update_display = True

@touch.on(touch.RIGHT)
def right(channel, event):
    global fn_n, update_display
    fn_n = (fn_n + 1) % len(fns)
    update_display = True

@touch.on(touch.BUTTON)
def toggle_backlight(channel, event):
    global backlight_state
    if backlight_state:
        backlight.off()
        backlight_state = False
    else:
        backlight_state = True

@touch.on(touch.UP)
def up(channel, event):
    global node, update_display
    node = (node - 1) % len(nodes)
    update_display = True

@touch.on(touch.DOWN)
def down(channel, event):
    global node, update_display
    node = (node + 1) % len(nodes)
    update_display = True

# Main Loop
while True:
    if backlight_state:
        backlight.sweep((i % 360) / 360.0)
    time.sleep(0.01)
    fns[fn_n](nodes[node], i, lcd, update_display, Config.get(nodes[node], "interfaces").split(","))
    update_display = False
    i += 1
