## Description:

Analyzes plant images, environmental data, and growth metrics to return a 0–100 vitality score and a rising, stable, or declining trend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and plant-monitoring operators use the skill to assess plant vitality from images and optional environmental or growth measurements, review changes over time, and query historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may register a service account, retain its tokens locally, and upload selected media, including when analysis is skipped.

Mitigation: Require explicit enrollment and upload controls, protect stored tokens, and use export-only mode when possible. Avoid sensitive footage and unrelated credentials.

Risk: The cloud service's retention and scoring behavior remain unverified.

Mitigation: Review deletion and retention controls before use, and treat returned scores as unverified assessments.

## Reference(s):

- [Plant Vitality API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis report; historical listings can be presented as Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a 0–100 score, grade, trend, change percentage, sub-scores, alerts, and a report link.]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
