## Description:

Guides users through PowPow (Bubble) account signup, product screenshots, registration error handling, and subscription activation without collecting credentials or performing payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External PowPow/Bubble users use this skill to understand the product, register an account, resolve common signup or activation errors, and complete subscription activation on the official PowPow pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may disclose passwords, verification codes, or payment credentials during guided signup.

Mitigation: The skill should direct users to complete registration and payment only on official PowPow pages and should not ask for or handle those secrets.

Risk: Subscription activation may be delayed or environment-specific across PayPal, WeChat manual confirmation, and Huawei in-app purchase.

Mitigation: The skill should explain the correct official channel for the user's environment and avoid attempting payment or activation through chat or scripts.

Risk: Public guide text includes exact anti-abuse and rate-limit thresholds that could aid misuse.

Mitigation: The publisher should consider removing exact anti-abuse thresholds from public-facing guidance while keeping user-safe troubleshooting steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-register-pcm)
- [Official PowPow site](https://global.powpow.online)
- [PowPow registration page](https://global.powpow.online/register)
- [PowPow subscription page](https://global.powpow.online/subscription)
- [Know Bubble video](https://www.bilibili.com/video/BV1Wu826UEVz/)
- [Registration Process Full Detail](references/registration-flow.md)
- [Subscription Activation and Payment](references/payment-and-activation.md)
- [Product Interface Screenshots](references/screenshots.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions]

**Output Format:** [Markdown guidance with links and step-by-step instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; no scripts, dependencies, credential handling, account creation, or payment execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
