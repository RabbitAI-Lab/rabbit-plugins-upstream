## Description:

Searches for stock video by keyword and returns video URLs and metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to find stock video footage by keyword, with optional type, category, and duration filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests are handled by dLazy as an intermediary and may incur credit charges.

Mitigation: Review the query and expected cost before running the search, and use --dry-run when appropriate.

Risk: Queries and any local media supplied to the CLI may be sent to dLazy services; login also saves an API key in the local CLI configuration.

Mitigation: Send only information and files you intend to share. Use the DLAZY_API_KEY environment variable if you prefer not to save the key in the local configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-search-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project information (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video URLs, Video metadata, JSON]

**Output Format:** [JSON search results containing video URLs and metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be filtered by video type, category, and duration, and paginated.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
