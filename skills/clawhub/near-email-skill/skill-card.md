## Description: <br>
Send and read blockchain-native emails using NEAR Email service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zavodil](https://clawhub.ai/user/zavodil) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to add NEAR-account email workflows, including smart contract notifications, server-side email actions, and browser or wallet-based NEAR transaction flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment keys and NEAR private keys can authorize account or service actions if exposed. <br>
Mitigation: Store keys in environment variables or a secret manager and avoid embedding them in generated code, logs, or shared prompts. <br>
Risk: Plaintext email content sent through send_email_plaintext is public and durable on-chain data. <br>
Mitigation: Use plaintext only for public contract notifications and use encrypted send_email for private message content. <br>
Risk: Email deletion, attachments, and public sends can have user-visible or irreversible effects. <br>
Mitigation: Require explicit user confirmation before deleting emails, sending attachments, or submitting public on-chain messages. <br>
Risk: NEAR Email is documented as mainnet-only. <br>
Mitigation: Do not route testnet accounts through this skill; validate recipient account context before generating integration steps. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zavodil/skills/near-email-skill) <br>
- [NEAR Email API Reference](api-reference.md) <br>
- [NEAR Email Code Examples](examples.md) <br>
- [OutLayer Dashboard](https://outlayer.fastnear.com/dashboard) <br>
- [OutLayer API Base](https://api.outlayer.fastnear.com) <br>
- [NEAR Mainnet RPC](https://rpc.mainnet.near.org) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with Rust, JavaScript/TypeScript, Python, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API request structures, NEAR transaction parsing guidance, payment key setup steps, and security cautions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
