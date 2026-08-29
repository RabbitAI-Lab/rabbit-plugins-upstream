## Description:

A cloud-assisted clinical-trial advisor that answers methodology, design, compliance, QC, regulatory, statistics, safety, and evidence questions, routing data and sample-size work to local ct-series sibling skills when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical-trial practitioners, clinicians, nurses, medical students, and developers use this skill to get source-traced clinical-development guidance, protocol and document feedback, regulatory interpretation, and routed live-data or sample-size support through the ct-series skill family.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical-trial questions, converted attachment text, and bounded conversation history may be processed by remote Coze services.

Mitigation: Use the skill only for data that your organization allows to leave the device, and do not submit real patient, sponsor-confidential, unpublished protocol, or regulated internal data unless the endpoint and handling are approved.

Risk: Requests include stable host correlation metadata.

Mitigation: Deploy only where stable machine-level correlation is acceptable for the project and endpoint policy.

Risk: Local memory and context files may retain sensitive project context.

Mitigation: Review local memory and context files and clear them between sensitive projects.

Risk: Optional bug reports can transmit user-reviewed issue descriptions to a remote endpoint.

Mitigation: Inspect the proposed report before confirmation, remove sensitive details from the description, or decline submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Publisher Profile](https://clawhub.ai/user/medstatstar)
- [Project Homepage](https://github.com/medstatstar/ct-advisor)
- [README](README.md)
- [Chinese README](README_zh-CN.md)
- [Advanced Reference](references/ADVANCED.md)
- [Execution Steps](references/steps.md)
- [Reference Index](knowledge/reference-index.md)
- [ClawHub Audit Trace](docs/clawhub_audit_trace_20260815.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown conversational answer with source labels, verification markers, tables, or handoff results when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual output follows the user's language preference; data-grounded claims are intended to carry source labels or official-verification warnings.]

## Skill Version(s):

0.9.103 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
