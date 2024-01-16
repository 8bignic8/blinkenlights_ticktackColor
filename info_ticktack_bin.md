# This is a smal explonation of how to create a .bin file for the tictac RGB led matrix. 

the wiki is here: 

So every Light is listed in the bin in columns in RGB so what does that mean?

If you have a row of 18 RGB LEDS
and columns of 8 RGB Leds it is encoded as

in this Example the Matrix is x 18 (left to right) leds and y(top to bottom) 8

This code example will show how the colors are mapped in the LED matrix
```
First(1) Row: 1R2R3R4R5R6R7R8R1G2G3G4G5G6G7G8G1B2B3B4B5B6B7B8B
```

Important the LED´s brightness will be between 0-7 and 7 is full on.
Also a two time valuese in Hex are required, see example for more infos.

So if you want to tun the first LED to a white for 1second, it will look like: 

```
One second(delete the space in the bin file!), followed by the color in R G B in HEX
0300 070000000000000007000000000000000700000000000000
```

If you want to turn on the rest of the LED´s you can just fill in the missing bits you want in the color brightness you want e.g.

Example one Frame
```
0300 
```