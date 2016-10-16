import client
import os

def line(lcd, i):
    lcd.set_cursor_position(0,i)

def hostname(node, lcd):
    line(lcd, 0)
    lcd.write("H: " + client.get_hostname(node))

def ip_address(node, i, lcd, update_display, interfaces):
    if i % 1000 == 0 or update_display:
        lcd.clear()
        hostname(node, lcd)
        line(lcd, 1)
        lcd.write("IP: " + client.get_ip_address(node, interfaces[0]))
        if len(interfaces) == 2:
            line(lcd, 2)
            lcd.write("IP: " + client.get_ip_address(node, interfaces[1]))

def load_average(node, i, lcd, update_display, useless):
    if i % 100 == 0 or update_display:
        lcd.clear()
        hostname(node, lcd)
        line(lcd, 1)
        lcd.write(" Load averages:")
        line(lcd, 2)
        lcd.write(client.get_load_averages(node))

def uptime(node, i, lcd, update_display, useless):
    if i % 100 == 0 or update_display:
        lcd.clear()
        hostname(node, lcd)
        line(lcd, 1)
        lcd.write("Uptime:")
        line(lcd, 2)
        lcd.write(client.uptime(node))
