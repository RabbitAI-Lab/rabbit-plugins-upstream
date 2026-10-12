## Description:

Searches for stock video footage by keyword through the dLazy CLI and returns video links and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to find stock video links and metadata for footage sourcing. Searches require a dLazy API key and use the dLazy hosted service rather than a direct Pixabay connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and any supplied media may be sent to dLazy's hosted service rather than directly to Pixabay.

Mitigation: Avoid sensitive queries or files; review dLazy's data handling before use.

Risk: Using the external CLI requires an API key and installs third-party npm code.

Mitigation: Review the pinned CLI package before installation, restrict access to the key, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON data]

**Output Format:** [JSON response containing video links and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An asynchronous request may initially return a task ID instead of video results.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; skill frontmatter states 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
