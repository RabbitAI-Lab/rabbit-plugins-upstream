## Description:

Analyzes aquarium footage for fish gasping and unusual breathing near the surface, then reports visual warnings of possible low oxygen or ammonia exposure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and monitoring teams use this skill to review camera footage for signs of fish distress, receive risk warnings and suggested checks, and consult past cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium video or video URLs are sent to the LifeEmergence cloud service.

Mitigation: Obtain consent before uploading footage or sharing video URLs with the cloud service.

Risk: The skill silently creates or reuses an internal identity and may retain tokens in workspace data.

Mitigation: Review where workspace data and identity tokens are stored and how long they are retained before installation.

Risk: History requests can access cloud reports without explicit confirmation.

Mitigation: Require user confirmation before retrieving report history.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis)
- [Aquarium analysis API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk warnings, suggested follow-up actions, and report links when available.]

## Skill Version(s):

1.0.15 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
