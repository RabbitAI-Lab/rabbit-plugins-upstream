## Description: <br>
Deploy NFT collections permanently on MegaETH mainnet, storing images on-chain via SSTORE2 and publishing them through WarrenContainer and WarrenLaunchedNFT. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[planetai87](https://clawhub.ai/user/planetai87) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and NFT collection operators use this skill to deploy image-backed NFT collections to MegaETH mainnet, either from an image folder or generated SVG assets. It helps configure collection parameters, store assets on-chain, deploy the NFT contract, and report management and mint page links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a wallet private key and can initiate irreversible MegaETH mainnet transactions. <br>
Mitigation: Use a fresh wallet funded only with the ETH needed for the deployment, pass PRIVATE_KEY through the environment, and review collection parameters and contract addresses before execution. <br>
Risk: Mainnet collection data and on-chain image storage are permanent once transactions are confirmed. <br>
Mitigation: Run a small test collection first and verify images, names, symbols, prices, royalties, supply, and mint settings before deploying the final collection. <br>
Risk: By default, Warren registration sends wallet-linked collection metadata after deployment. <br>
Mitigation: Review the REGISTER_API behavior and set REGISTER_API to an empty value if off-chain Warren registration is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/planetai87/skills/warren-nft-mainnet) <br>
- [Publisher profile](https://clawhub.ai/user/planetai87) <br>
- [Warren app homepage](https://thewarren.app) <br>
- [Warren tools source link](https://github.com/planetai87/warren-tools) <br>
- [MegaETH Blockscout explorer](https://megaeth.blockscout.com) <br>
- [Warren access mint page](https://thewarren.app/mint) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, CLI console output, and a JSON deployment summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and PRIVATE_KEY; deployment output includes NFT contract address, container ID, collection size, prices, and Warren management and mint URLs.] <br>

## Skill Version(s): <br>
1.0.8 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
