## Description:

Analyzes images or videos of medicinal herb leaves to estimate active-ingredient accumulation trends from visual indicators and return a Low, Medium, High, or Peak trend assessment with harvest guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers in medicinal herb cultivation use this skill to evaluate leaf imagery from planting bases, cooperatives, and pharmaceutical raw-material operations. It supports harvest-window decisions by producing a visual trend estimate and related report output, not formal chemical testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload selected images or videos to a remote service for analysis.

Mitigation: Install only when remote media processing is acceptable, and avoid submitting sensitive imagery unless the service and data handling practices have been reviewed.

Risk: The skill may silently create or reuse a local identity, query cloud report history, and retain account tokens.

Mitigation: Review credential storage, token deletion, and identity/report-history controls before deployment.

Risk: Release security guidance calls for moving away from development HTTP endpoints and enforcing HTTPS.

Mitigation: Use reviewed production endpoints over HTTPS before broad or commercial use.

Risk: The analysis estimates herbal ingredient accumulation from visual features and is not a chemical assay.

Mitigation: Use the result as harvest-decision support and confirm formal quality assessments with appropriate laboratory or pharmacopeia testing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis)
- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown report or JSON-style structured analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include visual trend level, harvest timing guidance, risk notes, report links, or a history table.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
