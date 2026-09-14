## Description:

Compliance AIops helps agents turn local AIops audit trails into framework-mapped compliance evidence, gap analyses, approval and exception reports, and tamper-evident evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and compliance teams use this skill to gather evidence from existing governed AIops audit logs for HIPAA, PCI-DSS, SOC 2, GDPR, ISO 27001, and DJCP L3 review workflows. It is intended for evidence collection, control coverage review, gap analysis, approval and exception reporting, and tamper-evident bundle generation, not for infrastructure operation or certification decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install mutable external package code.

Mitigation: Install only from a trusted publisher and pin or verify the package release before use.

Risk: Unattended signed evidence generation can use local secrets without a built-in approval gate.

Mitigation: Run the skill under a least-privileged account, restrict access to intended audit databases, and use secure handling for COMPLIANCE_AIOPS_MASTER_PASSWORD.

Risk: Generated bundles may be mistaken for compliance certification.

Mitigation: Treat outputs as evidence artifacts only and have qualified reviewers assess compliance scope and conclusions.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/Compliance-AIops)
- [Capabilities reference](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated evidence artifacts can be JSON, Markdown, CSV, or OSCAL JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on local read-only audit databases; evidence bundles are written under ~/.compliance-aiops/bundles/ and can include hash-chain seals and optional signatures.]

## Skill Version(s):

0.11.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
