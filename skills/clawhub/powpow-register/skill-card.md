## Description:

Guides users through understanding PowPow, creating an account, troubleshooting registration issues, and activating a subscription without handling credentials or payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow users and support agents use this skill to introduce the product, guide account registration, resolve common verification or activation problems, and route users to the appropriate subscription channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may disclose passwords, email verification codes, or payment details in chat while being guided through registration.

Mitigation: The skill instructs the agent not to request or handle credentials, verification codes, or payment credentials; users complete registration and payment directly in the browser or app.

Risk: Users may follow incorrect PowPow URLs or misunderstand externally hosted screenshot links.

Mitigation: The skill uses documented PowPow URLs and public screenshot links, and the security guidance tells users to verify PowPow URLs before proceeding.

## Reference(s):

- [PowPow Homepage](https://global.powpow.online)
- [PowPow Registration Page](https://global.powpow.online/register)
- [PowPow Subscription Page](https://global.powpow.online/subscription)
- [PowPow Intro Video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration Flow Reference](references/registration-flow.md)
- [Payment and Activation Reference](references/payment-and-activation.md)
- [Product Screenshot Reference](references/screenshots.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with links and step-by-step troubleshooting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include externally hosted screenshot links; does not generate code, shell commands, API calls, or form submissions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
