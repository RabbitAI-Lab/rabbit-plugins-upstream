## Description:

Detects morbid behavioral cues in poultry and pigs from continuous barn videos — such as difficulty standing, ruffled feathers/piloerection, isolation, drowsiness and appetite loss — and outputs behavior type with risk level up to 2-3 days ahead of visible clinical signs. | 识别站立困难、羽毛蓬松、离群、嗜睡等病态行为，比人工观察提前2-3天。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock farm operators and their AI agents can screen poultry or swine barn images and videos for unusual behavior, then review a structured report with observed cues, affected locations, and a risk level. The results support early health checks and do not provide a diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn footage submitted for analysis is sent to LifeEmergence's service, and the service's retention terms and charges are not established in the supplied evidence.

Mitigation: Avoid sensitive footage until the provider's retention terms and charges are confirmed; use footage approved for external processing.

Risk: The export-only option still runs analysis, and locally stored account credentials lack adequate safeguards.

Mitigation: Do not rely on export-only mode to prevent uploads; request fixes for export-only handling, credential destination checks, token protection, and debug logging before using sensitive footage.

Risk: Behavior screening results may be mistaken for a veterinary diagnosis.

Mitigation: Treat reports as early screening only and consult a veterinarian and laboratory testing for diagnosis or treatment decisions.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured behavior analysis reports in JSON or Markdown, plus Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior cues, animal locations, risk levels, group-level proportions, and report links; results are for screening reference.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
