## Description: <br>
ClawdWallet helps agents install and control a multi-chain Web3 wallet Chrome extension for wallet setup, dApp connections, transaction signing, and crypto management across EVM, Bitcoin, Solana, Cosmos, and other chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neomaking](https://clawhub.ai/user/neomaking) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agent users use this skill to set up an agent-controlled browser wallet, configure the Clawdbot gateway, and review, approve, or reject dApp signing requests across supported chains. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent sensitive crypto-wallet authority, including transaction signing and seed-based wallet initialization. <br>
Mitigation: Use a dedicated wallet with minimal funds, never import a primary seed phrase, and require explicit confirmation for every signature or transaction. <br>
Risk: The documented install path references external GitHub code without server-resolved pinned provenance. <br>
Mitigation: Review or pin the referenced code before installation, and prefer an audited release or known commit before granting signing authority. <br>
Risk: dApp requests may originate from untrusted sites or contain misleading transaction and contract-call details. <br>
Mitigation: Verify dApp origins, chain, recipient, value, request ID, and contract-call details before approving; reject unclear requests. <br>


## Reference(s): <br>
- [Clawdwallet on ClawHub](https://clawhub.ai/neomaking/skills/clawdwallet) <br>
- [ClawdWallet GitHub repository referenced by artifact](https://github.com/NeOMakinG/clawdwallet.git) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON messages, Guidance] <br>
**Output Format:** [Markdown with inline bash, YAML, and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes command examples and review guidance for wallet requests.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
