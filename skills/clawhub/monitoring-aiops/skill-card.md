## Description:

Monitoring AIops helps agents operate SolarWinds Orion, Paessler PRTG, and Zabbix monitoring environments for NOC overview, alert triage, health checks, read-only SWQL queries, and guarded maintenance or suppression writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, NOC engineers, and infrastructure operators use this skill to inspect monitoring state, triage alert storms, answer common SWQL questions, and carry out audited maintenance actions across SolarWinds Orion, PRTG, and Zabbix. It is intended for legitimate monitoring operations with account-level permissions controlling whether write actions can succeed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable monitoring credentials can allow an agent to suppress alerts, pause monitoring, delete maintenance windows, or remove SolarWinds nodes.

Mitigation: Use read-only SolarWinds, PRTG, or Zabbix accounts by default and grant write-capable credentials only for approved maintenance workflows.

Risk: TLS verification can be disabled for lab or self-signed environments.

Mitigation: Enable verify_ssl for production targets and avoid carrying lab TLS settings into operational monitoring configurations.

Risk: Secrets passed through command-line values or persistent environment variables can be exposed outside the encrypted store.

Mitigation: Prefer the encrypted secret store and interactive secret prompts; avoid command-line --value usage and long-lived secret environment variables.

Risk: Maintenance and suppression actions can hide active problems if they are left in place.

Mitigation: Prefer time-boxed maintenance windows, inspect muted or unmanaged objects after maintenance, and use undo records where available.

Risk: The artifact states mocked platform responses have been exercised but live NOC validation is still needed.

Mitigation: Run monitoring-aiops doctor and validate behavior against non-production or read-only live targets before relying on operational actions.

## Reference(s):

- [Monitoring AIops homepage](https://github.com/AIops-tools/Monitoring-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and monitoring result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call configured SolarWinds, PRTG, or Zabbix APIs through the skill's CLI or MCP tools and may produce audited write or undo actions when permitted by the connected account.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
