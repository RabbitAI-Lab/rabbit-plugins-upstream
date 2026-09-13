## Description:

Nutanix AIops helps an agent operate a Nutanix Prism Central v4 estate across cluster health, inventory, VM lifecycle, storage, networking, data protection, alerts, LCM, capacity forecasting, and diagnostics with governed MCP and CLI workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and operations teams use this skill to inspect and administer Nutanix Prism Central v4 environments, including health triage, VM lifecycle tasks, DR actions, LCM workflows, and capacity planning. It is intended for Nutanix Prism Central targets only and not for non-Nutanix infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive Nutanix infrastructure changes.

Mitigation: Use least-privileged or Viewer accounts first, require operator review for writes, and run destructive actions through dry-run before execution.

Risk: The skill persists local credentials and can unlock them from an environment-variable master password.

Mitigation: Protect the local credential store and master password, avoid plaintext legacy password variables, and rotate or migrate secrets when needed.

Risk: The release installs a mutable external executable package.

Mitigation: Prefer a pinned or otherwise verified package release before using the skill with production Prism Central credentials.

## Reference(s):

- [Nutanix AIops Homepage](https://github.com/AIops-tools/Nutanix-AIops)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and structured tool outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Prism Central identifiers, task references, diagnostics summaries, dry-run previews, and configuration steps.]

## Skill Version(s):

0.11.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
