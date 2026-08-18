## Description:

A/B testing framework for content, strategy, and pricing experiments that calculates statistical significance and recommends a best-performing variant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to create A/B experiments, record variant outcomes, compare content, strategy, or pricing performance, and turn significance results into recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reach shared tenant analytics data or behavior logs when comparison workflows are configured.

Mitigation: Use least-privilege database credentials and enforce tenant access controls outside the skill.

Risk: Stored experiment data and behavior logs may accumulate sensitive operational history.

Mitigation: Apply a retention policy to stored experiment data before using the skill with real tenants or production analytics.

Risk: Automated recommendations or notifications could influence executive decisions without adequate review.

Mitigation: Require human review before adopting recommendations or sending automated notifications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ab-testing)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [JSON command results, Markdown reports, and inline shell-command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and may read or write experiment records; comparison workflows can query tenant-scoped content statistics when configured.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
