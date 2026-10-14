## Description:

Helps agents convert PNG or JPG images into scalable vector artwork using the dLazy cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to vectorize logos, icons, and flat illustrations from raster images through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to dLazy's cloud service.

Mitigation: Send only images and prompts you are comfortable sharing with dLazy.

Risk: Using the service requires a dLazy API key.

Mitigation: Keep the key private and use dLazy's key rotation or revocation controls if needed.

Risk: The skill describes SVG results but shows a PNG example, and its command example differs from the listed image option.

Mitigation: Confirm the CLI command and returned file format before relying on the result.

## Reference(s):

- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a result URL; asynchronous requests return a task identifier for polling.]

## Skill Version(s):

1.2.28 (source: ClawHub release metadata; skill frontmatter says 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
