## Description:

Query and act on Evite events, guest lists, RSVPs, messages, invitations, and event settings from a shell using curl with an authenticated cookie jar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Evite event data and prepare authenticated curl commands for RSVP, guest, messaging, invitation, and event-management workflows without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for Evite account credentials and can read private event and guest data.

Mitigation: Install only when account-level Evite access is acceptable, avoid exporting the password, and use a throwaway event or limited account for testing.

Risk: Write operations can mutate real Evite state, including RSVPs, invitations, guest messages, broadcasts, cancellations, and reinstatements.

Mitigation: Require explicit user confirmation before every write and test sends or broadcasts only against throwaway events.

Risk: A reusable cookie jar contains live session cookies.

Mitigation: Use a unique restricted temporary cookie-jar path, keep permissions at 600, and remove the jar when the session is no longer needed.

Risk: The artifact marks two write request bodies, send_message and send_invitation, as assumed rather than fully verified.

Mitigation: Treat those operations as lower confidence and verify behavior on a throwaway event before using them on real guests.

## Reference(s):

- [Evite endpoint reference](artifact/references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash/curl commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided Evite credentials and a restricted cookie jar; write operations can mutate real events.]

## Skill Version(s):

0.8.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
