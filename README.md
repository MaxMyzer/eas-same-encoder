# Emergency Alert System (EAS) Specific Area Message Encoding (SAME) Encoder

During this Era of Our Perpetual 2020 COVID-Themed Lockdown, I assumed there'd be a bunch of emergency broadcasts sent over the FM airwaves giving us further
directions, so I did what any responsible emergency-obsessed turbonerd would do and purchased a SAGE Alerting Systems EAS ENDEC (Encoder/Decoder).

[Here's a quick background on how EAS SAME headers work.](https://www.youtube.com/watch?v=Z5o1sfXXf9E)

During the late 90's / early 2000's, this is a device that would sit in the headend room of TV / FM / AM stations, listen for EAS SAME signals on neighboring
stations, and, if the specified information matched the predefined filters, rebroadcast the emergency message on its local station.

Anyway, since I'm trying to flex my coding skills right now, I wrote a Python script that generates these tones!  Tested and is correctly interpreted by my SAGE
EAS ENDEC.

[YouTube demo!](https://www.youtube.com/watch?v=OVxHkMDX2F8)

# Important Note

Please please please please PLEASE use this responsibly.  Did you just buy an old ENDEC on eBay and want to put it through its paces?  This is the script for you!

Don't use this to hack / exploit anything.  I made this for funsies in a few hours.  Please use it accordingly.

# USAGE
[More about these perameters](https://en.wikipedia.org/wiki/Specific_Area_Message_Encoding#Header_format).
For a more condenced version, check out [the readme of the dsame repo](https://github.com/cuppa-joe/dsame/blob/master/README.md)
| --Argument      | -A   | Default  | Example | Function                                                             |
|-----------------|------|----------|---------|----------------------------------------------------------------------|
| --playaudiolive | -pal | -1       | 1       | Plays audio with command. Warning: Loud.                             |
| --code          | -c   |          |         | If you wanted to copy and paste a code string, you can do that here. |
| --org           | -o   | WXR      | PEP     | The organization in the SAME code                                    |
| --event         | -e   | RWT      | TOR     | The event type                                                       |
| --location      | -lo  |          |         | To paste an entire string of location codes, use this                |
| --location00    | -l00 | 000000   |         | A location code                                                      |
| --location**    | -l** |          |         | ** when between 01 and 30 are additional location codes              |
| --time          | -t   | 0015     |         | How long the duration is.                                            |
| --callsign      | -cs  | KEAX/NWS |         | Callsign of station broadcasting                                     |

# Self-activating
On may weather radios you can do something called self-activate, where you essentially feed your own audio instead of the radio audio into it. DO NOT transmit on the weather radio frequencies! A few notes: Make sure your radio is on channel 2. If it isn't working, adjust your volume until it sounds clear through the radio. If it still isn't working, change your SAME settings to any. The best way to do this is to have a mono 3.5mm jack to a single RCA connector. Plug the 3.5mm into your headphone jack and the RCA into the external antenna jack. There are a lot of other ways to do this with the PC port and the Ext. Alert port, but this seems to be the least work. Note: I have yet to test this.
