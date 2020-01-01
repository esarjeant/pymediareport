#!/usr/bin/env python
import glob
import argparse

from ffprobe3 import FFProbe

def is_stereo_only(metadata):

    has_stereo = False
    has_non_stereo = False

    for stream in metadata.streams:
        if stream.is_audio():
            if 2 == stream.channels():
                has_stereo = True

            if 2 != stream.channels():
                has_non_stereo = True

    return has_stereo and not has_non_stereo

def is_single_audio_only(metadata):

    audio_stream_count = 0

    for stream in metadata.streams:
        if stream.is_audio():
            audio_stream_count+=1

    return 1 == audio_stream_count

def is_fullscreen(metadata):

    for stream in metadata.streams:
        if stream.is_video():
            return stream.aspect_ratio() <= 1.339

    return False

def is_low_bit_rate(metadata, min_bit_rate):

    for stream in metadata.streams:
        if stream.is_video():
            return stream.bit_rate() <= min_bit_rate

    return True

parser = argparse.ArgumentParser(description='pyMediareport video file filter utility')
parser.add_argument('path', metavar='directory', help='directory to check video files')
parser.add_argument('--extension', dest='extension', action='store', default="m4v", help='extension to search; common ones include m4v and mpg')
parser.add_argument('--min_bit_rate', dest='min_bit_rate', action='store', default="500000", type=int, help='minimum bitrate for --find_low_bit_rate')
parser.add_argument('--recursive', dest='recursive', action='store_true', help='allow recursion into all sub-directories')
parser.add_argument('--verbose', dest='verbose', action='store_true', help='verbose output which includes media details')
parser.add_argument('--find_stereo_only', dest='find_stereo_only', action='store_true', help='filter results that have stereo only')
parser.add_argument('--find_single_audio_only', dest='find_single_audio_only', action='store_true', help='filter results that have a single audio stream')
parser.add_argument('--find_fullscreen', dest='find_fullscreen', action='store_true', help='filter results that are fullscreen aspect ratio')
parser.add_argument('--find_low_bit_rate', dest='find_low_bit_rate', action='store_true', help='filter results that are low bit rate')

args = parser.parse_args()

file_mask = "*."+args.extension

if args.recursive:
    file_mask = "**/*."+args.extension

print(f"Starting directory scan path={args.path} recursive={args.recursive} file_mask={file_mask}")

for filename in glob.iglob(args.path + file_mask, recursive=args.recursive):
    metadata=FFProbe(filename)

    pass_filter = True

    if args.find_stereo_only:
        pass_filter = is_stereo_only(metadata)

    if pass_filter and args.find_single_audio_only:
        pass_filter = is_single_audio_only(metadata)

    if pass_filter and args.find_fullscreen:
        pass_filter = is_fullscreen(metadata)

    if pass_filter and args.find_low_bit_rate:
        pass_filter = is_low_bit_rate(metadata, args.min_bit_rate)

    if pass_filter:
        if args.verbose:
            print(filename+" -> "+str(metadata))
        else:
            print(filename)
