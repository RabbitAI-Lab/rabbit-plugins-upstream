## Description:

Analyzes smart greenhouse plant imagery with environmental sensor context to produce structured climate-control recommendations for irrigation, shading, ventilation, cooling, and heating.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse operators, agritech developers, and facilities teams use this skill to analyze plant images or videos, optionally with environmental sensor context, and receive structured plant-stress assessments, prioritized control recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Greenhouse media, URLs, identity metadata, and report-history queries are sent to configured remote services.

Mitigation: Install and run the skill only in environments where those data transfers are approved, and restrict inputs to media and URLs suitable for the configured backend service.

Risk: The skill can create or reuse a backend identity and store authentication tokens in a workspace SQLite database.

Mitigation: Use an isolated workspace, protect the workspace data directory, and remove or rotate stored identity data and tokens when the skill is no longer needed.

Risk: Generated control recommendations could cause operational harm if connected directly to irrigation, shading, ventilation, cooling, or heating equipment.

Mitigation: Keep recommendations advisory unless an operator-approved local safety controller, bounded limits, validation checks, and emergency override are in place.

## Reference(s):

- [Greenhouse Climate Plant Feedback Analysis API documentation](artifact/references/api_doc.md)
- [SMYX analysis API error reference](artifact/skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links and optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local media paths, media URLs, detail-level selection, and cloud report-history listing.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
