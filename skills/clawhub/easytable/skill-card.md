## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect easyTable restaurant availability and manage reservations through the user's own browser session. Create, modify, and cancel actions are confirmation-gated and return a dry-run preview before applying changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed create, modify, or cancel actions can affect real restaurant reservations tied to a phone number.

Mitigation: Review the dry-run preview carefully before re-running an action with confirm: true.

Risk: The skill depends on the fetchproxy browser extension and an open easyTable widget tab for booking workflows.

Mitigation: Install only if that browser-extension dependency is acceptable, and keep the relevant booking widget tab open and loaded before confirming changes.

Risk: Create and modify actions use a single-use Cloudflare Turnstile token that can expire.

Mitigation: Reload the booking widget tab and retry if a confirmed create or modify action fails because of the token.

## Reference(s):

- [easytable ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [easyTable booking widget](https://book.easytable.com/book/?id=<restaurantId>)

## Skill Output:

**Output Type(s):** [Text, API Calls, Guidance]

**Output Format:** [Markdown or plain text with reservation availability, booking previews, confirmations, and next-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an open, loaded easyTable booking widget tab and user confirmation for create, modify, or cancel actions.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
