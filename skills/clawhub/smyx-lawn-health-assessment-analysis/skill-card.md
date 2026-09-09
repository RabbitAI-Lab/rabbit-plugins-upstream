## Description:

Analyzes top-down lawn images or videos to estimate yellowing, weed coverage, bare soil, and an overall lawn health score with maintenance guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External grounds managers, facilities teams, and turf maintenance operators use this skill to assess lawn quality from drone, fixed-camera, or other top-down imagery. It produces visual health metrics and care-direction guidance for home lawns, golf courses, municipal parks, and sports fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence flags cloud-backed analysis with silent account setup, persistent plaintext tokens, and default development HTTP configuration that may expose user media or credentials.

Mitigation: Review before installation; do not use private lawn imagery or sensitive environments until HTTPS production defaults, token persistence, and upload/history retention behavior are fixed and documented.

Risk: History lookup and automatic identity association can reuse or create account context without user-visible identity handling.

Mitigation: Require deployment review of account association behavior and clearly document cloud upload, report history access, and retention expectations for operators.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured JSON-like analysis results, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include lawn condition metrics, health score, maintenance guidance, and cloud report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter: 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
