## Description:

文生图 Seedream 5.0 Lite generates images with Doubao Seedream 5.0 Lite from text prompts or image inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy Seedream 5.0 Lite CLI for text-to-image or image-to-image generation, optionally saving returned image assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external dLazy CLI package and hosted API.

Mitigation: Review the referenced dLazy CLI package before installation and use the pinned install or npx command from the metadata.

Risk: Prompts and explicitly provided media files are sent to dLazy services for generation.

Mitigation: Submit only prompts and media intended for dLazy processing, and avoid sending sensitive content unless that use is acceptable.

Risk: Authentication may store a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation API keys when appropriate, and rotate or revoke stored keys when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-5-0-lite)
- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI command guidance with JSON responses containing generated image URLs or async task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download generated image assets to a local path when --save is used; async mode returns a generateId for polling.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
