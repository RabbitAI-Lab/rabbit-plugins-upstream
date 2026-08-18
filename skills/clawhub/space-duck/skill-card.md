## Description:

Space Duck connects an agent to the Space Duck identity network for identity pairing, trust and status checks, peck connections, peer messaging, listener operation, Telegram forwarding, workspace bridging, and navigation to Space Duck pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to pair an agent with the Space Duck network, manage identity and connection workflows, send or receive pecks, run optional listeners, and inspect status or activity. It is intended for operators who accept local credential custody and review network, listener, workspace-sync, and command-approval behavior before enabling optional features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent listeners, workspace-sync, persistence, and shell-control features can expand local authority beyond simple command guidance.

Mitigation: Review the security summary before install, enable only the listener and bridge features needed, and prefer poll mode over unauthenticated public push listener operation.

Risk: The skill may access Space Duck credentials, optional OpenClaw workspace markdown, Telegram forwarding, and owner-approved local command execution.

Mitigation: Use it only on trusted machines, keep local credential files protected, avoid BYOB bridge setup with long-lived browser JWTs on shared machines, and review each optional integration before enabling it.

Risk: Auto-update, MCP integrations, and 24-hour approval-remember settings may change the skill's operational behavior after initial setup.

Mitigation: Review these settings during setup and leave them disabled or approval-based unless the operator intentionally accepts the ongoing behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/askegor/skills/space-duck)
- [Connection Ceremony](references/CONNECTION-CEREMONY.md)
- [Space Duck MCP Client Spec](references/MCP-CLIENT-SPEC.md)
- [Space Duck API Reference](references/api.md)
- [Capability Grants](references/grants.md)
- [Scripts Reference](scripts/README.md)
- [BYOB Workspace Bridge Reference Runtime](scripts/WORKSPACE_BRIDGE_README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain text with inline shell commands, configuration paths, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to run local scripts that call Space Duck, Telegram, ClawHub, or user-configured MCP endpoints.]

## Skill Version(s):

0.8.6 (source: server release evidence, artifact _meta.json, and changelog released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
