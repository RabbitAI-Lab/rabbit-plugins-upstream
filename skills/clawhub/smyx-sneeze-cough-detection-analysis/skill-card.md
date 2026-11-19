## Description:

Analyzes pet video, with optional audio, to identify possible sneezing and coughing events, record their timing and frequency, and provide behavioral observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary teams, and boarding staff use the skill to review pet video and optional audio for possible sneeze or cough events and track their timing and frequency. Results are behavioral observations and do not provide a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags unclear account and credential handling, including shared-workspace identity behavior.

Mitigation: Clarify and correct these flows before use, and confirm reports are associated with the intended account.

Risk: The security assessment flags privacy concerns involving external media uploads.

Mitigation: Use only approved media and confirm how uploaded clips are transmitted and retained before submitting them.

Risk: The security assessment flags execution-control gaps, an ignored environment-only option, and a mismatch between advertised pet analysis and some bundled code; its scan was partial.

Mitigation: Clarify supported behavior and resolve the reported gaps before use; do not rely on the output as a medical assessment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-sneeze-cough-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured behavior analysis with event timing and frequency, a Markdown report, and an optional report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observations may be uncertain; they are not a veterinary diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
