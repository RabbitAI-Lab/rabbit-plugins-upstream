## Description:

Generates images from text prompts or reference images using Doubao Seedream 5.0 Lite through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from prompts or transform reference images through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied local image inputs may be sent to dLazy's cloud service.

Mitigation: Use only prompts and files appropriate to share with this third-party provider.

Risk: The CLI may persist an API key locally, and a global installation adds third-party software to the system.

Mitigation: Use the per-invocation environment variable when local key storage is unsuitable; consider npx or review the pinned npm package before global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image files]

**Output Format:** [JSON response containing generated image URLs; optional downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID instead of an immediate image URL.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
