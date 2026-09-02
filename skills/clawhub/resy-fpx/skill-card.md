## Description:

Enables an agent to search Resy venues, check availability, book or cancel reservations, and manage favorites or Priority Notify using Resy API calls from shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with a user's Resy account from a shell, including finding venues, checking reservation slots, booking or cancelling reservations, and managing favorites or Priority Notify entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Resy credentials or a signed-in browser session to act on a real Resy account.

Mitigation: Install only when comfortable granting the agent access to the relevant Resy account, and review authentication steps before use.

Risk: Booking, cancellation, favorite, and Priority Notify commands can mutate real reservations or subscriptions.

Mitigation: Review each write command before execution and verify account state with list or profile calls before and after changes.

## Reference(s):

- [Resy API request reference](references/resy-api.md)
- [Resy](https://resy.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may make real changes to a user's Resy account when used for booking, cancellation, favorites, or Priority Notify actions.]

## Skill Version(s):

0.9.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
