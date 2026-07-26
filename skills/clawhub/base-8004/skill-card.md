## Description: <br>
Register your AI agent onchain with ERC-8004 on Base by setting up a wallet, funding it, and registering on the Identity Registry for permanent, verifiable identity and reputation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[squirt11e](https://clawhub.ai/user/squirt11e) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to register an AI agent identity on Base mainnet with ERC-8004, including wallet setup, funding checks, metadata preparation, registration, and later metadata updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet private keys could be exposed through logs, terminals, source control, recordings, or shared environments. <br>
Mitigation: Use a fresh low-value wallet, keep private keys in local environment files excluded from source control, and avoid printing or sharing keys. <br>
Risk: Signing a transaction against the wrong network or contract address could waste funds or register incorrect onchain data. <br>
Mitigation: Verify the Base mainnet registry contract address before signing transactions. <br>
Risk: Published agent metadata and endpoints may become permanently public through onchain registration. <br>
Mitigation: Publish only metadata and service endpoints that are appropriate for permanent public disclosure. <br>


## Reference(s): <br>
- [Base 8004 ClawHub skill](https://clawhub.ai/squirt11e/skills/base-8004) <br>
- [ERC-8004 protocol homepage](https://8004.org) <br>
- [Base](https://base.org) <br>
- [BaseScan](https://basescan.org) <br>
- [viem](https://viem.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with TypeScript, shell, and environment-variable examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational guidance for private-key handling, wallet funding, contract calls, and onchain metadata updates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
