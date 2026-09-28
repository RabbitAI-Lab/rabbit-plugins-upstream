## Description:

Searches public Xiaohongshu notes and retrieves note details, comments, and creator posts for content and market research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and analysts use the skill to find popular public Xiaohongshu notes, compare creator activity, and analyze note engagement and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and Xiaohongshu links are sent to the guaikei.com service using an API token.

Mitigation: Use the service only when its data handling is acceptable; keep the API token in the designated environment variable.

Risk: Saved local JSON logs may expose sensitive research targets or returned public comments.

Mitigation: Restrict access to local logs and remove them when no longer needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/why20261/skills/xiaohongshu-notes-search)
- [Publisher-listed project homepage](https://github.com/um-why/xiaohongshu-openclaw-skill)
- [Usage options](references/options.md)
- [Troubleshooting](references/troubleshooting.md)
- [Data API and token information](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, JSON data, Guidance]

**Output Format:** [JSON results with optional text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search and lookup results are also saved to local temporary JSON logs.]

## Skill Version(s):

1.1.4 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
