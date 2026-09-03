## Description:

Analyzes elderly-person walking videos to estimate gait metrics such as step length, gait speed, cadence, trunk sway, and fall-risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and health-management developers use this skill to submit fixed-camera walking videos or video URLs for structured gait screening reports and historical report lookup. The output is a screening aid and does not replace professional clinical assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elderly-person gait videos and report history are sent to the configured LifeEmergence/SMYX cloud service.

Mitigation: Confirm the endpoint, data-retention terms, consent basis, and deletion process before installing or running the skill.

Risk: The skill manages user identity, remote registration, stored tokens, and history access automatically.

Mitigation: Review how identities are created, where tokens are stored, and who can access historical reports before deployment.

Risk: The output is a fall-risk screening report and may be mistaken for a diagnosis.

Mitigation: Present results as auxiliary screening information and require professional medical review for clinical decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-gait-instability-detection-analysis)
- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include gait metrics, fall-risk level, risk factors, alert text, medical follow-up hints, and historical report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
