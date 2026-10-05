## Description:

Guides agents in using shell commands to read Evite events, guest lists, RSVPs, and messages and to make changes through an authenticated Evite session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Evite account holders can use this skill to check events and guest responses or manage invitations and event communications from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and live session cookies can grant access to the Evite account.

Mitigation: Restrict access to credentials and the cookie jar, and delete the jar after use.

Risk: Write commands can change real events or email real guests without a built-in confirmation step.

Mitigation: Confirm each write command and its destination before execution; test sends on throwaway events.

Risk: Photo upload commands can read local files and send them to an unintended destination.

Mitigation: Limit allowed upload paths and verify the destination before uploading.

## Reference(s):

- [Evite API skill on ClawHub](https://clawhub.ai/chrischall/skills/evite-api)
- [Evite endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands interact with a live Evite account; write operations can change events or contact guests.]

## Skill Version(s):

1.3.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
