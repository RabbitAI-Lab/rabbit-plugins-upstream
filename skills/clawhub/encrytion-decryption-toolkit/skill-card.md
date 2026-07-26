## Description: <br>
Encryption Decryption Toolkit provides AgentPMT-hosted actions for secure random value generation, cryptographic hashing, HMAC computation, digital signing, and AES-256-GCM encryption or decryption. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call AgentPMT cryptographic utilities for token generation, checksums, webhook validation, request signing, and AES-256-GCM encryption workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote cryptographic operations can expose plaintext, encryption keys, HMAC secrets, or private signing keys to AgentPMT. <br>
Mitigation: Use this skill only when AgentPMT's retention, logging, and access controls are acceptable; avoid sending long-lived private keys, production secrets, access tokens, or sensitive plaintext, and prefer local cryptography for durable secrets. <br>
Risk: AES-256-GCM misuse, especially nonce reuse with the same key or incorrect key and IV sizes, can undermine confidentiality. <br>
Mitigation: Generate a fresh 12-byte IV for each encryption, use exactly a 32-byte key, and keep encoding consistent between encrypt and decrypt calls. <br>
Risk: Sensitive inputs may be captured in prompts, logs, or workflow traces around the remote call. <br>
Mitigation: Keep tool inputs scoped to the minimum data required and avoid placing account secrets, wallet keys, mnemonics, signatures, or payment headers in prompts or logs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/encrytion-decryption-toolkit) <br>
- [AgentPMT Marketplace Product](https://www.agentpmt.com/marketplace/encrytion-decryption-toolkit) <br>
- [Encryption Decryption Toolkit Schema](schema.md) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Guidance, Configuration] <br>
**Output Format:** [Markdown instructions with JSON request and response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote tool results can include generated random values, hashes, HMACs, signatures, ciphertext, or plaintext depending on the selected action.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
