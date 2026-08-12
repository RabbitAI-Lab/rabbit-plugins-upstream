## Description:

Analyzes aquarium plant images or videos to identify visual health issues and produce structured care suggestions and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to assess aquatic plant health from aquarium camera media, including color changes, morphology issues, algae, likely nutrient symptoms, and practical care direction. It also supports cloud report retrieval for prior analyses linked to the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media, provided URLs, report history, and an automatically generated or environment-derived identity may be sent to lifeemergence.com services.

Mitigation: Treat the skill as cloud-connected and account-linked; avoid sensitive aquarium footage or private media URLs unless that data flow is acceptable.

Risk: The skill stores or reuses local identity tokens to associate analyses and history retrieval.

Mitigation: Review token storage and identity handling before installation in shared or regulated environments.

Risk: Visual plant-health symptoms can be ambiguous and the output is not a substitute for full water-quality diagnosis.

Mitigation: Use the results as care direction only and confirm important decisions with water testing or an aquarium specialist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis report with optional saved output file and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video paths or media URLs; history lookup returns cloud report records.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
