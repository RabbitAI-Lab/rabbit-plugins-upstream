## Description:

Analyzes nighttime bedroom audio and video for sudden sitting up, screams, and arm movements, and reports when and how often these events occur.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and care staff use this skill to review an older person's nighttime sleep events and share observations with a clinician, not to make a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bedroom audio/video and historical sleep reports are sent to configured cloud services.

Mitigation: Obtain the older person's clear consent before use and review the cloud services' data handling before sharing recordings or reports.

Risk: The skill silently creates and reuses identities and tokens, including a local token database, without a clear deletion or opt-out path.

Mitigation: Audit identity creation, token storage and retention before installation or deployment; do not use until the deletion and opt-out expectations are acceptable.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured JSON or text/Markdown report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event times, counts, durations, summaries, recommendations and report links; optional saved JSON output.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
