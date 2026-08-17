## Description:

Collects public Xiaohongshu content, note details, creator post lists, and comments so agents can prepare structured data for competitive analysis, trend research, KOL screening, and content planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, marketing teams, content creators, and analysts use this skill to retrieve public Xiaohongshu search results, note details, creator posts, and comments for downstream analysis or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note or profile URLs, request options, and GUAIKEI_API_TOKEN are sent to the third-party guaikei.com service.

Mitigation: Use the skill only when that data sharing is approved, and provision the API token according to the user's security policy.

Risk: Generated logs can contain sensitive business research, links, and collected public content.

Mitigation: Protect, review, or delete log files before sharing or syncing the workspace.

Risk: Collected public social-platform data can be misused outside the intended analysis and reporting workflow.

Mitigation: Limit use to public, non-login data and follow applicable platform, legal, and organizational requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-see-details)
- [Guaikei API service](https://www.guaikei.com)
- [options.md](references/options.md)
- [changelog.md](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands; command results are structured JSON and may also be saved as local log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword, note URL, creator profile URL, limit, sort, type, and time options.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
