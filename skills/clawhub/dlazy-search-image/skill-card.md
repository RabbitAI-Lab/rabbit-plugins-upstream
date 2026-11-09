## Description:

Image search tool: queries the Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and designers can search for Pixabay images by keyword and use the returned URLs and metadata to find reference, background, and design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and partial coverage, and flagged CLI commands that were not clearly tied to the stated image-search purpose.

Mitigation: Review the CLI and confirm the command behavior before installing or running it.

Risk: The skill documentation says search prompts and any supplied local media may be sent to dLazy hosted services.

Mitigation: Avoid sending sensitive search terms or media unless their use with the service is permitted.

## Reference(s):

- [CLI repository link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Image metadata]

**Output Format:** [JSON search results containing image URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can optionally be downloaded to a local path.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
