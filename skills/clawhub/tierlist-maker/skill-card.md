## Description: <br>
Turn a published TierVibe tier list into a narrated video by fetching public tier-list data and card images, capturing a high-resolution board image, generating a reviewable narration script, producing TTS audio and subtitles, and composing the final video. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edison7009](https://clawhub.ai/user/edison7009) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to turn published TierVibe tier lists into narrated videos with reviewable card mappings, narration, subtitles, and generated media outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install Python video, TTS, and browser dependencies and download Chromium into the active environment. <br>
Mitigation: Run it in a dedicated virtual environment and review dependency installation before use. <br>
Risk: Narration text is sent to Microsoft online TTS. <br>
Mitigation: Avoid private or sensitive narration text and review the script before generating audio. <br>
Risk: The workflow downloads public TierVibe content and card images from supplied post URLs. <br>
Mitigation: Use only intended published TierVibe posts and verify the URL before running the fetch and capture steps. <br>
Risk: AI vision or derived labels can misidentify image cards without clear text or detail. <br>
Mitigation: Review the generated card manifest and narration before composing the final video, and ask the user for unclear card labels instead of guessing. <br>


## Reference(s): <br>
- [TierVibe API Reference](references/tiervibe-api.md) <br>
- [Project homepage](https://github.com/edison7009/TierList-Video-Maker) <br>
- [ClawHub skill page](https://clawhub.ai/edison7009/skills/tierlist-maker) <br>
- [Publisher profile](https://clawhub.ai/user/edison7009) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON, Markdown, Files] <br>
**Output Format:** [Markdown guidance with shell commands plus generated JSON, Markdown, subtitles, audio, images, and MP4 video files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces reviewable manifests and narration before composing final media; no credential environment variables were detected in server evidence.] <br>

## Skill Version(s): <br>
1.0.10 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
