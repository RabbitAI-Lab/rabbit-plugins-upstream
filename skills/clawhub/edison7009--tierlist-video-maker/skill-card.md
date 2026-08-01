## Description: <br>
Turns a published TierVibe tier list into a narrated video by fetching public list data and card images, capturing the board, preparing a reviewable narration script, generating TTS audio and subtitles, and composing a scrolling tier-list video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, developers, and agents use this skill to turn a public TierVibe ranking into a narrated video with a card manifest, subtitles, and generated audio. It is intended for published TierVibe posts, with human review of labels and narration before final media generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill auto-installs Python packages and Chromium on first run. <br>
Mitigation: Run it in an isolated virtual environment or sandbox and review installation behavior before execution. <br>
Risk: Narration text is sent to an online Microsoft-backed TTS service. <br>
Mitigation: Avoid sensitive or private narration text and review the narration before generating TTS audio. <br>
Risk: Generated narration or card labels can be wrong when images are unclear or not reviewed. <br>
Mitigation: Review the card manifest and narration before TTS; ask the user for labels when card identity is uncertain. <br>


## Reference(s): <br>
- [TierVibe API Reference](artifact/references/tiervibe-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-video-maker) <br>
- [Project homepage](https://github.com/edison7009/TierList-Video-Maker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON manifests, narration text, MP3 audio, SRT subtitles, and MP4 video files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user review for card labels and narration; published TierVibe posts are required.] <br>

## Skill Version(s): <br>
1.0.10 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
