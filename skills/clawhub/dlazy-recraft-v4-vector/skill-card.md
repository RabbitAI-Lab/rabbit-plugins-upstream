## Description:

Generates images from text prompts for logos, icons, and other design assets through dLazy's hosted Recraft V4 Vector service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers and developers use this skill to request generated logos, icons, and other visual assets from a text prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and file paths intentionally supplied to the CLI may be sent to dLazy's hosted service.

Mitigation: Review inputs before invoking the service and avoid sharing sensitive prompts or files.

Risk: The CLI can save a dLazy API key in local configuration.

Mitigation: Protect access to the local key and revoke or rotate it if exposed.

Risk: The skill description promises SVG vectors, while the example response shows a PNG image.

Mitigation: Confirm the returned file type and scalability before relying on vector output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON responses, Image asset links]

**Output Format:** [JSON containing generated image URLs; optional downloaded image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The description claims SVG output, but the provided response example returns PNG; asynchronous requests initially return a task identifier.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
