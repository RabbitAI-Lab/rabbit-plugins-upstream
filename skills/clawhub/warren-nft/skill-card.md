## Description: <br>
Deploy NFT collections permanently on MegaETH blockchain with images stored on-chain via SSTORE2, including royalties, minting, and management pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[planetai87](https://clawhub.ai/user/planetai87) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and NFT creators use this skill to deploy MegaETH testnet NFT collections with on-chain image storage, configurable minting, royalties, and public management or mint pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles raw wallet private keys. <br>
Mitigation: Use only a dedicated low-value MegaETH testnet wallet, provide keys through environment handling rather than inline command arguments when possible, and never reuse a mainnet or funded key. <br>
Risk: Blockchain deployments and on-chain image storage are public and hard to undo. <br>
Mitigation: Review collection metadata, image content, wallet address exposure, mint settings, and deployment costs before running the deployment. <br>
Risk: The skill performs irreversible blockchain actions with weak user safeguards. <br>
Mitigation: Run it only after local review and use a testnet wallet with limited funds so failed or unintended transactions have bounded impact. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/planetai87/skills/warren-nft) <br>
- [MegaWarren homepage](https://megawarren.xyz) <br>
- [MegaETH faucet documentation](https://docs.megaeth.com/faucet) <br>
- [MegaETH testnet explorer](https://megaeth-testnet-v2.blockscout.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and deployment result text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a MegaETH testnet wallet private key; produces NFT contract addresses, container IDs, and management and mint page URLs after deployment.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
