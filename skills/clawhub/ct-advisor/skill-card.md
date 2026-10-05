## Description:

Provides cloud-assisted guidance on clinical trial design, methodology, compliance, safety, and study execution, with optional document analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Clinical trial sponsors, CRO teams, clinicians, and researchers use this skill to ask about study design, methodology, GCP, regulatory compliance, and trial operations, optionally with supporting documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinical questions and attached documents are sent to external Coze services.

Mitigation: Use only when this transfer is authorized; do not attach patient information, confidential protocols, or sponsor-sensitive material without permission.

Risk: An environment-controlled upload destination may redirect document uploads.

Mitigation: Remove or constrain CT_ADVISOR_UPLOAD_ENDPOINT and review auto-approved endpoints before use.

Risk: Long-term memory rules may alter the agent's persistent behavior.

Mitigation: Disable or ignore AGENTS.md memory promotion rules unless persistent changes are intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/medstatstar/skills/ct-advisor)
- [Publisher-listed project homepage](https://github.com/medstatstar/ct-advisor)
- [English usage guide](https://github.com/medstatstar/ct-advisor/blob/main/README.md)
- [Chinese usage guide](https://github.com/medstatstar/ct-advisor/blob/main/README_zh-CN.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask clarifying questions before providing advice.]

## Skill Version(s):

1.2.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
