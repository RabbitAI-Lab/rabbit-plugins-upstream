## Description:

Helps users manage Evite invitations and hosted events, including guest lists, RSVPs, messages, and event creation or updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Evite users and event hosts use this skill to check invitations and guest responses, RSVP, message guests, and create or manage events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to Evite credentials, browser sessions, and private event data.

Mitigation: Use scoped credentials where possible and install only if this access is acceptable; set EVITE_DISABLE_FETCHPROXY=1 to disable signed-in browser-session bootstrap.

Risk: Event, guest, RSVP, or message changes may affect other people.

Mitigation: Review the proposed action or preview and explicitly approve it before confirming any write.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp npm package (linked in skill)](https://www.npmjs.com/package/evite-mcp)
- [evite-mcp project repository (linked in skill)](https://github.com/chrischall/evite-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown with event information, setup examples, and write-action previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require user confirmation before they are sent.]

## Skill Version(s):

1.3.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
