## Description:

Analyzes a source image's visuals, composition, colors, lighting, and style, then uses dLazy's hosted image-replication service to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy image replication from an agent workflow, passing reference images and receiving generated image output in a similar style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy API and storage endpoints for generation.

Mitigation: Do not submit confidential images, media, or prompts unless uploading them to dLazy is intended and approved.

Risk: The dLazy API key may be stored in local CLI configuration for reuse.

Mitigation: Use per-invocation credentials or rotate and revoke the key when access is no longer needed.

Risk: A global CLI install persists third-party code on the host environment.

Mitigation: Prefer npx or a contained environment when a persistent global installation is unnecessary.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files]

**Output Format:** [JSON response with hosted image URLs and optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return task metadata for later polling.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
