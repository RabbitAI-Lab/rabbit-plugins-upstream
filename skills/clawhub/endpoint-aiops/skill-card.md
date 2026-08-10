## Description:

endpoint-aiops helps agents operate managed-endpoint fleets by summarizing fleet health, inventory, login and boot sessions, login-storm patterns, patch/configuration drift, health scores, and guarded remediation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

IT operations engineers and endpoint administrators use this skill to triage managed endpoint fleets, rank unhealthy devices, investigate login storms, inspect patch or configuration drift, and perform scoped remediation such as profile assignment or reboot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes endpoint reboot and profile-change actions without a built-in read-only or approval gate for agent/MCP use.

Mitigation: Install it with least-privileged, preferably read-only endpoint-management credentials unless external approval and RBAC controls are in place; expose write tools only when reboots and profile changes are separately approved and scoped.

Risk: Endpoint-management credentials and the master password used to unlock the encrypted store are sensitive operational secrets.

Mitigation: Protect ~/.endpoint-aiops/secrets.enc and ENDPOINT_AIOPS_MASTER_PASSWORD, avoid exposing them in shared agent environments, and prefer scoped service accounts.

Risk: The artifact states that REST paths are modeled generically and have not yet been exercised against a live management server.

Mitigation: Validate connectivity and behavior with endpoint-aiops doctor and a staged or low-privilege target before relying on live fleet actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/endpoint-aiops)
- [Project homepage](https://github.com/AIops-tools/Endpoint-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Several list-producing tools report returned, limit, and truncated fields so agents can detect capped results.]

## Skill Version(s):

0.9.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
