## Description:

OLVM AIops helps agents inspect and troubleshoot Oracle Linux Virtualization Manager and oVirt 4.5 engines with read-only inventory, health, capacity, activity, and ranked diagnosis tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, administrators, and operations engineers use this skill to inspect OLVM or oVirt 4.5 environments, diagnose host, storage, VM, event, job, certificate, backup, and capacity issues, and prepare human-reviewed remediation guidance without performing engine writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an external `olvm-aiops` package that handles virtualization credentials.

Mitigation: Install only from a trusted package source, or pin and verify an exact reviewed release before use.

Risk: Credential handling includes legacy plaintext password fallbacks and local secret storage.

Mitigation: Use a dedicated read-only OLVM account, prefer the encrypted secret store, avoid legacy plaintext environment variables, and keep `~/.olvm-aiops` permissions tight.

Risk: Disabling TLS verification can expose engine credentials outside a controlled environment.

Mitigation: Keep TLS verification enabled with the engine CA and use `verify_ssl: false` only in an isolated lab.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/olvm-aiops)
- [Project homepage](https://github.com/AIops-tools/OLVM-AIops)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [uv documentation](https://docs.astral.sh/uv/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-capable OLVM tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only operational guidance; findings should be reported in rank order with measured signals and truncation noted when present.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
