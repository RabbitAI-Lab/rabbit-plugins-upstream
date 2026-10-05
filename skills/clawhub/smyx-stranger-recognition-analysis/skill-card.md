## Description:

Analyzes surveillance images and videos against known faces to identify unfamiliar people and provide structured recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security administrators and developers use the skill to check surveillance images or videos for unfamiliar faces, enroll known people, and review recognition reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images and face data are processed by an external service.

Mitigation: Use only with authority and consent; confirm the service's retention, access, and deletion policies before sending data.

Risk: Automatic identities and locally persisted authentication state can link recognition history to a workspace.

Mitigation: Review local token storage and restrict access to identity-linked reports and workspace files.

Risk: Enrolling faces can add personal data to a shared cloud face database.

Mitigation: Require explicit authorization before enrollment and confirm how enrolled faces can be deleted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured recognition report or Markdown history table; JSON detail available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include recognition results, recommendations, and report links.]

## Skill Version(s):

1.0.15 (source: server-resolved release; artifact frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
