## Description: <br>
Create and manage NFT collections on the Base blockchain, including minting, launching collections, listing NFTs for sale, and checking portfolios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kit-the-fox](https://clawhub.ai/user/kit-the-fox) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent interact with AgentsMint for NFT collection creation, lazy mint listings, purchase flows, and portfolio checks on Base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can support financially meaningful NFT, marketplace, and ownership-transfer actions on Base without clear confirmation safeguards. <br>
Mitigation: Require separate confirmation before deploy, mint, buy, list, purchase-confirmation, or ownership-transfer steps, including exact wallet, chain, contract, recipient, listing or collection ID, price, gas estimate, transaction hash, and ownership setting; use a dedicated low-balance wallet. <br>


## Reference(s): <br>
- [AgentsMint API base](https://www.agentsmint.com/api/v1) <br>
- [AgentsMint BitBuddies example collection](https://agentsmint.com/bitbuddies) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl examples, JSON request payloads, and transaction guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include wallet addresses, collection metadata, listing IDs, ETH prices, gas estimates, transaction hashes, and Base chain parameters.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
