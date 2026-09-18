## Description:

This skill helps agents retrieve public Kuaishou data for keyword video search, creator post tracking, and video comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External marketers, content operators, data analysts, and agents use this skill to search Kuaishou videos by keyword, retrieve public creator posts, and collect public video comments for competitive research, topic planning, trend monitoring, and sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, creator or video URLs, request parameters, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when that data sharing is acceptable, keep the token secret, and rotate or revoke it according to local policy.

Risk: CLI outputs and local logs may contain public Kuaishou comments, creator data, links, and interaction metrics.

Mitigation: Use the skill only for public Kuaishou data, follow platform terms and privacy rules, and protect or periodically clear local logs.

Risk: API, network, token, or rate-limit failures may produce error or empty JSON results.

Mitigation: Check the structured status and error_code before using results for analysis, and do not treat empty or error responses as evidence.

## Reference(s):

- [Server-resolved source repository](https://github.com/why20261/kuaishou-competitor-analysis)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishou-competitor-analysis)
- [Guaikei API service](https://www.guaikei.com)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; command runs may save result logs locally under logs/.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact package.json and changelog report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
