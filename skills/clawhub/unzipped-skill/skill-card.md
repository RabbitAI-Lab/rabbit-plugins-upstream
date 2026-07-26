## Description: <br>
Create Farcaster accounts, manage profile setup, and post casts through wallet-backed Farcaster automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jozh-bit](https://clawhub.ai/user/jozh-bit) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to create and configure Farcaster identities, manage signing credentials, and publish casts from command-line or programmatic workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet and signer secrets may be saved in plaintext credential files, creating account and funds takeover risk. <br>
Mitigation: Use only low-value wallets and accounts, avoid storing generated credentials in project directories, add credential files to .gitignore, and restrict file permissions. <br>
Risk: The skill can fund wallets, bridge or swap assets, register identities, add signers, and post publicly. <br>
Mitigation: Require explicit human approval before any funding, bridging, swapping, identity registration, signer addition, or public posting step. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jozh-bit/skills/unzipped-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes commands and snippets for wallet funding, account registration, signer setup, profile updates, credential handling, and cast posting.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
