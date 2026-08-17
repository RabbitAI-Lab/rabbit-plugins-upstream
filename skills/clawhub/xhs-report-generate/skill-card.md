## Description:

xhs-report-generate helps agents search public Xiaohongshu notes, retrieve note details and comments, monitor creator posts, and return structured data for content research and marketing analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, brand marketers, market researchers, and analysts use this skill to collect public Xiaohongshu note, comment, and creator-post data for trend discovery, competitor monitoring, KOL screening, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs to the third-party guaikei.com API using GUAIKEI_API_TOKEN.

Mitigation: Use the skill only for data that is acceptable to send to that API service, and keep GUAIKEI_API_TOKEN in environment configuration rather than prompts or shared logs.

Risk: Successful results are saved locally under logs and may include searched topics, target accounts, comments, or fetched public data.

Mitigation: Review and delete local log files when the search target, comments, or collected public data are sensitive.

Risk: The skill is intended for public Xiaohongshu data and not private, hidden, login-only, or restricted content.

Mitigation: Use only public keywords and public links, and do not use returned data for unlawful redistribution or other prohibited purposes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-report-generate)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and structured JSON command output; successful command results are also saved as local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands operate on Xiaohongshu keywords, note URLs, creator profile URLs, and optional result limits.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
