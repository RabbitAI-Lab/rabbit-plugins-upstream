## Description:

Helps agents create videos from text, images, and reference media, and extend or locally edit existing videos through AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to generate video footage from prompts or visual references, extend clips, and edit parts of existing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded media are sent to AdsTurbo, and uploaded assets become publicly reachable URLs.

Mitigation: Obtain permission before uploading media; avoid private, regulated, or proprietary assets unless the public-URL exposure is acceptable.

Risk: Video generation consumes AdsTurbo credits, and retrying a timed-out job can incur duplicate charges.

Mitigation: Use idempotency keys for submissions and check the existing job status instead of resubmitting after a timeout.

## Reference(s):

- [AdsTurbo video generation guide](references/video_generation.md)
- [Media upload guide](references/upload.md)
- [Async task status guide](references/work.md)
- [AdsTurbo API key portal](https://adsturbo.ai/iris/api)
- [ClawHub skill listing](https://clawhub.ai/adsturbo/skills/adsturbo-video-generation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with video links and status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video jobs are asynchronous; the skill returns a video link when a job completes.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
