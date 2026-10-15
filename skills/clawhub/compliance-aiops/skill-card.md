## Description:

Turns local AIops audit trails into framework-mapped compliance reports and tamper-evident evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Compliance teams, auditors, and developers use this skill to review local AIops audit trails for control coverage, approval and exception evidence, gaps, and sealed evidence bundles. It supports evidence preparation, not certification or infrastructure scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local AIops audit databases may contain sensitive activity records, and bundle creation writes evidence files.

Mitigation: Install only if local audit access is appropriate; keep sessions query-only unless bundle generation is intended and protect the resulting files.

Risk: Bundle signing relies on a master password and an optional signing key.

Mitigation: Protect COMPLIANCE_AIOPS_MASTER_PASSWORD and sign only when needed.

Risk: A proposed cron line could schedule unintended recurring evidence exports.

Mitigation: Review the cron line manually before installing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/compliance-aiops)
- [Project homepage](https://github.com/AIops-tools/Compliance-AIops)
- [Capabilities and tool reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Shell commands, Guidance]

**Output Format:** [Framework coverage and gap reports, approval and exception summaries, locally stored evidence bundles, and optional scheduling commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bundles use a reproducible hash-chain seal and may be signed; integrity is tamper-evident, not tamper-proof.]

## Skill Version(s):

0.13.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
