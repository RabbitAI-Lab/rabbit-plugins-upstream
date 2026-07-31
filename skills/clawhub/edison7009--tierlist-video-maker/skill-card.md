## Description: <br>
Turns a published TierVibe tier list into a narrated video by fetching public tier-list data, preparing card labels and narration, generating TTS audio and subtitles, and composing an MP4 with a scrolling board background. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, social media editors, and agents use this skill to turn a published TierVibe ranking into a reviewable narrated video workflow. It is useful when a user provides a public TierVibe URL or slug and wants a produced video, subtitles, narration assets, and a card-to-tier manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scripts auto-install media, browser, and TTS dependencies and may download a Chromium browser into the active Python environment. <br>
Mitigation: Run the workflow in a virtual environment or disposable workspace and review dependency installation before use. <br>
Risk: The workflow requires outbound network access to public TierVibe resources, package sources, a browser-helper CDN, and Microsoft edge-tts. <br>
Mitigation: Use it only where those network calls are acceptable, and review generated narration before creating audio or video. <br>
Risk: Image-card tier lists without detail text can require multimodal recognition, and incorrect labels can mislead narration. <br>
Mitigation: Use the board-first recognition, card manifest, and user review steps; ask the user to identify unclear cards instead of fabricating labels. <br>
Risk: Draft or private TierVibe posts do not provide the public board and card images needed for the workflow. <br>
Mitigation: Use only published public TierVibe posts and stop with a clear user message when a supplied post is not published. <br>


## Reference(s): <br>
- [TierVibe API Reference](artifact/references/tiervibe-api.md) <br>
- [TierList Video Maker repository](https://github.com/edison7009/TierList-Video-Maker) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Markdown, Files] <br>
**Output Format:** [Markdown guidance with shell commands plus generated JSON manifests, a review table, TTS audio, subtitles, and MP4 video files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a published TierVibe URL or slug; may require multimodal vision for image cards without detail and network access for TierVibe, package sources, browser assets, CDN-hosted browser helpers, and online TTS.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
