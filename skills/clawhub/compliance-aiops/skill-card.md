## Description:

Compliance AIops turns local AIops audit trails into framework-mapped evidence reports and tamper-evident evidence bundles for HIPAA, PCI-DSS, SOC 2, GDPR, ISO 27001, and DJCP L3.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform teams, and compliance operators use this skill to query existing AIops audit trails, map recorded activity to compliance controls, produce approval, exception, coverage, and gap reports, and generate sealed evidence bundles. It supports evidence collection and review, not certification or infrastructure operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive local audit evidence and may expose operational history through reports or bundles.

Mitigation: Run it under a dedicated least-privilege account with access only to the audit databases intended for review.

Risk: Unattended or signed bundle generation can depend on local secret delivery and may create evidence artifacts without an interactive review step.

Mitigation: Use protected secret delivery for COMPLIANCE_AIOPS_MASTER_PASSWORD, avoid unattended signing unless required, and review generated bundles before sharing.

Risk: Generated bundles are evidence derived from local audit logs and can be mistaken for certification or a complete compliance verdict.

Mitigation: Treat outputs as supporting evidence only, preserve the source audit databases as the system of record, and have qualified reviewers assess final compliance.

Risk: Package provenance is unavailable for this release in server-resolved evidence.

Mitigation: Review package provenance and pin or verify the exact release before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/compliance-aiops)
- [Project homepage](https://github.com/AIops-tools/Compliance-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON, Code, Configuration]

**Output Format:** [Markdown guidance with CLI commands and generated evidence outputs in JSON, Markdown, CSV, or OSCAL JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces reports and local evidence bundles from existing audit databases; signed bundles require an optional configured signing key.]

## Skill Version(s):

0.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
