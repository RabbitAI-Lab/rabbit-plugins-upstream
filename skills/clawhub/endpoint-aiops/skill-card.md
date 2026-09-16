## Description:

Endpoint AIops helps agents triage managed-endpoint fleets by summarizing health, inventory, login sessions, drift, patch posture, and audited remediation actions such as profile assignment and reboot.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and endpoint operations teams use this skill to inspect managed-endpoint fleet health, diagnose login storms, rank risky endpoints, review patch or configuration drift, and run controlled remediation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release may run an unpinned external executable.

Mitigation: Pin or otherwise verify the endpoint-aiops package before installation or execution.

Risk: Write-capable tools can assign profiles or reboot endpoints without an enforceable skill-side approval gate.

Mitigation: Start with a read-only endpoint-management account and expose write-capable tools only behind an external approval process.

Risk: The master password unlocks the encrypted credential store for non-interactive use.

Mitigation: Protect ENDPOINT_AIOPS_MASTER_PASSWORD as a secret and limit where it is exported.

## Reference(s):

- [Endpoint AIops on ClawHub](https://clawhub.ai/zw008/skills/endpoint-aiops)
- [Source repository](https://github.com/AIops-tools/Endpoint-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include capped list summaries, risk-tier notes, audit or undo guidance, and dry-run command suggestions.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
