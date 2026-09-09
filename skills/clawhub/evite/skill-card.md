## Description:

This skill helps an agent work with Evite events and invitations, including listing events, viewing guest lists and RSVP tallies, responding to invitations, messaging guests, and creating or editing hosted events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Evite invitations and hosted events through an MCP server, including event lookup, guest-list review, RSVP updates, guest messaging, and event authoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording is paired with access to private Evite event and guest-list data.

Mitigation: Invoke the skill only when the user is explicit about Evite intent, and keep credentials and session cookies in secret storage where possible.

Risk: The skill can change RSVPs, send messages, and create, update, send, cancel, or reinstate events.

Mitigation: Review the dry-run preview and require confirm: true only after the user approves the exact write action.

Risk: Browser-cookie bootstrap or session caching may not fit every credential-handling policy.

Mitigation: Disable browser-cookie bootstrap with EVITE_DISABLE_FETCHPROXY=1 or avoid session caching when that better matches the deployment threat model.

## Reference(s):

- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [Text, API Calls, Configuration, Guidance]

**Output Format:** [Text and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write tools require confirm: true; otherwise they return a dry-run preview without making the network call.]

## Skill Version(s):

0.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
