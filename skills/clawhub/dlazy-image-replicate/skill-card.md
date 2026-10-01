## Description:

Helps agents recreate an image's composition, colors, lighting, and style using dLazy's image-replication service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate a new image inspired by the composition and visual style of a reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied image or other media files may be sent to dLazy's cloud service.

Mitigation: Confirm the material may be shared with dLazy before providing sensitive prompts or files.

Risk: The dLazy CLI stores an API key locally after login, and the skill relies on a third-party package and service.

Mitigation: Review and trust the package and service before installation; protect the key and rotate, revoke, or remove it when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and image-result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service returns a generated image URL; optional CLI flags can save the image locally or return an asynchronous task ID.]

## Skill Version(s):

1.3.24 (source: ClawHub release evidence; bundled skill frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
