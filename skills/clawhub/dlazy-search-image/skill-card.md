## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can search Pixabay for image references, backgrounds, and design assets using keywords and optional image type, orientation, language, and paging settings. The skill returns image URLs and metadata through the dLazy search command.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found an unexplained mismatch between the stated image-search purpose and the dLazy CLI authentication and execution commands; the scan could not verify the CLI's internal behavior.

Mitigation: Before installing or authenticating, review the dLazy CLI and its authentication process, and confirm its commands match the intended Pixabay image-search task.

## Reference(s):

- [dLazy CLI project link listed in skill metadata (not server-verified provenance)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image metadata]

**Output Format:** [JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keyword-based results with image type, orientation, page, per-page, and language options.]

## Skill Version(s):

1.3.44 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
