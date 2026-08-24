## Description:

Assesses ornamental fish images or videos for color saturation, brightness, species-specific baseline fit, vibrancy score, trends, and husbandry-oriented recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, ornamental fish farms, public aquariums, and developers integrating smart aquarium workflows use this skill to analyze fish media and generate color vibrancy reports. It supports recurring review of saturation, brightness, baseline comparison, trend, and suggested management actions without providing veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied aquarium images, videos, or URL references may be sent to a remote cloud service for analysis.

Mitigation: Use only non-sensitive aquarium media and install the skill only where cloud processing of that media is acceptable.

Risk: The skill may automatically create or reuse account identity state and store identity tokens in a local workspace database.

Mitigation: Run it in a workspace where this persistence is acceptable, review local data handling before installation, and remove workspace data when the identity state is no longer needed.

Risk: Historical report lookup can query account-linked analysis history.

Mitigation: Use history lookup only when the user requests prior reports and confirm that the workspace account context is appropriate for the reports being retrieved.

Risk: Color-vibrancy results could be mistaken for a veterinary diagnosis or direct treatment instruction.

Mitigation: Treat outputs as color and husbandry screening guidance only; avoid medicine or product-brand recommendations and consult a qualified ornamental fish veterinarian or expert for health decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)
- [API documentation](references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, shell commands]

**Output Format:** [Markdown or JSON structured analysis report with report links and optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vibrancy score, HSV values, baseline comparison, trend fields, alert level, recommended actions, and report export URL.]

## Skill Version(s):

1.0.8 (source: server release metadata; packaged SKILL.md frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
