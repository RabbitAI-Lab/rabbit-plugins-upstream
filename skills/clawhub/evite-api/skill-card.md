## Description:

Query and act on Evite events, guest lists, RSVPs, messages, templates, photos, and event lifecycle operations from a shell using authenticated curl commands and a cookie jar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-oriented users use this skill to inspect Evite event data and prepare authenticated curl commands for event, guest, RSVP, message, photo, and lifecycle operations without running the evite-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare commands that send guest emails, change RSVPs, edit guest lists, create or update events, send invitations, cancel events, or reinstate events against a live Evite account.

Mitigation: Require explicit user confirmation before executing any write operation and test sends or broadcasts only against throwaway or low-risk events.

Risk: Authenticated cookie jars and Evite credentials grant live account authority if exposed.

Mitigation: Store the cookie jar with restrictive permissions, keep EVITE_PASSWORD out of logs and shell history, and remove the jar after use.

Risk: Some write request bodies are documented as assumed rather than fully verified.

Mitigation: Treat assumed write bodies as lower-confidence operations and validate against a non-production event before using them on real invitations.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may perform live authenticated Evite reads and writes when executed with user credentials and a session cookie jar.]

## Skill Version(s):

0.7.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
