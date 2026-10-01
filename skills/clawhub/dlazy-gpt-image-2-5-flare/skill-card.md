## Description:

Helps agents generate and edit images from prompts and optional reference images using dLazy's GPT Image 2.5 Flare service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit images from text prompts and optional reference images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image files are sent to dLazy's hosted service.

Mitigation: Submit only media and prompts you intend to share with dLazy; avoid sensitive content.

Risk: The login flow stores a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key in the dLazy dashboard if needed.

Risk: Installing the CLI globally leaves a persistent third-party executable.

Mitigation: Use the documented pinned npx invocation if a persistent global install is undesirable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [JSON with generated image URLs, or a task ID for asynchronous jobs; optional locally saved image]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to five reference images, selectable aspect ratios and quality, and optional local download.]

## Skill Version(s):

1.2.12 (source: ClawHub release evidence; skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
