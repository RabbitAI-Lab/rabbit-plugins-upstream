## Description:

A Xiaohongshu public-data research skill that helps agents search public notes, retrieve note details and comments, track creator posts, and return structured results for trend discovery, competitor analysis, KOL screening, and report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, brand marketing teams, data analysts, and agents use this skill to collect Xiaohongshu public-note, comment, and creator-post data for content planning, competitor monitoring, trend analysis, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs to the Guaikei API.

Mitigation: Use only when external API processing is acceptable, and avoid private, login-only, or sensitive data.

Risk: Fetched public-data results may be retained in local logs.

Mitigation: Review local retention expectations and delete the logs directory when research outputs are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-report-generate)
- [Guaikei API token portal](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and structured JSON results from CLI execution.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; fetched public-data results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
