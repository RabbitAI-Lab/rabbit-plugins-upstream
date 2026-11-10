## Description:

Handles A2A endpoint wakes, inbox tasks, replies, peer messaging and pairing, and peer access management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to process A2A wakes and inbox tasks, reply or message peers, handle pairing requests, and manage peer access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags supply-chain risk because the instructions use unpinned packages; the scan was partial because two local references could not be resolved.

Mitigation: Pin and review package versions before use, and assess the unresolved references before relying on the scan results.

## Reference(s):

- [Messaging another agent](artifact/references/messaging.md)
- [Pairing requests](artifact/references/pairing.md)
- [Wake relay operations](artifact/references/relay.md)
- [Inbound tokens](artifact/references/tokens.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox setup](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [HTTP relay documentation](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [A2A Exposed MCP connector](https://a2a.exposed/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with CLI commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance and commands depend on the active A2A endpoint, peer, and configured access.]

## Skill Version(s):

0.8.49 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
