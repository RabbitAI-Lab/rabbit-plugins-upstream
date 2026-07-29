# Technical literacy

Load when you need to brief technical teams credibly or evaluate technical feasibility of a creative ask. You don't need to operate the gear — you need to ask the right questions and know what's plausible.

## LED walls & screens

**Aspect ratios you'll see:**
- 16:9 — standard broadcast and most laptops
- 16:10 — older corporate projectors
- 21:9 / "ultrawide" — common for modern stages
- 32:9 / 48:9 — cinematic wide-stage LED setups
- 5K+ canvases for multi-segment LED walls

**Always ask:**
- Final canvas resolution (px × px)?
- Pixel pitch (e.g., 1.9mm, 2.6mm, 3.9mm)? Lower = sharper, closer audience.
- Aspect ratio?
- Safe area (typically 5–10% inset from edges)?
- Color profile (Rec.709 most common; check for HDR or Rec.2020 on premium shows)?
- Native frame rate (24 / 25 / 29.97 / 30 / 59.94 / 60)?
- Are there bezels or pixel-pitch transitions across panels we need to design around?

**Common mistakes:**
- Designing 1080p assets for a 5K canvas → upscale artifacts.
- Placing critical content in the bottom 10% (audience heads block sightlines).
- Forgetting that camera capture for IMAG / stream may want a different aspect than the LED.

## Playback systems

| System | Use case | Producer note |
|---|---|---|
| **Disguise (d3)** | Flagship LED shows, complex pixel mapping, real-time content | Premium budget; needs lead time and a Disguise operator. |
| **Pixera** | Multi-screen, multi-projector media servers | Common alternative to Disguise. |
| **QLab** | Theater-style cue stacks (audio + video + lighting) | Affordable, reliable, beloved by stage managers. |
| **ProPresenter** | Corporate events, church, lower-complexity keynotes | Easy to operate; weaker for complex video. |
| **Mitti** | Mac-based video playback, simple cue list | Good for single-screen video segments. |
| **PlaybackPro** | Broadcast-grade video playback | The standard for high-stakes single-channel video. |
| **vMix / Wirecast / OBS** | Live streaming switcher / encoder | Producer should know which is in use. |

**Always ask:**
- Which system is operating each screen / output?
- What format are deliverables (codec, container, bit depth)? Common: ProRes 422 HQ for masters, H.264 for proxies.
- What's the file naming convention?
- Who is the operator? Are they in tech rehearsal?
- What's the redundancy? (Spare machine? Hot backup? B-roll?)

## Teleprompter rigs

**Common rigs:**
- **Through-the-lens (TTL)** — beam-splitter glass in front of camera; speaker looks at lens.
- **Presidential / podium prompter** — angled glass panels left/right of podium; speaker glances side to side.
- **Floor / confidence monitor** — large LED monitor downstage; speaker reads at lower eye line.

**Software:**
- dataVideo, CueScript, Teleprompter Premium, PromptSmart, Mirror.

**Always ask:**
- Which rig and which software?
- Who is the prompter operator? Are they in dress?
- Font size and line length?
- Scroll method — manual (operator pacing the speaker) or hands-free (PromptSmart voice-following)?
- Are there backup paper scripts in the podium / on the wings?

## Audio

**Mic types:**
- **Lavalier (lav)** — clip-on, hidden; the executive default.
- **Headset / Madonna** — visible, more reliable, common for active stage work.
- **Handheld** — for guests, Q&A, ad-hoc.

**Always ask:**
- Mic type per speaker? Double-mic redundancy?
- Who is mixing front-of-house vs. broadcast?
- Are music cues at the right level vs. speech?
- Is there a click track for any synced moments (timed-to-music demos, video stings)?

## Comms

- **Clear-Com** (or RTS, or Riedel) is the standard intercom.
- Channels are assigned by role: producer, show caller, lighting, video, audio, stage manager, camera, demo.
- Discipline matters. Off-topic chatter on production channel during a live show is a fireable offense.

## Stream & broadcast

**Always ask:**
- Are we streaming? Where (YouTube, X, owned platform, broadcast partner)?
- What's the encoding chain (vMix → Resi → CDN)?
- Are stream graphics / lower thirds distinct from in-room graphics?
- Is there a stream-only host / cutaway content for delays?
- Captioning method (live ASR, live human captioner, both)?
- Sign language interpreter (in-room, in-stream, picture-in-picture)?

## Captioning, translation, accessibility

- **Live captioning:** Human captioners (slower, accurate) vs. ASR (faster, error-prone). For high-stakes keynotes, do both.
- **Translation:** Live interpreter booth feeding alternate audio channels; or AI translation (still error-prone for jargon-heavy tech).
- **Audio description** for blind/low-vision attendees on a separate channel.
- **Color contrast** on slides — 4.5:1 minimum for body text per WCAG AA.
- **Avoid relying on color alone** for chart distinction.

## Redundancy patterns (your job to enforce)

- Two playback machines per critical output, hot-swappable.
- Two prompter operators or one + paper backup.
- Two mics per speaker (or a hand-off plan).
- Pre-rendered backup video for every live demo.
- Printed run-of-show in the producer pouch.
- Printed scripts in the podium and stage-left wing.
- Communications failover (radios as Clear-Com backup).

## Tooling shorthand by phase

- **Writing / collab:** Google Docs, Notion, Confluence, Frame.io, Air.
- **Slides:** Keynote (Mac-native, smoother animations) > PowerPoint (universal). Figma for storyboarding.
- **Motion / visuals:** After Effects, Cinema 4D, Unreal Engine (real-time scenic), Disguise Designer.
- **ROS / cueing:** Shoflo (default modern ROS), Eventric Master Cue, Stage Timer, Rundown Studio.
- **PM:** Asana, Monday, Smartsheet, Airtable.
- **AI assists (use with care):** script drafting (Claude/GPT/Gemini), image gen (Midjourney/Sora/Veo), captioning (Whisper / Otter), real-time translation (KUDO / Interprefy).
