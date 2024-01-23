import cv2 as cv
from colormap import rgb2hex
import xml.etree.ElementTree as ET
import datetime
import argparse
import glob
import os

# Open an image
def currentdate():
   return datetime.datetime.now().strftime("%d%m%Y")

def set2hex(set = None):
    return rgb2hex(r=(set[0]),g=(set[1]),b=(set[2])).split('#')[1]

def create_content_xml(root, img, duration= str(1000)):
    """_summary_

    Args:
        img (list, optional): _description_. Defaults to [].
    """
    # Create the frame element
    frame = ET.SubElement(root, "frame", duration=duration)

    for x in range(img.shape[0]):
        line = []
        for y in range(img.shape[1]):
            #print(set2hex(image[x,y]))
            line.append((set2hex(img[x,y])))
        row = ET.SubElement(frame, "row")    
        row.text = str(''.join(line))
    return root

    
def start_part_of_xml(width=None, height=None, bits=None, channels=None, creator=None, presetINFO="my preset is aout"):
    """Creating the Header of the xml

    Args:
        width (_type_, optional): _description_. Defaults to None.
        height (_type_, optional): _description_. Defaults to None.
        bits (_type_, optional): _description_. Defaults to None.
        channels (_type_, optional): _description_. Defaults to None.
        creator (_type_, optional): _description_. Defaults to None.
        presetINFO (str, optional): _description_. Defaults to "my preset is aout".

    Returns:
        _type_: _description_
    """
    root = ET.Element("blm", width=width, height=height, bits=bits, channels=channels)

    # Create the header element
    header = ET.SubElement(root, "header")

    # Add description elements to the header
    descriptions = ["Creator: "+creator, "Update: "+currentdate(), "Additional_info: "+presetINFO]

    for description_text in descriptions:
        description = ET.SubElement(header, "description")
        description.text = description_text

    return root

def finish_and_write_xml(root, filename = "test" ):
    tree = ET.ElementTree(root)
    print(tree)
    # Write the XML to a file
    with open(str(currentdate())+"_"+filename+".bml", "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)
    print('writing xml, \n done')

def readimg(path):
    """read one img and convert it to RGB

    Args:
        path (string): path to the variable

    Returns:
        CV2: Reaturns the Image in the cv2 format in RGB
    """
    return cv.cvtColor(cv.imread(path), cv.COLOR_BGR2RGB)


if __name__ == "__main__":

    ## parser part
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--folder", 
        type=str,
        default="./pic",
        help="The path to the pictures, \n can be one")
    parser.add_argument(
        "--type", 
        type=str, 
        default="png",
        help="The picture type to convert,\n allowed are png, jpg")
    parser.add_argument(
        "--width", 
        type=int, 
        default=18,
        help="The pictures length")
    parser.add_argument(
        "--height", 
        type=int, 
        default=8,
        help="The pictures hight")
    parser.add_argument(
        "--channels", 
        type=int, 
        default=3,
        help="The picture color channels \n can be 1 or 3(default)")
    parser.add_argument(
        "--dim", 
        type=int, 
        default=0,
        help="The picture dimming value, 0 for noone")
    parser.add_argument(
        "--bml", 
        type=str, 
        default="movie",
        help="The filename for the .bml file")
    args = parser.parse_args()

    img_folder = glob.glob(os.path.join(args.folder,'*.'+args.type))
    #print(img_folder)
    root = start_part_of_xml(
        width="18", 
        height="8", 
        bits="8", 
        channels="3", 
        creator="noneInfo", 
        presetINFO="my preset is aout")
    
    for img in img_folder: 
        try:
            #print(readimg(img))
            root = create_content_xml(
                root=root, 
                img=readimg(img), 
                duration=str(1000))
        except: 
            print("exiting, wrong datatype")
            exit()
        
    finish_and_write_xml(
        root, 
        filename=args.bml)
    
## TODO 
## add dimming by multpyling a factor to the rgb values and than calculate the hex values