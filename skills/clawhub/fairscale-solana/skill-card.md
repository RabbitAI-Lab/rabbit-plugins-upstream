## Description: <br>
FairScale Solana gives agents real-time Solana wallet reputation intelligence for trust checks, bot and whale questions, custom criteria, and transaction risk review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[risheea](https://clawhub.ai/user/risheea) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to evaluate Solana wallet reputation before trades, swaps, airdrops, allowlists, or other wallet-gated decisions. It supports plain-English checks and API-backed scoring with optional custom criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet addresses, wallet lists, transaction amounts, and custom rules may be sent to FairScale for reputation checks. <br>
Mitigation: Require user confirmation before transmitting wallet or transaction details and avoid sending data that is not needed for the requested check. <br>
Risk: API keys and wallet-backed x402 payments could be exposed or used unintentionally. <br>
Mitigation: Store API keys as configured secrets, avoid passing keys on the command line, and require explicit spending limits and per-call approval before enabling wallet-funded payments. <br>
Risk: Reputation scores and recommendations may be incomplete or unsuitable as the sole basis for financial decisions. <br>
Mitigation: Treat results as decision support, review high-value or high-risk transactions manually, and define local thresholds before acting. <br>


## Reference(s): <br>
- [FairScale API Reference](artifact/references/API.md) <br>
- [FairScale Docs](https://docs.fairscale.xyz) <br>
- [FairScale API Docs](https://api2.fairscale.xyz/docs) <br>
- [FairScale API Key](https://sales.fairscale.xyz) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with API examples, shell commands, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call FairScale APIs with wallet addresses, wallet lists, transaction amounts, custom rules, and API keys or wallet-backed x402 payments.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
