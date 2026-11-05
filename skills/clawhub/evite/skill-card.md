## Description:

This skill should be used when the user asks about Evite events or invitations. Triggers on phrases like "check Evite", "my Evite events", "who RSVP'd", "Evite guest list", "RSVP to the party", "message my Evite guests", "create an Evite invite", or any request involving event invitations, guest lists, RSVPs, or party/event hosting on evite.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to review Evite invitations, events, guest lists, RSVP summaries, and messages, and to manage invitations or events with confirmation before changes are sent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party server can access private Evite information and act on the user's account; credentials or session cookies could expose that access.

Mitigation: Protect configuration containing passwords or cookies, retain user confirmations, and check recipients and event details before approving changes.

Risk: Browser-based session bootstrap can use cookies from a signed-in Evite tab, and the downloaded server code was not included in this artifact review.

Mitigation: Set EVITE_DISABLE_FETCHPROXY=1 to disable browser bootstrap and consider pinning a reviewed package version.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp on npm](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Brief text and structured event, guest, RSVP, and message details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event changes require user confirmation; review recipients and event details before approval.]

## Skill Version(s):

1.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
