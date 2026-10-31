## Description:

Analyzes overnight bedroom video and audio to summarize possible sleep events such as sudden sitting, shouting, and rapid arm movements, with event timing, frequency, and duration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and care staff use it to summarize possible nighttime sleep events from an older adult's bedroom recording and share event timing and frequency as reference for clinical evaluation. The report is not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private bedroom recordings may be uploaded even when analysis is disabled, and account credentials lack adequate safeguards.

Mitigation: Defer uploading recordings until the export-only and credential-handling defects are fixed. Confirm account ownership, consent to external processing, and the provider's retention, access, and deletion arrangements.

## Reference(s):

- [API interface notes (incomplete)](references/api_doc.md)
- [Skill introduction demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured event report with timeline, counts, risk signal, plain-language summary, and report link; JSON or Markdown depending on the selected detail level.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event timestamps, durations, counts, and suggested clinical follow-up; not a medical diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
