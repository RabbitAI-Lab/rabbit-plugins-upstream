## Description:

Provides preliminary stroke-risk screening from facial images or video and optional health indicators, with risk warnings and lifestyle and care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking preliminary screening can submit facial images or video and optional blood pressure, blood sugar, or blood lipid measurements to receive a risk report, suggested follow-up, and access to historical reports. Results are not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facial media and optional health indicators may be sent to lifeemergence.com services.

Mitigation: Obtain explicit consent before transfer and disclose what is shared, with whom, and under what privacy and retention terms.

Risk: Account identifiers and report history may be created, reused, or stored without clear user awareness.

Mitigation: Disclose identity and storage behavior, define retention and deletion controls, and confirm before retrieving historical reports.

Risk: Screening warnings may be mistaken for a clinical diagnosis or definitive stroke prediction.

Mitigation: Present results as preliminary screening only and direct users with concerning findings to a qualified clinician.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Bundled API reference (verify applicability)](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report with risk findings, recommendations, and report links; optional JSON or saved file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list historical reports; screening results do not replace clinical assessment.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
