## Description:

Analyzes in-cabin driver video or images for head-down and side-view posture abnormalities and returns distracted-driving alerts, structured reports, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, fleet operators, and safety teams can use this skill to analyze driver-facing DMS footage for sustained head-down or side-view posture events. It supports distracted-driving alerts, structured reports, and cloud-backed report history for passenger cars, commercial vehicles, ride-hailing fleets, and freight fleets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes real driver footage and cloud-backed report history that may contain sensitive personal or biometric information.

Mitigation: Require explicit consent before uploads or history lookups, document data handling practices, and verify that backend report access is scoped to the correct user or fleet.

Risk: Security evidence reports plaintext HTTP endpoints for some runtime traffic.

Mitigation: Require HTTPS-only API endpoints before deployment and reject non-TLS runtime configuration in production environments.

Risk: The skill uses automatic identity and token handling.

Mitigation: Document identity and token storage, protect local configuration, and review token lifetime and authorization boundaries before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)
- [Driver Head-Pose API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown summaries, JSON analysis results, report links, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud-backed report history and may save analysis output to a user-specified file.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
