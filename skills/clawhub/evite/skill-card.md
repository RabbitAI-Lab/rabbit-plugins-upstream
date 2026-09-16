## Description:

Helps an agent work with Evite invitations and hosted events, including event lookup, guest lists, RSVP summaries, messaging, and confirm-gated event changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read Evite invitations and hosted event details, summarize guests and RSVPs, draft or send guest messages, and create or update events through confirm-gated tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may use an unpinned npm server and sensitive Evite passwords or browser session cookies.

Mitigation: Prefer a pinned, reviewed package version; avoid project-local plaintext passwords; and disable Fetchproxy unless it is explicitly needed.

Risk: Confirmed write tools can change invitations, guests, messages, RSVPs, and event state.

Mitigation: Review dry-run previews before setting confirm: true and only confirm actions the user explicitly intends.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite)
- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON configuration and shell command snippets for MCP setup and Evite tool usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write tools require confirm: true; without confirmation they return dry-run previews.]

## Skill Version(s):

0.8.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
