## Description:

Compliance AIops maps local AIops audit trails to common compliance frameworks and produces reports, gap analysis, and tamper-evident evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform operators, and compliance teams use this skill to turn existing local AIops audit logs into framework-mapped evidence, approval and exception reports, gap analysis, and verifiable evidence bundles. It supports evidence collection and integrity checks, not infrastructure scanning, GRC policy management, or compliance certification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release installs executable tooling that may be unpinned.

Mitigation: Install only from a trusted publisher and pin or verify the exact release before running it.

Risk: The skill reads sensitive audit trails and may handle bundle-signing secrets.

Mitigation: Run it under a dedicated low-privilege account, limit readable audit databases to intended sources, and avoid command-line or inline environment secrets for signing keys.

Risk: Signed or sealed bundles may be mistaken for proof of compliance.

Mitigation: Treat generated bundles as evidence artifacts only; compliance certification requires separate assessor judgement and broader scope.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/Compliance-AIops)
- [compliance-aiops capabilities](references/capabilities.md)
- [compliance-aiops CLI reference](references/cli-reference.md)
- [compliance-aiops setup and security guide](references/setup-guide.md)
- [Agent guardrails for compliance-aiops](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated evidence artifacts in JSON, Markdown, CSV, or OSCAL formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local evidence bundles under the configured compliance-aiops home directory; signed bundles are tamper-evident, not certification.]

## Skill Version(s):

0.11.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
