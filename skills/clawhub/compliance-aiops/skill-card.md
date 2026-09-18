## Description:

Produces compliance evidence from governed AIops audit trails by mapping recorded agent activity to HIPAA, PCI-DSS, SOC 2, GDPR, ISO 27001, and DJCP controls, generating reports, and creating hash-chain-sealed evidence bundles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and compliance teams use this skill to inspect local AIops audit databases, summarize framework control coverage, identify evidence gaps, and prepare tamper-evident evidence bundles for review. It supports evidence preparation, not certification or infrastructure operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the release installs mutable external code.

Mitigation: Review before installing and use a pinned, verified package version where possible.

Risk: The release has inconsistent write-scope disclosures around generated bundles and exports.

Mitigation: Run under a restricted account with access only to the audit databases needed and treat generated bundles as sensitive compliance records.

Risk: Unattended signing through cron or CI can expose signing operations to misconfiguration or weak secret handling.

Mitigation: Avoid unattended signing until secret handling is reviewed; if signing is needed, provide the master password through a protected environment and verify the generated bundle.

Risk: Compliance outputs can be mistaken for a pass, certification, or full control verdict.

Mitigation: Present outputs as evidence from available audit trails only, preserve caveats about partial coverage, and have qualified reviewers assess certification or compliance status.

## Reference(s):

- [Compliance AIops source repository](https://github.com/AIops-tools/Compliance-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, plus generated JSON, Markdown, CSV, or OSCAL evidence artifacts when bundle tools are used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local audit databases read-only; generated bundles and exports are written under the compliance-aiops home directory and may contain sensitive compliance evidence.]

## Skill Version(s):

0.11.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
