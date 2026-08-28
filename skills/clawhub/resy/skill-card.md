## Description:

Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing and canceling reservations, managing favorites, and subscribing to Priority Notify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Resy restaurant reservations through an MCP server, including finding availability, booking tables, canceling existing reservations, and managing favorites or Priority Notify subscriptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can book or cancel real restaurant reservations using Resy account credentials.

Mitigation: Review venue, date, time, party size, payment details, and cancellation terms before confirming booking or cancellation actions.

Risk: Credential-bearing MCP configuration or environment files may expose Resy login details if shared or committed.

Mitigation: Keep MCP config and .env files private, avoid committing credentials, and rotate credentials if exposure is suspected.

Risk: The skill uses private Resy endpoints and may persist an authentication token on disk depending on configuration.

Mitigation: Install only if comfortable granting third-party MCP access to the Resy account, and disable token caching if persisted authentication tokens are not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/resy)
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp)
- [resy-mcp source link from artifact](https://github.com/chrischall/resy-mcp)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return reservation details, availability, cancellation status, favorite venues, notification subscriptions, and setup guidance.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
