## Description:

Midjourney style generation for artistic and strongly stylized creative images, with options for aspect ratio, bot type, and grid or U1-U4 output selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Midjourney-style creative images through the dLazy CLI, selecting prompt, aspect ratio, bot type, and output position.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy API.

Mitigation: Install only from the pinned @dlazy/cli@1.2.3 package and use npx or an isolated install when a persistent global binary is not desired.

Risk: Prompts and selected local files may be uploaded to dLazy services for generation.

Mitigation: Only pass prompts or files that are approved for upload to dLazy endpoints, and avoid sensitive local content unless the user has authorized it.

Risk: The skill requires a dLazy API key stored in local configuration or supplied through the environment.

Mitigation: Use a revocable API key, store it with user-only access, and rotate or revoke it if the CLI or execution environment is no longer trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [JSON response containing generated image output metadata and hosted result URLs, with optional downloaded image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task metadata when --no-wait is used; generated assets are hosted on files.dlazy.com.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
