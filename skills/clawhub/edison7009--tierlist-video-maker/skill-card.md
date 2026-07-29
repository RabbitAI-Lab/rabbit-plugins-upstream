## Description: <br>
Turns a published TierVibe tier list into a narrated video by fetching public tier-list data, capturing a high-resolution board image, preparing reviewable narration, generating TTS audio and subtitles, and composing the final video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators and agents use this skill to convert a published TierVibe ranking into a narrated video with a scrolling board background, enlarged card callouts, subtitles, and multilingual narration. It is intended for public TierVibe posts and includes review steps for card recognition and narration before final rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can install Python packages and Playwright Chromium and needs network access to TierVibe, CDN assets, and TTS services. <br>
Mitigation: Run it in a dedicated virtual environment and review dependency installation prompts and generated files before reuse. <br>
Risk: Narration text is sent to Microsoft edge-tts for online speech generation. <br>
Mitigation: Do not include sensitive, private, or copyrighted narration text unless that processing is acceptable. <br>
Risk: Image-card boards depend on multimodal recognition, and incorrect card labels can produce misleading narration. <br>
Mitigation: Use the board-first and per-card review workflow, ask the user for unclear labels, and require user review of the card manifest and narration before final rendering. <br>
Risk: Draft or editor-only TierVibe posts are not publicly readable and cannot provide the required board and card images. <br>
Mitigation: Use only published TierVibe post URLs or slugs and fail fast when the public post status is not published. <br>


## Reference(s): <br>
- [TierVibe API Reference](references/tiervibe-api.md) <br>
- [Project homepage](https://github.com/edison7009/TierList-Video-Maker) <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-video-maker) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, json, markdown, video, subtitles] <br>
**Output Format:** [Markdown instructions with shell commands and generated JSON, Markdown, MP4, MP3, and SRT files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user review of narration and image-card recognition before final video composition.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
