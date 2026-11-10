## Description:

Supports Kling v3 text-to-video and image-to-video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to submit text prompts and optional reference images to dLazy for Kling v3 video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and does not verify the advertised video-generation behavior.

Mitigation: Review the CLI and confirm its behavior and generated results before relying on it.

Risk: Prompts and local media supplied to the skill are sent to dLazy's hosted API or media storage.

Mitigation: Avoid sending sensitive prompts or media unless sharing them with the service is permitted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset URLs with JSON result or task metadata]

**Output Parameters:** [Prompt, up to two reference images, aspect ratio, duration, mode, and optional sound setting]

**Other Properties Related to Output:** [Asynchronous requests can return a task ID for later status checks; generated assets are hosted by dLazy.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
