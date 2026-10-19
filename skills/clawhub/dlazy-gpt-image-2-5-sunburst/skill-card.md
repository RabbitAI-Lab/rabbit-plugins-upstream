## Description:

Guides agents to generate and edit images using dLazy's GPT Image 2.5 Sunburst CLI, with optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate or edit detailed images from prompts and optional reference images through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or images unless you are comfortable sharing them with dLazy.

Risk: The third-party CLI stores a revocable API key in local user configuration.

Mitigation: Review the pinned CLI package before installation, protect the local key, and revoke it if compromised.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Image URLs, Image files]

**Output Format:** [CLI commands and JSON responses with image URLs; optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to five reference images; supports asynchronous generation.]

## Skill Version(s):

1.2.20 (source: ClawHub release metadata; skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
