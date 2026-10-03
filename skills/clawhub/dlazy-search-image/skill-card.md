## Description:

Searches for images by keyword and returns image URLs and metadata for references, backgrounds, and design assets through dLazy services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, creators, and developers use this skill to find image references, backgrounds, and design assets by keyword.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The description names Pixabay, but the instructions route searches and results through dLazy services.

Mitigation: Review the service routing and data-sharing implications before sending search terms or referenced media.

Risk: Using the skill requires a dLazy API key and running a pinned npm CLI.

Mitigation: Review the package before installing, protect the API key, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image URLs and metadata; optional local asset download.]

## Skill Version(s):

1.3.25 (source: ClawHub release; bundled skill frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
