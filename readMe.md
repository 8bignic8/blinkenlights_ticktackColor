# This is a smal explonation of how to create a .bin file for the blinkenlights tictac RGB led matrix. 

the wiki is here: https://wiki.blinkenarea.org/index.php/BlinkenPlus


# Code

how to use the Code: 

git clone this repo

```bash 
cd /blinkenligts_ticktackcolor
python3 main.py
# for more info use
python3 main.py -h
```
---
There is a parser now and you can call them by the attribute -h
```bash
python3 main.py -h
```
If you want to use gifs just use the glag --gifs folowed by the path to your gif as text in quotes'.

like:

```bash
python3 main.py --gifs '/myFiles/idk/funnyfail.gif'
```

---


So every Light is listed in the bin in columns in RGB so what does that mean?

If you have a row of 18 RGB LEDS
and columns of 8 RGB Leds it is encoded as

in this Example the Matrix is x 18 (left to right) leds and y(top to bottom) 8

This code example will show how the colors are mapped in the LED matrix
```
First(1) Row: 1R2R3R4R5R6R7R8R1G2G3G4G5G6G7G8G1B2B3B4B5B6B7B8B
```

# Important 
If you are using an mSD Card (fat16 or 32) you need to create a folder called: BP18X8.RGB

# .blm

> If you want to make a rgb picture in the blm format see:

see example_rgb.blm

The format for the ticktack RGB light should look like: 

RGB in two values in HEX from 00 to FF aka from 0 to 255 brightness

```xml
<?xml version="1.0" encoding="UTF-8"?>
<blm width="18" height="8" bits="8" channels="3">
	<header>
		<description>type1: info1</description>
		<description>type2: info2</description>
		<description>type2: info2</description>
	</header>

	<frame duration="100">
		<row>RRGGBB000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</row>
		<row>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</row>
		<row>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</row>
		<row>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</row>
		<row>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</row>
		<row>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</row>
		<row>000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</row>
		<row>0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FF</row>
	</frame>
</blm>

```

# .bin

the LED´s brightness will be between 0-7 and 7 is full on.
Also a two time valuese in Hex are required, see example for more infos.

So if you want to tun the first LED to a white for 1second, it will look like: 

```
One second(delete the space in the bin file!), followed by the color in R G B in HEX
0300 070000000000000007000000000000000700000000000000
```

If you want to turn on the rest of the LED´s you can just fill in the missing bits you want in the color brightness you want e.g.

Example one Frame 18(y)x8(x)x3(color)
```
30000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00070000 00000000 
```

# Contribute
If you want to contribute you can do so by sending merge requests setting um issues or giftig some money to my paypal.

Have a verry nice day :).