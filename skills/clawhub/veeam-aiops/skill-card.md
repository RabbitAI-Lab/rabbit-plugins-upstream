## Description:

Operates Veeam Backup & Replication environments through CLI and MCP tools for health checks, diagnostics, backup job control, restores, repository and backup inventory, and session monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Backup administrators, SREs, and IT operators use this skill to inspect Veeam Backup & Replication health, triage failed sessions and repository capacity, manage backup jobs, and start or monitor restores through audited CLI or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents can invoke high-impact Veeam write and restore operations, and the skill does not provide a tool-enforced read-only mode or approval gate.

Mitigation: Use a dedicated least-privilege Veeam account, prefer read-only roles for diagnostics, and restrict write-tool use in the supervising agent policy.

Risk: Restore and session-stop actions can be irreversible or lack an undo token.

Mitigation: Require operators to review dry-run previews, confirm the target object outside the model response, and rely on Veeam-side permissions for final authorization.

Risk: Credential exposure is possible if plaintext environment variables or hardcoded master passwords are used in automation.

Mitigation: Use the encrypted secret store, avoid plaintext .env credentials and hardcoded MCP config secrets, and rotate credentials when onboarding or changing operators.

Risk: TLS verification can be disabled for self-signed lab certificates, which can weaken production connections.

Mitigation: Keep TLS verification enabled outside lab environments and validate Veeam server connectivity with the doctor command before operational use.

Risk: Unpinned or unverified package resolution can introduce supply-chain uncertainty for production use.

Mitigation: Pin and verify the package version before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/veeam-aiops)
- [Project homepage](https://github.com/AIops-tools/Veeam-AIops)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI examples, operational guidance, and structured MCP/tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include audited Veeam operation results, dry-run previews, truncation indicators, and risk-tier context.]

## Skill Version(s):

0.15.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
