## Description:

Retrieves public Xiaohongshu note search results, note details, comments, and creator posts through command-line tools for downstream content, competitor, KOL, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brand marketers, market analysts, and operations teams use this skill to collect public Xiaohongshu data for topic research, competitor monitoring, KOL screening, comment analysis, and trend tracking. It is suited to workflows that need structured public data before human review or downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Xiaohongshu URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install and run only when that data transfer is acceptable for the user's organization and keep the token scoped and protected.

Risk: Generated logs can contain sensitive competitor, KOL, keyword, or comment-analysis data.

Mitigation: Protect or delete local logs when they are no longer needed, especially for commercial research workflows.

Risk: The skill only retrieves public Xiaohongshu data and may return empty or unavailable results for deleted, private, restricted, or incorrectly routed links.

Mitigation: Confirm the platform, URL type, keyword, and requested command before execution, and do not treat empty results as proof of absence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-note-detail)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Guaikei API website](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured JSON from CLI execution, saved log files, and concise Markdown guidance with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be archived locally under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata declares 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
