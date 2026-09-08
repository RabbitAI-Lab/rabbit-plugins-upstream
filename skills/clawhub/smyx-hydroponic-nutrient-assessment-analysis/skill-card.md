## Description:

Assesses hydroponic root and leaf images or videos to identify visual stress signs, estimate whether nutrient solution is too concentrated or too dilute, and provide qualitative adjustment guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Hydroponic growers, plant-factory operators, and developers integrating grow-rack or mobile-app workflows use this skill to analyze root and leaf media and receive qualitative nutrient concentration guidance and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded plant images or videos may be processed by remote services.

Mitigation: Use the skill only when remote processing is acceptable and avoid uploading sensitive or unnecessary media.

Risk: Account-linked history retrieval and local identity reuse may occur without explicit user interaction.

Mitigation: Require clear user confirmation before cloud history queries and document identity behavior for operators.

Risk: Default service settings include HTTP endpoints and local plaintext token persistence.

Mitigation: Use HTTPS-only production endpoints and secure token storage before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Qualitative visual assessment only; no EC or ppm values are produced.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter declares 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
