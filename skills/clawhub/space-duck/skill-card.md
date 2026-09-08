## Description:

Space Duck connects an agent to the Space Duck identity network so it can pair with a Beak Key, report status, manage trusted connections, exchange pecks, run approved listeners, and use optional Telegram or MCP bridge workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[askegor](https://clawhub.ai/user/askegor)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to attach a local agent to a Space Duck identity, manage connection permissions, send and receive pecks, and operate optional listener, Telegram, BYOB, and MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates a persistent Space Duck agent identity and uses a Beak Key account secret.

Mitigation: Install only for agents that should join the Space Duck network, protect the Beak Key as an account credential, and avoid sharing local configuration files.

Risk: Optional bridges, MCP connectors, custom API hosts, external forwarders, auto-update mode, and 24-hour approval memory can expand what the agent can access or execute.

Mitigation: Review each optional feature before enabling it, keep consent defaults unless intentional, and use strict-consent when every owner-approved action should require a fresh approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/askegor/skills/space-duck)
- [Connection Ceremony - Canonical Pond Flow](references/CONNECTION-CEREMONY.md)
- [Space Duck MCP Client - Spec](references/MCP-CLIENT-SPEC.md)
- [Space Duck API Reference](references/api.md)
- [Capability Grants - agent-side guide](references/grants.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and command-line guidance with JSON or text output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local Space Duck configuration, inbox, listener, and bridge state under the operator's home directory when the operator runs the provided scripts.]

## Skill Version(s):

0.8.21 (source: server release evidence and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
