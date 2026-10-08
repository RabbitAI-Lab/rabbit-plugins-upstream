## Description:

Analyzes emergency-shelter camera footage for observable acute-stress behaviors and provides crisis alerts to support on-site responders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized emergency-response teams use this skill to review footage from shelters and temporary settlements for behavioral signs that may warrant on-site psychological support. Alerts and location cues help qualified responders prioritize human assessment, not make clinical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive shelter camera footage is analyzed through a cloud service.

Mitigation: Deploy only with emergency-response authorization; confirm service operator, footage and report retention, and operator access before use.

Risk: The skill silently manages identities and stores access tokens.

Mitigation: Supply an approved service identity rather than relying on an auto-created default user, and verify token protection and access controls.

Risk: Behavioral alerts may be mistaken for clinical findings or prompt inappropriate dispatch.

Mitigation: Have qualified on-site responders review high-risk alerts before dispatch; treat results as observations, not diagnoses.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-trauma-stress-behavior-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured analysis reports or Markdown report lists; optionally saved to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavioral alerts, location cues, response suggestions and report links; high-risk alerts require human review.]

## Skill Version(s):

1.0.13 (source: server-resolved release; bundled frontmatter lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
