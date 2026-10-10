## Description:

Helps agents clean up videos by removing watermarks, logos, or hard-coded subtitles, upscaling resolution, and adding or translating subtitles through AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to prepare existing videos for publication or localization by improving resolution, removing visible marks or hard-coded subtitles, and adding translated subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos and uploaded local files are sent to AdsTurbo and may become publicly accessible by URL.

Mitigation: Upload only media you are authorized to share, and confirm that public URL access is acceptable before processing.

Risk: Removing watermarks, logos, or subtitles can obscure attribution or change how a video is understood.

Mitigation: Confirm the right to edit the video and review the processed result before publishing.

Risk: An exposed API key could permit unauthorized paid usage.

Mitigation: Keep the AdsTurbo API key in an environment variable and never include it in responses.

## Reference(s):

- [AdsTurbo Video Cleanup on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo-video-enhance)
- [Video enhancement guide](artifact/references/video_enhance.md)
- [Media upload guide](artifact/references/upload.md)
- [Task status guide](artifact/references/work.md)
- [AdsTurbo API key setup](https://adsturbo.ai/iris/api)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text with a processed-video URL when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video processing is asynchronous; tasks can be resumed using a workspace ID.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
