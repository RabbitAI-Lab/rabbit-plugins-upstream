## Description:

Analyzes tomato and chili flower or fruit-cluster images and videos to count open flowers and young fruits, calculate fruit-set rate, and return structured grower guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers and developers use this skill to analyze tomato, chili, and similar crop images or videos for flower counts, young-fruit counts, fruit-set rate, and practical pollination or environment-adjustment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill sends plant photos or videos, URLs, internal identity values, and report-history queries to a cloud service.

Mitigation: Install only where that data sharing is acceptable, and confirm user consent, retention expectations, and publisher trust before deployment.

Risk: The security evidence flags hidden identity handling, token storage, plaintext development API configuration, and server-triggered payment-skill promotion behavior.

Mitigation: Review configuration before release, require HTTPS production endpoints, avoid plaintext token storage, and remove or clearly gate payment-skill promotion in analysis results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-flowering-fruit-set-rate-analysis-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured text with analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce flower and young-fruit counts, fruit-set-rate calculations, recommendations, saved result files, and cloud report-history listings.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
