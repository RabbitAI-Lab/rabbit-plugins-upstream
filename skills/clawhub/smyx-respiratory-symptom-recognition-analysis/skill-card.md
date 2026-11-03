## Description:

Analyzes submitted videos for coughing, phlegm, and wheezing patterns and returns a structured respiratory monitoring report for early health awareness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their families can submit a respiratory video to review symptom frequency and receive an early health monitoring report. The report is for reference and does not replace medical diagnosis or examination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option can still upload recordings; account and credential handling and health-recording retention and deletion are not clearly explained.

Mitigation: Avoid identifiable recordings until safeguards are clear. Seek a corrected export-only mode, restricted credential destinations, and clear information about remote registration, token storage, and retention and deletion. Do not rely on --api-url to change the recipient.

Risk: The analysis results and detection accuracy have not been independently verified and could be mistaken for a diagnosis.

Mitigation: Treat reports as health-monitoring information only, not a diagnosis; consult a medical professional for assessment and care.

## Reference(s):

- [Respiratory analysis API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Guidance]

**Output Format:** [Structured respiratory monitoring report with symptom counts, risk indicators, health suggestions, and report links; JSON or Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Health monitoring information only; not a medical diagnosis.]

## Skill Version(s):

1.0.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
