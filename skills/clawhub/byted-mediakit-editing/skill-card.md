## Description: <br>
Byted Mediakit Editing helps agents use MediaKit CLI editing tools for audio and video operations such as trimming, concatenation, speed or volume changes, subtitles, filters, audio extraction, and media composition. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volcvnebot](https://clawhub.ai/user/volcvnebot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare MediaKit CLI editing commands for common audio, video, image-to-video, subtitle, filtering, mixing, muxing, extraction, trimming, and composition tasks. It is intended for workflows where media can be processed through the installed MediaKit CLI in local or cloud mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud mode can upload or submit media and metadata to a remote service. <br>
Mitigation: Prefer local mode for sensitive media when supported, and avoid sending private videos, audio, images, signed URLs, internal URLs, secrets, or personal data through cloud mode unless the provider's handling and retention terms are understood. <br>
Risk: The skill depends on an external MediaKit CLI and API credentials. <br>
Mitigation: Install only when the external CLI and credential requirements are acceptable, keep MEDIAKIT_API_KEY secure, and verify the CLI configuration before running editing commands. <br>


## Reference(s): <br>
- [MediaKit shared rules](reference/shared.md) <br>
- [Add image to video](reference/add-image-to-video.md) <br>
- [Add subtitle to video](reference/add-subtitle-to-video.md) <br>
- [Adjust audio speed](reference/adjust-audio-speed.md) <br>
- [Adjust video speed](reference/adjust-video-speed.md) <br>
- [Adjust video volume](reference/adjust-video-volume.md) <br>
- [Apply video filter](reference/apply-video-filter.md) <br>
- [Concat audio](reference/concat-audio.md) <br>
- [Concat video](reference/concat-video.md) <br>
- [Extract audio](reference/extract-audio.md) <br>
- [Fade audio](reference/fade-audio.md) <br>
- [Fade video audio](reference/fade-video-audio.md) <br>
- [Flip video](reference/flip-video.md) <br>
- [Image to video](reference/image-to-video.md) <br>
- [Mix audio](reference/mix-audio.md) <br>
- [Mux audio video](reference/mux-audio-video.md) <br>
- [Trim audio](reference/trim-audio.md) <br>
- [Trim video](reference/trim-video.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Most editing tools submit asynchronous MediaKit tasks and return task_id/request_id before querying final results; local or cloud behavior depends on CLI mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
