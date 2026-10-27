## Description:

Clone a voice from reference audio and generate spoken audio for new text using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can provide reference audio and text to generate speech in a cloned voice through dLazy's hosted Vidu Audio Clone service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference audio is uploaded to dLazy for voice cloning, and generated audio is hosted remotely.

Mitigation: Use only reference audio you have permission to clone and are comfortable uploading.

Risk: Authentication stores an API key locally, and generation can consume paid credits.

Mitigation: Protect the local key, review the pinned CLI before installation, and use the documented dry-run option to preview requests and estimated costs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [JSON response containing generated audio output URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated audio is hosted remotely; asynchronous requests may initially return task status without output URLs.]

## Skill Version(s):

1.3.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
