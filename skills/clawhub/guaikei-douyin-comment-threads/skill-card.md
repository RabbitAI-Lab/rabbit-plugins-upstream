## Description:

Retrieves public Douyin keyword search results, creator posts, video comments, and trending topics as structured JSON for content research, competitor monitoring, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, marketing analysts, and developers use this skill to collect public Douyin data before summarizing, comparing, clustering, or reporting on content performance, comments, creators, and trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin research inputs and the GUAIKEI_API_TOKEN are sent to guaikei.com for API access.

Mitigation: Use only authorized public-data research inputs, avoid confidential targets or regulated data, and protect the token as a credential.

Risk: Fetched public data may persist in local JSON log files.

Mitigation: Delete, restrict, or secure the logs directory when results should not persist or should not be shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-comment-threads)
- [Guaikei API token and support](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [JSON command output with brief user-facing guidance when inputs, token configuration, or errors require clarification.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command logs and fetched result snapshots may be written to the local logs directory.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
