## Description: <br>
Guides users through uploading an image and metadata, mining a vanity salt, and deploying a token on-chain through Nad.fun's BondingCurveRouter flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therealharpaljadeja](https://clawhub.ai/user/therealharpaljadeja) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and token creators use this skill to prepare Nad.fun token metadata, request a vanity salt, and generate code or guidance for deploying a token with an optional initial buy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload the user's image, token metadata, links, wallet address, and token details to Nad.fun. <br>
Mitigation: Require explicit confirmation before every upload and show the exact data and destination first. <br>
Risk: The skill can lead to fund-spending blockchain transactions for token deployment or an optional initial buy. <br>
Mitigation: Require confirmation before signing and verify the network, contract addresses, deploy fee, total spend, and initial-buy amount. <br>
Risk: Wallet actions depend on another skill for signer, private key, and RPC handling. <br>
Mitigation: Use the installed wallet-management skill for signer access and avoid exposing private keys in generated output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/therealharpaljadeja/skills/nadfun-token-creation) <br>
- [Nad.fun API base](https://api.nadapp.net) <br>
- [Source skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, API calls, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with JavaScript, Solidity, and shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Sequential four-step flow; outputs may precede uploads or wallet transactions that require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
