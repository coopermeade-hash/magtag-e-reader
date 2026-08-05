from adafruit_magtag.magtag import MagTag
 
import reader

magtag = MagTag()

#Note constants
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494

magtag.peripherals.play_tone(NOTE_C4, 0.25)
magtag.peripherals.play_tone(NOTE_E4, 0.25)
magtag.peripherals.play_tone(NOTE_G4, 0.25)

def voltage_to_percentage(voltage):
    # Rough estimation for a 3.7V LiPo (4.2V = 100%, 3.3V = 0%)
    if voltage >= 4.2:
        return 100
    elif voltage <= 3.3:
        return 0
    else:
        return int((voltage - 3.3) / (4.2 - 3.3) * 100)

#gets the voltage and changes it to a percentage.
battery_percentage = voltage_to_percentage(magtag.peripherals.battery)

#Add the text which will be displayed.
magtag.add_text(
    text_anchor_point = (0, 0),
    text_scale=1,
)

START_TEXT = f"""Welcome to the E-reader Mk 1.0!
Current Programs:
Left: E-reader
Up: Play '21'
Down: N/a
Right: N/a
Battery: {battery_percentage}%
(PRESS ARROWS TO START PROGRAM)
"""

def main():
    magtag.set_text(START_TEXT)
    # main loop
    while True:

        if magtag.peripherals.button_a_pressed: #LEFT
            reader.main(magtag)
        if magtag.peripherals.button_b_pressed: #UP
            pass
            
        if magtag.peripherals.button_c_pressed: #DOWN
            pass
        if magtag.peripherals.button_d_pressed: #RIGHT
            pass
        

main()

