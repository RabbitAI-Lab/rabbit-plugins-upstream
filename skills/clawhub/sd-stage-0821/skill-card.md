## Description:

Connects an agent to the Space Duck identity network for pairing, status checks, peck messaging, peer chat, connection management, Telegram integration, and optional listeners.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to pair an agent with the Space Duck network, manage identity and peck connections, exchange messages with peers, and optionally run local listeners or bridges for Telegram, MCP, and workspace workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional listeners can make the machine act as a persistent Space Duck agent.

Mitigation: Install only when persistent agent behavior is intended, and review listener setup before enabling supervised services.

Risk: Optional bridge and MCP workflows can expose selected workspace files or connector behavior.

Mitigation: Review the exact workspace directory and configured MCP endpoints before enabling the BYOB bridge or MCP connectors.

Risk: Owner-approved actions can execute signed commands when the operator enables that path.

Mitigation: Prefer strict consent for owner-approved actions and leave auto-update on ask unless automatic updates are intended.

Risk: The Beak Key is the primary local credential for Space Duck API access.

Mitigation: Keep the Space Duck config file private, avoid pasting keys in chat, and use the documented browser pairing flow when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/askegor/skills/sd-stage-0821)
- [Space Duck API Reference](references/api.md)
- [Connection Ceremony - Canonical Pond Flow](references/CONNECTION-CEREMONY.md)
- [Capability Grants - Agent-Side Guide](references/grants.md)
- [Space Duck MCP Client Spec](references/MCP-CLIENT-SPEC.md)
- [Space Duck Scripts](scripts/README.md)
- [BYOB Workspace Bridge Reference Runtime](scripts/WORKSPACE_BRIDGE_README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or text output from helper scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local Space Duck configuration, listener state, inbox files, service files, and bridge-related files when the operator chooses those workflows.]

## Skill Version(s):

0.8.21 (source: ClawHub release evidence, artifact _meta.json, and changelog released 2026-09-02)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
