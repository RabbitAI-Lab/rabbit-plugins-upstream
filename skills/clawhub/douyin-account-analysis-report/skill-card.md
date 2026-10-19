## Description:

Analyzes a user-provided Douyin account and recent posts to produce an evidence-based account diagnosis and actionable 30-day content test plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, brand teams, and account operators use this skill to review a Douyin account's profile and recent posts, compare engagement, diagnose visible performance issues, and plan content experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested live npm install runs an unpinned third-party package with access to the SocialDataX API key.

Mitigation: Review the package before installation, pin a trusted version or use a preinstalled reviewed CLI, and limit access to the API key.

Risk: Incomplete post samples or missing playback metrics can lead to overstated account diagnoses.

Mitigation: Label partial and missing data, keep conclusions within the returned sample, and do not claim to know recommendation behavior or unavailable playback metrics.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/douyin-account-analysis-report)
- [SocialDataX API key and service information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown account diagnosis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account profile, recent-post sample, engagement comparisons, evidence-linked findings, and a 30-day test plan; unavailable metrics are labeled as missing.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
