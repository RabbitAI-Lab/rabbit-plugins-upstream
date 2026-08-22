# FitCheck: Workout Readiness & Recovery

**The camera game that tries to read you, powered by EmoPulse on-device ML: grill a friend and watch the composure meter, check any video, send a challenge link. Plus stress, mood and a heart-rate estimate for training days.**

Live at [emo.city](https://emo.city?utm_source=clawhub&utm_medium=skill) | Built by [EmoPulse](https://www.emopulse.app)

---

## The three big plays

- **DECEPTION CHALLENGE** - the party duel: one asks, one answers, the live meters do the talking (DECEPTION, STRESS, VOICE_STRESS, MICRO_EXPR, EYE_CONTACT, AUTHENTIC). Difficulty levels: OPEN, EASY, GUARDED, HELD BACK.
- **Check any video** - drop a clip into UPLOAD and get a moment-by-moment read with flagged spikes.
- **Challenge your friends** - one link, no install, everyone compares scores.

Plus the training-day check-in: stress, mood and a heart-rate estimate before or after the gym.

## Signals

7 emotions, stress, authenticity (Duchenne smile), deception meter, heart rate (rPPG, contactless), HRV, eye contact, gaze breaks, micro-expressions, blink rate, voice stress, signal quality. 478 facial landmarks and 52 blendshapes per frame, up to 4 faces.

## How to Use

1. Say "can it read me", "challenge my friend" or "check my stress"
2. Open [emo.city](https://emo.city?utm_source=clawhub&utm_medium=skill) in Chrome or Edge
3. Pick LIVE, UPLOAD or CHALLENGE, allow camera, press SCAN
4. Results auto-summarize; export with SHARE, COPY_TEXT or DL_REPORT

## Technology

- MediaPipe Face Landmarker, GPU-accelerated, fully on-device
- rPPG contactless heart-rate estimation, adaptive per-session baseline
- Duchenne detection (AU6 + AU12) for genuine-smile reads
- Web Audio API spectral analysis for the voice cue

## Privacy

Everything runs on-device in the browser. No video, audio or raw signals leave the device. Exports share only text summaries. Close the tab and it is gone.

## Links

- Live app: [emo.city](https://emo.city?utm_source=clawhub&utm_medium=skill)
- Built by: [EmoPulse](https://www.emopulse.app)

## Plans

| Plan | Price | Scans |
|------|-------|-------|
| Free | $0 | 1 scan |
| Basic | $9.99/mo | 30 scans/month |
| Pro | $29.99/mo | 100 scans/month |

## License

Proprietary, patents pending. Terms and rules live inside [emo.city](https://emo.city) and [emopulse.app/license](https://www.emopulse.app/license.html).
