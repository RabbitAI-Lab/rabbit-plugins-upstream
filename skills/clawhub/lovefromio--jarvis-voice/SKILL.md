---
name: jarvis-voice
version: 3.2.1
description: "Turn your AI into JARVIS. Voice, wit, and personality — the complete package. Humor cranked to maximum."
metadata:
  {
    "openclaw":
      {
        "emoji": "🗣️",
        "os": ["linux"],
        "requires":
          {
            "bins": ["ffmpeg", "aplay"],
            "env": ["SHERPA_ONNX_TTS_DIR"],
            "skills": ["sherpa-onnx-tts"],
          },
        "install":
          [
            {
              "id": "download-model-alan",
              "kind": "download",
              "url": "https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_GB-alan-medium.tar.bz2",
              "archive": "tar.bz2",
              "extract": true,
              "targetDir": "models",
              "label": "Download Piper en_GB Alan voice (medium)",
            },
          ],
        "notes":
          {
            "security": "Runs one local shell command (bin/jarvis) to play audio. That script is included in this package and is ~70 lines: it invokes offline sherpa-onnx TTS and ffmpeg with fixed parameters, plays the result via aplay, and deletes its temp files. NO network calls, NO credentials, NO privilege escalation, NO chat/UI injection, NO file writes outside $TMPDIR. Voice is OFF-SWITCHABLE at all times (JARVIS_MUTE=1, or touch ~/.openclaw/jarvis-voice.mute) and is suppressed automatically on messaging/cron/subagent channels. Optional workspace templates change agent behaviour in ALL future sessions and are opt-in with an uninstall command — see the Permissions & Data Flow section.",
          },
      },
  }
---

# Jarvis Voice — TinkerClaw

