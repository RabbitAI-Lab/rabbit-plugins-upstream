#!/usr/bin/env python3
"""
Music Practice Buddy — analyze practice recordings for objective feedback.

Subcommands:
  analyze   — analyze a single recording, produce scores and report
  compare   — compare two recordings to track improvement
  plan      — generate a targeted practice plan based on analysis
  history   — show logged practice sessions and improvement trends

Usage:
  python practice_buddy.py analyze recording.wav
  python practice_buddy.py analyze recording.wav --target-bpm 120
  python practice_buddy.py compare week1.wav week2.wav
  python practice_buddy.py plan recording.wav --instrument guitar --minutes 30
  python practice_buddy.py history
"""

import argparse
import json
import math
import os
import struct
import sys
import wave
from datetime import datetime

PRACTICE_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "practice_log.json")

# ---------------------------------------------------------------------------
# WAV file loading (pure Python, no external dependencies for basic WAV)
# ---------------------------------------------------------------------------

def load_wav(filepath):
    """Load a WAV file and return (samples, sample_rate, duration_sec)."""
    try:
        import numpy as np
        return _load_wav_numpy(filepath)
    except ImportError:
        return _load_wav_pure(filepath)


def _load_wav_numpy(filepath):
    """Load WAV using numpy for efficient computation."""
    import numpy as np
    with wave.open(filepath, 'rb') as wf:
        n_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        sample_rate = wf.getframerate()
        n_frames = wf.getnframes()
        raw = wf.readframes(n_frames)

    if sample_width == 2:
        samples = np.frombuffer(raw, dtype=np.int16).astype(np.float64)
    elif sample_width == 1:
        samples = np.frombuffer(raw, dtype=np.uint8).astype(np.float64) - 128
    elif sample_width == 4:
        samples = np.frombuffer(raw, dtype=np.int32).astype(np.float64)
    else:
        raise ValueError(f"Unsupported sample width: {sample_width}")

    # Normalize to -1.0 to 1.0
    max_val = float(2 ** (8 * sample_width - 1))
    samples /= max_val

    # Mix to mono
    if n_channels > 1:
        samples = samples.reshape(-1, n_channels).mean(axis=1)

    duration = len(samples) / sample_rate
    return samples, sample_rate, duration


