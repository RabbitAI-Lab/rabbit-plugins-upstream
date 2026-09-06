## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Jimeng images from text prompts, optionally with reference images, through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy/Jimeng services for generation.

Mitigation: Use the skill only with prompts and media that are acceptable to send to the third-party service.

Risk: The dLazy CLI can save an API key in the local user configuration file.

Mitigation: Prefer per-run DLAZY_API_KEY use, or verify restrictive permissions on ~/.dlazy/config.json after login or auth setup.

Risk: Normal generation calls may consume account credits.

Mitigation: Use dry-run or review cost expectations before running generation requests when credit use matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated image URLs or saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and selected local media may be sent to dLazy endpoints.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
