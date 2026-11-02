## Description:

Analyzes respiratory images or videos to estimate cough, phlegm, and wheezing frequency, summarize severity, and provide early health monitoring alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, families, and care teams can use the skill to review respiratory monitoring media, track symptom frequency, and prepare reports that support follow-up with a healthcare professional. Results are for health reference and do not replace medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only setting may still allow health-video analysis, including identifiable content.

Mitigation: Correct and verify the setting and credential destination safeguards before using identifiable health videos.

Risk: Uploaded health media and analysis reports are handled by a cloud service, and credentials and a default account are used by the workflow.

Mitigation: Review the service's retention and deletion practices, protect the workspace token database, and avoid sharing the default account between unrelated users.

Risk: Automated symptom estimates and recommendations may be mistaken for a medical diagnosis.

Mitigation: Treat reports as health references only; consult a healthcare professional, and seek urgent care for severe breathing difficulty.

## Reference(s):

- [Respiratory Symptom Recognition API Documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured symptom analysis report in JSON or Markdown; history listings in Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include symptom counts, severity estimates, health warnings, medical suggestions, and report links. Health information is for reference only.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
