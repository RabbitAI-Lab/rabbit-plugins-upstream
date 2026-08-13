## Description:

Guides LinkFox users through API key setup, SMS-based registration, billing-shortage recovery, plan selection, payment order creation, and QR-code payment handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External LinkFox users and developers use this skill when a LinkFox API key is missing or rejected, or when a LinkFox workflow reports insufficient balance and the user needs guided recharge steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may handle SMS verification codes and live LinkFox API keys during onboarding.

Mitigation: Treat SMS codes and returned API keys as secrets, avoid exposing them in untrusted transcripts, and rotate the API key if it may have been shared.

Risk: The skill can help initiate paid recharge orders and account actions.

Mitigation: Proceed only when you trust LinkFox and have confirmed the selected plan and payment method before scanning or opening a payment QR/link.

Risk: Custom LINKFOX_* API URL environment variables can redirect requests away from the expected LinkFox services.

Mitigation: Verify any LINKFOX_* API URL environment variables before use.

## Reference(s):

- [LinkFox onboarding API contract](references/api.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-onboarding)
- [LinkFox Agent portal](https://agent.linkfox.com/)
- [LinkFox API key setup help](https://yxgb3sicy7.feishu.cn/wiki/IlkawdQP9ifKv9k22xcc7rjmnkb)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON script results, and optional QR-code PNG or ASCII output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local QR-code image files for payment handoff and environment-variable setup instructions.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
