## Description:

Analyzes child monitoring video, optional audio, images, or URLs to classify emotion states such as happy, calm, sad, angry, fearful, crying, or surprised and return a structured report with soothing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as parents, educators, early-childhood staff, and smart-care operators use this skill to analyze child monitoring media for emotion classification, negative-emotion alerts, report history, and non-clinical soothing suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child video, optional audio, media URLs, and inferred emotion reports may be sent to the publisher's cloud service.

Mitigation: Use only with guardian consent, avoid sensitive footage until retention and deletion practices are documented, and confirm where reports are stored.

Risk: The skill uses account identity, history access, and local token persistence to associate and retrieve reports.

Mitigation: Limit access to trusted environments, review account and token handling before deployment, and confirm opt-in, revocation, and report-deletion controls.

Risk: Emotion labels and soothing hints can be mistaken for clinical or psychological diagnosis.

Mitigation: Treat outputs as non-clinical support for caregiving decisions and seek qualified professional advice for persistent or severe distress.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [API error-code documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include emotion class, confidence, intensity, duration, alert status, soothing hint, and exported report link.]

## Skill Version(s):

1.0.21 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
