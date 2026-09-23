## Description:

Guides Turkish-speaking users through PowPow account registration, troubleshooting, and subscription activation without handling credentials or payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow users use this Turkish guidance skill to understand the product, create an account, resolve common registration problems, and activate a subscription through the official PowPow pages. Agents use it to provide step-by-step text guidance, relevant screenshots, and clear next actions while leaving all form entry and payment actions to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expose passwords, verification codes, or payment details to the chat agent while following registration guidance.

Mitigation: The skill instructs the agent not to request secrets or payment details and directs users to enter sensitive information only on official PowPow pages.

Risk: Users may be misdirected to non-official registration or payment pages.

Mitigation: The skill provides official PowPow registration and subscription URLs and tells users to verify they are on official PowPow pages before entering account or payment details.

Risk: Payment activation may be delayed or require manual confirmation, especially for WeChat QR payments.

Mitigation: The skill explains channel-specific activation behavior and sets expectations that manual approval or webhook delays can occur before account activation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-tr)
- [Publisher profile](https://clawhub.ai/user/durenzidu)
- [PowPow official site](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [Product video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration flow details](references/registration-flow.md)
- [Payment and activation details](references/payment-and-activation.md)
- [Product screenshots](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance with links and concise next-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guide-only output; no code execution, account access, credential collection, or payment handling.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
