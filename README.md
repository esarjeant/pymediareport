pymediareport
=============
Implements bulk filtering of directories to determine if any video media matches
specified criteria.

For example, to locate all movies that have stereo only soundtracks:

     pymediareport.py --find_stereo_only --recursive /mnt/movies
     
Where `/mnt/movies` is your top-level directory with one or more sub-directories 
containing video material.
 
The following flags are currently available:

`--find_stereo_only` to locate video files that only have stereo soundtracks

`--find_single_audio_only` to locate video files that only have a single audio stream

`--find_fullscreen` to locate video files that are in fullscreen (4:3) aspect ratio

`--find_low_bit_rate` to locate video files that are lower bitrate and therefore likely lower quality

Some of these can be used cumulatively; for example you may filter for stereo only
as well as single audio which should identify videos that only have a single AAC audio
stream.

Note that this currently depends on a fork of ffprobe3 which me be found here:

https://github.com/esarjeant/ffprobe3
 
You will need to install ffprobe to use this wrapper. 