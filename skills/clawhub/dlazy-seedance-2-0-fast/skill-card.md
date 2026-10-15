## Description:

Generates short videos from text prompts, reference media, or first and last frames using dLazy's hosted Seedance 2.0 Fast service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request short videos from text, reference images, videos, audio, or first and last frames through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected media are sent to dLazy's hosted service.

Mitigation: Avoid confidential prompts and sensitive media unless their upload is approved.

Risk: The third-party CLI requires a dLazy API key and runs locally.

Mitigation: Review the linked CLI and package before installation; protect the key and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI homepage linked in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Video URLs, Video files]

**Output Format:** [CLI JSON response with hosted media URLs; optional downloaded video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of media URLs.]

## Skill Version(s):

1.3.28 (source: ClawHub server release; artifact header lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