def _load_wav_pure(filepath):
    """Load WAV without numpy (fallback, limited analysis)."""
    with wave.open(filepath, 'rb') as wf:
        n_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        sample_rate = wf.getframerate()
        n_frames = wf.getnframes()
        raw = wf.readframes(n_frames)

    if sample_width == 2:
        fmt = '<' + 'h' * (len(raw) // 2)
        all_samples = struct.unpack(fmt, raw)
    elif sample_width == 1:
        all_samples = tuple(b - 128 for b in raw)
    else:
        raise ValueError(f"Unsupported sample width: {sample_width}")

    # Mix to mono
    if n_channels > 1:
        mono = []
        for i in range(0, len(all_samples), n_channels):
            chunk = all_samples[i:i+n_channels]
            mono.append(sum(chunk) / len(chunk))
        samples = mono
    else:
        samples = list(all_samples)

    # Normalize
    max_val = float(2 ** (8 * sample_width - 1))
    samples = [s / max_val for s in samples]
    duration = len(samples) / sample_rate
    return samples, sample_rate, duration


# ---------------------------------------------------------------------------
# Audio analysis
# ---------------------------------------------------------------------------

def compute_rms_energy(samples, sample_rate, window_ms=50):
    """Compute RMS energy envelope in fixed-size windows."""
    try:
        import numpy as np
        window_size = int(sample_rate * window_ms / 1000)
        n_windows = len(samples) // window_size
        energy = []
        for i in range(n_windows):
            chunk = samples[i * window_size:(i + 1) * window_size]
            rms = np.sqrt(np.mean(chunk ** 2))
            energy.append(float(rms))
        return energy
    except ImportError:
        window_size = int(sample_rate * window_ms / 1000)
        n_windows = len(samples) // window_size
        energy = []
        for i in range(n_windows):
            chunk = samples[i * window_size:(i + 1) * window_size]
            mean_sq = sum(s * s for s in chunk) / len(chunk)
            energy.append(math.sqrt(mean_sq))
        return energy


def detect_onsets(samples, sample_rate, threshold=0.3):
    """Detect note onsets using spectral flux approximation."""
    try:
        import numpy as np
        # Compute energy envelope with fine resolution
        window_size = int(sample_rate * 0.02)  # 20ms windows
        hop_size = int(sample_rate * 0.01)  # 10ms hop
        energy = []
        for i in range(0, len(samples) - window_size, hop_size):
            chunk = samples[i:i + window_size]
            rms = np.sqrt(np.mean(chunk ** 2))
            energy.append(float(rms))

        # Spectral flux approximation: positive derivative of energy
        flux = [max(0, energy[i] - energy[i-1]) for i in range(1, len(energy))]

        # Normalize
        max_flux = max(flux) if flux else 1
        if max_flux > 0:
            flux = [f / max_flux for f in flux]

        # Peak picking
        onsets = []
        for i in range(1, len(flux) - 1):
            if flux[i] > threshold and flux[i] > flux[i-1] and flux[i] >= flux[i+1]:
                time_sec = i * hop_size / sample_rate
                onsets.append(time_sec)

        # Merge onsets that are very close (within 50ms)
        merged = []
        for t in onsets:
            if not merged or t - merged[-1] > 0.05:
                merged.append(t)

        return merged
    except ImportError:
        return _detect_onsets_pure(samples, sample_rate, threshold)


def _detect_onsets_pure(samples, sample_rate, threshold=0.3):
    """Pure Python onset detection (fallback)."""
    window_size = int(sample_rate * 0.02)
    hop_size = int(sample_rate * 0.01)
    energy = []
    for i in range(0, len(samples) - window_size, hop_size):
        chunk = samples[i:i + window_size]
        mean_sq = sum(s * s for s in chunk) / len(chunk)
        energy.append(math.sqrt(mean_sq))

    flux = [max(0, energy[i] - energy[i-1]) for i in range(1, len(energy))]
    max_flux = max(flux) if flux else 1
    if max_flux > 0:
        flux = [f / max_flux for f in flux]

    onsets = []
    for i in range(1, len(flux) - 1):
        if flux[i] > threshold and flux[i] > flux[i-1] and flux[i] >= flux[i+1]:
            time_sec = i * hop_size / sample_rate
            onsets.append(time_sec)

    merged = []
    for t in onsets:
        if not merged or t - merged[-1] > 0.05:
            merged.append(t)
    return merged


def estimate_bpm(onsets):
    """Estimate BPM from onset times using inter-onset intervals."""
    if len(onsets) < 4:
        return None

    # Compute inter-onset intervals
    intervals = [onsets[i+1] - onsets[i] for i in range(len(onsets) - 1)]
    if not intervals:
        return None

    # Median interval → BPM
    try:
        import numpy as np
        median_interval = np.median(intervals)
    except ImportError:
        sorted_intervals = sorted(intervals)
        median_interval = sorted_intervals[len(sorted_intervals) // 2]

    if median_interval <= 0:
        return None

    bpm = 60.0 / median_interval

    # Normalize to reasonable musical range (40-240 BPM)
    while bpm < 60:
        bpm *= 2
    while bpm > 240:
        bpm /= 2

    return round(bpm)


def track_pitch(samples, sample_rate, frame_ms=50):
    """Track fundamental frequency over time using autocorrelation."""
    try:
        import numpy as np
        frame_size = int(sample_rate * frame_ms / 1000)
        hop_size = frame_size // 2
        frequencies = []

        min_freq = 50  # Hz
        max_freq = 2000  # Hz
        min_lag = int(sample_rate / max_freq)
        max_lag = int(sample_rate / min_freq)

        for i in range(0, len(samples) - frame_size, hop_size):
            frame = samples[i:i + frame_size]
            # Check if frame has enough energy
            rms = np.sqrt(np.mean(frame ** 2))
            if rms < 0.01:  # silence
                frequencies.append(0)
                continue

            # Autocorrelation
            corr = np.correlate(frame, frame, mode='full')
            corr = corr[len(corr) // 2:]  # Keep positive lags only

            # Find peak in the valid lag range
            search_region = corr[min_lag:max_lag]
            if len(search_region) > 0 and np.max(search_region) > 0.1 * corr[0]:
                peak_lag = np.argmax(search_region) + min_lag
                freq = sample_rate / peak_lag
                frequencies.append(float(freq))
            else:
                frequencies.append(0)

        return frequencies
    except ImportError:
        return []


def analyze_timing(onsets):
    """Analyze timing consistency from onsets."""
    if len(onsets) < 4:
        return {"score": 50, "n_onsets": len(onsets), "gaps": [], "detail": "Not enough onsets detected"}

    intervals = [onsets[i+1] - onsets[i] for i in range(len(onsets) - 1)]
    try:
        import numpy as np
        mean_interval = np.mean(intervals)
        std_interval = np.std(intervals)
        cv = std_interval / mean_interval if mean_interval > 0 else 1  # coefficient of variation
    except ImportError:
        mean_interval = sum(intervals) / len(intervals)
        variance = sum((x - mean_interval) ** 2 for x in intervals) / len(intervals)
        std_interval = math.sqrt(variance)
        cv = std_interval / mean_interval if mean_interval > 0 else 1

    # Score: lower CV = higher score. CV of 0.05 = 95, CV of 0.3 = 40
    score = max(0, min(100, int(100 - cv * 200)))

    # Find timing gaps > 50ms from the mean
    gaps = []
    for i, interval in enumerate(intervals):
        deviation = abs(interval - mean_interval)
        if deviation > 0.05:  # 50ms
            gaps.append({
                "after_onset": i + 1,
                "time": round(onsets[i + 1], 2),
                "deviation_ms": round(deviation * 1000),
                "direction": "rushed" if interval < mean_interval else "dragged",
            })

    return {
        "score": score,
        "n_onsets": len(onsets),
        "mean_interval_ms": round(mean_interval * 1000),
        "std_deviation_ms": round(std_interval * 1000),
        "coefficient_of_variation": round(cv, 4),
        "gaps": gaps[:10],  # Top 10
        "detail": f"{len(gaps)} timing deviations > 50ms detected"
    }


def analyze_pitch(frequencies):
    """Analyze pitch stability from frequency track."""
    freqs = [f for f in frequencies if f > 0]
    if len(freqs) < 10:
        return {"score": 75, "detail": "Not enough pitched audio for analysis"}

    try:
        import numpy as np
        mean_freq = np.mean(freqs)
        std_freq = np.std(freqs)
        cv = std_freq / mean_freq if mean_freq > 0 else 1
    except ImportError:
        mean_freq = sum(freqs) / len(freqs)
        variance = sum((f - mean_freq) ** 2 for f in freqs) / len(freqs)
        std_freq = math.sqrt(variance)
        cv = std_freq / mean_freq if mean_freq > 0 else 1

    # Score: lower CV = higher stability
    score = max(0, min(100, int(100 - cv * 300)))

    # Find the note closest to mean frequency
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    if mean_freq > 0:
        semitones = 12 * math.log2(mean_freq / 440.0)
        note_index = round(semitones) % 12
        octave = 4 + (round(semitones) + 9) // 12
        nearest_note = f"{note_names[note_index]}{octave}"
        cents_deviation = (semitones - round(semitones)) * 100
    else:
        nearest_note = "?"
        cents_deviation = 0

    return {
        "score": score,
        "mean_frequency": round(mean_freq, 1),
        "nearest_note": nearest_note,
        "cents_deviation": round(cents_deviation, 1),
        "std_deviation_hz": round(std_freq, 1),
        "detail": f"Pitch centered around {nearest_note} with {round(std_freq, 1)} Hz variation"
    }


def analyze_tempo(onsets, sample_rate, duration):
    """Analyze tempo consistency by section."""
    if len(onsets) < 8:
        return {"score": 70, "bpm": None, "drift": "Not enough data"}

    # Split into 4 sections
    section_duration = duration / 4
    section_bpms = []
    for s in range(4):
        start = s * section_duration
        end = (s + 1) * section_duration
        section_onsets = [o for o in onsets if start <= o < end]
        if len(section_onsets) >= 2:
            bpm = estimate_bpm(section_onsets)
            if bpm and 40 < bpm < 300:
                section_bpms.append(bpm)

    if len(section_bpms) < 2:
        return {"score": 70, "bpm": estimate_bpm(onsets), "drift": "Insufficient section data"}

    overall_bpm = estimate_bpm(onsets)
    try:
        import numpy as np
        mean_section_bpm = np.mean(section_bpms)
        std_bpm = np.std(section_bpms)
    except ImportError:
        mean_section_bpm = sum(section_bpms) / len(section_bpms)
        variance = sum((b - mean_section_bpm) ** 2 for b in section_bpms) / len(section_bpms)
        std_bpm = math.sqrt(variance)

    cv = std_bpm / mean_section_bpm if mean_section_bpm > 0 else 1
    score = max(0, min(100, int(100 - cv * 400)))

    # Detect drift direction
    if len(section_bpms) >= 2:
        first_half = sum(section_bpms[:len(section_bpms)//2]) / (len(section_bpms)//2)
        second_half = sum(section_bpms[len(section_bpms)//2:]) / (len(section_bpms) - len(section_bpms)//2)
        drift_pct = (second_half - first_half) / first_half * 100 if first_half > 0 else 0
        if drift_pct > 3:
            drift = f"Accelerating (+{drift_pct:.1f}% in later sections)"
        elif drift_pct < -3:
            drift = f"Decelerating ({drift_pct:.1f}% in later sections)"
        else:
            drift = f"Stable (±{abs(drift_pct):.1f}%)"
    else:
        drift = "Unknown"

    return {
        "score": score,
        "bpm": overall_bpm,
        "section_bpms": section_bpms,
        "drift": drift,
        "detail": f"~{overall_bpm} BPM, {drift}"
    }


def analyze_dynamics(energy):
    """Analyze dynamic range from RMS energy envelope."""
    if len(energy) < 10:
        return {"score": 70, "detail": "Not enough audio data"}

    try:
        import numpy as np
        rms_values = np.array(energy)
        # Convert to dB
        rms_db = 20 * np.log10(rms_values + 1e-10)
        dynamic_range = float(np.max(rms_db) - np.min(rms_db))
        mean_db = float(np.mean(rms_db))
    except ImportError:
        min_rms = min(energy)
        max_rms = max(energy)
        dynamic_range = 20 * math.log10(max_rms / (min_rms + 1e-10))
        mean_db = 20 * math.log10(sum(energy) / len(energy) + 1e-10)

    # Score: 6-12 dB is ideal. Too narrow = flat, too wide = inconsistent
    if dynamic_range < 3:
        score = 55  # Too flat
        assessment = "Narrow — may sound flat"
    elif dynamic_range <= 12:
        score = 85  # Good range
        assessment = "Good dynamic control"
    elif dynamic_range <= 18:
        score = 70
        assessment = "Wide — some inconsistency"
    else:
        score = 55
        assessment = "Very wide — inconsistent volume"

    return {
        "score": score,
        "dynamic_range_db": round(dynamic_range, 1),
        "mean_volume_db": round(mean_db, 1),
        "assessment": assessment,
        "detail": f"{dynamic_range:.1f} dB range — {assessment}"
    }


# ---------------------------------------------------------------------------
# Full analysis
# ---------------------------------------------------------------------------

def analyze_recording(filepath, target_bpm=None):
    """Perform full analysis of a recording."""
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)

    ext = os.path.splitext(filepath)[1].lower()
    if ext != '.wav':
        print(f"Warning: Only .wav files fully supported. Got: {ext}")
        print("Convert with: ffmpeg -i input.{ext} output.wav\n")

    print(f"Loading {filepath}...")
    samples, sample_rate, duration = load_wav(filepath)
    print(f"  Duration: {duration:.1f}s | Sample rate: {sample_rate} Hz | Samples: {len(samples):,}\n")

    # Energy envelope
    energy = compute_rms_energy(samples, sample_rate)

    # Onset detection
    print("Detecting note onsets...")
    onsets = detect_onsets(samples, sample_rate)
    print(f"  Found {len(onsets)} onsets\n")

    # Pitch tracking
    print("Tracking pitch...")
    frequencies = track_pitch(samples, sample_rate)
    print(f"  {len([f for f in frequencies if f > 0])} pitched frames\n")

    # Analyses
    timing = analyze_timing(onsets)
    pitch = analyze_pitch(frequencies)
    tempo = analyze_tempo(onsets, sample_rate, duration)
    dynamics = analyze_dynamics(energy)

    # Overall score
    overall = round((timing["score"] + pitch["score"] + tempo["score"] + dynamics["score"]) / 4)

    # Target BPM comparison
    target_comparison = None
    if target_bpm and tempo.get("bpm"):
        actual_bpm = tempo["bpm"]
        diff = actual_bpm - target_bpm
        pct = abs(diff) / target_bpm * 100
        target_comparison = {
            "target": target_bpm,
            "actual": actual_bpm,
            "difference": diff,
            "percent_off": round(pct, 1),
        }

    result = {
        "file": filepath,
        "timestamp": datetime.now().isoformat(),
        "duration_sec": round(duration, 1),
        "sample_rate": sample_rate,
        "n_onsets": len(onsets),
        "scores": {
            "timing": timing,
            "pitch": pitch,
            "tempo": tempo,
            "dynamics": dynamics,
        },
        "overall_score": overall,
        "target_bpm_comparison": target_comparison,
    }

    # Log the session
    log_session(result)

    return result


def score_bar(score):
    """Generate a visual score bar."""
    filled = score // 10
    return "█" * filled + "░" * (10 - filled)


def score_label(score):
    """Label for a score."""
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Solid"
    elif score >= 60:
        return "Developing"
    else:
        return "Needs work"


def print_report(result):
    """Print the analysis report."""
    scores = result["scores"]
    mins = int(result["duration_sec"]) // 60
    secs = int(result["duration_sec"]) % 60

    print()
    print("╔" + "═" * 50 + "╗")
    print("║" + f"{'🎵 PRACTICE ANALYSIS REPORT':^50}" + "║")
    print("╠" + "═" * 50 + "╣")
    print("║" + f"  Duration: {mins}:{secs:02d} | Sample Rate: {result['sample_rate']} Hz".ljust(50) + "║")
    print("║" + f"  Onsets detected: {result['n_onsets']}".ljust(50) + "║")
    print("╠" + "═" * 50 + "╣")
    print("║" + f"{'📊 SCORES':^50}" + "║")
    print("║" + " " * 50 + "║")

    for dim, key in [("Timing", "timing"), ("Pitch", "pitch"), ("Tempo", "tempo"), ("Dynamics", "dynamics")]:
        s = scores[key]["score"]
        bar = score_bar(s)
        label = score_label(s)
        line = f"  {dim:<10} {s:>3}/100  {bar}  {label}"
        print("║" + line.ljust(50) + "║")

    print("║" + " " + "─" * 48 + " ║")
    overall = result["overall_score"]
    bar = score_bar(overall)
    label = score_label(overall)
    line = f"  OVERALL:   {overall:>3}/100  {bar}  {label}"
    print("║" + line.ljust(50) + "║")

    print("╠" + "═" * 50 + "╣")
    print("║" + f"{'📝 ANALYSIS':^50}" + "║")
    print("║" + " " * 50 + "║")

    # Tempo details
    tempo = scores["tempo"]
    if tempo.get("bpm"):
        bpm_line = f"  Detected BPM: ~{tempo['bpm']}"
        if result.get("target_bpm_comparison"):
            tc = result["target_bpm_comparison"]
            bpm_line += f" (target: {tc['target']}, {tc['percent_off']}% off)"
        print("║" + bpm_line.ljust(50) + "║")

    if tempo.get("drift"):
        print("║" + f"  Tempo drift: {tempo['drift']}".ljust(50) + "║")

    # Timing details
    timing = scores["timing"]
    if timing.get("gaps"):
        print("║" + f"  Timing: {timing['detail']}".ljust(50) + "║")
        for gap in timing["gaps"][:3]:
            print("║" + f"    → {gap['deviation_ms']}ms {gap['direction']} at {gap['time']}s".ljust(50) + "║")

    # Pitch details
    pitch = scores["pitch"]
    if pitch.get("nearest_note"):
        print("║" + f"  Pitch: centered on {pitch['nearest_note']}".ljust(50) + "║")

    # Dynamics details
    dyn = scores["dynamics"]
    if dyn.get("dynamic_range_db"):
        print("║" + f"  Dynamics: {dyn['detail']}".ljust(50) + "║")

    print("╠" + "═" * 50 + "╣")

    # Weakest area
    dim_scores = {k: scores[k]["score"] for k in ["timing", "pitch", "tempo", "dynamics"]}
    weakest = min(dim_scores, key=dim_scores.get)
    weak_names = {"timing": "Timing", "pitch": "Pitch Accuracy", "tempo": "Tempo Consistency", "dynamics": "Dynamic Control"}

    print("║" + f"{'🎯 RECOMMENDED FOCUS: ' + weak_names[weakest]:^50}" + "║")

    exercises = {
        "timing": [
            "→ Practice with metronome at 60% of target speed",
            "→ Focus on transitions between sections",
            "→ Use speed bursts: 2-4 measures at 110% speed",
        ],
        "pitch": [
            "→ Practice with a drone on the tonic",
            "→ Slow long tones, matching pitch precisely",
            "→ Record, play back with tuner, fix problem notes",
        ],
        "tempo": [
            "→ Play with metronome and record — listen for drift",
            "→ Identify sections where you speed up/slow down",
            "→ Gradual tempo increase: 5 BPM when 3 reps are perfect",
        ],
        "dynamics": [
            "→ Practice at dynamic extremes (ppp then fff)",
            "→ Work on smooth crescendos/decrescendos",
            "→ Practice accent patterns on scales",
        ],
    }
    for ex in exercises[weakest]:
        print("║" + f"  {ex}".ljust(50) + "║")

    print("╚" + "═" * 50 + "╝")
    print()


def log_session(result):
    """Log the session to practice_log.json."""
    log = []
    if os.path.exists(PRACTICE_LOG):
        try:
            with open(PRACTICE_LOG) as f:
                log = json.load(f)
        except (json.JSONDecodeError, IOError):
            log = []
    entry = {
        "timestamp": result["timestamp"],
        "file": os.path.basename(result["file"]),
        "duration": result["duration_sec"],
        "overall_score": result["overall_score"],
        "scores": {k: v["score"] for k, v in result["scores"].items()},
        "bpm": result["scores"]["tempo"].get("bpm"),
    }
    log.append(entry)
    with open(PRACTICE_LOG, 'w') as f:
        json.dump(log, f, indent=2)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_analyze(args):
    result = analyze_recording(args.file, args.target_bpm)
    print_report(result)
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"✓ Full analysis saved to {args.output}")


def cmd_compare(args):
    print("Comparing recordings...\n")
    r1 = analyze_recording(args.file1)
    r2 = analyze_recording(args.file2)

    print("\n")
    print("=" * 60)
    print(f"{'COMPARISON':^60}")
    print("=" * 60)
    print(f"\n{'Metric':<20} {'Before':>10} {'After':>10} {'Change':>10}")
    print("-" * 60)

    metrics = [
        ("Overall", r1["overall_score"], r2["overall_score"]),
        ("Timing", r1["scores"]["timing"]["score"], r2["scores"]["timing"]["score"]),
        ("Pitch", r1["scores"]["pitch"]["score"], r2["scores"]["pitch"]["score"]),
        ("Tempo", r1["scores"]["tempo"]["score"], r2["scores"]["tempo"]["score"]),
        ("Dynamics", r1["scores"]["dynamics"]["score"], r2["scores"]["dynamics"]["score"]),
    ]

    for name, before, after in metrics:
        change = after - before
        arrow = "📈" if change > 0 else "📉" if change < 0 else "→"
        print(f"  {name:<18} {before:>8}/100 {after:>8}/100 {arrow} {change:+d}")

    overall_change = r2["overall_score"] - r1["overall_score"]
    print(f"\n  {'Overall change:':.<30} {overall_change:+d} points")
    if overall_change > 0:
        print(f"  ✅ Improvement detected! Keep doing what you're doing.")
    elif overall_change < 0:
        print(f"  ⚠️ Scores decreased. Review your practice approach.")
    else:
        print(f"  → No change. Try a different practice strategy.")
    print()


def cmd_plan(args):
    result = analyze_recording(args.file)
    scores = result["scores"]
    dim_scores = {k: scores[k]["score"] for k in ["timing", "pitch", "tempo", "dynamics"]}
    weakest = min(dim_scores, key=dim_scores.get)
    weak_names = {"timing": "Timing", "pitch": "Pitch Accuracy", "tempo": "Tempo Consistency", "dynamics": "Dynamic Control"}

    minutes = args.minutes
    print("\n" + "=" * 60)
    print(f"  🎸 PRACTICE PLAN — {args.instrument.title()} — {minutes} min")
    print(f"  Focus area: {weak_names[weakest]} (score: {dim_scores[weakest]}/100)")
    print("=" * 60 + "\n")

    plans = {
        "timing": [
            ("Warm-up: scales with metronome", 5, "Set metronome to 60 BPM. Play major scales, one note per click."),
            ("Slow practice: piece at 60% speed", 10, "Play the piece at 60% of target tempo. Stop and restart on any timing error."),
            ("Targeted section work", 10, "Identify the 2-3 measures with timing gaps. Loop them with metronome."),
            ("Speed bursts", int(minutes * 0.15), f"Play difficult passages at 110% speed, then relax to 100%."),
            ("Cool-down: play through at 80%", max(2, minutes - 28), "Play the full piece at 80% speed, focusing on even timing."),
        ],
        "pitch": [
            ("Warm-up: long tones with tuner", 5, "Hold each note for 8 counts. Watch the tuner. Memorize correct pitch."),
            ("Drone practice", 8, "Play piece against a drone on the tonic. Match every note to its interval."),
            ("Problem note isolation", 7, f"Find 3-5 consistently out-of-tune notes. Practice each for 1 minute."),
            ("Interval practice", int(minutes * 0.2), "Practice intervals (3rds, 5ths, octaves) slowly, checking tuning."),
            ("Play through with awareness", max(3, minutes - 25), "Play the piece, focusing your attention on pitch above all else."),
        ],
        "tempo": [
            ("Warm-up with metronome", 5, "Scales at target tempo. Stay exactly with the click."),
            ("Section-by-section tempo mapping", 8, "Play each section separately with metronome. Note where you drift."),
            ("Gradual tempo building", 10, "Start at 60% of target. Three perfect reps → +5 BPM. Repeat."),
            ("Full play-through with metronome", 5, "Record this. Then listen back — can you hear the metronome?"),
            (" tempo-free play and record", max(2, minutes - 28), "Play without metronome. Record. Analyze if drift improved."),
        ],
        "dynamics": [
            ("Warm-up: dynamic extremes", 5, "Play scales as softly as possible (ppp), then as loud as possible (fff)."),
            ("Crescendo/decrescendo practice", 7, "Long notes: 8-count crescendo pp→ff, then 8-count decrescendo."),
            ("Accent pattern practice", 8, "Play scales with varied accents: beats 1&3, 2&4, every note, none."),
            ("Dynamic mapping of piece", int(minutes * 0.2), "Mark intended dynamics in your score. Practice them deliberately."),
            ("Expressive play-through", max(3, minutes - 25), "Play the piece with full dynamic intention."),
        ],
    }

    total = 0
    for exercise, time_min, description in plans[weakest]:
        actual_time = min(time_min, minutes - total) if minutes - total > 0 else 0
        if actual_time <= 0:
            break
        print(f"  ⏱️  {total:>2}–{total + actual_time:>2} min  ({actual_time} min)")
        print(f"     📌 {exercise}")
        print(f"     💡 {description}")
        print()
        total += actual_time

    print(f"  Total: {total} minutes")
    print(f"\n  💡 Record yourself after this session and compare!")
    print()


def cmd_history(args):
    if not os.path.exists(PRACTICE_LOG):
        print("No practice history yet. Run 'analyze' to log your first session.")
        return

    with open(PRACTICE_LOG) as f:
        log = json.load(f)

    if not log:
        print("Practice log is empty.")
        return

    print("=" * 65)
    print(f"  📊 PRACTICE HISTORY — {len(log)} sessions")
    print("=" * 65)
    print(f"\n  {'Date':<20} {'File':<20} {'Overall':>8} {'Timing':>8} {'Pitch':>8} {'Tempo':>8} {'Dynamics':>8}")
    print("  " + "-" * 61)

    for entry in log[-20:]:  # Show last 20
        dt = datetime.fromisoformat(entry["timestamp"]).strftime("%Y-%m-%d %H:%M")
        fname = entry.get("file", "?")[:18]
        overall = entry.get("overall_score", 0)
        scores = entry.get("scores", {})
        timing = scores.get("timing", 0)
        pitch = scores.get("pitch", 0)
        tempo = scores.get("tempo", 0)
        dynamics = scores.get("dynamics", 0)
        print(f"  {dt:<20} {fname:<20} {overall:>7}/100 {timing:>7}/100 {pitch:>7}/100 {tempo:>7}/100 {dynamics:>7}/100")

    if len(log) >= 2:
        first = log[0].get("overall_score", 0)
        last = log[-1].get("overall_score", 0)
        change = last - first
        print(f"\n  📈 Overall progress: {first} → {last} ({change:+d} points over {len(log)} sessions)")
    print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Music Practice Buddy — analyze practice recordings for objective feedback.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    p_analyze = sub.add_parser("analyze", help="Analyze a recording")
    p_analyze.add_argument("file", help="WAV recording file")
    p_analyze.add_argument("--target-bpm", type=int, help="Target BPM for comparison")
    p_analyze.add_argument("--output", help="Save full analysis as JSON")

    p_compare = sub.add_parser("compare", help="Compare two recordings")
    p_compare.add_argument("file1", help="First (earlier) WAV file")
    p_compare.add_argument("file2", help="Second (later) WAV file")

    p_plan = sub.add_parser("plan", help="Generate a practice plan")
    p_plan.add_argument("file", help="WAV recording to analyze")
    p_plan.add_argument("--instrument", default="any", help="Your instrument")
    p_plan.add_argument("--minutes", type=int, default=30, help="Practice session length")

    sub.add_parser("history", help="Show practice history and trends")

    args = parser.parse_args()

    if args.command == "analyze":
        cmd_analyze(args)
    elif args.command == "compare":
        cmd_compare(args)
    elif args.command == "plan":
        cmd_plan(args)
    elif args.command == "history":
        cmd_history(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
