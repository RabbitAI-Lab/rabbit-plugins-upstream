## Description:

Helps agents generate and edit images from text prompts and reference images using Nano Banana 2.0.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate new images from prompts or edit images using reference inputs through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied local image files are sent to dLazy's cloud service.

Mitigation: Only submit content you intend to share with the service; avoid sensitive local files.

Risk: Authentication may store an API key locally.

Mitigation: Protect local credentials and avoid exposing the key in shared commands or logs.

Risk: The third-party CLI can write generated outputs when the save option is used.

Mitigation: Review the destination path and run the CLI only in an appropriate environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses include generated image URLs; the optional save flag downloads an image file.]

## Skill Version(s):

1.3.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
