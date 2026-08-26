## Description:

Evaluates plant images, optional environmental data, and growth metrics to produce a 0-100 plant vitality score, sub-scores, a trend, and alert hints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill in smart planter, plant factory, home gardening, or plant-monitoring workflows to analyze plant media and optional measurements for a vitality score and trend. It is intended for reference-level plant health assessment rather than prescriptive care instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media or URLs are processed by the Life Emergence remote service.

Mitigation: Avoid sensitive images or private URLs unless the publisher documents retention, account binding, endpoint configuration, and token storage controls.

Risk: The skill silently creates or reuses an internal identity, queries cloud history, and persists tokens locally.

Mitigation: Review account binding, cloud history, and token storage controls before deployment; restrict use to environments where those behaviors are acceptable.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or JSON structured analysis report with score, grade, trend, sub-scores, alert hints, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an output file when requested; history lookup returns a Markdown table based on cloud report data.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
