## Description:

Runs a Persian-language research and experiment lab that tests personal success hypotheses against evidence and tracks how the user's model changes over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use this skill to research success-related questions, design small personal experiments, and maintain a Persian-language research log and evolving model of their findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal research and experiment logs may contain sensitive information.

Mitigation: Keep lab files in a location you control and do not put secrets in logs.

Risk: Research sessions may access external research websites.

Mitigation: Use the source registry to scope searches and review sources before relying on findings.

Risk: Broad references to the lab may trigger an unintended session.

Mitigation: Use explicit commands such as today, question, experiment, review, dashboard, or audit.

## Reference(s):

- [ClawHub release](https://clawhub.ai/ehsanghaffar/skills/persian-success-lab)
- [Server-resolved source repository](https://github.com/ehsanghaffar/skills/tree/main/skills/persian-success-lab)
- [Source registry](references/source-registry.md)
- [Research and experiment record schemas](references/record-schemas.md)
- [Success model and review cadence](references/success-model.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Persian-language Markdown research summaries, experiment plans, logs, reviews, and dashboards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates persistent lab records when available; otherwise supplies copyable records for manual saving.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
