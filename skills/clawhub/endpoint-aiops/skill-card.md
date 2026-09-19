## Description:

Endpoint AIops helps agents operate managed-endpoint fleets by producing fleet health summaries, inventory views, login and boot session analysis, drift and patch reports, endpoint health rankings, and guarded remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, endpoint administrators, and operations engineers use this skill to inspect managed-endpoint fleet health, diagnose login storms or drift, rank endpoints by risk, and prepare controlled endpoint remediation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can reboot or reconfigure managed endpoints without a tool-enforced approval gate.

Mitigation: Use read-only or tightly scoped management credentials by default, require operator review before write tools, and prefer dry-run previews before any endpoint change.

Risk: The skill relies on sensitive endpoint-management credentials and may run in non-interactive MCP or CI contexts.

Mitigation: Keep HTTPS certificate verification enabled, avoid exporting the master password unless needed, and protect the encrypted credential store and local state directory.

Risk: The security review notes an unpinned external package and recommends review before installation.

Mitigation: Review the endpoint-aiops package source and exact version that will run before installing or enabling the skill.

Risk: The artifact says live endpoint-management server testing has not yet been completed.

Mitigation: Validate connectivity and representative read/write workflows in a controlled environment before using the skill against production fleets.

## Reference(s):

- [endpoint-aiops capabilities](references/capabilities.md)
- [endpoint-aiops CLI reference](references/cli-reference.md)
- [endpoint-aiops setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Project homepage](https://github.com/AIops-tools/Endpoint-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/endpoint-aiops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include capped fleet lists, endpoint risk summaries, audit and undo guidance, and dry-run remediation steps.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
