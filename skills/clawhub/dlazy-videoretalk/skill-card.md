## Description:

Helps agents use dLazy VideoRetalk to synchronize a person's lip movements in a video with a supplied voice recording, optionally selecting a face with a reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in matching a speaker's mouth movements to replacement audio in an existing video, with optional face selection for videos with multiple people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted videos, audio, reference images, and parameters are sent to dLazy's cloud service.

Mitigation: Only submit media you are authorized to share and review the service terms before uploading sensitive content.

Risk: Installing the pinned third-party CLI or saving an API key locally introduces software and credential exposure.

Mitigation: Review the pinned @dlazy/cli package before installing and use DLAZY_API_KEY per run if a saved key is undesirable.

Risk: The skill's --prompt example and image-output example conflict with its VideoRetalk options and video purpose.

Mitigation: Check dlazy videoretalk -h for current parameters and verify returned media types instead of relying on those examples.

## Reference(s):

- [ClawHub Video Retalk skill](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Command guidance and JSON service responses with a generated-media URL or asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the generated media locally on request; asynchronous jobs require polling.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
