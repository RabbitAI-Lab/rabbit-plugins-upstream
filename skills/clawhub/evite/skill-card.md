## Description:

This skill helps an agent work with Evite events and invitations, including event lookup, guest lists, RSVP management, guest messaging, and hosted event creation or updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can connect an agent to their Evite account to review invitations, manage guest lists and RSVPs, message guests, and draft or execute host actions such as creating, updating, sending, or canceling events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to Evite account data, including events, guest lists, RSVPs, and messages.

Mitigation: Install it only for accounts where that access is acceptable, and limit use to trusted agent sessions.

Risk: Write actions can send invitations or messages, edit guest lists, cancel events, or otherwise change real Evite account state.

Mitigation: Review the dry-run preview and require explicit confirmation before approving write actions.

## Reference(s):

- [ClawHub evite skill page](https://clawhub.ai/chrischall/skills/evite)
- [Evite](https://www.evite.com)
- [evite-mcp npm package](https://www.npmjs.com/package/evite-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls, Text]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions are confirmation-gated and should be reviewed with the dry-run preview before execution.]

## Skill Version(s):

0.7.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
