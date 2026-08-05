#!/usr/bin/env python3
"""
Bilibili Video Parser — Full Pipeline Script
Usage: python3 bilibili_parser.py "https://www.bilibili.com/video/BV1q2RhB9EQC" [--output result.json] [--frames-dir ./frames] [--skip-download] [--skip-visual] [--skip-audio]

Stages:
  1. Extract metadata via Bilibili public API
  2. Check for subtitles
  3. Download video/audio streams and merge
  4a. Extract key frames and analyze with VLM
  4b. Extract audio, split, transcribe with ASR
  5. Synthesize all results into structured JSON
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import shutil
from datetime import datetime
from pathlib import Path


def run_cmd(args, timeout=60):
    """Run a command with argument list and return stdout."""
    result = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    if result.returncode != 0:
        print(f"[WARN] Command failed: {args}", file=sys.stderr)
        print(f"  stderr: {result.stderr[:200]}", file=sys.stderr)
    return result.stdout.strip()


def extract_bvid(url):
    """Extract BV number from various Bilibili URL formats."""
    # Handle b23.tv short URLs (would need redirect resolution — skip for now)
    match = re.search(r'(BV[\w]+)', url)
    if match:
        return match.group(1)
    raise ValueError(f"Cannot extract BV number from URL: {url}")


def get_metadata(bvid):
    """Stage 1: Get video metadata from Bilibili API."""
    print("[Stage 1] Fetching metadata...")
    raw = run_cmd([
        'curl', '-s', f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}',
        '-H', 'User-Agent: Mozilla/5.0'
    ])
    data = json.loads(raw)
    if data.get('code') != 0:
        raise RuntimeError(f"Bilibili API error: {data.get('message', 'unknown')}")

    info = data['data']
    metadata = {
        'bvid': info.get('bvid'),
        'aid': info.get('aid'),
        'cid': info.get('cid'),
        'title': info.get('title'),
        'author': info.get('owner', {}).get('name'),
        'author_mid': info.get('owner', {}).get('mid'),
        'duration_seconds': info.get('duration'),
        'views': info.get('stat', {}).get('view'),
        'likes': info.get('stat', {}).get('like'),
        'coins': info.get('stat', {}).get('coin'),
        'favorites': info.get('stat', {}).get('favorite'),
        'shares': info.get('stat', {}).get('share'),
        'danmaku': info.get('stat', {}).get('danmaku'),
        'description': info.get('desc'),
        'published_at': datetime.fromtimestamp(info.get('pubdate', 0)).strftime('%Y-%m-%d %H:%M:%S'),
    }
    print(f"  Title: {metadata['title']}")
    print(f"  Author: {metadata['author']}")
    print(f"  Duration: {metadata['duration_seconds']}s")
    return metadata


def get_subtitles(bvid, cid):
    """Stage 2: Check for available subtitles."""
    print("[Stage 2] Checking subtitles...")
    raw = run_cmd([
        'curl', '-s', f'https://api.bilibili.com/x/player/v2?bvid={bvid}&cid={cid}',
        '-H', 'User-Agent: Mozilla/5.0'
    ])
    data = json.loads(raw)
    subtitle_info = data.get('data', {}).get('subtitle', {})
    subtitles = subtitle_info.get('subtitles', [])

    if subtitles:
        print(f"  Found {len(subtitles)} subtitle track(s)")
        # Download first subtitle
        sub_url = subtitles[0].get('subtitle_url', '')
        if sub_url.startswith('//'):
            sub_url = 'https:' + sub_url
        sub_raw = run_cmd(['curl', '-s', sub_url])
        sub_data = json.loads(sub_raw)
        transcript = ' '.join([entry.get('content', '') for entry in sub_data.get('body', [])])
        print(f"  Subtitle text length: {len(transcript)} chars")
        return transcript
    else:
        print("  No subtitles available")
        return None


def download_streams(bvid, cid, work_dir, quality=16):
    """Stage 3: Download and merge video/audio streams."""
    print("[Stage 3] Downloading streams...")
    mp4_path = os.path.join(work_dir, 'video.mp4')

    # Get stream URLs
    raw = run_cmd([
        'curl', '-s',
        f'https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&qn={quality}&fnver=0&fnval=16&fourk=0',
        '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        '-H', 'Referer: https://www.bilibili.com'
    ])
    data = json.loads(raw)
    if data.get('code') != 0:
        raise RuntimeError(f"playurl API error: {data.get('message', 'unknown')}")

    dash = data['data'].get('dash', {})
    videos = dash.get('video', [])
    audios = dash.get('audio', [])

    if not videos or not audios:
        raise RuntimeError("No video/audio streams found")

    video_url = videos[0].get('baseUrl', videos[0].get('base_url', ''))
    audio_url = audios[0].get('baseUrl', audios[0].get('base_url', ''))

    # Download streams
    video_m4s = os.path.join(work_dir, 'video.m4s')
    audio_m4s = os.path.join(work_dir, 'audio.m4s')

    print("  Downloading video stream...")
    run_cmd([
        'curl', '-L', '-o', video_m4s, video_url,
        '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        '-H', 'Referer: https://www.bilibili.com'
    ], timeout=120)

    print("  Downloading audio stream...")
    run_cmd([
        'curl', '-L', '-o', audio_m4s, audio_url,
        '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        '-H', 'Referer: https://www.bilibili.com'
    ], timeout=120)

    # Merge
    print("  Merging video and audio...")
    run_cmd(['ffmpeg', '-i', video_m4s, '-i', audio_m4s, '-c', 'copy', mp4_path, '-y'], timeout=30)

    # Clean up m4s files
    os.remove(video_m4s)
    os.remove(audio_m4s)

    file_size = os.path.getsize(mp4_path) / (1024 * 1024)
    print(f"  Merged: {mp4_path} ({file_size:.1f} MB)")
    return mp4_path


def analyze_frames(mp4_path, work_dir, interval=5, sample_count=None):
    """Stage 4a: Extract key frames and analyze with VLM."""
    print(f"[Stage 4a] Extracting frames (every {interval}s)...")
    frames_dir = os.path.join(work_dir, 'frames')
    os.makedirs(frames_dir, exist_ok=True)

    # Extract frames
    run_cmd([
        'ffmpeg', '-i', mp4_path, '-vf', f'fps=1/{interval}', '-q:v', '2',
        f'{frames_dir}/frame_%03d.jpg', '-y'
    ], timeout=30)

    frame_files = sorted([f for f in os.listdir(frames_dir) if f.endswith('.jpg')])
    print(f"  Extracted {len(frame_files)} frames")

    # Sample frames if sample_count specified
    if sample_count and len(frame_files) > sample_count:
        step = len(frame_files) / sample_count
        indices = [int(i * step) for i in range(sample_count)]
        frame_files = [frame_files[i] for i in indices if i < len(frame_files)]
        print(f"  Sampled {len(frame_files)} frames for analysis")

    # Analyze with VLM
    print("  Analyzing frames with VLM...")
    visual_results = []
    for i, fname in enumerate(frame_files):
        fpath = os.path.join(frames_dir, fname)
        print(f"    Analyzing {fname}...")
        result = run_cmd([
            'z-ai', 'vision',
            '-p', '请用中文描述这张视频截图的内容，包括人物、场景、屏幕上的文字等所有细节',
            '-i', fpath
        ], timeout=60)
        # Parse VLM response
        try:
            vlm_data = json.loads(result)
            content = vlm_data.get('choices', [{}])[0].get('message', {}).get('content', '')
        except (json.JSONDecodeError, IndexError):
            content = result

        visual_results.append({
            'frame': fname,
            'description': content
        })

    return visual_results


def transcribe_audio(mp4_path, work_dir, chunk_seconds=25):
    """Stage 4b: Extract audio, split, and transcribe with ASR."""
    print("[Stage 4b] Transcribing audio...")
    audio_wav = os.path.join(work_dir, 'audio.wav')
    chunks_dir = os.path.join(work_dir, 'chunks')
    os.makedirs(chunks_dir, exist_ok=True)

    # Extract audio
    print("  Extracting audio...")
    run_cmd([
        'ffmpeg', '-i', mp4_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', audio_wav, '-y'
    ], timeout=30)

    # Split into chunks
    print(f"  Splitting into {chunk_seconds}s chunks...")
    run_cmd([
        'ffmpeg', '-i', audio_wav, '-f', 'segment', '-segment_time', str(chunk_seconds),
        '-c', 'copy', f'{chunks_dir}/chunk_%03d.wav', '-y'
    ], timeout=30)

    chunk_files = sorted([f for f in os.listdir(chunks_dir) if f.endswith('.wav')])
    print(f"  Split into {len(chunk_files)} chunks")

    # Transcribe each chunk
    print("  Transcribing chunks...")
    transcripts = []
    for i, fname in enumerate(chunk_files):
        fpath = os.path.join(chunks_dir, fname)
        out_path = os.path.join(chunks_dir, f'transcript_{fname.replace(".wav", ".json")}')

        result = run_cmd(['z-ai', 'asr', '-f', fpath, '-o', out_path], timeout=60)

        try:
            with open(out_path, 'r') as f:
                tdata = json.load(f)
                text = tdata.get('text', '')
        except (json.JSONDecodeError, FileNotFoundError):
            text = ''

        transcripts.append(text)
        if (i + 1) % 5 == 0 or i == len(chunk_files) - 1:
            print(f"    Transcribed {i + 1}/{len(chunk_files)} chunks")

    full_transcript = ' '.join(transcripts).strip()
    print(f"  Full transcript length: {len(full_transcript)} chars")
    return full_transcript


def synthesize(metadata, visual_results, transcript, subtitle_text=None):
    """Stage 5: Combine all results into structured output."""
    # Use subtitle text if ASR transcript is empty
    speech_text = transcript or subtitle_text or ""

    result = {
        'metadata': metadata,
        'visual_analysis': {
            'frames_analyzed': len(visual_results),
            'frame_descriptions': visual_results,
        },
        'speech': {
            'source': 'subtitle' if subtitle_text and not transcript else 'asr',
            'transcript': speech_text,
        },
        'parsed_at': datetime.now().isoformat(),
    }
    return result


def main():
    parser = argparse.ArgumentParser(description='Bilibili Video Parser')
    parser.add_argument('url', help='Bilibili video URL (e.g., https://www.bilibili.com/video/BV...)')
    parser.add_argument('--output', '-o', help='Output JSON file path')
    parser.add_argument('--work-dir', help='Working directory for temp files (default: auto temp dir)')
    parser.add_argument('--quality', type=int, default=16, help='Video quality qn value (default: 16=360p)')
    parser.add_argument('--frame-interval', type=int, default=5, help='Seconds between extracted frames (default: 5)')
    parser.add_argument('--sample-frames', type=int, default=None, help='Max number of frames to analyze with VLM')
    parser.add_argument('--skip-download', action='store_true', help='Skip stream download (metadata + subtitles only)')
    parser.add_argument('--skip-visual', action='store_true', help='Skip VLM frame analysis')
    parser.add_argument('--skip-audio', action='store_true', help='Skip ASR transcription')
    parser.add_argument('--keep-temp', action='store_true', help='Keep temporary files after processing')
    args = parser.parse_args()

    # Extract BV number
    bvid = extract_bvid(args.url)
    print(f"Bilibili Video Parser — BV: {bvid}\n")

    # Determine work directory
    if args.work_dir:
        work_dir = args.work_dir
        os.makedirs(work_dir, exist_ok=True)
        cleanup = False
    else:
        work_dir = tempfile.mkdtemp(prefix='bilibili_')
        cleanup = not args.keep_temp

    try:
        # Stage 1: Metadata
        metadata = get_metadata(bvid)

        # Stage 2: Subtitles
        subtitle_text = get_subtitles(bvid, metadata['cid'])

        # If we have subtitles and skip-download, we can finish early
        if args.skip_download:
            result = synthesize(metadata, [], "", subtitle_text)
            _output_result(result, args.output)
            return

        # Stage 3: Download
        mp4_path = download_streams(bvid, metadata['cid'], work_dir, args.quality)

        # Stage 4a: Visual analysis
        visual_results = []
        if not args.skip_visual:
            visual_results = analyze_frames(mp4_path, work_dir, args.frame_interval, args.sample_frames)

        # Stage 4b: Audio transcription
        transcript = ""
        if not args.skip_audio:
            # Skip ASR if we already have subtitles
            if subtitle_text:
                print("[Stage 4b] Skipping ASR — subtitles already available")
            else:
                transcript = transcribe_audio(mp4_path, work_dir)

        # Stage 5: Synthesize
        result = synthesize(metadata, visual_results, transcript or "", subtitle_text)

        _output_result(result, args.output)

    finally:
        if cleanup:
            print(f"\nCleaning up temp directory: {work_dir}")
            shutil.rmtree(work_dir, ignore_errors=True)


def _output_result(result, output_path=None):
    """Output result as JSON."""
    json_str = json.dumps(result, ensure_ascii=False, indent=2)
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(json_str)
        print(f"\nResult saved to: {output_path}")
    else:
        print("\n=== RESULT ===")
        print(json_str)


if __name__ == '__main__':
    main()
