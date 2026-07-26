#!/data/data/com.termux/files/usr/bin/bash
set -euo pipefail

video="$1"
output_dir="$2"
duration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$video" 2>/dev/null | cut -d. -f1)

if [ "$duration" -lt 30 ]; then
    interval=1
    max_frames=30
elif [ "$duration" -lt 300 ]; then
    interval=5
    max_frames=60
else
    interval=15
    max_frames=40
fi

mkdir -p "$output_dir"
ffmpeg -i "$video" -vf "fps=1/$interval" -q:v 2 -frames:v "$max_frames" "$output_dir/frame_%03d.jpg" -y 2>/dev/null

ls -1 "$output_dir"/frame_*.jpg