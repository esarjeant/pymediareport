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

parser = argparse.ArgumentParser(description='pyMediareport video file filter utility')
parser.add_argument('path', metavar='directory', help='directory to check video files')
parser.add_argument('--extension', dest='extension', action='store', default="m4v", help='extension to search; common ones include m4v and mpg')
parser.add_argument('--recursive', dest='recursive', action='store_true', help='allow recursion into all sub-directories')
parser.add_argument('--find_stereo_only', dest='find_stereo_only', action='store_true', help='filter results that have stereo only')
parser.add_argument('--find_single_audio_only', dest='find_single_audio_only', action='store_true', help='filter results that have a single audio stream')

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

    if pass_filter:
        print(filename+" -> "+str(metadata))
