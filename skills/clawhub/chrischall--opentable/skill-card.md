## Description:

Manage OpenTable reservations through MCP, including restaurant search, slot availability checks, bookings, reservation cancellation, and favorites management, using a signed-in OpenTable browser session with the fetchproxy extension.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent help find restaurants, check availability, book or cancel reservations, and manage OpenTable favorites from a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on external MCP code and a browser extension operating in a signed-in OpenTable session.

Mitigation: Review the package and extension before installation, pin them to reviewed versions, use a dedicated browser profile where possible, and keep the extension running only while needed.

Risk: Booking, modifying, cancelling, and favorites tools can change the user's OpenTable account state, and some reservations may involve saved-card holds or no-show fees.

Mitigation: Require explicit user confirmation before account-changing actions, surface cancellation policies and saved-card details from preview results, and preserve confirmation and security tokens needed for cancellation.

Risk: OpenTable slot tokens are short-lived, so stale availability can lead to failed or unintended booking attempts.

Mitigation: Fetch fresh slots immediately before booking and re-check availability when the user delays or changes reservation details.

## Reference(s):

- [ClawHub opentable skill page](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp project reference](https://github.com/chrischall/opentable-mcp)
- [fetchproxy extension reference](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool names, JSON configuration examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent outputs may include reservation details, cancellation policies, confirmation numbers, security tokens, and profile or favorites data returned by OpenTable tools.]

## Skill Version(s):

0.19.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
