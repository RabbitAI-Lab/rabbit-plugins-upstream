# WeChat Article Video Skill

Turn Chinese WeChat public-account articles and supplied images into polished
vertical videos for WeChat Channels.

The skill defines a reusable production workflow for:

- article analysis and evidence mapping
- information-complete 30-40 second edits
- 9:16 mobile-first layouts
- Edge TTS narration and subtitle synchronization
- HyperFrames or Remotion rendering
- visible first-frame covers
- medical-content safeguards and delivery QA

## Highlights

- Defaults to a `compact-standard` 30-40 second format for daily publishing.
- Preserves critical company, product, indication, specification, CTA, and
  disclaimer information.
- Uses real subtitle boundaries to synchronize scenes, captions, and narration.
- Requires a useful, non-black first encoded frame and a separate upload cover.
- Includes storyboard validation, contact-sheet generation, and video QA tools.

## Install

Clone the repository into your agent's skills directory:

```bash
git clone https://github.com/ToBeWin/wechat-article-video-skill.git
```

Then read `SKILL.md` and follow the workflow described there. The scripts expect
Python 3, FFmpeg/FFprobe, and `edge-tts`. HyperFrames or Remotion is required
only when that renderer is selected.

## Contents

```text
SKILL.md
agents/openai.yaml
references/
scripts/
```

The repository intentionally contains only the reusable skill source. It does
not include private article drafts, customer materials, generated media,
credentials, local filesystem paths, or environment files.

## Privacy And Compliance

- Review article text before sending it to any network TTS service.
- Keep API keys in environment variables and never commit them.
- Use only supplied or licensed visual assets.
- Preserve mandatory medical disclaimers and do not expand claims beyond the
  source material.

## License

MIT-0. See `LICENSE`.
