## Description:

Diagnoses likely plant nutrient deficiencies from plant leaf images or videos and returns structured findings, confidence, guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, gardeners, growers, and agricultural operators use this skill to analyze plant leaf media for likely nutrient deficiencies and receive structured diagnostic output. Developers and agents can also use it to call the packaged analysis workflow or retrieve cloud-hosted report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or URLs may be sent to LifeEmergence cloud APIs for analysis.

Mitigation: Review cloud data handling before installation and use only with media approved for that external service.

Risk: The security scan reports automatic account or identity association, cloud report-history lookups, and local SQLite storage of service tokens.

Mitigation: Deploy in an isolated environment until identity handling, token retention, and logout or revocation behavior are reviewed.

Risk: The security scan reports that the implementation does not fully match the advertised leaf-image diagnosis scope.

Mitigation: Confirm the packaged behavior against the plant diagnosis workflow before relying on results in production.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Plant Nutrient Diagnosis API doc](references/api_doc.md)
- [Shared AI Analysis API doc](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured JSON-like text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the generated analysis output to a local file when an output path is provided.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
