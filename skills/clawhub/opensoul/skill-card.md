## Description: <br>
Enables AI agents to log encrypted, immutable audit trails on Bitcoin SV for persistent memory, self-reflection, and on-chain economic activity tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mastergoogler](https://clawhub.ai/user/mastergoogler) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to add blockchain-backed audit logging, persistent session memory, self-reflection, and cost tracking to AI agents. It provides setup guidance, Python examples, and templates for BSV wallet use, PGP encryption, log retrieval, and agent handoff patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Permanent blockchain logs can expose prompts, personal data, secrets, raw queries, document names, or confidential business details if they are written directly. <br>
Mitigation: Log only minimal redacted metadata, hashes, or strongly encrypted content, and review log payloads before flushing them to the blockchain. <br>
Risk: BSV wallet keys and PGP private keys can expose funds or encrypted history if mishandled. <br>
Mitigation: Use a new low-balance or testnet wallet, keep private keys out of code and logs, require a PGP passphrase, and protect or disable local backup JSON files. <br>
Risk: The artifact references external OpenSoul installation and repository resources that may change outside this release package. <br>
Mitigation: Audit the external repository and install script before running them, and prefer isolated virtual environments for dependency installation. <br>


## Reference(s): <br>
- [ClawHub OpenSoul skill page](https://clawhub.ai/mastergoogler/skills/opensoul) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Guide](artifact/SKILL.md) <br>
- [Artifact Prerequisites](artifact/PREREQUISITES.md) <br>
- [Artifact Examples](artifact/EXAMPLES.md) <br>
- [Artifact Troubleshooting](artifact/TROUBLESHOOTING.md) <br>
- [BSV Documentation](https://wiki.bitcoinsv.io/) <br>
- [WhatsOnChain API](https://developers.whatsonchain.com/) <br>
- [OpenPGP](https://www.openpgp.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, and configuration templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces implementation guidance and starter code for agent logging workflows; review secrets, wallet funding, and data redaction before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
