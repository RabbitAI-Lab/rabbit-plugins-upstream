## Description:

Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to inspect easyTable restaurant availability and manage reservations through their own browser session. It supports booking-area lookup, date and time discovery, booking lookup by phone, and confirm-gated create, modify, and cancel actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install an unpinned browser extension that can act through a live booking tab.

Mitigation: Review the fetchproxy extension source, permissions, release provenance, and revocation process before installing, and leave it paired only as long as needed.

Risk: Create, modify, and cancel operations can change real reservations.

Mitigation: Use the built-in dry-run preview and set confirm: true only after checking the requested booking change.

Risk: Create and modify operations depend on a single-use Cloudflare Turnstile token from the active widget tab.

Mitigation: Keep the correct book.easytable.com widget tab open and reload the tab before retrying if token submission fails.

## Reference(s):

- [fetchproxy browser extension source](https://github.com/chrischall/fetchproxy)
- [easyTable booking widget](https://book.easytable.com/book/?id=<restaurantId>)

## Skill Output:

**Output Type(s):** [Guidance, API Calls]

**Output Format:** [Text guidance with MCP tool call sequencing and dry-run confirmation previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an open, loaded easyTable browser tab for create and modify confirmation.]

## Skill Version(s):

0.4.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
