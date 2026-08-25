## Description:

Clean up a video without changing its content: remove watermarks, logos and burnt-in subtitles, upscale to 2K/4K, add or translate subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and video operators use this skill to clean existing videos by removing watermarks, logos, objects, or burnt-in subtitles, improving resolution, and adding or translating subtitles through AdsTurbo's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media may be uploaded to a public third-party AdsTurbo service under the user's API key.

Mitigation: Use only media the user is authorized to process, and avoid private, confidential, licensed, or third-party content unless authorization is clear.

Risk: Watermark, logo, or subtitle removal can alter visible attribution.

Mitigation: Confirm the user has rights to remove visible attribution before running removal workflows.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-video-enhance)
- [AdsTurbo Publisher Profile](https://clawhub.ai/user/adsturbo)
- [Video Enhance Reference](references/video_enhance.md)
- [Upload Reference](references/upload.md)
- [Work Status Reference](references/work.md)
- [AdsTurbo Website](https://www.adsturbo.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and final video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ADSTURBO_API_KEY and public media URLs or workspace IDs; asynchronous jobs may require polling.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
