## Description:

Calculates a metric trend summary from a user-supplied CSV series.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and business teams use the skill to summarize a single metric's CSV time series for routine operating reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The README mentions output directories and SQLite behavior that the active package does not use.

Mitigation: Follow the current skill instructions for local CSV summarization and confirm behavior against the bundled example before relying on the README's extra claims.

## Reference(s):

- [ClawHub release: Metric Trend Calculator](https://clawhub.ai/wxt-ai/skills/metric-stakeholder-digest-identifier)

## Skill Output:

**Output Type(s):** [Analysis]

**Output Format:** [JSON metric digest with first, latest, delta, mean, and direction]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes metric ID, percentage change, and point count.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
