## Description:

Analyzes images and video for unfamiliar faces and returns recognition reports and alerts for monitored areas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security teams and authorized site operators use this skill to check surveillance images or video against a face database, review unfamiliar-person alerts, and retrieve recognition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Biometric footage is processed by a cloud service.

Mitigation: Use only with explicit authority to process the footage; confirm where media and reports are stored and set retention and deletion rules.

Risk: Implicit identity handling and local token persistence may expose account-linked reports.

Mitigation: Restrict access to the local environment and history reports; verify account identity before retrieving reports.

Risk: Face enrollment can add people to a shared recognition database.

Mitigation: Keep enrollment disabled unless separately authorized and limit who can add faces.

## Reference(s):

- [API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Text or JSON recognition reports; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional report links and saved result files]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
