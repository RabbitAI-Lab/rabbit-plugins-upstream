## Description:

Analyzes overnight bedroom video and audio to summarize events such as sudden sitting up, shouting, and rapid arm movements with their times, counts, and durations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family members and caregivers use it to review overnight recordings and summarize unusual movement or sound events. Clinicians may use the event report as supporting information during an evaluation; it does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private bedroom recordings may be uploaded for remote analysis, including in export-only mode.

Mitigation: Wait until the export-only behavior is fixed before using private recordings; obtain the recorded person's explicit consent and confirm the provider's retention and deletion practices before transfer.

Risk: Service-account credential handling lacks safeguards.

Mitigation: Wait for credential handling to be fixed before using service credentials with private recordings.

Risk: Server-side privacy protections and analysis reliability are unverified, and reports could be mistaken for medical conclusions.

Mitigation: Treat results as observational event summaries rather than diagnoses, and seek clinical assessment for health concerns.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Guidance]

**Output Format:** [Structured JSON or text analysis reports, with Markdown tables for history lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event times, counts, durations, summaries, risk signals, recommendations, and report links based on the supplied recording.]

## Skill Version(s):

1.0.15 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
