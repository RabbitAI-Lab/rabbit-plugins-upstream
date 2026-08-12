## Description:

Governed Veeam Backup & Replication operations with MCP and CLI support for health checks, diagnostics, backup jobs, restores, repositories, infrastructure inventory, sessions, audit logging, budget guards, and undo workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and backup administrators use this skill to inspect and operate Veeam Backup & Replication environments, including health triage, failed-job RCA, backup job control, restore-point lookup, VM restore initiation, repository capacity checks, and async session monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent high-impact write and restore authority without an enforced read-only mode or approval gate.

Mitigation: Install it only with Veeam server-side permissions limited to the intended workflow; use read-only or restricted Veeam roles for diagnostics and do not expose write-capable MCP tools to untrusted prompts or unattended workflows.

Risk: Restore and session-stop operations can have irreversible operational impact.

Mitigation: Use dry-run previews, independently confirm the restore target, and reserve restore or stop privileges for accounts and workflows that explicitly require them.

Risk: Credential handling can become unsafe if legacy plaintext environment storage is used.

Mitigation: Use the encrypted secret store, unlock it with VEEAM_AIOPS_MASTER_PASSWORD only where needed, migrate legacy plaintext secrets, and avoid logging or exposing configured credentials.

Risk: Agent mistakes can re-issue async operations or poll too aggressively.

Mitigation: Start jobs or restores once, follow progress through session tools, and rely on the skill's runaway guard as a backstop rather than as primary authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Project homepage](https://github.com/AIops-tools/Veeam-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured command outputs from Veeam tools; write operations are expected to be audited by the skill.]

## Skill Version(s):

0.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
