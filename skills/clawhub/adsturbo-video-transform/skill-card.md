## Description:

Helps agents replace a person in a video, animate a portrait from reference motion, or translate and re-dub a video using AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to swap on-screen presenters, animate still portraits from reference footage, or translate and re-dub video for other audiences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded videos, images, and related media URLs are sent to AdsTurbo; uploads may become externally accessible.

Mitigation: Only upload authorized, non-sensitive media after confirming that external processing and access are acceptable.

Risk: Swapping a person's likeness or re-dubbing a video can misrepresent that person or the original message.

Mitigation: Obtain appropriate permission for likeness and voice use, and review transformed output before sharing.

Risk: Retrying a timed-out task can create a duplicate billable job.

Mitigation: Check the existing workspace ID and continue polling rather than resubmitting; reuse an idempotency key when retrying after a network interruption.

## Reference(s):

- [ClawHub release](https://clawhub.ai/adsturbo/skills/adsturbo-video-transform)
- [Video transformation guide](references/video_transform.md)
- [Upload guide](references/upload.md)
- [Work status guide](references/work.md)
- [AdsTurbo API key portal](https://adsturbo.ai/iris/api)
- [AdsTurbo pricing](https://adsturbo.ai/pricing)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with video links and optional bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video processing is asynchronous; completed results are shared as links.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
