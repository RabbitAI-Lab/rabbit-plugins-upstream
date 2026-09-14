## Description:

Veeam AIops helps agents operate Veeam Backup & Replication for health checks, diagnostics, backup job operations, repository and backup inventory, session monitoring, and VM restore workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and backup administrators use this skill to let an agent inspect Veeam Backup & Replication state, triage failed backup sessions, manage backup jobs, review repository capacity, and guide restore workflows. It is intended for explicitly Veeam/VBR contexts and not for other backup products, hypervisors, Kubernetes, or cloud lifecycle management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact Veeam write and restore actions without an enforced MCP approval or read-only boundary.

Mitigation: Use a dedicated read-only or tightly restricted Veeam account by default, and allow write tools only through a separate operational approval process.

Risk: Production use with verify_ssl:false could weaken TLS protection for Veeam API access.

Mitigation: Keep SSL verification enabled in production and reserve verify_ssl:false only for explicitly controlled self-signed lab environments.

Risk: A legacy plaintext password fallback may expose credentials if retained.

Mitigation: Migrate credentials into the encrypted store and remove plaintext .env or environment fallback usage.

Risk: Installing an unpinned or unaudited package version can make release contents harder to verify.

Mitigation: Prefer a pinned, audited package version or a verified source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Project homepage](https://github.com/AIops-tools/Veeam-AIops)
- [Capabilities](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, configuration examples, and MCP tool-use instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide agents through structured Veeam diagnostics and operations; some underlying MCP and CLI results can include JSON-like status, pagination, truncation, audit, dry-run, or undo metadata.]

## Skill Version(s):

0.16.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
