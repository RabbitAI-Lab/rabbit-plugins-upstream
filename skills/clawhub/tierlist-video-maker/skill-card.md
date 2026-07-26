## Description: <br>
Turns a published TierVibe tier list into a narrated video by fetching public list data and card images, capturing a board image, generating a reviewable narration script, producing TTS audio and subtitles, and composing the final video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators and agents use this skill to convert a published TierVibe tier list URL or slug into a narrated ranking video with subtitles. It is intended for published posts where a multimodal model can identify card images and the user can review the narration before video generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic setup may install Python packages and Chromium and may contact TierVibe/CDN resources and Microsoft online TTS during normal use. <br>
Mitigation: Run the skill in an isolated Python environment, review or preinstall pinned dependencies, and allow only the expected network destinations. <br>
Risk: Card identification and narration can be wrong when image recognition is unavailable or uncertain. <br>
Mitigation: Use a multimodal model, leave uncertain labels for user confirmation, and review the card manifest and narration before generating audio or video. <br>
Risk: Draft or still-editing TierVibe posts are unsupported and can fail because they are not publicly readable. <br>
Mitigation: Accept only published TierVibe posts and stop with a publish-first instruction when the URL or status is not public. <br>


## Reference(s): <br>
- [Source provenance: edison7009/TierList-Video-Maker](https://github.com/edison7009/TierList-Video-Maker/tree/main/plugins/tierlist-video-maker/skills/tierlist-video-maker) <br>
- [TierVibe API Reference](references/tiervibe-api.md) <br>
- [TierVibe public post format](https://tiervibe.com/t/{slug}) <br>
- [TierVibe public API endpoint](https://tiervibe.com/api/posts/{slugOrNumericId}) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [MP4 video, SRT subtitles, JSON manifests, Markdown review table, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a published TierVibe post, AI vision for card identification, network access for TierVibe/CDN resources and Microsoft online TTS, and user review of narration before final composition.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
