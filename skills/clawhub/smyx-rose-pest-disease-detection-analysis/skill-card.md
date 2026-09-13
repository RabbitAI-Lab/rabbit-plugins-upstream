## Description:

Analyzes rose images or videos to identify common pests and diseases, grade severity, and provide general control suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External gardeners, horticulture staff, and developers use this skill to analyze rose leaf, shoot, and bud media for pest or disease type, severity, and practical care guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rose images or videos may be uploaded to external services.

Mitigation: Review destination and service terms before use, and avoid private media unless the publisher fixes destination validation and consent issues.

Risk: The skill can silently create or reuse an internal identity and store reusable authentication tokens in a shared local SQLite database.

Mitigation: Run the skill in an isolated workspace, inspect and clear stored tokens, and require explicit identity consent before deployment.

Risk: The server security guidance flags unsafe default networking or configuration behavior.

Mitigation: Validate endpoint configuration, pin dependencies, and block unsafe default endpoints before commercial deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rose-pest-disease-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports and JSON-like structured text with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity grades, general control suggestions, report links, and Markdown tables for history queries.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
