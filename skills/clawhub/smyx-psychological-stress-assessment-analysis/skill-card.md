## Description:

Analyzes facial images or videos through a remote service to provide stress assessments and anxiety and depression tendency reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and wellness staff use this skill to assess stress and review anxiety or depression tendencies from consented face media. Results are for informational screening, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face media and derived mental-health signals may be sent to a remote service and associated with an identity.

Mitigation: Obtain explicit consent from each person assessed and review the service's data handling before submission.

Risk: The skill creates or reuses identities, persists tokens locally, and retrieves sensitive cloud report history with limited user-facing consent.

Mitigation: Review before installation; avoid shared or sensitive environments unless local persistence and cloud history access are acceptable.

Risk: Stress, anxiety, and depression tendency results can be mistaken for a clinical diagnosis.

Mitigation: Treat assessments as informational only and seek qualified professional help for persistent concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured assessment text or JSON; history listings may include report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include stress indicators, anxiety and depression tendencies, and suggestions.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
