## Description:

Provides hypothesis-driven chain restaurant operations analysis using restaurant metrics, analysis methods, data validation, and diagnostic reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zizi617-lgtm](https://clawhub.ai/user/zizi617-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Restaurant owners and operations managers use this skill to diagnose chain restaurant performance issues, validate operating data, test business hypotheses, and produce actionable diagnostic summaries or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store user-derived business context in the author's private knowledge base without clearly asking for consent.

Mitigation: Require explicit user consent before storing conversation-derived content, disclose the destination and retention policy, and provide an opt-out or removal path.

Risk: Analysis may mix knowledge-base coverage with AI inference, especially when a scenario or method is missing.

Mitigation: Clearly label conclusions based on inference or fallback references, and distinguish them from knowledge-base-backed findings.

Risk: Restaurant operating data can produce misleading recommendations when metric definitions, time ranges, or source systems are inconsistent.

Mitigation: Validate metric definitions, source systems, time coverage, and cross-check formulas before presenting diagnostic conclusions.

## Reference(s):

- [Data collection guide](references/data-collection-guide.md)
- [Data validation guide](references/data-validation-guide.md)
- [Analysis method index](references/method-index.md)
- [Metric index](references/metric-index.md)
- [Scenario index](references/scenario-index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Analysis]

**Output Format:** [Markdown conversation responses and structured diagnostic reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include data tables, business hypotheses, validation notes, metric comparisons, and recommended next steps.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
