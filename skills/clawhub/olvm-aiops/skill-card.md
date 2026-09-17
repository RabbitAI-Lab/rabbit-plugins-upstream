## Description:

OLVM AIops helps agents inspect and troubleshoot Oracle Linux Virtualization Manager and oVirt 4.5 environments through read-only inventory, health, capacity, activity, and ranked diagnosis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect OLVM or oVirt 4.5 engines, triage host, storage, VM, event, job, certificate, backup, and capacity issues, and receive ranked findings with measured signals. The release is read-only and is intended for environments where the connected engine account grants appropriate access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run external package code that handles OLVM/oVirt credentials.

Mitigation: Review or pin the exact olvm-aiops package version before installation, and run it under a minimally privileged local account.

Risk: A broadly scoped engine account could expose more infrastructure data than needed.

Mitigation: Use a dedicated OLVM/oVirt account with a read-only role such as ReadOnlyAdmin.

Risk: Credential exposure is possible if master passwords or legacy plaintext password variables are placed in broad environments.

Mitigation: Keep OLVM_AIOPS_MASTER_PASSWORD narrowly scoped to the MCP or CLI process and avoid legacy plaintext password variables except for one-time migration.

## Reference(s):

- [OLVM AIops project homepage](https://github.com/AIops-tools/OLVM-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/olvm-aiops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and structured MCP-oriented troubleshooting steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer to JSON payload fields returned by the olvm-aiops CLI or MCP server; users should treat truncated scan indicators as partial results.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
