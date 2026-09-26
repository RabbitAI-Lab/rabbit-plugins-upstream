## Description:

Guides agents in reading and managing Evite events, guest lists, RSVPs, and messages through authenticated shell requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Event hosts and invited guests can use this skill to inspect Evite events and guest responses, manage invitations and RSVPs, and communicate with guests from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access exposes guest details and a live Evite session.

Mitigation: Keep credentials and the cookie jar private, grant access only when needed, and delete the jar afterward.

Risk: Writes can change RSVPs or events, cancel events, and send messages or invitations to real guests.

Mitigation: Verify event and guest IDs before writes, preview outgoing messages, and test sends on a throwaway event.

Risk: Some message and invitation request bodies are unverified.

Mitigation: Test those actions on a throwaway event before relying on them for real guests.

## Reference(s):

- [Evite API skill release](https://clawhub.ai/chrischall/skills/evite-api)
- [Evite endpoint reference](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Markdown with shell examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return event and guest information; write commands can change events or contact guests.]

## Skill Version(s):

1.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
