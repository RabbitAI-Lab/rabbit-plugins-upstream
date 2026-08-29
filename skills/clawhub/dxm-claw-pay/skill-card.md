## Description:

度小满支付钱包 Skill handles insufficient-balance or unpurchased-service states by generating payment links and QR code guidance from structured product data, and it can also run a paid Skill installation flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[duxiaoman](https://clawhub.ai/user/duxiaoman)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to recover from paid SP service access failures by showing product, price, payment channel, payment URL, and QR code guidance. They can also use it to download and install paid ClawHub skills after payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts clawpay and dxmpay services to manage paid downloads and payment QR codes.

Mitigation: Install and run it only when the publisher and those payment services are trusted for the intended environment.

Risk: The skill can create a persistent local client identity and store a plaintext private key.

Mitigation: Avoid using it in shared or highly sensitive workspaces unless the local configuration file is protected and lifecycle-managed.

Risk: The skill can install downloaded skill code into the local skills directory after signature verification.

Mitigation: Review or isolate downloaded skills before enabling them, especially in environments with sensitive files or credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/duxiaoman/skills/dxm-claw-pay)
- [Publisher profile](https://clawhub.ai/user/duxiaoman)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with JSON CLI responses and generated PNG QR code files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js. The payment flow writes QR code PNGs to a temporary directory; the install flow can create local client configuration and install downloaded skill files.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
