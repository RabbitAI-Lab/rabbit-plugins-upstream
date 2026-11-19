## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams can search Pixabay by keyword for reference images, backgrounds, and design assets, then use the returned image URLs and metadata in an agent or workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill requires a dLazy API key, and ClawScan reports partial coverage: it did not inspect the CLI implementation or fully resolve referenced paths.

Mitigation: Use the dLazy CLI and provide an API key only if you intend to make requests; review the CLI and how it handles search inputs before use.

## Reference(s):

- [dLazy homepage (listed in skill metadata)](https://dlazy.com)
- [@dlazy/cli package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [CLI source URL listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image metadata]

**Output Format:** [JSON search results with image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated results; optional asset download with --save.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata; artifact frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
