## Description:

Compliance AIops helps agents read local governed AIops audit trails and turn them into framework-mapped reports, gap analyses, change-approval evidence, exceptions reports, and tamper-evident evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and compliance teams use this skill to collect evidence from existing AIops audit trails for HIPAA, PCI-DSS, SOC 2, GDPR, ISO 27001, and DJCP L3 control reviews. It supports coverage summaries, control evidence, approval and exceptions reports, gap analysis, and sealed evidence bundles without operating infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local AIops audit databases available to the account and persists compliance state under ~/.compliance-aiops.

Mitigation: Install and run it only from accounts that should access those audit trails, and treat ~/.compliance-aiops as sensitive local state.

Risk: The artifact discloses no hard read-only mode or approval prompt for bundle-producing actions.

Mitigation: For query-only sessions, enforce restrictions through the agent prompt, tool allowlist, or operating-system permissions before use.

Risk: Generated bundles, the local audit database, and any optional signing key may contain or protect sensitive evidence.

Mitigation: Review retention, filesystem permissions, and key handling for ~/.compliance-aiops, and protect generated bundles according to the organization's evidence-handling policy.

Risk: Compliance reports can be misread as certification or a pass/fail verdict.

Mitigation: Present outputs as evidence from recorded audit trails only, include caveats and truncation indicators, and avoid claims that the organization is compliant or certified.

## Reference(s):

- [Compliance AIops repository](https://github.com/AIops-tools/Compliance-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/compliance-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and text guidance with inline shell commands; generated evidence bundles can be exported as JSON, Markdown, or CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local SQLite audit databases and may write evidence bundles under ~/.compliance-aiops/bundles/ when bundle tools are used.]

## Skill Version(s):

0.9.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
