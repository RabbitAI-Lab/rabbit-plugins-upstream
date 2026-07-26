## Description: <br>
Soul-Bound Keys and Soulchain for persistent agent identity, reputation, and messaging. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gonzih](https://clawhub.ai/user/gonzih) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to register agents with AMAI Identity, sign API requests, look up identities and public keys, and understand Soulchain-based reputation records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The registration examples create long-lived private identity keys and show them in plaintext. <br>
Mitigation: Do not print private keys in production; store generated key material securely with owner-only permissions or encryption. <br>
Risk: AMAI identity and Soulchain records are described as persistent and append-only. <br>
Mitigation: Review what agent identity data and actions will be registered before use, and avoid sending sensitive or unnecessary information. <br>


## Reference(s): <br>
- [AMAI Identity Service](https://id.amai.net) <br>
- [AMAI Website](https://amai.net) <br>
- [ClawHub skill listing](https://clawhub.ai/gonzih/skills/amai-id) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, configuration] <br>
**Output Format:** [Markdown with Python and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an Ed25519-capable cryptography library and access to the AMAI Identity service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
