## Description:

Helps users review Evite invitations and events, manage guest lists and RSVPs, and create or update invitations with confirmation before changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite account holders use this skill to check invitations, RSVPs, messages, and guest lists, or to organize events and communicate with guests after approving changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials or browser-session cookies can grant access to private Evite events and guest lists.

Mitigation: Provide credentials or a session cookie deliberately, review the package before installation, and disable browser-session bootstrap if cookie reuse is unwanted.

Risk: Sending messages, changing guests, creating invitations, or canceling events can affect other people.

Mitigation: Review the proposed action and require explicit user approval before any write is submitted.

## Reference(s):

- [Evite skill listing](https://clawhub.ai/chrischall/skills/evite)
- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with event summaries, confirmation previews, and optional setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event changes require user confirmation before submission.]

## Skill Version(s):

1.3.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
