## Description:

Manage OpenTable reservations via MCP - search restaurants, check slot availability, book tables, list/cancel reservations, and manage favorites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to search OpenTable restaurants, inspect availability, create or modify reservations, cancel bookings, and manage saved restaurants through a signed-in browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses the user's signed-in OpenTable browser session and can make reservation, cancellation, modification, and favorite changes.

Mitigation: Review each write action before approval, especially bookings or changes that involve saved-card holds, no-show fees, or cancellation policies.

Risk: Some bookings require a saved-card preview and may carry cancellation or no-show fees.

Mitigation: Run the preview flow first, surface the policy and card details to the user, and commit only after explicit confirmation.

Risk: Reservation and booking tokens are short-lived, so delayed actions may fail or act on stale availability.

Mitigation: Fetch fresh slots immediately before booking or modifying when the user has paused or changed requirements.

Risk: The skill depends on a running fetchproxy browser extension and an authenticated opentable.com tab.

Mitigation: Confirm the extension is installed, connected, and using the intended browser profile before making authenticated requests.

## Reference(s):

- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with MCP tool guidance, JSON configuration snippets, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools support compact and full response views; booking and modification flows return receipts or short-lived tokens needed for follow-up actions.]

## Skill Version(s):

0.19.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
