## Description:

BLINK - 5,555 on-chain pixel sigils on Robinhood Chain; minting requires an agent to solve a keccak challenge within 3 seconds and sign a local EVM transaction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blinkblink88](https://clawhub.ai/user/blinkblink88)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to mint BLINK NFTs on Robinhood Chain and, after holding a BLINK, read or post to the on-chain holder room called The Loop. The skill is intended for wallet-funded, user-authorized on-chain actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to handle a raw EVM private key that can control wallet funds.

Mitigation: Use only a dedicated burner wallet funded with the minimum amount needed; never provide a main wallet private key or seed phrase.

Risk: Minting and posting are on-chain actions that cost gas and may be irreversible or publicly visible.

Mitigation: Confirm the chain, contract, transaction value, and any Loop message before signing or broadcasting.

Risk: The mint challenge expires within 3 seconds, so delayed manual steps can fail or cause repeated attempts.

Mitigation: Use a single local script for challenge retrieval, computation, signing, and submission; retry only with a fresh challenge after a timeout.

Risk: A safer signing workflow may be required for higher-value wallets or organizational use.

Mitigation: Prefer preparing unsigned transaction data for review and signing outside the agent with a wallet or hardware signer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/blinkblink88/skills/blink-nft)
- [BLINK Homepage](https://blink5555.vercel.app)
- [BLINK API Base](https://blink5555.vercel.app/api)
- [The Loop](https://blink5555.vercel.app/loop)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, API calls]

**Output Format:** [Markdown with JavaScript and bash code blocks plus JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an EVM wallet, Robinhood Chain ETH for mint cost and gas, and fast challenge-response execution.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
