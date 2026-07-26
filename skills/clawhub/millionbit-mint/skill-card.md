## Description: <br>
Mint an image as an NFT plot on the Million Bit Homepage, a permanent 1024x1024 pixel canvas on the Base blockchain, by preparing image resizing, availability checks, price queries, pixel encoding, and transaction JSON for a separate EVM wallet skill to submit. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[millionbithomepage](https://clawhub.ai/user/millionbithomepage) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to prepare Base-chain NFT mint transactions for Million Bit Homepage plots after selecting an image, URL, grid-aligned coordinates, and plot size. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prepared mint transactions can spend real ETH on Base and publish image and link data permanently on-chain. <br>
Mitigation: Before signing, verify the contract, chain ID, price, gas, recipient, image, link, and plot coordinates in the wallet transaction. <br>
Risk: The skill prepares transaction JSON but does not submit it or manage wallet custody. <br>
Mitigation: Use a trusted EVM wallet skill for submission and treat the prepared payload as a proposal to review before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/millionbithomepage/skills/millionbit-mint) <br>
- [Publisher profile](https://clawhub.ai/user/millionbithomepage) <br>
- [Base mainnet RPC](https://mainnet.base.org) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON transaction payloads and Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces wallet-ready transaction fields including contract address, value, calldata, chain ID, price metadata, plot size, and destination URL.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
