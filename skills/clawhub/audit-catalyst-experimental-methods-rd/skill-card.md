## Description:

Audit catalyst preparation and evaluation methods for executability, reproducibility, controlled comparison, attribution, measurement reliability, safety-review readiness, and claim-to-evidence linkage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Research scientists, principal investigators, technical reviewers, and R&D teams use this skill to audit catalyst preparation and evaluation methods before experimentation or review. It identifies missing execution details, reproducibility gaps, weak controls or baselines, measurement-reliability issues, safety-review readiness gaps, and unsupported performance or mechanistic claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes potentially confidential experimental methods and writes local report files.

Mitigation: Provide only files intended for audit, use a dedicated output directory, and handle generated JSON, HTML, and DOCX reports according to the applicable confidentiality rules.

Risk: Optional patent or scientific evidence lookups could expose submitted material or related context to an external service if authorized separately.

Mitigation: Do not authorize external lookups unless that transmission is intended and approved for the material under review.

Risk: The audit can surface safety-review readiness gaps but does not certify laboratory safety, regulatory compliance, patentability, or result authenticity.

Mitigation: Use the report as technical review input and route hazards, pressure equipment, toxic gases, waste, and institutional requirements to qualified specialist review.

## Reference(s):

- [Audit methodology](references/methodology.md)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/audit-catalyst-experimental-methods-rd)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and generated JSON, HTML, and DOCX report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local workflow writes report_context.json plus one HTML report and one Word report to a dedicated output directory, then validates those outputs.]

## Skill Version(s):

1.0.0 (source: server release metadata); artifact VERSION and CHANGELOG show 0.5.0 source package lineage

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
