## Description:

Helps agents create videos from text, images, and reference media, or extend and locally edit existing videos through AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to generate video clips from prompts or media references, extend footage, and edit selected parts of a video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images, audio, or video may be accessible through public URLs, and prompts and selected media are sent to AdsTurbo.

Mitigation: Avoid confidential or sensitive media unless you accept that exposure and AdsTurbo's retention and access practices.

Risk: Resubmitting a still-running video task can incur duplicate usage charges.

Mitigation: Check the existing task's status after a timeout rather than resubmitting; use the same idempotency key for retries.

## Reference(s):

- [AdsTurbo Video Generation on ClawHub](https://clawhub.ai/adsturbo/skills/adsturbo-video-generation)
- [Video generation and model options](references/video_generation.md)
- [Media upload guidance](references/upload.md)
- [Async task status guidance](references/work.md)
- [AdsTurbo API access](https://adsturbo.ai/iris/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with video result links and optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A completed request returns a video link; generation is asynchronous.]

## Skill Version(s):

1.2.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
