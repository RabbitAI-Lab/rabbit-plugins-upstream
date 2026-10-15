## Description:

Guides shell-based retrieval of Credit Karma transactions using a captured browser session, fpx, and curl without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve and paginate their Credit Karma transactions from a shell or script without the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge and shell can access Credit Karma session cookies, refresh tokens, and private financial transactions.

Mitigation: Use a private machine; treat CKAT, ACCESS, and REFRESH as passwords and avoid exposing them in logs.

Risk: Example commands write private transaction responses to shared temporary paths.

Mitigation: Use a private directory with restricted permissions instead of shared /tmp paths, and remove sensitive files after use.

Risk: Refreshing tokens may rotate credentials and sign out the browser session.

Mitigation: Refresh only when needed and be prepared to sign in again and recapture the session.

## Reference(s):

- [Credit Karma request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for paginating and interpreting transaction responses.]

## Skill Version(s):

3.3.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
