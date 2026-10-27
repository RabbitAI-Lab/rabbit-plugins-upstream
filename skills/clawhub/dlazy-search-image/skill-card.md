## Description:

Image search tool: queries Pixabay image API by keywords and returns image URLs and metadata for references, backgrounds, and design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can search for image assets by keyword, image type, orientation, and language, then use the returned URLs and metadata as references, backgrounds, or design assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image searches may consume dLazy account credits.

Mitigation: Use dry-run estimates where applicable, limit searches to what is needed, and monitor account credits.

Risk: The CLI stores an organization API key locally, and submitted queries or selected files may be sent to dLazy services.

Mitigation: Keep API keys private; use DLAZY_API_KEY when avoiding saved local credentials, and send only queries or files you are comfortable sharing with the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-image)
- [CLI project repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON results containing image URLs and metadata; asynchronous requests may initially return a task identifier.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can optionally be saved as a local file.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
