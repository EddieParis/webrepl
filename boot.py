import gc
import webrepl

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("{ssid}", "{passwd}")
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

webrepl.start()

do_connect()
gc.collect()

###END###
