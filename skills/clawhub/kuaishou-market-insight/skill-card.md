## Description:

Analyzes public Kuaishou videos, creator posts, and comments to help agents research market trends, creator activity, competitive content, and audience response.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content teams, marketers, and analysts use this skill to collect structured public Kuaishou search, creator-post, and video-comment data for trend research, content planning, competitor monitoring, and reporting. It requires a GUAIKEI_API_TOKEN and should be used only for lawful, platform-compliant analysis of public data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou queries, profile or video URLs, and returned public data are sent through guaikei.com using GUAIKEI_API_TOKEN.

Mitigation: Install and use the skill only when that third-party data flow is acceptable, and avoid submitting sensitive or non-public inputs.

Risk: Saved logs can retain copies of comments and research results on local, shared, or synced machines.

Mitigation: Store logs in an approved location, restrict access where needed, and delete retained outputs when they are no longer required.

Risk: The skill is intended for public Kuaishou data and may be misused for unsupported private, hidden, or non-compliant collection.

Mitigation: Use it only for public data and lawful, platform-compliant analysis; do not attempt login-state, private, hidden, or unauthorized data access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/kuaishou-market-insight)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from the CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results include status, request metadata, skill metadata, and result payloads; local logs may retain returned public comments and research results.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
