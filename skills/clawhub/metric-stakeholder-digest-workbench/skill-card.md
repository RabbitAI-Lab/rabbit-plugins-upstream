## Description:

Build a stakeholder metric digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, analysts, and reporting agents use this skill to turn a supplied structured metric summary into a concise stakeholder digest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Metric digests can expose sensitive business context if restricted metric summaries are supplied.

Mitigation: Only provide metric summaries approved for the target workflow and audience.

Risk: A stakeholder digest may be misleading if the supplied first, latest, delta, mean, or direction values are inaccurate.

Mitigation: Validate source metric summaries before relying on or distributing the generated HTML digest.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/metric-stakeholder-digest-workbench)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code]

**Output Format:** [JSON object containing an HTML digest artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns digest_artifact with digest_id, metric_id, and html fields.]

## Skill Version(s):

1.0.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
