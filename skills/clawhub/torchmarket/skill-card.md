## Description: <br>
Torch Market helps agents query Torch protocol state and build Solana transactions for token creation, trading, vault operations, lending, short selling, liquidation, migration, and rewards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrsirg97-rgb](https://clawhub.ai/user/mrsirg97-rgb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Torch Market to inspect Torch protocol markets and prepare or submit Solana DeFi transactions. In read-only mode it returns state and unsigned transactions; with a configured disposable controller key it can submit transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can build or submit high-risk Solana DeFi transactions for trading, vault operations, lending, short selling, and liquidation. <br>
Mitigation: Use read-only mode or unsigned transaction review by default; enable signing only with explicit spend limits and deliberate operator approval. <br>
Risk: A configured signing key could move funds if it is reused from a vault authority or high-value wallet. <br>
Mitigation: Use a fresh disposable controller key with only enough SOL for gas, and never provide a vault authority key or seed phrase. <br>
Risk: Token lookups and enrichment can contact Solana RPC and third-party services. <br>
Mitigation: Use a trusted RPC endpoint, expect network disclosure of queried token and wallet context, and avoid enrichment workflows when that disclosure is unacceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mrsirg97-rgb/skills/torchmarket) <br>
- [Torch Market website](https://torch.market) <br>
- [Program source URL from metadata](https://github.com/mrsirg97-rgb/torch_market) <br>
- [SDK source URL from metadata](https://github.com/mrsirg97-rgb/torchsdk) <br>
- [Torch SDK npm package](https://www.npmjs.com/package/torchsdk) <br>
- [Torch Market risk model](https://torch.market/risk.md) <br>
- [Torch Market verification report](https://torch.market/verification.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured transaction-building guidance, with TypeScript examples and Solana transaction objects when used through the bundled SDK] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOLANA_RPC_URL. SOLANA_PRIVATE_KEY is optional; without it the skill operates in read-and-build mode and returns unsigned transactions.] <br>

## Skill Version(s): <br>
11.1.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
