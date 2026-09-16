## Description:

Manage OpenTable reservations via MCP by searching restaurants, checking slot availability, booking tables, listing or canceling reservations, and managing favorites through a signed-in OpenTable browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search OpenTable restaurants, inspect availability, and manage reservations or saved restaurants through an authenticated OpenTable browser session. Developers use it to configure the required MCP server and fetchproxy browser extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned MCP package and browser extension in an authenticated OpenTable browser session.

Mitigation: Use a pinned, reviewed version of the MCP server when possible and verify the fetchproxy extension source and permissions before installing.

Risk: Profile details, reservation identifiers, security tokens, and masked payment details may enter agent context or logs.

Mitigation: Use a separate browser profile where practical and avoid retaining or sharing sensitive reservation and payment metadata.

Risk: Booking, modifying, canceling, and favorite changes affect the user's OpenTable account and are not consistently confirmation-gated.

Mitigation: Require explicit user confirmation before booking, modifying, canceling, adding favorites, or removing favorites.

Risk: Short-lived reservation and booking tokens can expire or refer to unavailable slots if the user delays.

Mitigation: Re-check availability and run preview immediately before committing a booking or modification.

## Reference(s):

- [ClawHub opentable Skill](https://clawhub.ai/chrischall/skills/opentable)
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp)
- [opentable-mcp source link from artifact](https://github.com/chrischall/opentable-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [OpenTable](https://www.opentable.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool-call recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools can return compact or full OpenTable payloads; write tools return receipts such as confirmation numbers, security tokens, and status.]

## Skill Version(s):

0.19.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
