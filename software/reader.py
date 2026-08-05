import os

SECTIONS = []


def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def format_text(DATA):
  new_section = ""
  new_line = ""
  i = 0
  j = 0

  
  for char in DATA:
    #Evrey 45 characters, start a new line
    if i == 45:
      new_section += new_line + "\n"
      #Increase line count
      j += 1
      #Evrey 9 lines, start a new section.
      if j == 8:
        SECTIONS.append(new_section)
        new_section = ""
        j = 0
        
      i = 0
      new_line = ""
    #Reset line count if there is a new line natrualy.
    if char == "\n":
      i = 0
      j += 1
    new_line += char
    i += 1
    


def main(magtag, FILE_PATH = "reader_texts\\lorem.txt"):
    FILE = open(FILE_PATH)
    DATA = FILE.read()
    FILE.close()

    format_text(DATA)

    current_section = 0

    magtag.set_text(SECTIONS[current_section] + f"{current_section + 1} / {len(SECTIONS)}")

    while True:
        section_text = SECTIONS[current_section] + f"{current_section + 1} / {len(SECTIONS)}"
        if magtag.peripherals.button_a_pressed: #LEFT
            current_section = 0 #Set the text to the first section
            magtag.set_text(section_text)            

        if magtag.peripherals.button_b_pressed: #UP
            #Go back one section
            current_section = max(current_section - 1, 0) 
            magtag.set_text(section_text)

        if magtag.peripherals.button_c_pressed: #DOWN
            #Go forward one section
            current_section = min(current_section + 1, len(SECTIONS) - 1)
            magtag.set_text(section_text)

        if magtag.peripherals.button_d_pressed: #RIGHT
            #Go to the last section.
            current_section = len(SECTIONS) - 1
            magtag.set_text(section_text)

