## Description:

Searches public Xiaohongshu notes, retrieves note details and comments, and fetches public creator posts as structured data for trend research, competitor analysis, KOL screening, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketers, content operators, and analysts use this skill to choose the correct Xiaohongshu lookup command and retrieve public search results, note details, comments, or creator posts for business and content research. It is not intended for login, publishing, interaction, private content, or hidden data access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note URLs, profile URLs, limits, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only when data sharing with guaikei.com is approved, and provide a scoped token suitable for the task.

Risk: Returned public social-media data and comments may persist locally in generated log files.

Mitigation: Review or delete the logs directory when results should not remain on disk.

Risk: The skill is limited to public Xiaohongshu data and does not support private, hidden, login-required, publishing, or interaction workflows.

Mitigation: Do not use it for account actions or private data access; request a public keyword, note URL, or profile URL before execution.

Risk: API errors, rate limits, empty results, or deleted content can produce incomplete retrievals.

Mitigation: Check the returned status field and error_code, avoid fabricating missing data, and retry or adjust inputs only when the documented error handling supports it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-search-detail-comment)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands; CLI execution returns JSON status objects and may save JSON logs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN for data retrieval.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
