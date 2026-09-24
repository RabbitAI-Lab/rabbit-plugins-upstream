## Description:

Calculate metric trends and render stakeholder metric digests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts, operators, and stakeholder-reporting teams use this skill to summarize metric series and produce concise stakeholder digests from supplied metric data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The broad analytics-reporting trigger may select this skill for requests outside its two documented workflows.

Mitigation: Use it only when calculating a metric trend summary or rendering a stakeholder metric digest.

Risk: User-supplied business metrics may include sensitive operating data.

Mitigation: Provide sensitive metric data only when it is intended to be processed in the current request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/stakeholder-metrics-studio)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, code]

**Output Format:** [Structured objects containing metric summary fields or an HTML digest artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes user-supplied metric data in the current request.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
