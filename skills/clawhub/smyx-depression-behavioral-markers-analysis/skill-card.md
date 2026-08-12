## Description:

Analyzes long-running fixed-camera video from bedroom and dining areas to produce non-diagnostic behavior-change reports about extended bed time and reduced eating activity for elder-care or solo-living monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, community doctors, and health-management operators use this skill to submit consented fixed-camera videos or URLs and receive structured behavior summaries that flag prolonged immobility and appetite-related changes without diagnosing depression.

### Deployment Geography for Use:

Global, subject to local health, privacy, and consent requirements.

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive home-video and health-adjacent data.

Mitigation: Use only with explicit consent from the monitored person, apply local privacy controls, and confirm that the service and retention policy are acceptable before installation.

Risk: Analysis and report history may involve remote uploads, automatic identity creation, persistent tokens, and cloud retrieval.

Mitigation: Use controlled environments with clear identity separation and token storage, and avoid shared machines or multi-user workspaces unless those controls are in place.

Risk: Behavioral signals could be mistaken for a medical diagnosis or treatment recommendation.

Mitigation: Present results as behavior observations only and route clinical interpretation, urgent self-harm concerns, or treatment decisions to qualified professionals or emergency support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured behavior report text or JSON; history queries may be rendered as Markdown tables with report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned report to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact SKILL.md frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
