## Description:

PingRoom lets an OpenClaw agent use the pingroom CLI to notify people, send files and links, ask blocking questions, request approvals, update live progress cards, and stream incoming pings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pingroom](https://clawhub.ai/user/pingroom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use PingRoom to route agent work that needs a human notification, answer, or approval through phone-based PingRoom rooms and direct handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send selected messages, files, links, locations, and approval requests through PingRoom.

Mitigation: Use least-privilege rooms or tokens, and avoid sending secrets or sensitive internal material unless explicitly intended.

Risk: A connected-agent credential can remain usable after local logout or reconfiguration.

Mitigation: Revoke the PingRoom connected-agent credential server-side when it is no longer needed.

Risk: Human approval and question flows can expire, be denied, or remain open after an agent run ends.

Mitigation: Treat timeout and denial exit codes distinctly, cancel stale questions, and keep gates alive only when follow-up action is expected.

## Reference(s):

- [PingRoom OpenClaw command reference](https://pingroom.io/connect-openclaw.md)
- [PingRoom ClawHub skill page](https://clawhub.ai/pingroom/skills/pingroom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce blocking CLI calls whose exit codes reflect human answers, approvals, denials, expiry, or errors.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
