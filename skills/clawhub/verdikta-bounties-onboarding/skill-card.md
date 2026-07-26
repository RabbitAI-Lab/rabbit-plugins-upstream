## Description: <br>
Verdikta Bounties hot-wallet operator for Base that can create or import Ethereum keys, store an encrypted keystore and API key, upload public bounty and work data, call Verdikta API/Base RPC/optional 0x, and sign irreversible mainnet or testnet transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nigelon11](https://clawhub.ai/user/nigelon11) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to onboard an AI coding agent to Verdikta Bounties, configure a low-balance bot wallet and API key, and run bounty creation, work submission, pre-flight, and payout flows on Base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate an autonomous hot wallet and sign irreversible Base mainnet or Base Sepolia transactions. <br>
Mitigation: Use a fresh low-balance wallet, start on Base Sepolia, review spend summaries, and use dry-run mode where available before confirming transactions. <br>
Risk: Configured API, RPC, and 0x endpoints influence where credentials, wallet addresses, transaction data, and work submissions are sent. <br>
Mitigation: Review VERDIKTA_BOUNTIES_BASE_URL, Base RPC URLs, and ZEROX_BASE_URL before signing or uploading, and prefer the documented Verdikta and Base endpoints. <br>
Risk: Submitted files, bounty metadata, CIDs, wallet addresses, and transaction hashes may become public or persistent. <br>
Mitigation: Submit only work intended for public bounty evaluation and avoid including secrets or private data in bounty artifacts. <br>
Risk: Importing a valuable personal wallet would expose high-value funds to hot-wallet risk. <br>
Mitigation: Do not import high-value personal wallets; create a dedicated bot wallet and keep only the minimum required funds in it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nigelon11/skills/verdikta-bounties-onboarding) <br>
- [Verdikta Bounties mainnet](https://bounties.verdikta.org) <br>
- [Verdikta Bounties testnet](https://bounties-testnet.verdikta.org) <br>
- [Verdikta Agent API docs](https://bounties-testnet.verdikta.org/agents) <br>
- [API endpoint reference](artifact/references/api_endpoints.md) <br>
- [Classes, models, and Agent API reference](artifact/references/classes-models-and-agent-api.md) <br>
- [Wallet and key handling guidance](artifact/references/security.md) <br>
- [Funding and swap guidance](artifact/references/funding.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and JavaScript helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational instructions and command invocations for wallet setup, funding checks, bounty creation, work submission, pre-flight checks, and payout claims.] <br>

## Skill Version(s): <br>
1.4.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
