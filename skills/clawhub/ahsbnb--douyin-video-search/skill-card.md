## Description:

Searches Douyin videos through the TikHub API with keyword search, pagination, sorting, and publish-time or duration filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ahsbnb](https://clawhub.ai/user/ahsbnb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run targeted Douyin video searches via a CLI, retrieve formatted summaries or raw JSON, and paginate or filter results for social-media discovery and downstream workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and the TikHub API token are sent to TikHub.

Mitigation: Use the skill only when TikHub is trusted for the intended searches, and avoid sensitive search terms or credentials in shared logs.

Risk: The script prints raw response snippets for debugging, which may expose returned content in terminal output or logs.

Mitigation: Review logging behavior before deployment and avoid running sensitive searches in environments where stdout is captured broadly.

## Reference(s):

- [Douyin Video Search on ClawHub](https://clawhub.ai/ahsbnb/skills/douyin-video-search)
- [TikHub registration](https://user.tikhub.io/register)
- [TikHub Douyin search API endpoint](https://api.tikhub.io/api/v1/douyin/search/fetch_general_search_v1)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration]

**Output Format:** [Plain text search summaries or raw JSON from a command-line Python script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TikHub API token and accepts keyword, cursor, sorting, publish-time, duration, content-type, search-id, backtrace, and raw-output parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
