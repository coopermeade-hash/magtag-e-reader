
SECTIONS = []
"""
ORIGINAL FUNCTION

def format_text(file_path, CHUNK_SIZE = 45):
    text = ""
    #reads the file
    with open(file_path, "r") as f:
        text = f.read()
    #Takes text and chops it up into chunk_size lines
    LINES = []
    new_line = ""
    current_characters_in_line = 0

    for character in text: #Less efficent, but needed for finer control.
        new_line += character
        current_characters_in_line += 1
        if current_characters_in_line >= CHUNK_SIZE: #Wrap if text greater than chunk size.
            LINES.append(new_line + "\n")
            current_characters_in_line = 0
        elif character == "\n": #if a new line, stop the current_line
            LINES.append(new_line)
            current_characters_in_line = 0
            
        
    #Takes evrey lines and stiches them into 8 line sections.
    chunks = []
    new_chunk = ""
    for i in range(0, len(LINES)):
        
        
        new_chunk += lines + "\n"
        if i % 8 == 7:
            chunks.append(new_chunk)
            new_chunk = ""
    #adding any remants from the stitching process.
    if new_chunk != "":
        chunks.append(new_chunk)
    
    return chunks
"""

## Note: This was taken from Google's AI as I had trouble with memory limitations.
## I used the original function above as the input for the prompt.
def format_text(file_path, chunk_size=45):
    """
    Memory-efficient text formatter. 
    Streams the file sequentially instead of loading it entirely into RAM.
    """
    chunks = []
    with open(file_path, "r", encoding="utf-8") as f:
        current_line = []
        line_count = 0
        current_chunk = []

        while True:
            char = f.read(1)  # Read exactly 1 character at a time
            if not char:      # End of file reached
                break

            current_line.append(char)
            
            # Check for chunk size limits or existing newlines
            if len(current_line) >= chunk_size:
                current_chunk.append("".join(current_line) + "\n")
                current_line = []
                line_count += 1
            elif char == "\n":
                current_chunk.append("".join(current_line))
                current_line = []
                line_count += 1

            # If we hit an 8-line section, yield it immediately
            if line_count == 8:
                chunks.append("".join(current_chunk))
                current_chunk = []
                line_count = 0

        # Handle remaining text inside the active line
        if current_line:
            current_chunk.append("".join(current_line))
            line_count += 1

        # Handle remaining lines inside the active chunk
        if current_chunk:
            chunks.append("".join(current_chunk))
    return chunks
        


def main(magtag, FILE_PATH = "reader_texts\\lorem.txt"):
    magtag.set_text("The text is loading. This may take a while...")

    SECTIONS = format_text(FILE_PATH)

    current_section = 0
    
    magtag.set_text(SECTIONS[current_section] + f"{current_section + 1} / {len(SECTIONS)}")

    while True:
        
        if magtag.peripherals.button_a_pressed: #LEFT
            current_section = 0 #Set the text to the first section
            section_text = SECTIONS[current_section] + f"{current_section + 1} / {len(SECTIONS)}"
            magtag.set_text(section_text)            

        if magtag.peripherals.button_b_pressed: #UP
            #Go back one section
            current_section = max(current_section - 1, 0)
            section_text = SECTIONS[current_section] + f"{current_section + 1} / {len(SECTIONS)}"
            magtag.set_text(section_text)

        if magtag.peripherals.button_c_pressed: #DOWN
            #Go forward one section
            current_section = min(current_section + 1, len(SECTIONS) - 1)
            section_text = SECTIONS[current_section] + f"{current_section + 1} / {len(SECTIONS)}"
            magtag.set_text(section_text)

        if magtag.peripherals.button_d_pressed: #RIGHT
            #Go to the last section.
            current_section = len(SECTIONS) - 1
            section_text = SECTIONS[current_section] + f"{current_section + 1} / {len(SECTIONS)}"
            magtag.set_text(section_text)
