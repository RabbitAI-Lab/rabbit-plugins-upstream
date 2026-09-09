## Description:

Generates 4MP high-resolution raster images suitable for print-ready assets and large-scale use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent generate high-resolution raster images through the dLazy Recraft V4 Pro CLI and retrieve or save the resulting image assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and selected local media files to the dLazy hosted API and media storage.

Mitigation: Use it only with data that may be processed by dLazy services, and review organization data-handling requirements before sending sensitive content.

Risk: Authentication requires trusting the dLazy CLI and storing or supplying a dLazy API key.

Mitigation: Prefer temporary npx execution when avoiding a persistent global binary, keep API keys scoped to the intended organization, and rotate or revoke keys when access is no longer needed.

Risk: Generated assets are returned from dLazy-hosted file URLs.

Mitigation: Download and review generated files before redistribution, and avoid assuming hosted URLs are a permanent archive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-pro)
- [dLazy CLI project homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The invoked CLI can return hosted PNG image URLs, save generated assets locally, or return an asynchronous generation ID for polling.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
