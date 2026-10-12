## Description:

Helps agents recreate the style of a reference image by analyzing its visual features and using dLazy's image-replicate service to generate a new image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to ask an agent to generate a new image resembling the composition, lighting, colors, and style of a reference image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are sent to dLazy for generation, and generated assets are hosted by dLazy.

Mitigation: Share only media and prompts approved for the service; review its handling of sensitive content before upload.

Risk: The dLazy CLI stores an API key locally and requires installation of a pinned package.

Mitigation: Confirm you trust dLazy and the pinned CLI before installing; safeguard the key and rotate it if exposed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source (listed in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown and CLI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses can contain a generated image URL or an asynchronous task ID; the agent may save the image locally on request.]

## Skill Version(s):

1.3.29 (source: ClawHub release evidence; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
