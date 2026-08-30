# Motion and quality control

## Why micro-jitter happens

FFmpeg `zoompan` evaluates crop position on a pixel grid. A slow move may request less than one source pixel per output frame. Integer rounding then produces a repeating pattern: hold, hold, jump one pixel. Fine comic linework makes the jump look like camera shake or texture shimmer.

Additional causes:

- rendering motion directly at 1080×1920 with little overscan;
- 24 fps linear movement across a small distance;
- simultaneous zoom and pan with unrelated timing;
- high-frequency paper grain or ink lines resampled with a weak filter;
- H.264 bitrate too low for moving line art.

## Required prevention

Use `scripts/render_still_clip.sh`, or reproduce all of its principles:

1. Scale to a working canvas at least twice delivery resolution.
2. Animate crop/zoom coordinates on that oversized canvas.
3. Use cosine ease-in/ease-out.
4. Downsample with Lanczos.
5. Default to 30 fps.
6. Move only one dominant camera parameter per shot.
7. Keep zoom strength around 2–5%.
8. Include intentional holds.

Do not use shake, random motion, unseeded noise, or frame-by-frame position randomness unless the story explicitly calls for an impact.

## Motion grammar

| Story purpose | Motion |
|---|---|
| Realization, danger, intimacy | Slow push |
| Isolation, consequence | Slow pull |
| Reveal a prop or second character | Eased pan |
| Shock, grief, final line | Hold |
| Entering a location | Short pan or push, not both |

Alternate movement with holds. If every shot moves, motion stops carrying meaning.

## Validation

Inspect the final encoded video, not only the raw source:

- play on a phone-sized window and full size;
- inspect eyes, hair strands, bottle edges, and high-contrast lines;
- step frame-by-frame through the slowest move;
- extract 2–3 consecutive frames and compare crop movement;
- check 100% and 50% playback speed.

Technical checks:

```bash
ffmpeg -v error -i final.mp4 -f null -
ffmpeg -hide_banner -i final.mp4 -vf blackdetect=d=0.3:pix_th=0.05 -an -f null -
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height,r_frame_rate,pix_fmt -of json final.mp4
```

Use CRF 16–19 for detailed line art and `yuv420p` for broad compatibility.

