## Description:

Query and act on Evite events, guest lists, RSVPs, and messages from a shell using curl and a cookie jar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect and manage Evite events from an agent-assisted shell workflow without installing the Evite MCP server. It helps with event reads, guest and RSVP updates, broadcasts, invitations, uploads, and event lifecycle actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent direct access to an Evite account and can perform real writes such as RSVPs, guest changes, broadcast emails, invitations, uploads, cancellations, and reinstatements.

Mitigation: Approve every write only after reviewing the exact event, guest, message, and file details, and test risky actions on a throwaway event first.

Risk: Credentials and live session cookies can expose the user's Evite account if stored in shell history or reused cookie jars.

Mitigation: Use a secrets manager for credentials, keep a unique temporary cookie jar per run, restrict the jar to the current user, and delete it when finished.

Risk: Some write request bodies are documented as assumed rather than fully verified.

Mitigation: Treat assumed-body actions as lower confidence and verify behavior on a non-important event before using them on real invitations or guests.

## Reference(s):

- [Evite endpoint reference](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)
- [Evite](https://www.evite.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated Evite session cookie jar and fresh CSRF token handling for writes.]

## Skill Version(s):

0.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
