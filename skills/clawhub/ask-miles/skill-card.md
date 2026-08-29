## Description:

Ask Miles routes credit card rewards and points questions to the Ask Miles service so an agent can answer using the account owner's wallet, card catalog, valuations, transfer data, and offer context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[assareh](https://clawhub.ai/user/assareh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to ask card rewards, transfer partner, award strategy, and keep-or-cancel questions against the approving Miles account owner's wallet. It is most useful when the answer depends on current card multipliers, active offers, or the owner's actual card lineup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth client secrets and refresh tokens are required to ask questions using the Miles account owner's approved grant.

Mitigation: Store credentials in an appropriate secret store, review where the client secret and refresh token are persisted, and refresh access tokens instead of pasting static tokens.

Risk: Questions may include unrelated calendar, email, household, or other personal details that the Ask Miles service does not need.

Mitigation: Send only the rewards-related part of the user's question and avoid routing unrelated personal details to the service.

Risk: Answers are tied to one Miles account owner's wallet and usage allowance.

Mitigation: Use the skill only for that account owner's questions; require a separate Miles account for other users rather than answering from the wrong wallet.

Risk: A response without Miles tool provenance may rely on model knowledge instead of the current catalog.

Mitigation: Check the Miles response metadata and treat answers without tools called as unverified when relaying them.

## Reference(s):

- [Ask Miles OpenClaw homepage](https://askmiles.ai/openclaw)
- [Ask Miles skill source](https://askmiles.ai/skills/ask-miles.md)
- [Ask Miles chat completions endpoint](https://askmiles.ai/v1/chat/completions)
- [Ask Miles OAuth authorization server metadata](https://mcp.askmiles.ai/.well-known/oauth-authorization-server)
- [ClawHub skill page](https://clawhub.ai/assareh/skills/ask-miles)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP, OAuth, and JSON examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Miles service metadata such as tools called and response duration.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
