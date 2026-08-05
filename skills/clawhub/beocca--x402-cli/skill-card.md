## Description: <br>
A simple CLI that helps AI agents discover x402 services, make paywalled requests, and manage local EVM wallets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[beocca](https://clawhub.ai/user/beocca) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to discover x402 services, issue paywalled HTTP requests, and create local EVM wallets for agent payment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate x402 paid requests that spend real wallet funds through arbitrary URLs without an approval step. <br>
Mitigation: Use a dedicated, low-balance EVM wallet; review each request URL, header, and payload before invocation; and add spend caps, allowlists, or a manual approval gate where possible. <br>
Risk: Wallet creation stores a spend-capable EVM private key as plaintext on disk. <br>
Mitigation: Keep generated wallet files out of version control and shared storage, preserve restrictive file permissions, and fund only the minimum amount needed. <br>
Risk: Request headers and payloads are sent to the destination endpoint selected by the caller. <br>
Mitigation: Confirm the destination and payload contents before running paid requests, and avoid sending sensitive values unless the endpoint is trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/beocca/skills/x402-cli) <br>
- [Publisher profile](https://clawhub.ai/user/beocca) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance] <br>
**Output Format:** [Markdown guidance with bash examples and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI invocations are documented to emit one JSON object on stdout; security warnings may appear on stderr.] <br>

## Skill Version(s): <br>
1.1.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
