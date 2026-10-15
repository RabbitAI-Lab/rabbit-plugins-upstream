## Description:

Helps agents search Untappd beers and venues, explore account activity, and perform approved account actions such as check-ins, toasts, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Untappd users can ask an agent for beer, brewery, venue, and account information, or approve check-ins and other interactions on their own account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server requires an Untappd password and mobile API credentials.

Mitigation: Install only if comfortable sharing these credentials with the server; avoid unattended or shared deployments.

Risk: Account actions can post publicly if confirmations are weakened by server settings.

Mitigation: Keep write confirmations enabled and review the proposed action before approving it.

Risk: The local cache can retain your and friends' Untappd history until removed.

Mitigation: Treat cached history as sensitive and explicitly forget users' cached records when no longer needed.

## Reference(s):

- [Untappd MCP on ClawHub](https://clawhub.ai/chrischall/skills/untappd-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown guidance and structured Untappd tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some reads return compact results by default; cached-history answers report completeness and freshness.]

## Skill Version(s):

2.3.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
