## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can search for reference images, backgrounds, and design assets by keyword, then use the returned image URLs and metadata in their work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found a mismatch between the image-search purpose and the dLazy CLI authentication and launch instructions; the external CLI and its credential handling were not inspected.

Mitigation: Before use, verify that the dLazy CLI and its authentication flow are intended for this task, and review its credential handling before providing an API key or sensitive inputs.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image metadata]

**Output Format:** [JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image results can optionally be downloaded to a local path.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
