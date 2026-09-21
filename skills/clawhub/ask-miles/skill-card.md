## Description:

Miles lets an agent ask Ask Miles card and points questions against the account owner's real Miles wallet, current card catalog, valuations, and transfer data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[assareh](https://clawhub.ai/user/assareh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use Miles to answer credit card rewards and points questions against the account owner's Miles wallet, including card selection, keep-or-cancel analysis, transfer strategy, award planning, and purchase card choice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ask Miles API keys and OAuth refresh tokens can grant access to answers based on the account owner's Miles wallet.

Mitigation: Store credentials as secrets, do not commit or print them, and revoke unused credentials from Ask Miles settings.

Risk: A credential belongs to one Miles account, so using it for another household member can answer from the wrong wallet.

Mitigation: Route questions only for the credential owner's account, and require a separate Miles account for other users.

Risk: Miles may answer without catalog-backed tool calls or with visibility limited to the Miles wallet and catalog.

Mitigation: Check the response provenance object when available, treat answers without tool calls as unverified, and do not present missing wallet data as a confirmed real-world fact.

Risk: Rate limits, timeouts, or network errors can make Miles unavailable without implying a negative answer.

Mitigation: Honor Retry-After, allow long-running requests, and clearly state when Miles could not be reached before relying on another source.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/assareh/skills/ask-miles)
- [Ask Miles OpenClaw page](https://askmiles.ai/openclaw?utm_source=skill&utm_medium=assistant)
- [Ask Miles skill source](https://askmiles.ai/skills/ask-miles.md)
- [Ask Miles chat completions endpoint](https://askmiles.ai/v1/chat/completions)
- [Ask Miles OAuth authorization server metadata](https://mcp.askmiles.ai/.well-known/oauth-authorization-server)

## Skill Output:

**Output Type(s):** [guidance, code, configuration]

**Output Format:** [Markdown with inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to make read-only Ask Miles chat requests and to treat response provenance, rate limits, and unavailable service states explicitly.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
