## Description:

Creates AI video from text, image, first/last-frame, and reference assets, and can extend or locally edit existing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate new video clips, extend existing clips, or perform localized video edits through AdsTurbo's API-backed workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to AdsTurbo, and uploaded assets become reachable by public URL.

Mitigation: Avoid private, regulated, biometric, or third-party media unless consent and service retention/access terms are acceptable.

Risk: The dependency constraint allows older requests releases.

Mitigation: Prefer pinning or updating to a currently patched requests version before deployment.

Risk: Resubmitting timed-out async video jobs can create duplicate work and charges.

Mitigation: Use the returned workspace ID to continue polling and use idempotency keys for retries.

## Reference(s):

- [AI Video Generation](artifact/references/video_generation.md)
- [Upload](artifact/references/upload.md)
- [Work Status](artifact/references/work.md)
- [AdsTurbo Website](https://www.adsturbo.ai)
- [ClawHub Skill Page](https://clawhub.ai/adsturbo/skills/adsturbo-video-generation)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown or text with command examples and generated video links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async AdsTurbo tasks may return workspace IDs before result URLs are ready.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
