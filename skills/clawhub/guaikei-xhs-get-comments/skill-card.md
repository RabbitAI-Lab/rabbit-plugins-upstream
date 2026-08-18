## Description:

Retrieves public Xiaohongshu notes, note details, comments, and creator post lists through command-line tools that return structured data for content, competitor, KOL, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, content creators, marketers, and analysts use this skill to collect public Xiaohongshu search results, note details, comments, and creator posts for downstream reporting and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, URLs, and GUAIKEI_API_TOKEN to the third-party Guaikei API service.

Mitigation: Use only when external processing by guaikei.com is acceptable, and avoid sensitive research targets unless that data sharing is approved.

Risk: Returned data is saved locally in logs.

Mitigation: Review local retention expectations and remove generated logs when the collected Xiaohongshu data should not persist.

Risk: The skill is limited to public Xiaohongshu data and may fail or return empty results for invalid links, deleted notes, unavailable data, or API errors.

Mitigation: Check inputs before execution, do not treat empty or error responses as successful data collection, and retry later for transient service failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-get-comments)
- [Guaikei service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands; command execution returns structured JSON and local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0+ and GUAIKEI_API_TOKEN; results may be saved under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
