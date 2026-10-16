## Description:

Generates detailed images from text prompts, with optional reference images, for brand visuals and other demanding creative work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and brand teams use this skill to produce high-detail commercial key visuals and brand assets from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to the external dLazy service.

Mitigation: Confirm the service is acceptable before use and avoid sending sensitive prompts or files.

Risk: The external dLazy CLI requires an API key; login may store it locally.

Mitigation: Use an on-demand CLI invocation or DLAZY_API_KEY to reduce local persistence, and rotate or revoke keys in the dLazy dashboard if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image URLs]

**Output Format:** [Markdown with command examples and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images may be saved locally; asynchronous jobs may return a task ID instead of an immediate image.]

## Skill Version(s):

1.2.26 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
