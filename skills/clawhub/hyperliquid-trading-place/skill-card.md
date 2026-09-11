## Description:

Helps an agent place Hyperliquid perpetual orders only after explicit trade intent, setup completion, builder-fee approval, and filled-order confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading operators use this skill to configure a local Hyperliquid trading rail and have an agent place perpetual orders after explicit trade confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unaudited third-party setup code runs in a wallet and trading context.

Mitigation: Install only in a dedicated low-privilege environment and inspect or verify @hypelens/hypelens-agent-rail@0.1.28 before running npm install or setup.

Risk: A master private key could be exposed during npm lifecycle or setup flows.

Mitigation: Avoid exposing a master private key to npm lifecycle scripts; use the narrowest signing flow available and confirm each approval before signing.

Risk: Builder-fee approval authorizes fees to a configured address and limit.

Mitigation: Confirm the builder fee address and approval limit before signing, and place orders only after explicit confirmTrade consent and filled-order polling.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/polyparlay/skills/hyperliquid-trading-place)
- [ClawHub Publisher Profile](https://clawhub.ai/user/polyparlay)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration guidance, and code-oriented tool call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and npm; setup gates trading until local setup and builder-fee approval are complete.]

## Skill Version(s):

1.0.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
