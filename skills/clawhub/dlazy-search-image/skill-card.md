## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can use this skill to search for Pixabay images by keyword and obtain image URLs and metadata for references, backgrounds, and design assets. The scan notes that it did not verify whether the dLazy CLI provides the stated Pixabay search capability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan reported an unexplained dLazy CLI login/authentication step and incomplete review of references and external package behavior; it did not verify that the CLI provides the stated Pixabay search capability.

Mitigation: Before installing, confirm that you intend to use the dLazy CLI and authentication flow, and review its relevant references and package behavior.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image metadata]

**Output Format:** [JSON containing image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With --no-wait, the CLI may return a task ID before results are available.]

## Skill Version(s):

1.3.40 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
