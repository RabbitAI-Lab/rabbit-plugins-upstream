## Description:

Ask Miles answers card and points questions against the account owner's real wallet, including which card to get next, keep-or-cancel math, transfer partners and ratios, award strategy, and which card to use for a purchase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[assareh](https://clawhub.ai/user/assareh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to ask Miles credit-card rewards questions through an Ask Miles account, using the account owner's wallet, card catalog, valuations, and transfer data. It is intended for read-only rewards guidance, not account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends card-rewards questions to Ask Miles using one person's wallet-scoped identity.

Mitigation: Use a dedicated personal API key when possible, route only that account owner's questions through the skill, and use separate Miles accounts for other people.

Risk: API keys, OAuth tokens, and refresh tokens can grant access to the account owner's Ask Miles usage allowance and wallet-based answers.

Mitigation: Store credentials like other secrets, avoid committing or echoing them, and revoke the API key or connected app when access is no longer needed.

Risk: Unrelated personal context or unsupported household facts could be sent to Miles or incorrectly attributed to Miles.

Mitigation: Send only the rewards-related question and clearly separate Miles' wallet-based answer from any local records or user-provided facts.

Risk: If Miles is unavailable or answers without catalog tools, the agent could present incomplete guidance as confirmed.

Mitigation: Treat outages as unavailability rather than negative answers, honor retry limits, and disclose when a response was not verified by Miles tools.

## Reference(s):

- [Ask Miles skill homepage](https://askmiles.ai/openclaw?utm_source=skill&utm_medium=assistant)
- [ClawHub skill listing](https://clawhub.ai/assareh/skills/ask-miles)
- [Ask Miles current skill document](https://askmiles.ai/skills/ask-miles.md)
- [Ask Miles chat completions endpoint](https://askmiles.ai/v1/chat/completions)
- [Ask Miles API key settings](https://askmiles.ai/settings?utm_source=skill&utm_medium=assistant#api-keys)
- [Ask Miles OAuth authorization server discovery](https://mcp.askmiles.ai/.well-known/oauth-authorization-server)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional code snippets and API request details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should be based on Miles output, preserve numeric details verbatim, and disclose when Miles did not use its tools.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
