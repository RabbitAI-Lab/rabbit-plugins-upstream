## Description:

Using a camera installed at the bathroom doorway, or inside the bathroom only detecting human silhouettes without capturing private details, this skill detects elderly bathroom entry and exit events, calculates continuous occupancy time, and raises an abnormal alert when the stay exceeds the configured threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elder-care operators use this skill to analyze privacy-minimized bathroom doorway or silhouette video for prolonged toilet occupancy alerts and report history. It supports safety monitoring workflows for solo-living elder households, nursing homes, senior apartments, and home-security integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send highly sensitive bathroom-adjacent video, video URLs, and report history to a configured cloud service.

Mitigation: Use only with explicit consent, privacy-minimized camera placement, HTTPS production endpoints, and documented data retention controls.

Risk: The skill silently manages local identity and persistent tokens for report association.

Mitigation: Review identity and token storage before deployment, restrict access to local configuration and history, and rotate or revoke credentials when needed.

Risk: Alerts are safety-monitoring signals and may be incorrect or incomplete.

Mitigation: Treat abnormal occupancy alerts as prompts for human verification, not as medical diagnosis or a substitute for emergency response judgment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured analysis report or history table, with JSON detail available by parameter]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include occupancy duration, entry and exit events, alert level, suggested contacts, and report links.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
