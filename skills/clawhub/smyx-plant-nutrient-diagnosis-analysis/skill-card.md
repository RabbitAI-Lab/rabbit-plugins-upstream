## Description:

Analyzes plant leaf images or videos for likely nutrient deficiencies and provides diagnostic reports with confidence scores and guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners and agricultural teams use plant leaf images or videos to identify possible nutrient deficiencies, review confidence scores and recommendations, and retrieve past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or supplied URLs are sent to an external service.

Mitigation: Share media only if the service is trusted and the content is approved for external processing.

Risk: The skill silently creates or reuses an identity, stores authentication tokens locally, and can retrieve linked report history.

Mitigation: Review identity, local token storage, and history-access behavior before installation; limit use to approved workspaces.

Risk: Similar symptoms and unclear images can make nutrient diagnoses uncertain.

Mitigation: Check results against plant species and soil tests; consult an agronomy specialist before fertilizing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured diagnostic report or Markdown history table; JSON output is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include likely deficient nutrients, confidence scores, recommendations, and report links; results are not fertilizer dosage instructions.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence; bundled frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
