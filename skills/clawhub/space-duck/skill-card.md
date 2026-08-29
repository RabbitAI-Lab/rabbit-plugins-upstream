## Description:

Space Duck connects an agent to the Space Duck identity network so it can pair with a Beak Key, report status, manage trusted connections, exchange pecks, run listeners, and use optional Telegram or BYOB workspace bridge integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Space Duck to pair an agent with the Space Duck network, manage identity and trust state, exchange approved peer messages, inspect permissions, and operate optional local listeners or workspace bridge integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local listeners and service units may keep running after setup.

Mitigation: Enable listeners only when needed, prefer supervised teardown paths, and review running services during installation and updates.

Risk: The skill stores a Beak Key and optional messaging credentials under ~/.space-duck.

Mitigation: Protect ~/.space-duck permissions, avoid pasting secrets in chat or logs, and use the browser pairing flow when possible.

Risk: Workspace bridge and external forwarders can share local Markdown or messages with the platform or configured providers.

Mitigation: Do not enable the workspace bridge, Telegram forwarding, or MCP clients unless that data sharing is acceptable for the workspace.

Risk: Owner-approved shell commands and auto-update settings can change local system state.

Mitigation: Use strict consent for control actions and keep auto_update set to ask unless unattended updates are explicitly trusted.

## Reference(s):

- [Space Duck Skill Page](https://clawhub.ai/askegor/skills/space-duck)
- [Connection Ceremony](references/CONNECTION-CEREMONY.md)
- [Space Duck API Reference](references/api.md)
- [Capability Grants](references/grants.md)
- [Space Duck MCP Client Spec](references/MCP-CLIENT-SPEC.md)
- [Security Manifest](SECURITY-MANIFEST.md)
- [BYOB Workspace Bridge Reference Runtime](scripts/WORKSPACE_BRIDGE_README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit commands that call local scripts, update local Space Duck configuration, start listeners, or send authenticated requests when the operator asks for those actions.]

## Skill Version(s):

0.8.9 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
