---
name: speak
description: Speak text aloud through a Linux device's physical speaker using OpenClaw Talk.
metadata:
  openclaw:
    requires:
      bins:
        - openclaw
        - python3
        - aplay
    envVars:
      - name: SPEAK_ALSA_DEVICE
        required: false
        description: Optional ALSA playback device. Defaults to the system default device.
    os:
      - linux
---

# Speak

Use this skill when the assistant should say text aloud through the device's physical speaker.

## Usage

Run:

python3 {baseDir}/scripts/run.py "$SPEAK_TEXT"

where `$SPEAK_TEXT` is exactly the text that should be spoken.

## Architecture

The skill does not call an AI provider directly and does not handle provider API credentials.

The Python wrapper:

1. calls the local OpenClaw Gateway through the `openclaw` CLI;
2. invokes `talk.speak`;
3. requests WAV output;
4. decodes the returned Base64 audio;
5. plays it through ALSA using `aplay`.

The active OpenClaw Talk provider owns the speech model, voice, and provider credentials.

## Requirements

- Linux
- OpenClaw installed and configured
- an active OpenClaw Talk speech provider
- Python 3
- ALSA `aplay`

`SPEAK_ALSA_DEVICE` may optionally select a specific ALSA playback device.

## Rules

- Pass only the text that should be spoken.
- Do not read or expose provider API keys.
- Do not call OpenAI or another speech provider directly.
- Use OpenClaw `talk.speak` for synthesis.
