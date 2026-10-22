## Description:

Analyzes infant sleep monitoring video to identify sleep states and provide sleep reports and routine insights for parents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use infant monitoring footage to review sleep states, daily sleep patterns, and past reports. Results are for parenting reference, not a substitute for professional medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant monitoring media and report queries are sent to a remote cloud service.

Mitigation: Review the cloud data flow and obtain appropriate consent before submitting child-monitoring footage or reports.

Risk: The skill may silently create or reuse a shared identity and persist reusable credentials locally.

Mitigation: Use only in a trusted, single-user workspace where shared account access and local credential persistence are acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text reports and Markdown tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports brief or detailed results and historical report listings.]

## Skill Version(s):

1.0.15 (source: ClawHub release; bundled SKILL.md lists 1.0.21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
