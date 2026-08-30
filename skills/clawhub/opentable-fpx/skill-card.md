## Description:

Query and manage OpenTable restaurant reservations from a shell using the fpx CLI, including restaurant search, slot availability, reservation and favorite listing, and booking, modification, or cancellation through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search OpenTable data and manage reservations or favorites from shell workflows without running the OpenTable MCP server. It is most useful when OpenTable access must reuse a user's signed-in browser session through fpx.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a signed-in OpenTable browser session to make, modify, or cancel real reservations without a built-in confirmation step.

Mitigation: Require an explicit preview and user confirmation before booking, modifying, canceling, changing favorites, or using saved-card-backed reservation flows.

Risk: Booking flows may involve cancellation fees, saved cards, 3-D Secure, required Experiences, or same-day reservation conflicts.

Mitigation: Fetch and review the booking details page before any commit, including cancellation policy, card requirements, Experience details, dining area, and conflict data.

## Reference(s):

- [OpenTable requests for fpx](references/opentable-fpx-requests.md)
- [extract-initial-state.mjs](references/extract-initial-state.mjs)
- [OpenTable](https://www.opentable.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, JavaScript helper code, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include commands that perform real OpenTable account actions when executed against a signed-in browser session.]

## Skill Version(s):

0.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
