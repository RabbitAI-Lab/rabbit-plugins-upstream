## Description: <br>
A simple CLI that helps AI agents discover x402 services, make paywalled requests, and manage local EVM wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to discover x402 services, make paid HTTP requests, and create local EVM wallets for x402 payment flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The request command can spend wallet funds and send headers or payload data to arbitrary endpoints without a confirmation gate. <br>
Mitigation: Review the destination URL, headers, payload, and expected cost before invocation; prefer external spending limits, allowlists, or manual approval. <br>
Risk: The skill uses an EVM wallet secret and can create plaintext spend-capable wallet files on disk. <br>
Mitigation: Use a dedicated low-balance wallet, avoid personal or high-value keys, keep wallet files out of version control and shared storage, and rely on restrictive file permissions. <br>


## Reference(s): <br>
- [x402-CLI on ClawHub](https://clawhub.ai/beocca/skills/x402-cli) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Configuration, Files] <br>
**Output Format:** [JSON command results with stderr warnings for security-relevant actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may write wallet JSON files or saved discovery responses when requested.] <br>

## Skill Version(s): <br>
1.1.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
