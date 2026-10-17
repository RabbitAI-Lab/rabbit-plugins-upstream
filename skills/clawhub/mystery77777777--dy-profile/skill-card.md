## Description:

Collects public Douyin profile videos and engagement metrics for review and CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and analysts use this skill to collect public Douyin creator video listings and engagement metrics for creator screening, content reviews, and account monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved login tokens and collected data can travel over plaintext HTTP to the configured service by default.

Mitigation: Use a trusted HTTPS endpoint with certificate verification and avoid the default HTTP endpoint on untrusted networks; review data-sharing before use.

Risk: Collection can incur charges, and the CLI does not enforce a confirmation step; --force can resubmit a job.

Mitigation: Show the page count and estimated charges, and obtain explicit user approval before every collect command, especially with --force.

## Reference(s):

- [dy-profile ClawHub release](https://clawhub.ai/mystery77777777/skills/dy-profile)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files]

**Output Format:** [Markdown summaries, JSON task results, and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports collected video counts, charges, and refunds; CSV includes video details and engagement metrics.]

## Skill Version(s):

1.0.0 (source: release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
