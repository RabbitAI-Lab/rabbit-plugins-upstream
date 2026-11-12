## Description:

Analyzes infant diaper or stool images for color categories such as pale, red, or black, then returns a structured risk-oriented report and follow-up guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and pediatric-care teams can submit infant diaper or stool images to review an automated color classification and risk-oriented report. The skill can also retrieve previously generated reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied security assessment marks this release suspicious because scanners report behavior beyond its stated image-analysis purpose, with privacy, consent, and unexpected-processing concerns; the scan is partial.

Mitigation: Before installing, verify the remote service, what data is sent, and how account creation and token storage work. Confirm that image processing requires consent and export-only mode does not process inputs; the partial scan cannot resolve behavior involving the missing reference.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [API reference](references/api_doc.md)
- [Sample demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance, Report links]

**Output Format:** [Structured JSON text with risk guidance and report export links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Color classification, risk level, confidence, suggested next step, and links to reports when provided by the service.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
