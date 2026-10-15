# Delivery Reference (music-with-comfyui)

The SKILL.md core says "send the audio, in the user's session, no paths". This
file holds the per-channel delivery formats and the staging steps. Open it when
you need the exact prefix for a channel.

## The one rule

After generating, **send the file**, don't describe it. A text line like
"music attachment" is NOT a send.

## Per-channel format

| Channel | Format | Example |
|---|---|---|
| WhatsApp | `MEDIA:` + absolute path | `MEDIA:/home/user/.openclaw/media/outbound/song.mp3` |
| Telegram | `MEDIA:` or `filePath:` | varies by implementation |
| Discord | Direct attachment | varies by implementation |

## Staging steps

1. Copy the output to `~/.openclaw/media/outbound/` first.
2. Send via `MEDIA:/home/user/.openclaw/media/outbound/<filename>` (absolute path).
3. The `MEDIA:` line must be the **sole content** of the message — no
   `[[reply_to_current]]`, no text before it — otherwise WhatsApp splits the file
   and text into two messages. For a caption use `MEDIA:./file.ext caption=...`.
4. **Clean up:** delete the staged file after a successful send so generated
   audio doesn't linger across sessions.

## Telegram gotchas (measured 2026-10-06)

These were verified on the live channel (text delivery confirmed working, file
upload path failing). Follow these exactly or the file will not arrive.

- **`MEDIA:` must be the SOLE content of the message** — no text before it, no
  `[[reply_to_current]]`. Any preceding text makes Telegram split the message
  into "text + file", and the file often does not land. Put the file on its own
  line, alone, as the whole message.
- **Use pure ASCII filenames** in `~/.openclaw/media/outbound/`. Chinese/non-
  ASCII filenames (e.g. `404副歌_take2.zip`) reliably fail the Telegram upload
  (`Network request for 'sendDocument' failed!`). Copy to an ASCII name first
  (`404_tak2.zip`), then send.
- **Do NOT use the `message` tool's attachment/upload-file path** for Telegram.
  `sendDocument` / `upload-file` return `Network request ... failed!`. The
  `MEDIA:` + plain-text-line path is the one that works.
- If a previous attempt failed, **do not immediately re-send** the same message.
  Re-check the file exists, confirm the filename is ASCII, then send once more.

## Always

- Deliver in the **user's original request session/thread** — not a separate
  topic/group/thread unless explicitly told.
- Never send raw local file paths, ComfyUI URLs, or host info unless asked.
- **WhatsApp: always transcode to 44.1 kHz** (AceStep writes 48 kHz, which does
  not play on WhatsApp). `ffmpeg -y -i <src> -c:a aac -b:a 128k -ar 44100 -ac 1
  -movflags +faststart <out>.m4a`, then send the .m4a.
- **User wants original file**: do NOT transcode. Zip the original audio and
  send it as a document attachment.