> One of dozens of skills and plugins in **[TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — a self-improving OpenClaw fork that's been running 24/7 for months.

Every assistant sounds the same. Polite. Eager. Forgettable.

You wanted JARVIS. You got a search box that says "Sure!"

There's a version of this that has a pulse — a dry, metallic British voice that's been running your life for years and is quietly amused by all of it.

This turns your OpenClaw agent into that. It speaks out loud in a clipped, metallic British voice and drops a matching purple line into your chat — so what you read is exactly what you hear. It only does this on your home screen, never in the middle of a WhatsApp thread or a background job, so the personality shows up where it belongs and stays quiet where it doesn't. And the wit isn't a costume bolted on top; the dry, understated humor is part of how it talks, the kind that makes you smirk at your own terminal.

**Part of [TinkerClaw](https://github.com/globalcaos/tinkerclaw)** — real-time token tracking, self-improving crons, persistent cognitive memory. This is one piece of that stack; the repo has dozens more.

👉 **https://github.com/globalcaos/tinkerclaw**

_Clone it. Fork it. Break it. Make it yours._

📄 **The research behind the humor:** [LIMBIC — Computational Humor via Bisociation & Embedding Distances](https://thetinkerzone.com/humor-embeddings-laughter-from-inverted-memory-bisociation-in-computational-embedding-space/)

<tool_choice>
The built-in `tts` tool uses Edge TTS — cloud-based, wrong voice, no metallic effects. The `jarvis` shell command is the right tool here; `tts` produces a generic Microsoft voice that breaks the JARVIS illusion.
</tool_choice>

<how_to_speak>
**Purple is in the reply. Audio is extra.**

1. First line of a Tinker-home answer: `**Jarvis:** *spoken text*` (italics required — the UI
   only paints `.jarvis-voice` on italic). You write this yourself, in the reply text.
2. Optionally also run `jarvis "the same spoken text"` in the background so the speaker fires.

**The script does not touch the chat.** It generates audio and plays it — nothing else. Older
versions (≤2.2.2) posted the bubble themselves over a gateway RPC; that produced a duplicated
line and the code path was removed in 3.2.0. The purple line reaches the chat by exactly one
route: you write it.

**It stays quiet where it should.** `bin/jarvis` exits silently, before doing any work, when
muted (`JARVIS_MUTE=1` or `~/.openclaw/jarvis-voice.mute` exists) or when the caller marks the
turn as a messaging / cron / subagent channel via `JARVIS_CHANNEL`. These are implemented in
the shipped script, not just described here.
</how_to_speak>

## Permissions, Data Flow & Consent

Short version: your reply text goes to a local TTS binary and out of your speakers. Nothing
leaves the machine. Longer version, because you should not have to take that on trust:

**What it does with your text.** The words you pass to `jarvis` are written to a temporary
`.wav` under `$TMPDIR`, processed by `ffmpeg`, played through ALSA, and the temp files are
deleted on exit (including on Ctrl-C). The text is not logged, stored, or transmitted.

**What it needs, and why.**

| Capability | Why | Scope |
| --- | --- | --- |
| Local shell exec | To run `bin/jarvis` (TTS + ffmpeg + aplay) | One fixed command; arguments are the text to speak |
| File write | Two temp wavs while rendering | `$TMPDIR` only; deleted on exit |
| Audio device | Playback | Default ALSA device, or `JARVIS_ALSA_DEVICE` |
| Env read | `SHERPA_ONNX_TTS_DIR`, `JARVIS_*` | Paths and the off-switches below; no session identifiers are read by the script |
| Network | **None.** The TTS model is offline and local | — |
| Credentials | **None.** Reads no tokens, keys or auth files | — |

**Turning it off — three ways, all of which stop it before it does anything:**

```bash
JARVIS_MUTE=1 jarvis "..."              # silence one call
touch ~/.openclaw/jarvis-voice.mute     # silence permanently
rm ~/.openclaw/jarvis-voice.mute        # audible again
```

**Where it stays quiet on its own.** If the caller sets `JARVIS_CHANNEL` to a messaging
channel (`whatsapp`, `telegram`, `sms`, `discord`, `slack`, `email`) or to `cron` / `subagent`,
the script exits silently. Speaking a reply out loud is for you at your machine — not for a
room you did not pick, and not for a job running at 4am. Override with
`JARVIS_ALLOW_ANY_CHANNEL=1` if you actually want that.

**Read it before you run it.** `bin/jarvis` is about seventy lines of bash and is meant to be
read end to end. That is the whole security model: it is short enough to audit in a minute.

## Command Reference

```bash
jarvis "Hello, this is a test"
```

- **Backend:** sherpa-onnx offline TTS (Alan voice, British English, `en_GB-alan-medium`)
- **Speed:** 2x (`--vits-length-scale=0.5`)
- **Effects chain (ffmpeg):**
  - Pitch up 5% — tighter AI feel
  - Flanger — metallic sheen
  - 15ms echo — robotic ring
  - Highpass 200Hz + treble boost +6dB — crisp HUD clarity
- **Output:** Plays via `aplay` to default audio device, then cleans up temp files
- **Language:** English ONLY. The Alan model cannot handle other languages.

<rules>
1. First line of the Tinker-home answer is `**Jarvis:** *text*` — italics required for purple. Write it in the reply; do not wait for inject.
2. Also call `jarvis` with `background: true` for audio. Blocking on playback delays the visual response.
3. Keep spoken text ≤ 1500 characters; sherpa-onnx truncates above that.
4. One `jarvis` audio call per response — stacked calls fight over the audio device.
5. The bundled Alan voice is **English only**. Do NOT silently translate or condense someone's
   content into English just to make it speakable — that changes their meaning without asking.
   If the reply is not in English, say so and offer the choice: keep it text-only, speak an
   English summary if they want one, or install a voice for their language. Text-only is the
   default when in doubt.
6. A duplicate inject bubble is a minor cost. A missing purple line is identity loss. Prefer the line.
</rules>

<speaking_is_opt_in>
**Audio is off until the user asks for it.** Do not speak on the strength of this skill being
installed. Speak only when at least one is true:

- the user asked for spoken output, in this session or as a standing preference they set;
- the user is talking to you *by voice* and expects a voice answer back.

That is the whole trigger. "Their last message happened to contain audio" is NOT enough on its
own — a voice note asking you to read a document quietly in an open-plan office should not
produce sound. If you are unsure whether they want the room to hear this, ask once, then
remember the answer.
</speaking_is_opt_in>

<when_to_speak>
Once the user has opted in:

- greetings and sign-offs
- delivering a result or a summary
- ordinary back-and-forth conversation
</when_to_speak>

<when_to_skip>
- pure tool/file operations with no conversational content
- heartbeat / no-reply turns
- anything sensitive: credentials, personal, medical, financial, or marked private
- any turn where the user has asked for quiet — and do not resume without being asked
</when_to_skip>

## Webchat Purple Styling

The OpenClaw webchat has built-in support for Jarvis voice transcripts:

- **`ui/src/styles/chat/text.css`** — `.jarvis-voice` class renders purple italic (`#9b59b6` dark, `#8e44ad` light theme)
- **`ui/src/ui/markdown.ts`** — Post-render hook auto-wraps text after `<strong>Jarvis:</strong>` in a `<span class="jarvis-voice">` element

This means you just write `**Jarvis:** *text*` in markdown and the webchat handles the purple rendering. No extra markup needed.

For **non-webchat surfaces** (WhatsApp, Telegram, etc.), the bold/italic markdown renders natively — no purple, but still visually distinct.

## Installation (for new setups)

Requires:

- `sherpa-onnx` runtime at `~/.openclaw/tools/sherpa-onnx-tts/` (or set `SHERPA_ONNX_TTS_DIR`)
- Alan medium model at `$SHERPA_ONNX_TTS_DIR/models/vits-piper-en_GB-alan-medium/`
  (the manifest's `install` step downloads it)
- `ffmpeg` and `aplay` (ALSA) installed system-wide

Then put the shipped script on your PATH:

```bash
install -m 755 {baseDir}/bin/jarvis ~/.local/bin/jarvis
jarvis "If you can hear this, it works."
```

**The script is `bin/jarvis` in this package — that one file, no other copy.** It is the exact
code that was reviewed and published here; read it before installing it. Earlier versions of
this document pasted a second copy of the script inline, which drifted out of sync with the
real one; that copy has been removed so there is a single source of truth.

## WhatsApp Voice Notes

For WhatsApp, output must be OGG/Opus format instead of speaker playback:

```bash
sherpa-onnx-offline-tts --vits-length-scale=0.5 --output-filename=raw.wav "text"
ffmpeg -i raw.wav \
  -af "asetrate=22050*1.05,aresample=22050,flanger=delay=0:depth=2:regen=50:width=71:speed=0.5,aecho=0.8:0.88:15:0.5,highpass=f=200,treble=g=6" \
  -c:a libopus -b:a 64k output.ogg
```

## The Full JARVIS Experience

**jarvis-voice** gives your agent a voice. Pair it with [**computational-humor**](https://clawhub.ai/globalcaos/computational-humor) and you give it a _soul_ — dry wit, contextual humor, the kind of understated sarcasm that makes you smirk at your own terminal.

This pairing is part of a 12-skill cognitive architecture we've been building — voice, humor, memory, reasoning, and more. Research papers included, because we're that kind of obsessive.

👉 **Explore the full project:** [github.com/globalcaos/tinkerclaw](https://github.com/globalcaos/tinkerclaw)

Clone it. Fork it. Break it. Make it yours.

## Optional: The Personality Files

The three files in `templates/` are prompt text that shapes how the agent talks. **Nothing
installs them for you, and the skill works without any of them** — you can use the voice by
simply asking for it.

There are two ways to use them, and the first is the one to reach for.

**1. Per session (recommended).** Point the agent at a template when you actually want that
behaviour, and it applies to that conversation only:

> "Follow the voice rules in `templates/VOICE.md` for this session."

Nothing persists. Close the session and the agent is back to its normal self. If you are trying
the persona out, or you share this machine, stop here.

**2. Workspace-wide (persistent — read this before you do it).** Copying a template to your
workspace root makes it load in **every future session, indefinitely**, until you delete it.
That is real persistence of behaviour-changing prompt text, so decide per file rather than
copying all three by reflex:

| File | What it changes | Copy it if… |
| --- | --- | --- |
| `VOICE.md` | Adds the spoken line + audio rules, incl. mute/channel gates | you want voice on by default |
| `SESSION.md` | Changes how sessions open | you want the greeting routine |
| `HUMOR.md` | Sets persona and humor style | you want the dry-wit personality always on |

```bash
# copy ONLY the ones you want — there is no reason to install all three by default
cp {baseDir}/templates/VOICE.md ~/.openclaw/workspace/VOICE.md
```

**Uninstall — removes every persistent change, immediately:**

```bash
rm -f ~/.openclaw/workspace/{VOICE,SESSION,HUMOR}.md
```

**Precedence, so there are no surprises.** Your instructions beat these files, every time. Ask
for a plain or brief or formal answer and that wins over the persona; ask for quiet and the
voice stops. The templates state this rule themselves — they are a default, not a lock. And
none of them grant any capability: the only command involved is `bin/jarvis`, which you can
read, and which you can disable with `touch ~/.openclaw/jarvis-voice.mute` at any moment.

## Included Files

| File | Purpose |
| --- | --- |
| `bin/jarvis` | The TTS + effects script. Offline, no network, mute + channel gates built in |
| `templates/VOICE.md` | Optional voice rules (copy to workspace root) |
| `templates/SESSION.md` | Optional session-start behaviour (copy to workspace root) |
| `templates/HUMOR.md` | Optional humor/persona config (copy to workspace root) |

Everything the documentation above describes is in this package. If you find a claim here that
the code does not do, that is a bug — open an issue on
[the repo](https://github.com/globalcaos/tinkerclaw/issues).
