## Description:

Collects public Xiaohongshu note comments in user-approved, paid steps, with optional replies and CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cuiyunhai](https://clawhub.ai/user/cuiyunhai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to review public Xiaohongshu comments for audience feedback and sentiment, expanding replies or exporting a CSV when needed. Each paid collection step requires the user's confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service connection uses unencrypted HTTP and may expose account tokens in transit.

Mitigation: Configure a working HTTPS service URL before signing in; avoid insecure TLS settings except in controlled tests.

Risk: Existing credentials may be copied automatically from an older local configuration.

Mitigation: Review the older configuration before use and remove or replace credentials you do not want reused.

Risk: Each comment page or reply expansion may incur a charge.

Mitigation: Show the estimated page count and seek explicit user confirmation before each paid step.

Risk: Exported comments can contain identifiable nicknames and IP locations.

Mitigation: Collect only appropriate public data and store or share CSV exports with care.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/cuiyunhai/skills/xhs-comments)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV files]

**Output Format:** [Markdown summaries of JSON comment results; optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes comment text, public nicknames, likes, IP location and reply counts; collection proceeds one paid page or reply expansion at a time.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
