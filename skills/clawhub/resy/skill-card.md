## Description:

Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing and canceling reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to resy-mcp so it can search restaurant availability, book or cancel reservations, manage favorites, and create Priority Notify subscriptions for a Resy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live reservation actions, including booking and canceling reservations, on a user's Resy account.

Mitigation: Require explicit confirmation of the restaurant, date, time, party size, and reservation before booking or canceling.

Risk: The skill requires Resy email/password credentials and may use saved payment details.

Mitigation: Install only when comfortable sharing Resy credentials with the third-party MCP server, and avoid delegating payment-sensitive actions without user review.

Risk: The skill uses Resy's private web-app API, which may change or behave differently from the official site.

Mitigation: Confirm that private API behavior is acceptable before use and re-check behavior when Resy changes its web app.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP tool use for live Resy account actions, including reservation booking, cancellation, favorites, notifications, and account/payment metadata lookup.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
