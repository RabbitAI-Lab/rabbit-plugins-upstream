## Description:

Analyzes plant leaf images or videos to identify likely nutrient deficiencies and return a confidence-scored diagnosis with fertilization direction guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, gardeners, growers, and developers use this skill to submit plant leaf media for nutrient deficiency diagnosis and retrieve current or historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or media URLs may be sent to an external service for analysis.

Mitigation: Use only with media the user is permitted to upload and disclose external processing before deployment.

Risk: The skill can silently create or reuse an identity, query cloud history, and store tokens or profile data in a local workspace database.

Mitigation: Review identity, retention, token storage, and history-query behavior with the publisher before use.

Risk: The evidence reports private development API endpoints in the packaged configuration.

Mitigation: Correct configuration to production HTTPS endpoints and verify endpoint ownership before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [Plant nutrient diagnosis API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON diagnosis reports, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include nutrient labels, confidence scores, fertilization direction guidance, report links, and historical report tables.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
