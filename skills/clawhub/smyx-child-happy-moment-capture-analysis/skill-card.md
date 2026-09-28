## Description:

Analyzes children's video for joyful expressions and actions, generating happy-moment reports and capture recommendations for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to analyze children's activity footage, identify joyful moments, and review reports or happy-diary history. Kindergarten and playground use requires consent from guardians of every child captured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Footage of minors may be captured without adequate consent.

Mitigation: Obtain explicit guardian consent for every child captured before use, especially in shared spaces; do not capture children without consent.

Risk: Sensitive media and reports may be sent to LifeEmergence cloud endpoints.

Mitigation: Review cloud transfer, storage, retention, and deletion practices before uploading footage; provide controls to delete captures and pause or opt out.

Risk: The skill creates or reuses a local identity and stores session tokens in the workspace data directory.

Mitigation: Limit access to workspace data and tokens, and review identity and token handling before installation.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/18072937735/skills/smyx-child-happy-moment-capture-analysis)
- [Skill API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown reports or structured JSON analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to remotely stored reports and captured media.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
