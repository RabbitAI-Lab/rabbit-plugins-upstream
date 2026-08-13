## Description:

Searches public XiaoHongShu notes, retrieves note details and comments, and collects public creator posts as structured data for content research, competitor analysis, KOL screening, and comment insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and content operators use this skill to retrieve public XiaoHongShu content, note details, comments, and creator posts for trend research, competitor monitoring, KOL screening, and comment analysis. It is not intended for login-gated, private, posting, liking, or hidden-data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Keywords, XiaoHongShu URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com for data retrieval.

Mitigation: Confirm the user is comfortable with this data transfer before use and protect the API token as a secret.

Risk: The skill can collect public comments, profile-related data, and sensitive research terms into command output or logs.

Mitigation: Use it only for public data, limit collection to the minimum needed, and delete or protect output and logs when they contain sensitive material.

Risk: Bulk collection or downstream reuse of XiaoHongShu content may conflict with platform rules, privacy obligations, or internal policy.

Mitigation: Respect platform rules and applicable privacy obligations, and avoid prohibited distribution or misuse of retrieved data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-comments)
- [Guaikei API website](https://www.guaikei.com)
- [Parameter and command options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with executable Node.js commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may also be written to local logs.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
