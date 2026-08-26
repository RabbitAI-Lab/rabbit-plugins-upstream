## Description:

Clean up a video without changing its content: remove watermarks, logos and burnt-in subtitles, upscale to 2K/4K, add or translate subtitles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route video cleanup requests to AdsTurbo: watermark, logo, object, or hard-subtitle removal; 2K/4K upscaling; and subtitle generation or translation while preserving the video's content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded or selected videos may become accessible through public URLs and are sent to AdsTurbo for processing.

Mitigation: Avoid confidential, private, or regulated media unless AdsTurbo retention and access controls are acceptable for the use case.

Risk: Watermark, logo, or subtitle removal can be misused on media the user is not allowed to edit.

Mitigation: Use cleanup operations only on content the user owns or has permission to modify.

Risk: Polling timeouts do not mean the server task failed; resubmitting can create duplicate work or charges.

Mitigation: Resume polling with the existing workspace ID after a timeout instead of submitting the same job again.

Risk: The bundled dependency range allows any requests version greater than or equal to 2.28.0.

Mitigation: Pin and update the requests dependency according to the deployment environment before production use.

## Reference(s):

- [Video Enhance Reference](artifact/references/video_enhance.md)
- [Upload Reference](artifact/references/upload.md)
- [Work Status Reference](artifact/references/work.md)
- [AdsTurbo](https://www.adsturbo.ai)
- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-video-enhance)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline shell commands and returned video URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADSTURBO_API_KEY and public video URLs or uploaded assets; async tasks may return workspace IDs before final result URLs.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
