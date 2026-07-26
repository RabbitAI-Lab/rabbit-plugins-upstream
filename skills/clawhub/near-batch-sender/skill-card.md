## Description: <br>
Batch operations for NEAR tokens - send to multiple recipients, transfer NFTs, claim rewards with cost estimation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to prepare and run batch NEAR token sends, NFT transfers, reward claims, and cost estimates from JSON input files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk NEAR token or NFT operations can move valuable assets to multiple recipients. <br>
Mitigation: Run on testnet or with very small transfers first, and use only sender accounts and JSON files that have been reviewed. <br>
Risk: Weak input validation can allow malformed account, contract, token, or amount fields to produce unintended transfers or command behavior. <br>
Mitigation: Validate every account, contract, token ID, amount, and operation type before execution. <br>
Risk: Shell-string command execution increases risk when untrusted JSON or account values are used. <br>
Mitigation: Replace shell-string execution with argument-based process execution before relying on the skill for valuable assets. <br>
Risk: The artifact does not provide an explicit preview and confirmation step before asset-moving operations. <br>
Mitigation: Add a preview of all recipients, assets, amounts, estimated costs, and commands, then require explicit confirmation before executing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shaiss/skills/near-batch-sender) <br>
- [NEAR CLI](https://docs.near.org/tools/near-cli) <br>
- [NEAR Batch Actions](https://docs.near.org/api/rpc/transactions/batch-actions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute NEAR CLI commands that transfer assets when used with configured accounts.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
