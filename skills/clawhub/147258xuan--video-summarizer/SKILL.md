---
name: video-summarizer
description: Extract keyframes and metadata from video files using ffmpeg scene detection. Use when you need to analyze, summarize, or extract scenes from a video file.
---

# Video Summarizer

Extracts scene keyframes and metadata from video files using ffmpeg's scene detection.

## When to use

- User uploads/provides a video file and asks what's in it
- You need to summarize a video's content by extracting keyframes
- You want to know video metadata (duration, resolution, fps, scene count)

## Usage

```javascript
const vs = require('./skills/video-summarizer');

// Basic usage
const result = vs.summarize('/path/to/video.mp4');
console.log(result.scenes);     // array of { time, frame } objects
console.log(result.duration);   // duration in seconds
console.log(result.keyframeCount);

// Custom scene sensitivity
const detailed = vs.summarize('/path/to/video.mp4', { sceneThreshold: 0.3 });
// Lower threshold = more scenes detected

// Custom output directory
const custom = vs.summarize('/path/to/video.mp4', { outputDir: '/tmp/frames' });
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `sceneThreshold` | 0.4 | ffmpeg scene detection threshold (0.0-1.0, lower = more sensitive) |
| `outputDir` | video directory | Where to save extracted keyframe images |

## Return Value

```json
{
  "scenes": [
    { "time": "0.00", "frame": "/path/to/frames/frame-00001.jpg" },
    { "time": "12.34", "frame": "/path/to/frames/frame-00002.jpg" }
  ],
  "duration": 120.5,
  "width": 1920,
  "height": 1080,
  "fps": 23.98,
  "keyframeCount": 8
}
```

## Requirements

- ffmpeg must be installed and available in PATH
- Tested with ffmpeg 6+

## Scripts

- `scripts/extract-frames.js` - CLI wrapper for standalone use
- `node scripts/extract-frames.js <videoPath> [options]`

## Notes

- Keyframes are saved as JPEG files next to the video in a `{filename}_keyframes/` directory
- Scene detection uses ffmpeg's `select='gt(scene,{threshold})'` filter
- Large videos may take time to process; the internal timeout is 120 seconds
