# FitCheck: Live Emotional Mirror & Readiness

**The camera game that tries to read you, powered by EmoPulse on-device ML: grill a friend and watch the composure meter, check any video, send a challenge link. Plus stress, mood and a heart-rate estimate for training days.**

Live at [emo.city](https://emo.city?utm_source=clawhub&utm_medium=skill) | Built by [EmoPulse](https://www.emopulse.app)

---

## What It Does

EmoCity is a browser-based biometric intelligence platform that analyzes your face, voice, and physiological signals in real time. No downloads required. All biometric processing runs on-device using MediaPipe Face Landmarker with GPU acceleration.

Point your camera at a face and EmoCity detects:

- **Felt-vs-shown composure** - how relaxed vs. guarded you look (a party game, not a lie detector)
- Real-time **stress levels** from facial micro-tension
- **Emotions** - happy, sad, angry, fearful, surprised, disgusted, neutral
- **Heart rate** without any contact (rPPG forehead analysis)
- **Voice stress** via spectral frequency analysis
- **Micro-expressions** - involuntary facial movements lasting milliseconds
- **Eye contact** stability and gaze aversion patterns
- **Authenticity** - Duchenne smile detection (genuine vs fake)

## 47 Biometric Parameters

EmoCity processes **478 facial landmarks** and **52 blendshapes** every frame to extract:

| Category | Parameters |
|----------|-----------|
| Emotions | 7 emotions with competitive scoring + confidence |
| Action Units | AU1, AU2, AU4, AU6, AU7, AU9, AU12, AU15, AU25, AU26, AU45 |
| Stress | Composite score (facial + cardiac + vocal) |
| Composure (felt-vs-shown) | Multi-factor read (stress + genuineness + gaze + micro-expressions) - entertainment, not lie detection |
| Cardiac | Heart rate (BPM), HRV (RMSSD), RR intervals |
| Gaze | Eye contact %, gaze stability, aversion detection |
| Voice | Stress %, voice detection, frequency analysis |
| Expression | Micro-expression count, blink rate, Duchenne markers |
| Tracking | Face count (up to 4), face position, 478 landmark coordinates |

## How to Use

### Quick Start
1. Say **"scan my face"** or **"read my composure"**
2. Open [emo.city](https://emo.city?utm_source=clawhub&utm_medium=skill) in Chrome or Edge
3. Click **SCAN** and allow camera + microphone
4. The 478-point face mesh confirms detection
5. Speak during the scan for voice stress analysis
6. Results auto-summarize when the scan completes

### Scan Modes

- **LIVE** - Real-time camera analysis (up to 2 minutes)
- **UPLOAD** - Analyze a photo (JPG/PNG) or video (MP4/MOV)
- **CHALLENGE** - Share a composure-game link with friends

### Example Commands

```
"scan my face"
"how composed do I look?"
"check my stress level"
"read my felt-vs-shown"
"analyze this photo"
"what's my heart rate?"
"challenge my friend"
"how do I look - stressed or relaxed?"
"read my emotions"
"give me a full biometric report"
```

## Technology

- **MediaPipe Face Landmarker** v0.10.18 - 478 landmarks + 52 blendshapes, GPU-accelerated
- **rPPG** - Remote photoplethysmography for contactless heart rate
- **Adaptive baseline calibration** - 30-frame personalized baseline per session
- **Competitive emotion normalization** - dominant emotion suppression for accurate classification
- **Duchenne detection** - AU6 + AU12 co-activation for genuine smile verification
- **Web Audio API** - Real-time spectral analysis for voice stress detection
- **Next.js 16 + React 19 + Tailwind v4** - Modern web stack with Turbopack

## Privacy

The browser scan runs on-device. During a scan no video, audio, or raw biometric data leaves the device. The camera feed is analyzed frame-by-frame using WebAssembly + WebGL. Export features (Share to X, Copy Text, Download Report) only share aggregated text summaries - never raw video or biometric signals. Anonymous usage analytics (page views, feature usage counts) are collected via Vercel Analytics, and a signed-in user's own summary scores are saved to their account so the dashboard and history work. When you close the tab, all local biometric data is gone. The RapidAPI product linked below is the separate case: there a developer deliberately uploads a photo or clip to the API, so it is not an on-device path.

Scan only people who know it is running and agreed to it, and in UPLOAD mode only footage the person is fine with you analysing. A scan is a mirror and a party game, never a way to screen or judge someone.

## Links

- **Live app:** [emo.city](https://emo.city?utm_source=clawhub&utm_medium=skill)
- **Built by:** [EmoPulse](https://www.emopulse.app)
- **Repository:** [github.com/gv66co/Emo-City](https://github.com/gv66co/Emo-City)
- API for builders (same engine, free tier, media is uploaded to the API by the developer): https://rapidapi.com/emocity/api/emopulse-face-analysis

## Plans

| Plan | Price | Scans |
|------|-------|-------|
| Free | $0 | 1 scan |
| Basic | $9.99/mo | 30 scans/month |
| Pro | $29.99/mo | 100 scans/month |

---

## License

This software is **proprietary** and protected by copyright, with patents pending. Unauthorized copying, modification, distribution, reverse engineering, or use to train AI models is strictly prohibited. See [emopulse.app/license](https://www.emopulse.app/license.html).

Built by EmoPulse. All rights reserved.
