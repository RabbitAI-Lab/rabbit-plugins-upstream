## Description:

Image search tool: queries the Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents looking for visual references, backgrounds, or design assets can search images by keyword and use the returned URLs and metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search inputs or files are sent to dLazy, and service use may incur charges.

Mitigation: Share only intended inputs, keep API keys out of chat, and review account costs.

Risk: The external CLI/API were not fully audited, and the example and listed search option differ.

Mitigation: Check `dlazy search_image -h` before use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [dLazy CLI project (metadata link; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [JSON, Image URLs, Metadata]

**Output Format:** [JSON containing image search results, URLs, and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can optionally be saved to a local path.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
