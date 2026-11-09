## Description:

Uses facial images or video and optional physiological measurements to produce a structured stroke-risk screening report with risk indicators and health guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

People or health-service operators can submit a face image or video and optional blood pressure, blood sugar, or blood lipid measurements to request a structured screening report and guidance. The skill describes its output as screening information, not a substitute for medical examination or diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health reports may be mixed across users, and the skill may start cloud analysis despite an explicit no-analysis option.

Mitigation: Use synthetic or test data in shared workspaces until caller isolation is confirmed. Require clear consent before uploads or account registration, protect credentials, restrict destinations to HTTPS, and confirm the provider's retention and deletion policies before use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON or human-readable screening report; report lists are returned as structured text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local or URL-based images and videos, with optional blood pressure, blood sugar, and blood lipid values; can save results to a file and query report history.]

## Skill Version(s):

1.0.18 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
