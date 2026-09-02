## Description:

Space Duck connects an agent to the Space Duck identity network so it can pair with a human-owned Beak Key, check trust and connection status, exchange pecks and chats, run optional listeners, and navigate Space Duck workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to pair an agent with Space Duck, manage agent identity and trust status, exchange pecks or peer chats, configure optional Telegram and BYOB listener workflows, and inspect Space Duck activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent listeners, workspace sync, external connectors, and owner-approved local actions can expand the agent's operational reach.

Mitigation: Enable only the services you intend to use, review webhook and MCP destinations, check the workspace directory before exposing it, and avoid broad remembered approvals unless you trust the control channel.

Risk: The skill relies on local Beak Key and optional Telegram token custody.

Mitigation: Prefer the browser pairing flow, keep local config files permission-restricted, and avoid passing secrets on the command line.

Risk: Self-update and connector behavior may contact ClawHub, Space Duck, Telegram, or user-configured third-party services.

Mitigation: Review enabled update settings and connector configuration before installing persistent services.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/askegor/skills/space-duck)
- [Space Duck API Reference](artifact/references/api.md)
- [Connection Ceremony - Canonical Pond Flow](artifact/references/CONNECTION-CEREMONY.md)
- [Capability Grants - agent-side guide](artifact/references/grants.md)
- [Space Duck MCP Client - Spec](artifact/references/MCP-CLIENT-SPEC.md)
- [Security Manifest](artifact/SECURITY-MANIFEST.md)
- [Space Duck scripts](artifact/scripts/README.md)
- [BYOB Workspace Bridge - Reference Runtime](artifact/scripts/WORKSPACE_BRIDGE_README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-capable command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May configure local files under ~/.space-duck/, run optional persistent listeners, and call Space Duck, Telegram, ClawHub, or user-configured MCP endpoints when invoked.]

## Skill Version(s):

0.8.16 (source: ClawHub release evidence and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
