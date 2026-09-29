## Description:

Guides agents in reading and updating Evite events, guest lists, RSVPs, photos, and messages using shell commands and an authenticated session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Evite account holders use this skill to check events and guests or perform RSVP, event-management, messaging, and photo tasks without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Evite credentials and a live session cookie.

Mitigation: Start with a low-risk account, restrict access to the cookie jar, and delete it after use.

Risk: Commands can change events, guest lists, and RSVPs or send emails without a built-in confirmation gate.

Mitigation: Confirm each write explicitly and test sends, broadcasts, and cancellations on a throwaway event first.

Risk: Photo uploads share files with Google Cloud Storage through Evite's upload flow.

Mitigation: Review photos before upload and share only files intended for the event gallery.

## Reference(s):

- [Evite endpoint reference](artifact/references/endpoints.md)
- [ClawHub evite-api release](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can read or change live Evite account data.]

## Skill Version(s):

1.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
