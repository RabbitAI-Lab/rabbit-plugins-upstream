## Description:

Turns local AIops audit trails into framework-mapped compliance reports and tamper-evident evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and auditors use this skill to assess control coverage, investigate gaps and approvals, and generate or verify evidence bundles from existing local AIops audit trails. It provides evidence, not compliance certification or infrastructure scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to local audit trails or generated evidence could expose sensitive operational records.

Mitigation: Run under an account authorized to read the discovered audit databases and restrict access to local configuration, audit logs, and bundles.

Risk: An unattended signing setup could expose the signing password or run under an overprivileged account.

Mitigation: Use a least-privilege account, protect COMPLIANCE_AIOPS_MASTER_PASSWORD, and review the generated cron line before installation.

Risk: Incomplete audit trails or an unanchored bundle could lead to overstated compliance or integrity claims.

Mitigation: Check source coverage and report caveats, verify the source and bundle chains, and retain the bundle chain head out of band; treat the output as evidence, not certification.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/compliance-aiops)
- [Project homepage (skill metadata; not verified provenance)](https://github.com/AIops-tools/Compliance-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, CSV, Configuration guidance]

**Output Format:** [Framework-mapped reports and locally generated evidence bundles; JSON, Markdown, CSV, and OSCAL export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bundles include a reproducible hash-chain seal and support optional signing; evidence does not establish certification.]

## Skill Version(s):

0.14.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
