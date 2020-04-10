import RPi.GPIO as g
import time

g.setmode(g.Board)
g.setup(7, g.OUT)
global GIVE_WEIGHT
GIVE_WEIGHT = 0
import RPi.GPIO as g
def load_cell():
    EMULATE_HX711=False

    referenceUnit = 1

    if not EMULATE_HX711:
        from hx711 import HX711
    else:
        from emulated_hx711 import HX711

    hx = HX711(29, 31)

    hx.set_reading_format("MSB", "MSB")

    hx.set_reference_unit(referenceUnit)

    hx.reset()

    hx.tare()

    print("Tare done! Add weight now...")
    val = hx.get_weight(5)
    print(val)
    hx.power_down()
    hx.power_up()
    time.sleep(0.1)
    return val
    
global GIVE_WEIGHT
while True:
	curr_weight = load_cell()
	if (curr_weight < GIVE_WEIGHT):
		g.output(7, g.HIGH)
	else:
		g.output(7, g.LOW)
		break
