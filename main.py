import cv2
from colormap import rgb2hex
import xml.etree.ElementTree as ET
import datetime
import argparse
import glob
import os
from PIL import Image
import numpy


def sep_gif_frames(gif_path, nums = None):
    """_summary_

    Args:
        gif_path (str, optional): _description_. Defaults to 'blinkenlights_ticktackColor/pic/zoom_in.gif'.
        nums (int, optional): _description_. Defaults to 3.

    Returns:
        array of cv2: returns a array with all the frames
    """
# https://giphy.com/gifs/loop-trippy-3o7ZeODTGuQOeLr3l6
    
    img = Image.open(gif_path)
    returned_frames = []
    if nums == None:
        nums = img.n_frames

    with img as im:
        for i in range(nums):
            im.seek(int(im.n_frames // nums * i))
            open_cv_image = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
            returned_frames.append(open_cv_image)

    return returned_frames
    

# Open an image
def currentdate():
   return datetime.datetime.now().strftime("%H%M%S_%d%m%Y")

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
    #print(tree)
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
    return cv2.imread(path)

def dim_image(img, contrast=1, brightness = 0):
    """dimm your image(bgr) 

    Args:
        img (cv2): _description_
        contrast (int, optional): To get a darker result use 0.5 or smaler. Defaults to 1.
        brightness (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
    """
    return cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)


def parser():
        ## parser part
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--folder", 
        type=str,
        default="./pic",
        help="The path to the pictures, \n can be one picture")
    parser.add_argument(
        "--gifs", 
        type=str,
        default="None",
        help="The path one gif, \n need to be one")
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
        "--contrast", 
        type=float, 
        default=1.0,
        help="The picture dimming value from dark 0.0 to 2.0 all white, \n normal and default is 1.0")
    parser.add_argument(
        "--absoluteframes", 
        type=int, 
        default=0,
        help="Number of frames from the gif,\n default 0 for all")
    parser.add_argument(
        "--repeats", 
        type=int, 
        default=2,
        help="Number of repeats the gif runs before the next in the folder is played\n default 2")
    parser.add_argument(
        "--speed", 
        type=int, 
        default=500,
        help="Number of the frameduration in miliseconds \n change this to speed up(smaler number) or slow down the animation\n default 500 for 1second per frame \n 4ms for 25fps")
    parser.add_argument(
        "--bml", 
        type=str, 
        default="movie",
        help="The filename for the .bml file")
    parser.add_argument(
        "--info", 
        type=str, 
        default="my movie is about fun",
        help="The information about the created movie :)")
    parser.add_argument(
        "--username", 
        type=str, 
        default="dontWantToSay",
        help="Please tell me your name, \n gets saved in the files :)")
    return parser.parse_args()

# TODO make it for all the gives in a folder
# TODO make pip projekt
# TODO add better brightness controll
# TODO add text scroling support

if __name__ == "__main__":

    args = parser()

    img_folder = glob.glob(os.path.join(args.folder,'*.'+args.type))
    #print(img_folder)

    ## all are clled root because the underlying object ist changed not the var in on off itself
    root = start_part_of_xml(
        width=str(args.width), 
        height=str(args.height), 
        bits="8", 
        channels=str(args.channels), 
        creator=args.username, 
        presetINFO=args.info)
    
    is_gif = True # default to gif
    if args.gifs == "None":
        is_gif = False # changes to png folder
    
    if is_gif == True:
        for repeats in range(args.repeats):
            ## using the gif frames instead of the read png images
            frames = args.absoluteframes
            if frames ==  0: 
                frames = None
            for img in sep_gif_frames(
                args.gifs,
                frames):
                img = cv2.cvtColor(dim_image(img,args.contrast), cv2.COLOR_BGR2RGB)
                img = cv2.resize(img, (args.width, args.height)) # scale image to fit
                try:
                        #print(readimg(img))
                        root = create_content_xml(
                            root=root, 
                            img=img, 
                            duration=str(args.speed))
                except: 
                        print("exiting, wrong datatype or gif can not be read")
                        exit()

    else:
        for img in img_folder: 
            try:
                #print(readimg(img))
                root = create_content_xml(
                    root=root, 
                    img= cv2.resize(
                            cv2.cvtColor(
                                dim_image(
                                    readimg(img),
                                    args.contrast), 
                                    cv2.COLOR_BGR2RGB), 
                        (args.width, 
                         args.height)), 
                    duration=str(args.speed))
            except: 
                print("exiting, wrong datatype")
                exit()

    finish_and_write_xml(
        root, 
        filename=args.bml)

    
## TODO 
## add dimming by multpyling a factor to the rgb values and than calculate the hex values