---
name: whisper-server
description: Set up fast, private speech-to-text for OpenClaw with a resident whisper.cpp server. Voice messages are transcribed on this machine, the Whisper model stays loaded so there is no reload per message, and nothing goes to the cloud. Use to install, check, or troubleshoot local transcription.
version: 0.1.0
metadata:
  openclaw:
    emoji: "🎙️"
    homepage: https://github.com/rickysinghmba/openclaw-whisper-server
    os: ["macos", "linux"]
    requires:
      bins:
        - curl
---

# Whisper server (local speech-to-text)

Sets up transcription that runs entirely on this machine, in two parts:

- `whisper-server`, from [whisper.cpp](https://github.com/ggml-org/whisper.cpp). It keeps the
  Whisper model loaded and listens on `127.0.0.1` only.
- The `openclaw-whisper-server` plugin. It makes that server OpenClaw's audio transcription
  provider, so incoming voice messages are transcribed without the agent running any commands.

Running the `whisper` or `whisper-cli` command for each message works too, but it loads the model
every time. This setup loads it once.

## Rules for this skill

- **Ask before you change anything.** Building software, downloading a model, installing the
  plugin, editing OpenClaw config and creating a login item each need the user's yes. Say what the
  step does and roughly how large the download is.
- **Check first.** Run the check script before proposing any setup step, and skip steps that are
  already done.
- **Loopback only.** Never start the server on `0.0.0.0` or another network address. It accepts
  file uploads and runs `ffmpeg`.
- **No cloud fallback.** If local transcription fails, report the error. Do not send the audio
  to another service unless the user asks.

## 1. Check what is already there

```bash
bash {baseDir}/scripts/check.sh
```

The script only reads. It reports whether the server answers, whether `ffmpeg` and
`whisper-server` are on the `PATH`, whether the plugin is installed, and whether OpenClaw is
configured to use it. Set `WHISPER_SERVER_URL` if the server is not on `http://127.0.0.1:8080`.

If every line says `ok` or `info`, setup is finished: go to step 6 to test. A line that says
`unknown` means an `openclaw` command failed, so that item could not be checked.

## 2. Build whisper.cpp with the server

The Homebrew `whisper-cpp` package does not include `whisper-server`, so build from source. This
needs `git`, `cmake` and a C++ compiler. The source takes about 60 MB on disk.

```bash
git clone --depth 1 https://github.com/ggml-org/whisper.cpp ~/whisper.cpp
cd ~/whisper.cpp
cmake -B build
cmake --build build -j --config Release
```

Then download a model. `base.en` is about 140 MB, English only, and fast. `small` or `medium`
are more accurate and slower. Use a model without `.en` for other languages.

```bash
sh ./models/download-ggml-model.sh base.en
```

The server also needs `ffmpeg` on the `PATH` to read voice notes (OGG/Opus, M4A, MP3). If the
check says it is missing, ask the user to install it with their package manager.

## 3. Start the server

```bash
~/whisper.cpp/build/bin/whisper-server -m ~/whisper.cpp/models/ggml-base.en.bin \
  --host 127.0.0.1 --port 8080 --convert
```

Check it with `curl -s http://127.0.0.1:8080/health`. While the model loads it answers
`{"status":"loading model"}`. When ready it answers `{"status":"ok"}`.

This command stops when the terminal closes. To keep the server running, see step 5.

## 4. Install the plugin and select it

```bash
openclaw plugins install openclaw-whisper-server --accept-capabilities
openclaw config set tools.media.models '[{"provider":"whisper-server","capabilities":["audio"]}]'
```

`--accept-capabilities` consents to the plugin registering an audio transcription provider. If
`tools.media.models` already lists other providers, show the user the current value and add the
`whisper-server` entry to it instead of replacing the list.

## 5. Keep the server running (optional, only if the user asks)

This creates a login item, so the server starts on its own and restarts if it stops. Explain
that to the user and get a clear yes first.

- **macOS:** copy `{baseDir}/templates/local.whisper-server.plist` to
  `~/Library/LaunchAgents/local.whisper-server.plist`, replace each `__WHISPER_DIR__` with the
  absolute path of the whisper.cpp folder and `__FFMPEG_DIR__` with the folder that holds
  `ffmpeg`, then run
  `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/local.whisper-server.plist`.
  To stop it: `launchctl bootout gui/$(id -u)/local.whisper-server`.
- **Linux:** copy `{baseDir}/templates/whisper-server.service` to
  `~/.config/systemd/user/whisper-server.service`, replace `__WHISPER_DIR__` the same way, then
  run `systemctl --user daemon-reload` and `systemctl --user enable --now whisper-server`.
  To stop it: `systemctl --user disable --now whisper-server`.

To remove the login item later, stop it as above and delete the file.

## 6. Test

```bash
openclaw infer audio transcribe --file /path/to/voice-note.ogg --json
```

The output should name `whisper-server` as the provider and contain the transcript.

## Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `unreachable` | The server is not running. Start it (step 3) or check the login item (step 5). |
| `loading` | The model is still loading. Wait a few seconds and retry. |
| Error mentioning WAV or audio data | `ffmpeg` is missing or the server was started without `--convert`. |
| `not-loopback` | The plugin's `baseUrl` points at another machine. Only `localhost`, `127.0.0.0/8` and `::1` are accepted. |
| `queue-full` | Too many voice messages at once. The server handles one at a time; raise `maxQueuedRequests` in the plugin config. |
| The transcript comes from another provider | `tools.media.models` does not list `whisper-server`. Repeat step 4. |
| `whisper-server: command not found` after `brew install whisper-cpp` | The Homebrew package has no server. Build from source (step 2). |

Plugin settings (`baseUrl`, `inferencePath`, `model`, `maxQueuedRequests`, `temperature`) go
under `plugins.entries.whisper-server.config`. See the
[plugin README](https://github.com/rickysinghmba/openclaw-whisper-server#readme).
