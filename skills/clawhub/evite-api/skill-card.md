## Description:

Helps agents read and manage Evite events, guests, RSVPs, and messages using shell commands instead of an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite account holders and developers use this skill to inspect events and guest lists, manage RSVPs, and perform event and messaging actions from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-initiated writes can send invitations or broadcasts and change or cancel real events without an enforced confirmation step.

Mitigation: Require the account holder to approve each write before execution; test sends and broadcasts only on a throwaway event.

Risk: Evite credentials and live session cookies can be exposed through shell history or an accessible cookie jar.

Mitigation: Use a secret manager rather than typing passwords into shell history; restrict access to the cookie jar and delete or protect it after use.

Risk: The request bodies for sending a message or invitation are not fully verified and may behave unexpectedly.

Mitigation: Confirm the intended recipients and content before sending, and test uncertain send operations on a throwaway event first.

## Reference(s):

- [Evite endpoint reference](artifact/references/endpoints.md)
- [evite-api ClawHub release](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.3.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
