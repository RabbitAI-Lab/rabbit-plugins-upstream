## Description:

Helps agents generate scalable design assets from text prompts using dLazy's hosted Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request logos, icons, and other scalable design assets from text prompts through dLazy's image-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and deliberately supplied files may be sent to dLazy's hosted service.

Mitigation: Review the service and CLI before installing, and avoid submitting sensitive prompts or files without approval.

Risk: Authentication may save an API key locally.

Mitigation: Protect local credentials and rotate or revoke keys when needed.

Risk: The skill describes SVG output, but its sample response identifies a PNG asset.

Mitigation: Confirm the delivered file format before relying on an SVG workflow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation responses include an asset URL; the example shows PNG despite the SVG description.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
