import cv2 as cv
from colormap import rgb2hex
import xml.etree.ElementTree as ET
import datetime
# Open an image


def currentdate():
   return datetime.datetime.now().strftime("%d%m%Y")

def set2hex(set = None):
    return rgb2hex(r=(set[0]),g=(set[1]),b=(set[2])).split('#')[1]

def createxml(img = None, filename ='idk', width="18", height="8", bits="8", channels="3", creator="noneInfo", presetINFO="my preset is aout"):
    """_summary_

    Args:
        width (str, optional): _description_. Defaults to "18".
        height (str, optional): _description_. Defaults to "8".
        bits (str, optional): _description_. Defaults to "8".
        channels (str, optional): _description_. Defaults to "3".
        creator (str, optional): _description_. Defaults to "noneInfo".
        presetINFO (str, optional): _description_. Defaults to "my preset is aout".
    """
    # Create the root element
    root = ET.Element("blm", width=width, height=height, bits=bits, channels=channels)

    # Create the header element
    header = ET.SubElement(root, "header")

    # Add description elements to the header
    descriptions = ["Creator: "+creator, "Update: "+currentdate(), "type3: info3"]

    for description_text in descriptions:
        description = ET.SubElement(header, "description")
        description.text = description_text

        # Create the frame element
    frame = ET.SubElement(root, "frame", duration="5000")

    for x in range(img.shape[0]):
        line = []
        for y in range(img.shape[1]):
            #print(set2hex(image[x,y]))
            line.append((set2hex(image[x,y])))
        row = ET.SubElement(frame, "row")    
        row.text = str(''.join(line))

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Write the XML to a file
    with open(filename+".bml", "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)

image = cv.imread("pixi.png")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
createxml(image)

## TODO 
## add dimming by multpyling a factor to the rgb values and than calculate the hex values