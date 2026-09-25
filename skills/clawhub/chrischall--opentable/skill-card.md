## Description:

Manage OpenTable reservations via MCP - search restaurants, check slot availability, book tables, list/cancel reservations, and manage favorites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search restaurants, inspect OpenTable availability, book or modify reservations, cancel reservations, and manage saved restaurants through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill acts through the user's signed-in OpenTable browser session and can access reservation details and basic profile information.

Mitigation: Install only after reviewing the external npm package and fetchproxy extension, and use a browser profile where this session access is acceptable.

Risk: Booking, cancellation, modification, and favorite changes can alter the user's OpenTable account state.

Mitigation: Require explicit user confirmation before every booking, cancellation, modification, or favorite change.

Risk: Credit-card-required reservations may involve cancellation policies, card holds, or no-show fees.

Mitigation: Run the booking or modification preview first and show the cancellation policy and saved-card details before the user confirms.

## Reference(s):

- [OpenTable skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp source](https://github.com/chrischall/opentable-mcp)
- [fetchproxy extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, API calls, text]

**Output Format:** [Markdown guidance with inline JSON and shell command examples; tool responses may include structured text and JSON-like reservation data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools support compact and full views; write actions require explicit confirmation and may return confirmation tokens, booking tokens, confirmation numbers, and security tokens.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
