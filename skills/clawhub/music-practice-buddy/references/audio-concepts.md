# Audio Analysis Concepts for Musicians

This document explains the signal processing techniques behind Music Practice Buddy in musician-friendly terms.

## Onset Detection: Finding Note Starts

### What It Is

Onset detection is the process of identifying the moment each note begins in an audio recording. Think of it as the computer "tapping its foot" to each note.

### How It Works

1. **Spectral flux**: The analyzer computes how much the frequency spectrum changes from one moment to the next. A note onset creates a sharp change in the spectrum.
2. **Energy envelope**: A sharp increase in audio energy often indicates a note attack.
3. **Peak picking**: The analyzer identifies local peaks in the onset detection function — each peak is a likely note start.

### Why It Matters for Practice

If you play 8 notes but the analyzer detects only 6 onsets, two notes were either:
- Played too softly (the attack wasn't strong enough)
- Played too close together (slurred rather than articulated)

Consistent onset detection means clear, articulated playing.

## Tempo Estimation: Finding the BPM

### What It Is

Tempo estimation determines the overall speed of a performance in beats per minute (BPM).

### How It Works

1. **Onset detection** produces a list of note-start times
2. **Autocorrelation** finds the periodic pattern — the time interval that best explains the spacing between onsets
3. The inverse of that interval is the BPM: interval of 0.5s → 120 BPM

### Tempo Drift Detection

The analyzer divides the recording into sections (e.g., 10-second windows) and estimates BPM for each section. If BPM varies by more than 3% between sections, you're drifting.

Common drift patterns:
- **Acceleration**: Speeding up during technically easy passages, slowing during hard ones
- **Excitement rush**: Gradually speeding up throughout the piece
- **Fatigue slowdown**: Tempo dropping in the last third of the piece

## Pitch Tracking: Following the Notes

### What It Is

Pitch tracking (also called fundamental frequency estimation or f0 tracking) follows the main frequency of a note over time — like a graph of which note you're playing, second by second.

### How It Works

1. **Autocorrelation**: The signal is compared with delayed copies of itself. The delay that produces maximum similarity corresponds to the fundamental period. Inverse = frequency.
2. **Windowed analysis**: The recording is analyzed in short windows (e.g., 50ms) to track pitch over time.

### Pitch Stability Score

The pitch stability score measures how much the fundamental frequency varies around its mean:

```
Stability = 100 - (frequency_standard_deviation / mean_frequency * 100 * scale_factor)
```

High variation (low score) indicates:
- **Intonation issues**: Not quite hitting the right note
- **Vibrato**: Intentional pitch oscillation (can be good or excessive)
- **Technique problems**: String players pressing too hard/soft, wind players with breath support issues

### Note-to-Note Pitch

For pitched instruments, the analyzer can compare detected frequencies to the nearest equal-tempered note:

- **0 cents deviation**: Perfectly in tune
- **±5 cents**: Acceptable (most listeners won't notice)
- **±10 cents**: Noticeably out of tune
- **±20+ cents**: Clearly out of tune

(There are 100 cents in a semitone.)

## Dynamic Analysis: Volume Over Time

### What It Is

Dynamic analysis measures how loud or soft your playing is throughout the recording.

### How It Works

1. **RMS energy**: The Root Mean Square of the audio signal amplitude, computed in short windows, produces a volume envelope.
2. **Dynamic range**: The difference (in decibels) between the loudest and quietest moments.

### What the Numbers Mean

- **Dynamic range < 3 dB**: Very flat — everything is the same volume. May sound mechanical.
- **Dynamic range 6–12 dB**: Good — natural variation, expressive playing.
- **Dynamic range > 18 dB**: Inconsistent — some notes are lost while others jump out.

### Common Issues

- **Volume drops during fast passages**: Technique breaks down when speed increases
- ** crescendos that don't reach peak**: Starting too loud, no room to grow
- **Accent imbalances**: Some notes in a pattern consistently louder/softer than intended

## Sampling Rate and Frequency Resolution

The sampling rate of your recording affects analysis quality:

- **44100 Hz** (CD quality): Detects frequencies up to 22050 Hz — covers all musical pitches
- **22050 Hz**: Covers up to 11025 Hz — sufficient for most instruments
- **8000 Hz**: Only covers up to 4000 Hz — not enough for high notes

Always record at 44100 Hz or higher for best results.

## Nyquist Frequency

The highest frequency a digital system can represent is half the sampling rate (the Nyquist frequency). Frequencies above this limit cause **aliasing** — they "fold back" and appear as false lower frequencies. Always use recordings sampled at adequate rates.

## Windowing and Time-Frequency Trade-off

Audio analysis involves a trade-off:
- **Longer analysis windows** = better frequency resolution, worse time resolution
- **Shorter analysis windows** = better time resolution, worse frequency resolution

Music Practice Buddy uses adaptive window sizes:
- **Tempo/timing**: Short windows (50ms) for precise onset timing
- **Pitch tracking**: Medium windows (50ms) for balance
- **Dynamic range**: Long windows (200ms) for smooth volume curves

## References

1. Bello, J. P., et al. (2005). "A tutorial on onset detection in music signals." *IEEE Transactions on Speech and Audio Processing*, 13(5), 1035–1047.
2. de Cheveigné, A., & Kawahara, H. (2002). "YIN, a fundamental frequency estimator for speech and music." *JASA*, 111(4), 1917–1930.
3. Klapuri, A. (2004). "Automatic music transcription as we know it today." *Journal of New Music Research*, 33(3), 269–282.
4. Grosche, P., et al. (2010). "What makes beat tracking difficult?" *ISMIR Proceedings*.
