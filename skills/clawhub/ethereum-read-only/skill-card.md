## Description: <br>
Guides agents through read-only Ethereum state inspection with Foundry cast, including blocks, contracts, logs, ENS, ABI decoding, and DeFi balance checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byron-mckeeby](https://clawhub.ai/user/byron-mckeeby) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to inspect public Ethereum-compatible chain data without wallet access or transaction signing. It is suited for read-only checks of block metadata, contract state, event logs, ENS records, transaction inputs, and DeFi token balances. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read-only blockchain queries sent to public RPC or API providers can reveal addresses, contracts, and investigation patterns. <br>
Mitigation: Use a dedicated low-privilege RPC key or a trusted/self-hosted node for sensitive investigations, and avoid sending private research targets to shared endpoints. <br>
Risk: The guide includes shell commands for installing Foundry and composing blockchain queries, so copied commands can run network installers or malformed arguments if used without review. <br>
Mitigation: Review commands before execution, install Foundry only from its official source, quote user-controlled values, and test scripts on non-sensitive targets first. <br>
Risk: External wallet or transaction guidance referenced by the artifact is outside the reviewed read-only scope. <br>
Mitigation: Keep usage limited to read-only cast commands, do not enter seed phrases or private keys, and do not send transactions based on this skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byron-mckeeby/skills/ethereum-read-only) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/byron-mckeeby) <br>
- [Foundry installer](https://foundry.paradigm.xyz) <br>
- [4byte Directory API](https://www.4byte.directory/api/v1/signatures/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only command examples that depend on user-provided RPC endpoints, addresses, contract ABIs, block ranges, and transaction hashes.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
