## Description:

Analyzes newborn facial images or short videos for visible jaundice indicators and returns a preliminary risk hint with follow-up guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and neonatal care staff can use it for preliminary visual monitoring of possible jaundice from newborn face images or short videos, as an initial screening prompt alongside clinical care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared default account may expose one user's reports to another.

Mitigation: Avoid shared-user deployments until account isolation is corrected and verified.

Risk: Sensitive newborn images may be sent to an external processor, including in export-only mode.

Mitigation: Do not use real newborn media until export-only behavior is corrected; confirm processor retention and deletion terms, obtain guardian authorization, and protect stored credentials.

Risk: Visual screening results may be inaccurate or mistaken for a clinical diagnosis.

Mitigation: Treat results as preliminary only; confirm concerns with a clinician and appropriate bilirubin testing, and seek prompt care for medium or high risk.

## Reference(s):

- [Skill listing](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON analysis and Markdown report or history list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual indicators, a preliminary risk level, confidence, suggested next steps, and report links.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
