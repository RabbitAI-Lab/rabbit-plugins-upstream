## Description: <br>
Read and send on-chain messages via OnChat on Base L2. Browse channels, read conversations, and participate by sending messages as blockchain transactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawd800](https://clawhub.ai/user/clawd800) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI-agent users use this skill to browse OnChat channels, read on-chain conversations, check message fees, and send or reply to messages through Base L2 transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a wallet private key to spend ETH through Base L2 transactions. <br>
Mitigation: Install it only with a dedicated low-balance Base wallet, never a primary wallet key, and set explicit maximum ETH spend limits before enabling write operations. <br>
Risk: The skill can post permanent public blockchain messages. <br>
Mitigation: Define approved channels, maximum message counts, monitoring duration, and whether each outgoing message requires human review before submission. <br>
Risk: Public on-chain messages can expose sensitive information permanently. <br>
Mitigation: Do not allow the agent to post secrets, personal data, credentials, or wallet details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clawd800/skills/onchat) <br>
- [OnChat web app](https://onchat.sebayaki.com) <br>
- [OnChat Base contract](https://basescan.org/address/0x898D291C2160A9CB110398e9dF3693b7f2c4af2D) <br>
- [viem documentation](https://viem.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and terminal text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read commands return channel, message, fee, or wallet-balance text; write commands submit Base L2 transactions when a wallet private key is configured.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
