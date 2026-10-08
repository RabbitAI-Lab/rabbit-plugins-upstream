## Description:

Guides agents in reading and updating Evite events, guest lists, RSVPs, and messages through authenticated shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite users and developers use this skill to inspect events and guest responses or perform authorized event updates from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can send invitations or broadcasts and change RSVPs, guests, photos, or event status without a built-in confirmation step.

Mitigation: Review exact event and guest IDs, recipient counts, and message bodies; require explicit human approval before sends, deletions, uploads, RSVP changes, or cancellations.

Risk: A saved cookie jar grants live Evite account access, and shell credentials may be exposed.

Mitigation: Keep credentials out of shell history; protect and delete the cookie jar after use, and test with a throwaway event.

## Reference(s):

- [Evite API endpoint reference](artifact/references/endpoints.md)
- [evite-api ClawHub release](https://clawhub.ai/chrischall/skills/evite-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return Evite data or change live account and event records when executed.]

## Skill Version(s):

1.3.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
