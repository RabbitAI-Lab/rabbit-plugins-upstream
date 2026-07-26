## Description: <br>
Integrate SanctifAI Trust Proof-of-Human attestations. Use when an app needs cryptographic proof a human performed a task or human-in-the-loop verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanctifai](https://clawhub.ai/user/sanctifai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to integrate SanctifAI Trust attestations into applications that need proof a human completed or approved a task. It guides embedded REST API and extension-based integration paths that return a participation ID, certificate URL, QR URL, and optional verification URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Trust API key could be exposed if embedded integration code places it in client-side JavaScript. <br>
Mitigation: Keep TRUST_API_KEY only on the backend or in a secret manager, and mint browser sessions server-side. <br>
Risk: Public certificate URLs or on-chain attestations could reveal sensitive metadata if identifiers or labels contain PII. <br>
Mitigation: Use opaque internal identifiers and avoid names, emails, account numbers, government IDs, addresses, or other PII in certificate-visible fields. <br>
Risk: Production attestations depend on an external SanctifAI service and tenant configuration. <br>
Mitigation: Confirm the organization trusts SanctifAI Trust before production use, target the production API, and verify tenant origin allowlists before asking users to test. <br>


## Reference(s): <br>
- [SanctifAI Trust documentation](https://trust.sanctifai.com) <br>
- [ClawHub skill page](https://clawhub.ai/sanctifai/skills/sanctifai-trust) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with JavaScript, HTML, environment variable, and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may produce backend API calls to SanctifAI Trust; no package install is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
