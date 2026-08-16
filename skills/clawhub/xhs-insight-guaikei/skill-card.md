## Description:

Searches, retrieves, and analyzes public Xiaohongshu (RED/XHS) posts, comments, and creator posts for content research, competitor monitoring, KOL screening, trend tracking, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, marketers, and analysts use this skill to gather public Xiaohongshu search results, note details, comments, and creator post data for content planning, competitor monitoring, KOL evaluation, sentiment review, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, links, and retrieved public data are sent to Guaikei using the user's GUAIKEI_API_TOKEN.

Mitigation: Use only when the user is comfortable with that data transfer and has authorization for lawful, platform-permitted public-data analysis.

Risk: Saved logs may contain sensitive research output.

Mitigation: Treat local logs as sensitive and delete them when they are no longer needed.

Risk: Requests for private, hidden, login-only, or non-public platform data would exceed the skill's documented scope.

Mitigation: Limit use to public Xiaohongshu data and decline requests involving private data, account login, publishing, liking, or commenting.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/engheng-art/skills/xhs-insight-guaikei)
- [Guaikei API token and support site](https://www.guaikei.com)
- [Options and invocation guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI results are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; retrieved public-data outputs may be saved locally and should be handled as sensitive research material.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
