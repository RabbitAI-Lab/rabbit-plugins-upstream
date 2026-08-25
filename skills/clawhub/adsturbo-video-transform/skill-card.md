## Description:

AdsTurbo 视频改造 swaps video elements by replacing an on-screen person, animating a portrait from reference motion, or re-voicing a video in another language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and marketing teams use this skill to operate AdsTurbo video transformation workflows for character replacement, reference-motion portrait animation, and dubbed video translation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected videos, images, and audio are sent to AdsTurbo and upload steps can produce public URLs.

Mitigation: Use only media that the user owns or is authorized to transform, and avoid sensitive private footage unless the user accepts the upload and URL exposure.

Risk: The skill can alter a person's likeness or dubbed speech.

Mitigation: Confirm authorization for real people, avoid deceptive impersonation, and disclose transformed or translated media where appropriate.

Risk: Async task timeouts can be mistaken for failed jobs, causing duplicate submissions or charges.

Mitigation: Resume polling with the workspace ID after a timeout and resubmit only when the service reports a failed status.

## Reference(s):

- [Video Transform](references/video_transform.md)
- [Upload](references/upload.md)
- [Work Status](references/work.md)
- [AdsTurbo website](https://www.adsturbo.ai)
- [ClawHub skill page](https://clawhub.ai/adsturbo/skills/adsturbo-video-transform)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and final video result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous AdsTurbo tasks may return workspace IDs before final public result URLs are available.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
