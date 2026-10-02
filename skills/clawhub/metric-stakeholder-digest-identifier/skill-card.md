## Description:

Calculate a metric trend summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Analytics teams use supplied metric CSV data to calculate a concise trend digest for operating reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CSV containing no valid METRIC-prefixed metric ID or multiple metric IDs is rejected.

Mitigation: Supply a single metric series with a METRIC-prefixed metric ID and check the input before running.

Risk: A calculated trend can mislead when the supplied metric data is incomplete or incorrect.

Mitigation: Review the input series and resulting digest before using it in an operating review.

## Reference(s):

- [Metric Trend Calculator on ClawHub](https://clawhub.ai/wxt-ai/skills/metric-stakeholder-digest-identifier)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns metric ID, first and latest values, change, mean, and trend direction; does not persist a business artifact.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
