## Description:

快手内容研究助手 enables agents to search Kuaishou public content by keyword, retrieve creator posts, and collect video comments as structured JSON for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External creators, marketers, content operators, and analysts use this skill to research public Kuaishou videos, creator activity, and comment discussions. It supports topic discovery, competitor monitoring, trend review, and follow-on reporting from returned structured data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile URLs, video URLs, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only where third-party API sharing is approved, and configure only tokens intended for this service.

Risk: Saved logs may retain competitive research or personal data present in public comments.

Mitigation: Protect, rotate, or delete local logs according to the user's data-retention policy.

Risk: API responses may be empty, rate-limited, unavailable, or unsuitable as a sole basis for marketing decisions.

Mitigation: Check the returned status and error_code fields, avoid inventing missing data, and corroborate findings before acting on them.

## Reference(s):

- [Server-resolved source repository](https://github.com/why20261/kuaishou-content-research-skill)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishou-content-research-skill)
- [GUAIKEI API service](https://www.guaikei.com)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Guidance]

**Output Format:** [Structured JSON results with concise text or Markdown summaries when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and may save task results to local logs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
