# Emergency Alert System (EAS) Specific Area Message Encoding (SAME) Encoder

## Important Note

Please please please please PLEASE use this responsibly.  Did you just buy an old ENDEC on eBay and want to put it through its paces?  This is the script for you!

Don't use this to hack / exploit anything.  I made this for funsies in a few hours.  Please use it accordingly.

## Installation
To Run: `python3 <location of same.py> <args>`

  OR: `cd <directory of git folder>` THEN `python3 same.py <args>`

Install:
  Download this repo and unzip (You only actually need [same.py](https://raw.githubusercontent.com/MaxMyzer/eas-same-encoder/master/same.py), you can just download that if you want)

Install Python3
  - Windows: `python3` then install from Microsoft Store.
  - Linux and MacOS: `sudo apt update && sudo apt-get install python3`

Install dependencies: Single command version: `pip3 install --upgrade pip && pip3 install numpy && pip3 install scipy`
  - `pip3 install --upgrade pip`
  - `pip3 install <dependency>`
     -  numpy
     -  scipy
 You should now be ready to run it.

## USAGE
[More about these perameters](https://en.wikipedia.org/wiki/Specific_Area_Message_Encoding#Header_format).
For a more condenced version, check out [the readme of the dsame repo](https://github.com/cuppa-joe/dsame/blob/master/README.md)
| --Argument      | -A   | Default  | Example | Function                                                             |
|-----------------|------|----------|---------|----------------------------------------------------------------------|
| --playaudiolive | -pal | -1       | 1       | Plays audio with command. Warning: Loud.                             |
---|
| --attention | -as | 0       | 1       | 1 = single tone (1050hz), 2 = duel tone (853hz and 960hz)                             |
---|
| --attentionlength | -al | 8       | 1       | How many seconds to play the attention signal                          |
| --code          | -c   |          |         | If you wanted to copy and paste a code string, you can do that here. |
| --org           | -o   | WXR      | PEP     | The organization in the SAME code                                    |
| --event         | -e   | RWT      | TOR     | The event type                                                       |
| --location      | -lo  |          |         | To paste an entire string of location codes, use this                |
| --location00    | -l00 | 000000   |         | A location code                                                      |
| --location**    | -l** |          |         | ** when between 01 and 30 are additional location codes              |
| --time          | -t   | 0015     |         | How long the duration is.                                            |
| --callsign      | -cs  | KEAX/NWS |         | Callsign of station broadcasting                                     |

## Self-activating
On may weather radios you can do something called self-activate, where you essentially feed your own audio instead of the radio audio into it. DO NOT transmit on the weather radio frequencies! A few notes: Make sure your radio is on channel 2. If it isn't working, adjust your volume until it sounds clear through the radio. If it still isn't working, change your SAME settings to any. The best way to do this is to have a mono 3.5mm jack to a single RCA connector. Plug the 3.5mm into your headphone jack and the RCA into the external antenna jack. There are a lot of other ways to do this with the PC port and the Ext. Alert port, but this seems to be the least work. Note: I have yet to test this.

## A note to creators:
This is a good way to do cool things. I can see it being used in EAS scenerios and other cool projects.
IF you use this for use in projects (eg; videos), I would appreciate credit via a link in description. 
I have seen a lot of similar things that only work on some platforms, so when I finally found something close to what I wanted in python, I forked it so I could improve on it. I just don't want others to have to have to search for hours to find how to do this kind of thing after seeing it in a video. I'm not going to do anything if you don't include a credit. I didn't write the code this is based on, and the specifcations are government documents. I just think that many people would appreciate knowing how to do what you did.
