## Description:

Generate and edit images with Nano Banana Pro using text prompts or input images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through dLazy's hosted Nano Banana Pro service with text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media files may be uploaded to dLazy for hosted image generation.

Mitigation: Use the skill only when cloud processing is acceptable, and avoid sending sensitive media or confidential prompt content.

Risk: Generated files are hosted by dLazy and API credits may be consumed.

Mitigation: Review output URLs before sharing and use dry-run or cost-estimate behavior when credit usage matters.

Risk: A dLazy API key may be stored in the local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY on shared machines or verify permissions on ~/.dlazy/config.json.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Configuration instructions]

**Output Format:** [JSON responses with image URLs, optional downloaded image files, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI package; asynchronous runs can return a generateId for polling.]

## Skill Version(s):

1.2.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
