## Description:

Provides governed Veeam Backup & Replication operations for health overview, diagnostics, backup job control, restore-point inspection, VM restore starts, repository capacity checks, backup inventory, infrastructure inventory, and async session polling or cancellation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and backup administrators use this skill to let an agent inspect and operate Veeam Backup & Replication environments through CLI or MCP workflows. It is intended for common backup operations, diagnostics, repository capacity review, restore-point discovery, controlled job actions, and audited restore/session workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose high-impact backup, job-control, session-stop, and restore actions to an agent without an enforced MCP approval or read-only gate.

Mitigation: Use a dedicated least-privilege or read-only Veeam account by default, and rely on the Veeam account role plus agent policy to limit write tools.

Risk: Restore starts and session stops can be irreversible or lack an undo path.

Mitigation: Use dry-run previews, verify the named target before approval, and prefer restore operations only under an explicit operational change window.

Risk: Credential handling can become risky if legacy plaintext environment variables or shared static configs are used.

Mitigation: Use the encrypted secret store, keep the master password out of shared configuration, and migrate legacy plaintext password paths.

Risk: Package or plugin resolution could introduce supply-chain uncertainty before write or restore features are used.

Mitigation: Pin and verify the package or plugin source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Project homepage](https://github.com/AIops-tools/Veeam-AIops)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and structured MCP tool-call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may include JSON payloads, truncation indicators, audit context, risk tiers, and undo identifiers for reversible writes.]

## Skill Version(s):

0.16.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
