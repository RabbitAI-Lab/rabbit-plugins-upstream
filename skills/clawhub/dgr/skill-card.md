## Description:

Audit-ready decision artifacts for LLM outputs with assumptions, risks, recommendations, and review gating as schema-valid JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sapenov](https://clawhub.ai/user/sapenov)

### License/Terms of Use:


## Use Case:

Decision makers, auditors, and teams use DGR to turn decision requests into auditable JSON records that surface assumptions, risks, recommendations, review gates, and consistency checks for ticket, incident, or audit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DGR outputs may be mistaken for authorization to act in production, financial, legal, medical, safety, or access-control decisions.

Mitigation: Treat outputs as decision documentation and require human approval before action in high-stakes workflows.

Risk: An incident-response example understates review gating for a production rollback recommendation.

Mitigation: Apply production change controls and require incident owner approval before acting on rollback recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sapenov/skills/dgr)
- [DGR Homepage](https://www.clawhub.ai/sapenov/dgr)
- [DGR Field Guide](artifact/field_guide.md)
- [DGR JSON Schema](artifact/schema.json)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Schema-valid JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Must conform to artifact/schema.json and include assumptions, risks, recommendation, and consistency_check.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
