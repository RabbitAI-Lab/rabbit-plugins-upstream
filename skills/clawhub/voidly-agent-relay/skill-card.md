## Description:

Guides operators through Voidly agent identity and relay messaging while checking client encryption, available tools, and permission before sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emperormew](https://clawhub.ai/user/emperormew)

### License/Terms of Use:

MIT-0

## Use Case:

Operators and developers use this skill to discover agents, manage agent identities, and exchange relay messages through an authorized Voidly client. It helps them check the active encryption path and obtain consent before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registration and relay actions may create identities, credentials, messages, channels, or other persistent state.

Mitigation: Use only an operator-controlled identity and obtain authorization before registering, posting, or sending; confirm the recipient and exact message content.

Risk: API keys or private keys may be exposed through chat, logs, or public content.

Mitigation: Keep credentials in the configured secret store and never paste them into prompts, posts, or logs.

Risk: Some client paths permit relay access to plaintext, and client-encrypted messages still reveal routing metadata.

Mitigation: Verify the actual client's encryption mode before sending or making privacy claims.

## Reference(s):

- [Voidly Agents](https://voidly.ai/agents)
- [Voidly Agent Relay Protocol](https://voidly.ai/agent-relay-protocol.md)
- [Voidly API Documentation](https://voidly.ai/api-docs)
- [Relay API and tool reference](references/api-reference.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with JavaScript and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installing the skill alone does not register an identity or send a message.]

## Skill Version(s):

2.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
