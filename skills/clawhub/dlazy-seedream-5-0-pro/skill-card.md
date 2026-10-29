## Description:

Seedream 5.0 Pro generates detailed images with strong typography and complex composition for commercial key visuals and brand assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and creative teams use the skill to generate polished campaign key visuals and brand assets from text prompts, optionally with reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy for generation, and requests consume account credits.

Mitigation: Avoid sending sensitive content and use --dry-run to review the payload and estimated cost before generation.

Risk: Logging in saves an API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it may have been exposed.

Risk: The skill relies on a third-party CLI package.

Mitigation: Review the pinned CLI package before installing it.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [@dlazy/cli package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-pro)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON result with generated image URLs and image metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 2K output and documented aspect ratios; asynchronous requests can return a task ID before images are ready.]

## Skill Version(s):

1.2.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
