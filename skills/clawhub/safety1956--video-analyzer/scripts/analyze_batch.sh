#!/data/data/com.termux/files/usr/bin/bash
# Batch video analyzer - process multiple videos and extract metadata
# Usage: analyze_batch.sh <input_path> [output_dir]
# input_path can be a single file or directory

set -e

INPUT_PATH="$1"
OUTPUT_BASE="${2:-${TMPDIR:-/data/data/com.termux/files/usr/tmp}/video_analysis}"

if [ -z "$INPUT_PATH" ]; then
    echo "Usage: analyze_batch.sh <video_file|directory> [output_dir]"
    exit 1
fi

mkdir -p "$OUTPUT_BASE"

# Collect video files
declare -a VIDEO_FILES
if [ -f "$INPUT_PATH" ]; then
    VIDEO_FILES=("$INPUT_PATH")
elif [ -d "$INPUT_PATH" ]; then
    while IFS= read -r -d '' file; do
        VIDEO_FILES+=("$file")
    done < <(find "$INPUT_PATH" -type f \( -iname "*.mp4" -o -iname "*.mov" -o -iname "*.avi" -o -iname "*.mkv" \) -print0)
else
    echo "Error: Input path does not exist: $INPUT_PATH"
    exit 1
fi

if [ ${#VIDEO_FILES[@]} -eq 0 ]; then
    echo "No video files found in: $INPUT_PATH"
    exit 1
fi

echo "Found ${#VIDEO_FILES[@]} video(s) to analyze"
echo ""

# Process each video
for video in "${VIDEO_FILES[@]}"; do
    filename=$(basename "$video")
    video_name="${filename%.*}"
    video_dir="$OUTPUT_BASE/$video_name"
    
    echo "=== Processing: $filename ==="
    mkdir -p "$video_dir"
    
    # Extract metadata
    duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$video" 2>/dev/null | cut -d. -f1)
    resolution=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$video" 2>/dev/null | sed 's/x$//')
    codec=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 "$video" 2>/dev/null)
    size=$(du -h "$video" | cut -f1)
    
    # Convert duration to mm:ss
    if [ -n "$duration" ] && [ "$duration" -gt 0 ]; then
        minutes=$((duration / 60))
        seconds=$((duration % 60))
        duration_fmt=$(printf "%02d:%02d" $minutes $seconds)
    else
        duration_fmt="unknown"
    fi
    
    # Write metadata
    cat > "$video_dir/metadata.txt" << EOF
File: $filename
Duration: $duration_fmt
Resolution: $resolution
Codec: $codec
Size: $size
Path: $video
EOF
    
    echo "Duration: $duration_fmt | Resolution: $resolution | Size: $size"
    
    # Extract frames based on duration
    if [ -z "$duration" ] || [ "$duration" -lt 30 ]; then
        interval=1
        max_frames=30
    elif [ "$duration" -lt 300 ]; then
        interval=5
        max_frames=60
    else
        interval=15
        max_frames=40
    fi
    
    ffmpeg -i "$video" -vf "fps=1/$interval" -q:v 2 -frames:v "$max_frames" "$video_dir/frame_%03d.jpg" -y 2>/dev/null
    
    frame_count=$(ls -1 "$video_dir"/frame_*.jpg 2>/dev/null | wc -l)
    echo "Extracted $frame_count frames to $video_dir/"
    
    # List frames for analysis
    ls -1 "$video_dir"/frame_*.jpg | head -10
    
    echo ""
done

echo "=== Summary ==="
echo "Processed ${#VIDEO_FILES[@]} video(s)"
echo "Output directory: $OUTPUT_BASE"
echo ""
echo "Next steps:"
echo "1. Pick 3-5 evenly spaced frames from each video"
echo "2. Use the image tool to analyze them"
echo "3. Generate a summary report"
