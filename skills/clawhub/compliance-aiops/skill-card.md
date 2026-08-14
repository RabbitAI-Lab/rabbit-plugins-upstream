## Description:

Compliance AIops turns local governed AIops audit trails into framework-mapped compliance evidence, reports, gap analysis, OSCAL assessment results, and hash-chain-sealed evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and compliance teams use this skill to inspect local AIops audit trails, map recorded activity to HIPAA, PCI-DSS, SOC 2, GDPR, ISO 27001, or DJCP L3 controls, and produce evidence reports or sealed bundles for review. It supports evidence gathering and integrity checks, not compliance certification or infrastructure operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local AIops audit databases and may write evidence bundles and state under ~/.compliance-aiops.

Mitigation: Use a dedicated account or filesystem permissions for query-only operation, and verify discovered audit sources before generating bundles.

Risk: Generated bundles and reports can be mistaken for compliance certification.

Mitigation: Treat outputs as evidence artifacts for qualified review; do not present them as proof of certification or full compliance.

Risk: Optional bundle signing depends on a local signing secret and master password.

Mitigation: Only configure signing when needed, keep COMPLIANCE_AIOPS_MASTER_PASSWORD out of command history and cron lines, and rely on the encrypted secrets store.

Risk: A sealed bundle is tamper-evident, not tamper-proof.

Mitigation: Record chain heads out of band and use verify_bundle and verify_source_chain to check delivered bundles and source audit trails.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/compliance-aiops)
- [Project Homepage](https://github.com/AIops-tools/Compliance-AIops)
- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup and Security Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, CSV, OSCAL JSON, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local evidence reports, exported bundles, integrity verification results, and setup or scheduling guidance.]

## Skill Version(s):

0.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
