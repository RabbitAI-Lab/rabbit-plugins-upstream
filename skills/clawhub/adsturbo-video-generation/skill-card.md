## Description:

Helps agents generate videos from text, images, or reference assets and extend or edit existing videos through AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to generate video footage from prompts or images, interpolate frames, and extend or locally edit existing videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploading private, confidential, or regulated media makes it reachable through a public URL on a third-party service.

Mitigation: Upload only media intended to be sent to AdsTurbo and made publicly reachable; avoid sensitive materials.

Risk: An exposed API key could allow unauthorized use of the AdsTurbo account.

Mitigation: Keep the key in ADSTURBO_API_KEY and do not share it in chat or logs.

Risk: Resubmitting a job after a polling timeout can incur duplicate charges.

Mitigation: Check the existing job by workspace ID instead of resubmitting; use an idempotency key for retries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/adsturbo/skills/adsturbo-video-generation)
- [AdsTurbo API key workspace](https://adsturbo.ai/iris/api)
- [Video generation and model constraints](artifact/references/video_generation.md)
- [Asset upload requirements](artifact/references/upload.md)
- [Asynchronous task handling](artifact/references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with generated-video links and optional command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video jobs run asynchronously; a completed result is shared by link.]

## Skill Version(s):

1.2.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
