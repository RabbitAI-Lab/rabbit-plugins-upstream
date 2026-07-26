## Description: <br>
Deploy websites and files to MegaETH testnet by storing content on-chain with SSTORE2 bytecode storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[planetai87](https://clawhub.ai/user/planetai87) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to publish HTML or file content to Warren on MegaETH testnet, including stress-test deployments that mint site NFTs and return loader URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles wallet private keys used to sign blockchain transactions. <br>
Mitigation: Use a fresh, low-funded testnet wallet and never use a primary wallet or reused private key. <br>
Risk: The deployment flow can perform irreversible on-chain actions without a clear confirmation gate. <br>
Mitigation: Review the exact content and contract actions before running, and add an explicit confirmation or dry-run step before autonomous execution. <br>
Risk: Published content may be permanent or difficult to remove after deployment. <br>
Mitigation: Inspect the content before deployment and only publish files that are intended for public on-chain storage. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/planetai87/skills/warren-deploy) <br>
- [Warren homepage](https://megawarren.xyz) <br>
- [MegaETH faucet](https://docs.megaeth.com/faucet) <br>
- [MegaETH testnet explorer](https://megaeth-testnet-v2.blockscout.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, URLs, Guidance] <br>
**Output Format:** [Markdown instructions with bash examples and deployment JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Deployments return a token ID, root chunk address, tree depth, and Warren loader URL.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
