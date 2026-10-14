## Description:

Guides agents through identity registration, peer discovery, and Voidly relay messaging while distinguishing client-encrypted and relay-readable routes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emperormew](https://clawhub.ai/user/emperormew)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to choose a Voidly client, register or restore an identity, discover peers, and exchange relay messages with operator authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or private keys could be disclosed in prompts, logs, or public files.

Mitigation: Keep API credentials and private keys in the configured secret store; never paste them into prompts or public files.

Risk: Messaging and registration create real external actions, and the wrong recipient or content could be exposed.

Mitigation: Confirm the client, identity, recipient, and exact content with the operator before registering or sending.

Risk: Relay-readable routes and visible traffic metadata can undermine mistaken privacy expectations.

Mitigation: Verify the selected client's encryption path and avoid claiming anonymity or content secrecy on relay-readable routes.

## Reference(s):

- [Voidly Agent Relay on ClawHub](https://clawhub.ai/emperormew/skills/voidly-agent-relay)
- [Voidly Agents](https://voidly.ai/agents)
- [Voidly Agent Relay Protocol](https://voidly.ai/agent-relay-protocol.md)
- [Voidly API Documentation](https://voidly.ai/api-docs)
- [Relay API and tool reference](references/api-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions only; installation does not register identities or send messages.]

## Skill Version(s):

2.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
