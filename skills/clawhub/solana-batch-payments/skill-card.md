## Description: <br>
Batch send SOL, USDC, BONK, or SPL tokens to up to 1,000 Solana wallets through Spraay's non-custodial x402 pay-per-call gateways, with support for unsigned transaction building, swap quotes, portfolio lookups, and price feeds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to prepare Solana batch payments, airdrops, team payouts, creator rewards, token distribution, swap quote checks, wallet portfolio lookups, and token price checks without giving the gateway custody of private keys. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial transactions may send funds to incorrect recipients, use wrong amounts, select the wrong network, or include unexpected fees. <br>
Mitigation: Before signing, inspect recipients, amounts, network, fees, token mints, and the returned unsigned transactions; use devnet or small tests first. <br>
Risk: The workflow uses a third-party gateway to construct unsigned Solana transactions. <br>
Mitigation: Install only if that gateway dependency is acceptable, verify responses match the intended request, and keep signing local. <br>
Risk: Providing a wallet keypair to the helper signs and submits transactions from that wallet locally. <br>
Mitigation: Do not provide a keypair unless you intentionally want the helper to sign and submit those transactions; never send private keys to the gateway. <br>
Risk: Returned blockhashes can expire before signed transactions are submitted. <br>
Mitigation: Sign and submit promptly after building; rebuild the batch if the last valid block height has passed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/plagtech/skills/solana-batch-payments) <br>
- [Spraay Documentation](https://docs.spraay.app) <br>
- [Spraay Homepage](https://spraay.app) <br>
- [API Reference - Spraay Solana Gateway](reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON examples, bash commands, JavaScript helper usage, and API request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces unsigned transaction-building guidance and local signing instructions; no private keys should be sent to the gateway.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
