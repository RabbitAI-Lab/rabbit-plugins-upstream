## Description:

Launch a token on Flap BNB.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flapguy](https://clawhub.ai/user/flapguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and token creators use this skill to prepare and submit a Flap Tax Token V3 launch on BNB Chain, including quote-token selection, metadata upload, tax parameters, optional vault configuration, vanity salt generation, and EVM transaction construction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow prepares a real BNB Chain token launch, and signed blockchain transactions are irreversible.

Mitigation: Use the skill only when intending to launch a real token, and independently review the transaction in the wallet before signing.

Risk: Incorrect contract addresses, calldata, quote amounts, token taxes, beneficiary, vault settings, or ERC-20 approvals can produce unintended on-chain effects.

Mitigation: Verify all launch parameters, approvals, and wallet-displayed transaction details before broadcasting.

Risk: The skill depends on BNB mainnet RPC access and may use a public fallback endpoint if the user does not provide one.

Mitigation: Prefer a trusted RPC endpoint, confirm chain ID 56, and verify connectivity during preflight.

## Reference(s):

- [Flap Documentation](https://docs.flap.sh)
- [ClawHub Skill Page](https://clawhub.ai/flapguy/skills/launch-bnb-token-on-flap)
- [Preflight Checks](references/preflight.md)
- [Choosing a Quote Token](references/quote-tokens.md)
- [Vault Factory Setup](references/vault-factory.md)
- [Token Metadata Upload](references/meta-upload.md)
- [Tax Token Parameters](references/tax-params.md)
- [Finding the Vanity Salt](references/salt-finding.md)
- [Construct the EVM Transaction](references/construct-tx.md)
- [Flap Quote Tokens API](https://flap.sh/api/launch/quote-tokens)
- [Flap Metadata Upload API](https://funcs.flap.sh/api/upload)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with TypeScript and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces transaction parameters and instructions for wallet review and signing; does not itself guarantee transaction execution.]

## Skill Version(s):

1.3.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
