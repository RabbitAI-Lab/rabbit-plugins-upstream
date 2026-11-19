## Description:

Public TikTok creator profiles for agents — follower, video, and like counts as structured JSON, with no TikTok key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and research teams use the skill to retrieve public TikTok creator and video data for social listening, creator research, monitoring, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes an API credits check, and the skill exposes video, collection, and search lookups beyond creator profile statistics.

Mitigation: Review the credits check and requested lookup before use, and limit calls to the TikTok data the user requested.

## Reference(s):

- [TikTok Data documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [MCP installation guide](https://www.superagnt.com/install?facet=tiktok)
- [API key setup](https://superagnt.com/r/ch-tiktok-data-key)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration guidance]

**Output Format:** [Structured JSON API responses and Markdown setup guidance with inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SUPERAGNT_API_KEY for API requests; curl is used by the command-line setup.]

## Skill Version(s):

2.0.17 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
