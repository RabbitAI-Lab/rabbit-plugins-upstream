## Description:

Analyzes children's behavior videos for repetitive movements such as spinning and hand-flapping, and provides behavior summaries and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Therapists and guardians use the skill to review children's behavior videos, track repetitive movement events and trends, and retrieve prior reports. Its observations support review by professionals rather than diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive videos or video URLs involving children are sent to a cloud service.

Mitigation: Obtain guardian consent first and confirm the provider's retention, deletion, and access-control practices before submitting media.

Risk: Silent account creation and token persistence tie reports to an account with limited user control.

Mitigation: Disclose cloud account and report storage to users; avoid history lookup unless access to prior cloud reports is expected.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/18072937735/skills/smyx-autism-stereotyped-behavior-detect-analysis)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured behavior report or Markdown table of historical reports, with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior counts, durations, and optional trend summaries; not a diagnosis]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
