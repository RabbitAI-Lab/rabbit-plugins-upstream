## Description:

Collects public Xiaohongshu note, comment, creator post, and keyword-search data for trend research, competitor monitoring, KOL screening, and reporting without account login or content publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, content teams, market researchers, and analysts use this skill to retrieve public Xiaohongshu search results, note details, comments, and creator post lists for content research, competitor monitoring, KOL screening, trend analysis, and report preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, URLs, request limits, and GUAIKEI_API_TOKEN to Guaikei's API.

Mitigation: Use it only when the user is comfortable with that third-party API exchange and has authorization for the public targets being collected.

Risk: Fetched public results may be retained in local log files.

Mitigation: Avoid collecting private, sensitive, or unauthorized data, and clear the logs directory when retained results are no longer needed.

Risk: Requests for private, hidden, logged-in, or non-public content would fall outside the documented collection boundary.

Mitigation: Limit use to public Xiaohongshu data and decline tasks that require account access, hidden data, private content, posting, liking, commenting, or following.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/guaikei-xhs-collector)
- [Guaikei API access](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands; command output is structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched public results may be saved to local log files.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
