## Description:

evite-api helps agents query Evite events, guest lists, RSVPs, messages, and related event actions from a shell using curl and an authenticated cookie jar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to script Evite account workflows without an MCP server or browser, including reading event data and issuing authenticated event, guest, RSVP, messaging, photo, and lifecycle calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent direct authenticated Evite account access through shell commands.

Mitigation: Use a dedicated or temporary session where possible, protect the cookie jar with restrictive permissions, and delete it after use.

Risk: Evite guest lists and event payloads can include personal information such as names, emails, phone numbers, RSVP status, and messages.

Mitigation: Avoid printing, logging, or sharing full guest payloads unless the user explicitly needs that data.

Risk: Write operations can modify real Evite state, email guests, upload photos, send invitations, or cancel events.

Mitigation: Require explicit user confirmation before writes and test broadcast or send flows only against throwaway events.

Risk: Two documented write bodies are marked as assumed rather than fully verified.

Mitigation: Review `send_message` and `send_invitation` requests before relying on them for important workflows.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated Evite session cookies and CSRF tokens; some commands can mutate live Evite data.]

## Skill Version(s):

0.6.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
