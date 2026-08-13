## Description:

Generate and edit images with Nano Banana Pro using text-to-image and image-to-image workflows through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate or edit images from prompts and optional image inputs with the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image paths can be uploaded to dLazy, and generated outputs are hosted by dLazy.

Mitigation: Avoid passing private files or sensitive prompt content unless the user intends to upload them to dLazy.

Risk: Image generation may consume dLazy account credits.

Mitigation: Use the CLI dry-run option for payload and cost estimation when cost or quota is uncertain.

Risk: A global CLI install persists a third-party binary and local API key configuration.

Mitigation: Prefer the pinned npx invocation or review the pinned CLI before global installation, and rotate or revoke API keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, image URLs, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image outputs are returned as hosted file URLs; async requests can return a task identifier for polling.]

## Skill Version(s):

1.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
