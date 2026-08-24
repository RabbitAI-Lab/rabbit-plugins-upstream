## Description:

Calculate a metric trend summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and analysts use this skill for routine operating review work when they need a concise trend digest from a supplied metric series CSV.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Metric CSV input may contain sensitive business data if users include more information than needed.

Mitigation: Provide only the metric series data intended for analysis and avoid including credentials, private files, or unrelated confidential content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/metric-stakeholder-digest-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [Structured object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns metric_digest with metric_id, first, latest, delta, mean, and direction.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
