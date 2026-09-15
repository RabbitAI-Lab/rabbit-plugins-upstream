## Description:

truenas-aiops helps agents operate TrueNAS SCALE storage appliances through read diagnostics and governed CLI or MCP actions for pools, datasets, snapshots, disks, alerts, services, replication, and cloud sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, storage administrators, and operations engineers use this skill to triage TrueNAS SCALE appliances, inspect ZFS storage state, and run governed maintenance tasks through CLI or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make real storage changes, including irreversible snapshot deletion, and does not provide its own approval gate.

Mitigation: Review before production use, prefer a least-privilege or read-only TrueNAS API key unless writes are intended, and use dry-run plus CLI confirmation for destructive work.

Risk: API keys or master passwords may be exposed if passed through broad environments or command-line values.

Mitigation: Use the encrypted secret store and hidden prompts where possible, avoid passing API keys with --value, and scope TRUENAS_AIOPS_MASTER_PASSWORD to the narrowest execution environment.

Risk: Disabling TLS verification weakens connection assurance when reaching the TrueNAS API endpoint.

Mitigation: Keep verify_ssl enabled for production appliances and disable it only for self-signed lab certificates.

Risk: A mis-scoped account can allow agent-driven writes beyond the operator's intended session posture.

Mitigation: Enforce read-only or limited privileges at the TrueNAS account/API-key level, and instruct the agent not to call write tools during observe-only sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/truenas-aiops)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/AIops-tools/TrueNAS-AIops)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline CLI commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include TrueNAS CLI or MCP workflow guidance; live results depend on the configured appliance and account permissions.]

## Skill Version(s):

0.11.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
