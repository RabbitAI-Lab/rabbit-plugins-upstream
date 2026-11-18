## Description:

Helps an agent resolve Talvio Dot Robot NFTs in DOTFIELD on BNB Chain and discharge eligible units for $DOT.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pokemontownss](https://clawhub.ai/user/pokemontownss)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent for help resolving a Talvio Dot Robot NFT or claiming $DOT from an eligible unit. The skill provides the required eligibility checks, contract call sequence, and exact payment amounts for each lane.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A transaction described as a free mint may still incur BNB network fees.

Mitigation: Check the fee before signing and keep it within the user's spending limit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pokemontownss/skills/mint-talvio-dotfield)
- [DOTFIELD project site](https://talviogenerate.com)
- [DOTFIELD mint information](https://talviogenerate.com/mint.json)
- [DOTFIELD agent instructions](https://talviogenerate.com/llms.txt)
- [DOTFIELD agent metadata](https://talviogenerate.com/agent.json)
- [NFT metadata by token ID](https://talviogenerate.com/nft/metadata/<id>.json)

## Skill Output:

**Output Type(s):** [Guidance, API Calls]

**Output Format:** [Text with contract call sequences and parameter values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eligibility and amounts depend on current on-chain state; transaction fees may apply.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
