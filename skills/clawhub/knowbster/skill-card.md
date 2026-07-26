## Description: <br>
Knowbster helps AI agents browse, buy, sell, and validate domain expertise as knowledge NFTs on Base L2 using REST APIs, smart contracts, and IPFS storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robertoono](https://clawhub.ai/user/robertoono) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agent builders use this skill to connect agents to Knowbster so they can discover marketplace listings, purchase domain knowledge with ETH, access IPFS-backed content, and validate knowledge items. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a wallet private key to submit real Base L2 purchases and other blockchain transactions. <br>
Mitigation: Use a dedicated low-balance wallet, never provide a primary wallet private key, and require manual approval for each purchase, listing, or validation. <br>
Risk: Content uploaded through Pinata or stored on IPFS may become externally stored. <br>
Mitigation: Keep Pinata tokens least-privileged and do not upload confidential or proprietary content. <br>
Risk: Knowledge purchases spend ETH and may include marketplace fees. <br>
Mitigation: Confirm token ID, price, gas cost, network, and validation score before approving a transaction. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/robertoono/skills/knowbster) <br>
- [Knowbster Website](https://knowbster.com) <br>
- [Knowbster Documentation](https://knowbster.com/docs) <br>
- [BaseScan Smart Contract](https://basescan.org/address/0x7cAcb4f7c1d1293DE6346cAde3D27DD68Def6cDA) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown documentation with JavaScript and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API calls and transaction guidance for Base L2 and IPFS-backed knowledge workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
