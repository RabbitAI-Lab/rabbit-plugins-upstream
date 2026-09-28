# Delivery Reference (image-with-comfyui)

The SKILL.md core says "send the media, in the user's session, no paths". This
file holds the per-channel delivery formats and the staging steps. Open it when
you need the exact prefix for a channel.

## The one rule

After generating, **send the file**, don't describe it. A text line like "video
attachment" is NOT a send.

## Per-channel format

| Channel | Format | Example |
|---|---|---|
| WhatsApp | `MEDIA:` + absolute path | `MEDIA:/home/user/.openclaw/media/outbound/angel_video.mp4` |
| Telegram | `MEDIA:` or `filePath:` | varies by implementation |
| Discord | Direct attachment | varies by implementation |

## Staging steps (WhatsApp)

1. Copy the output to `~/.openclaw/media/outbound/` first.
2. Send via `MEDIA:/home/user/.openclaw/media/outbound/<filename>` (use absolute file path).
3. The `MEDIA:` line must be the **sole content** of the WhatsApp message — no
   `[[reply_to_current]]`, no text before it — otherwise WhatsApp splits the file
   and text into two messages. For a caption use `MEDIA:./file.ext caption=...`.
4. **Clean up:** delete the staged file after a successful send so sensitive
   generated media doesn't linger across sessions.

## Always

- Deliver in the **user's original request session/thread** — not a separate
  topic/group/thread unless explicitly told.
- Never send raw local file paths, ComfyUI URLs, or host info unless asked.
